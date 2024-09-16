from ccxt.base.exchange import Exchange
import hashlib
import hmac
from ccxt.base.errors import ExchangeError, AuthenticationError, ArgumentsRequired, BadRequest

class lmex(Exchange):

    def describe(self):
        return self.deep_extend(super(lmex, self).describe(), {
            'id': 'lmex',
            'name': 'LMEX',
            'countries': ['SG'],  # Singapore
            'version': 'v2.1',
            'rateLimit': 100,
            'has': {
                'CORS': False,
                'spot': False,
                'margin': False,
                'swap': True,
                'future': True,
                'option': False,
                'cancelOrder': True,
                'createOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,  # LMEX supports OHLCV data
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchPositions': True,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchLeverage': True,
                'fetchLeverageTiers': True,
                'fetchFundingRate': True,
                'fetchFundingRateHistory': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/YOUR_LOGO_URL_HERE',
                'api': {
                    'public': 'https://api.lmex.io/futures',
                    'private': 'https://api.lmex.io/futures',
                },
                'www': 'https://www.lmex.io',
                'doc': 'https://www.lmex.io/apidoc/futures',
            },
            'api': {
                'public': {
                    'get': [
                        'api/v2.1/market_summary',
                        'api/v2.1/price',
                        'api/v2.1/orderbook',
                        'api/v2.1/trades',
                    ],
                },
                'private': {
                    'get': [
                        'api/v2.1/user/open_orders',
                        'api/v2.1/user/trade_history',
                        'api/v2.1/user/positions',
                        'api/v2.1/user/wallet',
                    ],
                    'post': [
                        'api/v2.1/order',
                    ],
                    'put': [
                        'api/v2.1/order',
                    ],
                    'delete': [
                        'api/v2.1/order',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': 0.0002,
                    'taker': 0.0005,
                },
            },
            'timeframes': {
                '1': '1min',
                '5': '5m',
                '15': '15m',
                '30': '30m',
                '60': '1h',
                '240': '4h',
                '360': '6h',
                '1440': '1d',
                '10080': '1w',
                '43200': '1M',
            },
            'exceptions': {
                '-8104': ExchangeError,  # ORDER_BELONGS_TO_VENDOR
                '-7006': BadSymbol,  # COIN_PAIR_IS_NOT_EXISTS_ERROR
                '-2023': BadRequest,  # UNKNOWN_CURRENCY
                '-1042': PermissionDenied,  # USER_CANT_TRADE
                '-22': RateLimitExceeded,  # COMM_EXCESS_RATE_LIMIT_ERROR
                '-7': AuthenticationError,  # COMM_AUTHENTICATE_ERROR
                '-2': BadRequest,  # COMM_REQUEST_PARAM_ERROR
                '-1': ExchangeError,  # COMM_FAILED_ERROR
                '10002': AuthenticationError,  # USER_TOKEN_EXPIRED
                '51523': InsufficientFunds,  # FINANCE_INSUFFICIENT_WALLET_BALANCE_ERROR
            },
        })

    def fetch_markets(self, params={}):
        """
        Fetch the list of markets available on the exchange
        :param params:
        :return:
        """
        response = self.publicGetApiV21MarketSummary(params)
        result = []
        for market in response:
            id = self.safe_string(market, 'symbol')
            baseId, quoteId = id.split('-')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            active = self.safe_value(market, 'active', False)
            precision = {
                'amount': self.safe_number(market, 'minOrderSize'),
                'price': self.safe_number(market, 'minPriceIncrement'),
            }
            limits = {
                'amount': {
                    'min': self.safe_number(market, 'minOrderSize'),
                    'max': self.safe_number(market, 'maxOrderSize'),
                },
                'price': {
                    'min': self.safe_number(market, 'minValidPrice'),
                    'max': None,
                },
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetApiV21Price(self.extend(request, params))
        ticker = self.safe_value(response, 0)
        return self.parse_ticker(ticker, market)

    def parse_ticker(self, ticker, market=None):
        symbol = self.safe_symbol(None, market)
        timestamp = self.milliseconds()
        last = self.safe_number(ticker, 'lastPrice')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': None,
            'low': None,
            'bid': None,
            'bidVolume': None,
            'ask': None,
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': None,
            'quoteVolume': None,
            'info': ticker,
        }

    def fetch_order_book(self, symbol, limit=None, params={}):
        """
        Fetch the order book for a particular symbol
        :param symbol:
        :param limit:
        :param params:
        :return:
        """
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        if limit is not None:
            request['depth'] = limit
        response = self.publicGetApiV21OrderbookL2(self.extend(request, params))
        return self.parse_order_book(response, symbol, None, 'buyQuote', 'sellQuote', 'price', 'size')

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if since is not None:
            request['startTime'] = since
        if limit is not None:
            request['count'] = limit
        response = self.publicGetApiV21Trades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def parse_trade(self, trade, market=None):
        timestamp = self.safe_integer(trade, 'timestamp')
        side = self.safe_string_lower(trade, 'side')
        id = self.safe_string(trade, 'serialId')
        symbol = self.safe_symbol(self.safe_string(trade, 'symbol'), market)
        price = self.safe_number(trade, 'price')
        amount = self.safe_number(trade, 'size')
        cost = None
        if price is not None and amount is not None:
            cost = price * amount
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': None,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': None,
        }

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderID': id,
        }
        if symbol is not None:
            request['symbol'] = self.market_id(symbol)
        response = self.privateDeleteApiV21Order(self.extend(request, params))
        return self.parse_order(response)

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'orderID': id,
        }
        if symbol is not None:
            request['symbol'] = self.market_id(symbol)
        response = self.privateGetApiV21Order(self.extend(request, params))
        return self.parse_order(response)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        response = self.privateGetApiV21UserOpenOrders(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if since is not None:
            request['startTime'] = since
        if limit is not None:
            request['count'] = limit
        response = self.privateGetApiV21UserTradeHistory(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if since is not None:
            request['startTime'] = since
        if limit is not None:
            request['count'] = limit
        response = self.privateGetApiV21UserTradeHistory(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def fetch_leverage(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.privateGetApiV21Leverage(self.extend(request, params))
        return self.parse_leverage(response)

    def parse_leverage(self, leverage):
        return {
            'info': leverage,
            'leverage': self.safe_number(leverage, 'leverage'),
        }

    def set_leverage(self, leverage, symbol=None, params={}):
        self.load_markets()
        if symbol is None:
            raise ArgumentsRequired(self.id + ' setLeverage() requires a symbol argument')
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'leverage': leverage,
        }
        return self.privatePostApiV21Leverage(self.extend(request, params))

    def fetch_funding_rate(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetApiV21FundingHistory(self.extend(request, params))
        return self.parse_funding_rate(response, market)

    def parse_funding_rate(self, fundingRate, market=None):
        data = self.safe_value(fundingRate, market['id'], [])
        latest = self.safe_value(data, 0, {})
        return {
            'info': fundingRate,
            'symbol': market['symbol'],
            'markPrice': None,
            'indexPrice': None,
            'interestRate': None,
            'estimatedSettlePrice': None,
            'timestamp': self.safe_timestamp(latest, 'time'),
            'datetime': self.iso8601(self.safe_timestamp(latest, 'time')),
            'fundingRate': self.safe_number(latest, 'rate'),
            'fundingTimestamp': None,
            'fundingDatetime': None,
            'nextFundingRate': None,
            'nextFundingTimestamp': None,
            'nextFundingDatetime': None,
            'previousFundingRate': None,
            'previousFundingTimestamp': None,
            'previousFundingDatetime': None,
        }

    def fetch_funding_rate_history(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if since is not None:
            request['from'] = since
        if limit is not None:
            request['count'] = limit
        response = self.publicGetApiV21FundingHistory(self.extend(request, params))
        rates = []
        for key, value in response.items():
            market = self.safe_market(key)
            for rate in value:
                rates.append(self.extend(self.parse_funding_rate(rate, market), {
                    'symbol': market['symbol'],
                }))
        sorted_rates = self.sort_by(rates, 'timestamp')
        return self.filter_by_symbol_since_limit(sorted_rates, symbol, since, limit)

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetApiV21UserWallet(params)
        result = {'info': response}
        for balance in response:
            currencyId = self.safe_string(balance, 'currency')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_string(balance, 'availableBalance')
            account['total'] = self.safe_string(balance, 'balance')
            result[code] = account
        return self.parse_balance(result)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'side': side.upper(),
            'type': type.upper(),
            'size': self.amount_to_precision(symbol, amount),
        }
        if type == 'LIMIT':
            if price is None:
                raise ArgumentsRequired(self.id + ' createOrder() requires a price argument for limit orders')
            request['price'] = self.price_to_precision(symbol, price)

        time_in_force = self.safe_string(params, 'timeInForce')
        if time_in_force is not None:
            request['time_in_force'] = time_in_force

        post_only = self.safe_value(params, 'postOnly', False)
        if post_only:
            request['postOnly'] = True

        reduce_only = self.safe_value(params, 'reduceOnly', False)
        if reduce_only:
            request['reduceOnly'] = True

        trigger_price = self.safe_number_2(params, 'triggerPrice', 'stopPrice')
        if trigger_price is not None:
            request['triggerPrice'] = self.price_to_precision(symbol, trigger_price)
            request['txType'] = 'STOP'

        response = self.privatePostApiV21Order(self.extend(request, params))
        return self.parse_order(response, market)

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'orderID')
        timestamp = self.safe_integer(order, 'timestamp')
        symbol = self.safe_symbol(self.safe_string(order, 'symbol'), market)
        type = self.safe_string_lower(order, 'orderType')
        side = self.safe_string_lower(order, 'side')
        price = self.safe_number(order, 'price')
        amount = self.safe_number(order, 'size')
        filled = self.safe_number(order, 'fillSize')
        remaining = None
        if amount is not None and filled is not None:
            remaining = amount - filled
        status = self.parse_order_status(self.safe_string(order, 'status'))
        return {
            'id': id,
            'clientOrderId': self.safe_string(order, 'clOrderID'),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': None,
            'average': self.safe_number(order, 'avgFillPrice'),
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': None,
            'trades': None,
            'info': order,
        }

    def parse_order_status(self, status):
        statuses = {
            '2': 'open',
            '4': 'closed',
            '5': 'open',
            '6': 'canceled',
            '7': 'canceled',
            '8': 'rejected',
            '9': 'open',
            '10': 'open',
        }
        return self.safe_string(statuses, status, status)

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            auth = path + nonce
            headers = {
                'request-api': self.apiKey,
                'request-nonce': nonce,
                'Content-Type': 'application/json'
            }
            if method == 'GET':
                if query:
                    url += '?' + self.urlencode(query)
            else:
                body = self.json(query)
                auth += body
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha384)
            headers['request-sign'] = signature
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, statusCode, statusText, url, method, responseHeaders, responseBody, response, requestHeaders, requestBody):
        if response is None:
            return
        if 'code' in response:
            code = self.safe_string(response, 'code')
            message = self.safe_string(response, 'msg')
            feedback = self.id + ' ' + self.json(response)
            if code != '0':
                exceptions = self.exceptions
                if code in exceptions:
                    ExceptionClass = exceptions[code]
                    raise ExceptionClass(feedback)
                else:
                    raise ExchangeError(feedback)

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'resolution': self.timeframes[timeframe],
        }
        if since is not None:
            request['start'] = since
        if limit is not None:
            request['end'] = self.sum(since, limit * self.parse_timeframe(timeframe) * 1000)
        response = self.publicGetApiV21Ohlcv(self.extend(request, params))
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def parse_ohlcv(self, ohlcv, market=None):
        return [
            self.safe_integer(ohlcv, 0),
            self.safe_number(ohlcv, 1),
            self.safe_number(ohlcv, 2),
            self.safe_number(ohlcv, 3),
            self.safe_number(ohlcv, 4),
            self.safe_number(ohlcv, 5),
        ]

    def fetch_positions(self, symbols=None, params={}):
        self.load_markets()
        response = self.privateGetApiV21UserPositions(params)
        return self.parse_positions(response, symbols)

    def parse_position(self, position, market=None):
        market_id = self.safe_string(position, 'symbol')
        market = self.safe_market(market_id, market)
        symbol = market['symbol']
        side = self.safe_string(position, 'side')
        amount = self.safe_number(position, 'size')
        if side == 'SELL':
            amount = -amount
        entry_price = self.safe_number(position, 'entryPrice')
        unrealized_pnl = self.safe_number(position, 'unrealizedProfitLoss')
        leverage = self.safe_number(position, 'isolatedLeverage')
        margin_mode = 'isolated' if leverage else 'cross'
        return {
            'info': position,
            'symbol': symbol,
            'timestamp': None,
            'datetime': None,
            'initialMargin': None,
            'initialMarginPercentage': None,
            'maintenanceMargin': self.safe_number(position, 'totalMaintenanceMargin'),
            'maintenanceMarginPercentage': None,
            'entryPrice': entry_price,
            'notional': None,
            'leverage': leverage,
            'unrealizedPnl': unrealized_pnl,
            'contracts': abs(amount),
            'contractSize': self.safe_number(market, 'contractSize'),
            'marginRatio': None,
            'liquidationPrice': self.safe_number(position, 'liquidationPrice'),
            'markPrice': self.safe_number(position, 'markPrice'),
            'collateral': None,
            'marginMode': margin_mode,
            'side': 'long' if amount > 0 else 'short',
            'percentage': None,
        }

    def fetch_leverage_tiers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetApiV21RiskLimit(params)
        return self.parse_leverage_tiers(response, symbols, 'symbol')

    def parse_leverage_tiers(self, response, symbols=None, symbolKey=None):
        result = {}
        for i in range(0, len(response)):
            item = response[i]
            id = self.safe_string(item, 'symbol')
            market = self.safe_market(id)
            symbol = market['symbol']
            result[symbol] = self.parse_market_leverage_tiers(item, market)
        return self.filter_by_array(result, 'symbol', symbols)

    def parse_market_leverage_tiers(self, info, market=None):
        tiers = []
        minRiskLimit = self.safe_number(info, 'minRiskLimit')
        maxRiskLimit = self.safe_number(info, 'maxRiskLimit')
        riskLimitStep = self.safe_number(info, 'riskLimitStep', 100000)  # Assuming a default step if not provided
        maxLeverage = self.safe_number(info, 'maxLeverage')

        currentRiskLimit = minRiskLimit
        while currentRiskLimit <= maxRiskLimit:
            tierLeverage = min(maxLeverage, 100000000 / currentRiskLimit)  # This is an approximation, adjust if needed
            tiers.append({
                'tier': len(tiers) + 1,
                'currency': market['quote'] if market else None,
                'minNotional': currentRiskLimit - riskLimitStep,
                'maxNotional': currentRiskLimit,
                'maintenanceMarginRate': 0.01,  # This is an approximation, adjust if LMEX provides specific values
                'maxLeverage': tierLeverage,
                'info': info,
            })
            currentRiskLimit += riskLimitStep

        return tiers

    def parse_funding_rate_history(self, response, market=None, since=None, limit=None):
        rates = []
        for key, values in response.items():
            symbol = self.safe_symbol(key)
            for rate in values:
                parsed = self.parse_funding_rate({key: [rate]}, market)
                rates.append(self.extend(parsed, {'symbol': symbol}))
        sorted_rates = self.sort_by(rates, 'timestamp')
        return self.filter_by_symbol_since_limit(sorted_rates, market['symbol'] if market else None, since, limit)