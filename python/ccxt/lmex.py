from http.cookiejar import debug

from ccxt.base.exchange import Exchange
import hashlib
import hmac
from ccxt.base.errors import ExchangeError, AuthenticationError, ArgumentsRequired, BadRequest, BadSymbol, PermissionDenied, RateLimitExceeded, InsufficientFunds, NotSupported
import time

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
                'spot': True,
                'margin': True,
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
                'fetchTickers': True,
                'fetchTrades': True,
                'fetchLeverage': True,
                'fetchLeverageTiers': True,
                'fetchFundingRate': True,
                'fetchFundingRateHistory': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/YOUR_LOGO_URL_HERE',
                'api': {
                    'public': 'https://test-api.lmex.io/futures',
                    'private': 'https://test-api.lmex.io/futures',
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
                        'api/v2.1/ohlcv',
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
                '1m': '1',
                '5m': '5',
                '15m': '15',
                '30m': '30',
                '1h': '60',
                '4h': '240',
                '6h': '360',
                '1d': '1440',
                '1w': '10080',
                '1M': '43200',
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
        response = self.request('api/v2.1/market_summary', 'public', 'GET', params)
        result = []
        for market in response:
            id = self.safe_string(market, 'symbol')
            baseId = self.safe_string(market, 'base')
            quoteId = self.safe_string(market, 'quote')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = id  # Use the 'symbol' field directly as CCXT symbol
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'settle': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'settleId': quoteId,
                'type': 'swap',
                'spot': False,
                'margin': False,
                'swap': True,
                'future': False,
                'option': False,
                'active': self.safe_value(market, 'active', False),
                'contract': True,
                'linear': True,
                'inverse': False,
                'contractSize': self.safe_number(market, 'contractSize'),
                'expiry': None,
                'expiryDatetime': None,
                'strike': None,
                'optionType': None,
                'precision': {
                    'amount': self.safe_number(market, 'minSizeIncrement'),
                    'price': self.safe_number(market, 'minPriceIncrement'),
                },
                'limits': {
                    'leverage': {
                        'min': None,
                        'max': None,
                    },
                    'amount': {
                        'min': self.safe_number(market, 'minOrderSize'),
                        'max': self.safe_number(market, 'maxOrderSize'),
                    },
                    'price': {
                        'min': self.safe_number(market, 'minValidPrice'),
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
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
        symbol = self.safe_symbol(self.safe_string(ticker, 'symbol'), market)
        timestamp = self.milliseconds()
        last = self.safe_number(ticker, 'lastPrice')
        index = self.safe_number(ticker, 'indexPrice')
        mark = self.safe_number(ticker, 'markPrice')
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
            'index': index,
            'mark': mark,
        }

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.request('api/v2.1/market_summary', 'public', 'GET', params)
        result = {}
        for ticker in response:
            market = self.safe_market(ticker['symbol'])
            parsed = self.parse_ticker(ticker, market)
            symbol = parsed['symbol']
            result[symbol] = parsed
        return self.filter_by_array(result, 'symbol', symbols)

    def parse_tickers(self, response, symbols=None):
        result = {}
        for ticker in response:
            parsed = self.parse_ticker(ticker)
            symbol = parsed['symbol']
            result[symbol] = parsed
        return self.filter_by_array(result, 'symbol', symbols)

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
        if symbol is None:
            raise ArgumentsRequired(self.id + ' cancelOrder() requires a symbol argument')
        market = self.market(symbol)
        request = {
            'orderID': id,
            'symbol': market['id'],
        }
        print(f"Cancel order request: {request}")  # Debug log
        response = self.privateDeleteApiV21Order(request)  # Pass request directly, not extended with params
        return self.parse_order(response, market)

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
        wallet = params.get('wallet', 'CROSS@')
        response = self.privateGetApiV21UserWallet({'wallet': wallet})
        result = {'info': response}

        if response and isinstance(response, list) and len(response) > 0:
            wallet_data = response[0]
            result['total'] = self.safe_number(wallet_data, 'totalValue')
            result['free'] = self.safe_number(wallet_data, 'availableBalance')
            result['used'] = self.safe_number(wallet_data, 'openMargin')

            assets = self.safe_value(wallet_data, 'assets', [])
            for asset in assets:
                currency = self.safe_currency_code(self.safe_string(asset, 'currency'))
                account = self.account()
                account['total'] = self.safe_number(asset, 'balance')
                account['free'] = account['total']  # LMEX doesn't provide separate free balance per asset
                account['used'] = 0  # LMEX doesn't provide used balance per asset
                result[currency] = account

        return self.safe_balance(result)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'side': side.upper(),
            'type': type.upper(),
            'size': self.amount_to_precision(symbol, amount),
        }
        if type.upper() == 'LIMIT':
            if price is None:
                raise ArgumentsRequired(self.id + ' createOrder() requires a price argument for limit orders')
            request['price'] = self.price_to_precision(symbol, price)

        time_in_force = self.safe_string(params, 'timeInForce')
        if time_in_force is not None:
            request['time_in_force'] = time_in_force
        elif type.upper() == 'LIMIT':
            request['time_in_force'] = 'GTC'  # Default to GTC for limit orders if not specified

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
        order = self.safe_value(order, 0, order)  # LMEX returns an array with one order
        id = self.safe_string(order, 'orderID')
        timestamp = self.safe_integer(order, 'timestamp')
        symbol = self.safe_symbol(self.safe_string(order, 'symbol'), market)
        type_raw = self.safe_integer(order, 'orderType')
        type = 'limit' if type_raw == 76 else 'market' if type_raw == 77 else 'unknown'
        side = self.safe_string_lower(order, 'side')
        price = self.safe_number(order, 'price')
        amount = self.safe_number(order, 'size')
        filled = self.safe_number(order, 'fillSize')
        remaining = self.safe_number(order, 'remainingSize')
        status = self.parse_order_status(self.safe_integer(order, 'status'))
        average = self.safe_number(order, 'avgFillPrice')
        cost = None
        if filled is not None and average is not None:
            cost = filled * average

        return {
            'id': id,
            'clientOrderId': self.safe_string(order, 'clOrderID'),
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': None,  # LMEX doesn't provide this
            'status': status,
            'symbol': symbol,
            'type': type,
            'timeInForce': self.safe_string(order, 'time_in_force'),
            'side': side,
            'price': price,
            'average': average,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'cost': cost,
            'trades': None,  # LMEX doesn't provide this in the order response
            'fee': None,  # LMEX doesn't provide this in the order response
            'info': order,
        }

    def parse_order_status(self, status):
        statuses = {
            2: 'open',
            4: 'closed',
            5: 'open',  # partially filled
            6: 'canceled',
            7: 'canceled',  # refunded
            8: 'rejected',
            9: 'open',  # trigger inserted
            10: 'open',  # trigger activated
            15: 'rejected',
            16: 'rejected',  # not found
            17: 'rejected',  # request failed
        }
        return self.safe_string(statuses, status, 'unknown')

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))

        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            nonce = str(int(self.milliseconds()))
            auth = '/' + path + nonce
            body = ''

            headers = {
                'request-api': self.apiKey,
                'request-nonce': nonce,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }

            if method == 'GET' or method == 'DELETE':
                if query:
                    url += '?' + self.urlencode(query)
            elif method == 'POST':
                if query:
                    body = self.json(query)
                    auth += body

            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha384).lower()
            headers['request-sign'] = signature

            if debug:
                print(f"Path: /{path}")
                print(f"Nonce: {nonce}")
                print(f"Method: {method}")
                print(f"URL: {url}")
                print(f"Headers: {headers}")
                print(f"Body: {body}")
                print(f"Auth string: {auth}")
                print(f"Signature: {signature}")
                print(f"Headers: {headers}")

        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, request_headers, request_body):
        if response is None:
            return
        if 'status' in response:
            status = self.safe_integer(response, 'status')
            if status == 400:
                errorCode = self.safe_string(response, 'errorCode')
                message = self.safe_string(response, 'message')
                feedback = self.id + ' ' + body
                self.throw_exactly_matched_exception(self.exceptions, errorCode, feedback)
                self.throw_exactly_matched_exception(self.exceptions, message, feedback)
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
            request['end'] = self.sum(since or self.milliseconds(), limit * self.parse_timeframe(timeframe) * 1000)

        response = self.publicGetApiV21Ohlcv(self.extend(request, params))

        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def parse_timeframe(self, timeframe):
        timeframe_map = {
            '1m': 60,
            '5m': 300,
            '15m': 900,
            '30m': 1800,
            '1h': 3600,
            '4h': 14400,
            '6h': 21600,
            '1d': 86400,
            '1w': 604800,
            '1M': 2592000,
        }
        return timeframe_map[timeframe] if timeframe in timeframe_map else None

    def parse_ohlcv(self, ohlcv, market=None):
        return [
            self.safe_integer(ohlcv, 0),  # timestamp
            self.safe_number(ohlcv, 1),  # open
            self.safe_number(ohlcv, 2),  # high
            self.safe_number(ohlcv, 3),  # low
            self.safe_number(ohlcv, 4),  # close
            self.safe_number(ohlcv, 5),  # volume
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

    def publicGetApiV21Ohlcv(self, params={}):
        return self.request('api/v2.1/ohlcv', 'public', 'GET', params)

    def publicGetApiV21(self, endpoint, params={}):
        url = self.urls['api']['public'] + '/api/v2.1/' + endpoint
        return self.fetch(url, 'GET', params)

    def publicGetApiV21FundingHistory(self, params={}):
        return self.request('api/v2.1/funding_history', 'public', 'GET', params)

    def publicGetApiV21Trades(self, params={}):
        return self.request('api/v2.1/trades', 'public', 'GET', params)

    def publicGetApiV21Orderbook(self, params={}):
        return self.request('api/v2.1/orderbook', 'public', 'GET', params)

    def publicGetApiV21OrderbookL2(self, params={}):
        return self.request('api/v2.1/orderbook/L2', 'public', 'GET', params)

    def publicGetApiV21Price(self, params={}):
        return self.request('api/v2.1/price', 'public', 'GET', params)

    def publicGetApiV21MarketSummary(self, params={}):
        return self.request('api/v2.1/market_summary', 'public', 'GET', params)

    def privateGetApiV21UserOpenOrders(self, params={}):
        return self.request('api/v2.1/user/open_orders', 'private', 'GET', params)

    def privateGetApiV21UserTradeHistory(self, params={}):
        return self.request('api/v2.1/user/trade_history', 'private', 'GET', params)

    def privateGetApiV21UserPositions(self, params={}):
        return self.request('api/v2.1/user/positions', 'private', 'GET', params)

    def privateGetApiV21UserWallet(self, params={}):
        return self.request('api/v2.1/user/wallet', 'private', 'GET', params)

    def privateGetApiV21Order(self, params={}):
        return self.request('api/v2.1/order', 'private', 'GET', params)

    def privatePostApiV21Order(self, params={}):
        return self.request('api/v2.1/order', 'private', 'POST', params)

    def privatePostApiV21Leverage(self, params={}):
        return self.request('api/v2.1/leverage', 'private', 'POST', params)

    def privateDeleteApiV21Order(self, params={}):
        path = 'api/v2.1/order'
        return self.request(path, 'private', 'DELETE', params, {}, None)  # Explicitly pass empty headers and body

