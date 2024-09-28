from ccxt.base.exchange import Exchange
import hashlib
from ccxt.base.errors import ExchangeError, AuthenticationError, ArgumentsRequired, BadRequest, BadSymbol, PermissionDenied, RateLimitExceeded, InsufficientFunds, NotSupported


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
                'fetchOHLCV': True,
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
                'setPositionMode': True,
                'fetchOpenInterest': True,
                'setLeverage': True,
                'setMarginMode': True,
                'fetchPositionsRisk': True,
                'closePosition': True,
                'fetchFees': True,
                'fetchTradingFees': True,
            },
            'urls': {
                'logo': 'https://github.com/user-attachments/assets/227c21b7-00f6-4911-8ca1-cf3a2dc357b6',
                'test': {
                    'public': 'https://test-api.lmex.io/futures',
                    'private': 'https://test-api.lmex.io/futures',
                    'www': 'https://test.lmex.io',
                },
                'api': {
                    'public': 'https://api.lmex.io/futures',
                    'private': 'https://api.lmex.io/futures',
                },
                'www': 'https://www.lmex.io',
                'doc': 'https://docs.lmex.io',
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
                        'api/v2.1/risk_limit',
                        'api/v2.1/leverage',
                        'api/v2.1/user/fees',
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

# Market data methods
    def fetch_markets(self, params={}):
        """
            Retrieves market data for all available trading pairs
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-market_summary
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of market structures
        """
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
        """
            Fetches a price ticker for a specific market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-price
            :param str symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A ticker structure
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetApiV21Price(self.extend(request, params))
        ticker = self.safe_value(response, 0)
        return self.parse_ticker(ticker, market)

    def fetch_tickers(self, symbols=None, params={}):
        """
            Fetches price tickers for multiple markets
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-market_summary
            :param [str]|None symbols: List of unified market symbols, all tickers are returned if None
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A dictionary of ticker structures
        """
        self.load_markets()
        response = self.request('api/v2.1/market_summary', 'public', 'GET', params)
        result = {}
        for ticker in response:
            market = self.safe_market(ticker['symbol'])
            parsed = self.parse_ticker(ticker, market)
            symbol = parsed['symbol']
            result[symbol] = parsed
        return self.filter_by_array(result, 'symbol', symbols)

    def fetch_order_book(self, symbol, limit=None, params={}):
        """
        Fetches information on open orders with bid and ask data
        :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-orderbook-L2
        :param str symbol: Unified market symbol
        :param int|None limit: The maximum number of order book entries to return
        :param dict params: Extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of order book structures
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
        """
            Fetches information on past trades for a given market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-trades
            :param str symbol: Unified market symbol
            :param int|None since: Timestamp in ms of the earliest trade to fetch
            :param int|None limit: The maximum number of trades to fetch
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of trade structures
        """
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

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
            Fetch historical candlestick data containing the open, high, low, and close price, and the volume of a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-ohlcv
            :param str symbol: Unified symbol of the market to fetch OHLCV data for
            :param str timeframe: The length of time each candle represents
            :param int|None since: Timestamp in ms of the earliest candle to fetch
            :param int|None limit: The maximum amount of candles to fetch
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [[int]]: A list of candles ordered as timestamp, open, high, low, close, volume
        """
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

    def fetch_funding_rate(self, symbol, params={}):
        """
            Fetch the current funding rate for a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-funding_history
            :param str symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A funding rate structure
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetApiV21FundingHistory(self.extend(request, params))
        # {
        #   "BTC-PERP": [
        #     {
        #       "time": 1706515200,
        #       "rate": 0.000011405,
        #       "symbol": "BTC-PERP"
        #     }
        #   ]
        # }
        return self.parse_funding_rate(response, market)

    def fetch_funding_rate_history(self, symbol=None, since=None, limit=None, params={}):
        """
            Fetches historical funding rate prices
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-funding_history
            :param str|None symbol: Unified symbol of the market to fetch the funding rate history for
            :param int|None since: Timestamp in ms of the earliest funding rate to fetch
            :param int|None limit: The maximum amount of funding rate structures to fetch
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: A list of funding rate structures
        """
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

    def fetch_open_interest(self, symbol, params={}):
        """
            Fetch the open interest of a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-market_summary
            :param str symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: An open interest structure
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetApiV21MarketSummary(self.extend(request, params))

        # Find the market summary for the requested symbol
        marketSummary = None
        for summary in response:
            if summary['symbol'] == market['id']:
                marketSummary = summary
                break

        if marketSummary is None:
            raise ExchangeError(self.id + ' fetchOpenInterest() could not find market summary for symbol ' + symbol)

        return self.parse_open_interest(marketSummary, market)

# Account methods
    def fetch_balance(self, params={}):
        """
            Query for balance and get the amount of funds available for trading or funds locked in orders
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-wallet
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A balance structure
        """
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

    def fetch_fees(self, params={}):
        """
        Fetch the trading fees for all markets
        :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-fees
        :param dict params: Extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of fee structures indexed by market symbols
        """
        self.load_markets()
        response = self.privateGetApiV21UserFees(params)

        result = {
            'info': response,
            'maker': {},
            'taker': {},
        }

        for fee_info in response:
            market_id = self.safe_string(fee_info, 'symbol')
            market = self.safe_market(market_id)
            symbol = market['symbol']

            maker_fee = self.safe_number(fee_info, 'makerFee')
            taker_fee = self.safe_number(fee_info, 'takerFee')

            result['maker'][symbol] = maker_fee
            result['taker'][symbol] = taker_fee

        return result

    fetchTradingFees = fetch_fees

# Trading methods
    def create_order(self, symbol, type, side, amount, price=None, params={}):
        """
            Create a trade order
            :see: https://docs.lmex.io/pages/futures.html#/operations/post-api-v2.1-order
            :param str symbol: Unified symbol of the market to create an order in
            :param str type: 'market' or 'limit'
            :param str side: 'buy' or 'sell'
            :param float amount: How much of currency you want to trade in units of base currency
            :param float|None price: The price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: An order structure
        """
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

    def cancel_order(self, id, symbol=None, params={}):
        """
            Cancels an open order
            :see: https://docs.lmex.io/pages/futures.html#/operations/delete-api-v2.1-order
            :param str id: Order id
            :param str|None symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: An order structure
        """
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
        """
            Fetches information on an order
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-order
            :param str id: Order id
            :param str|None symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: An order structure
        """
        self.load_markets()
        request = {
            'orderID': id,
        }
        if symbol is not None:
            request['symbol'] = self.market_id(symbol)
        response = self.privateGetApiV21Order(self.extend(request, params))
        return self.parse_order(response)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        """
            Fetches information on multiple open orders
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-open_orders
            :param str|None symbol: Unified market symbol
            :param int|None since: The earliest time in ms to fetch open orders for
            :param int|None limit: The maximum number of open orders structures to retrieve
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of order structures
        """
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        response = self.privateGetApiV21UserOpenOrders(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        """
            Fetches information on multiple closed orders
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-trade_history
            :param str|None symbol: Unified market symbol
            :param int|None since: The earliest time in ms to fetch closed orders for
            :param int|None limit: The maximum number of closed orders structures to retrieve
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of order structures
        """
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
        """
            Fetches information on multiple trades made by the user
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-trade_history
            :param str|None symbol: Unified market symbol
            :param int|None since: The earliest time in ms to fetch trades for
            :param int|None limit: The maximum number of trade structures to retrieve
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of trade structures
        """
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

# Positions and leverage methods
    def fetch_positions(self, symbols=None, params={}):
        """
            Fetch all open positions
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-positions
            :param [str]|None symbols: List of unified market symbols
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: An array of position structures
        """
        self.load_markets()
        response = self.privateGetApiV21UserPositions(params)
        return self.parse_positions(response, symbols)

    def fetch_positions_risk(self, symbols=None, params={}):
        """
            Fetch positions with risk data
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-user-positions
            :param [str]|None symbols: List of unified market symbols
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns [dict]: A list of position risk structures
        """
        self.load_markets()
        response = self.privateGetApiV21UserPositions(params)

        result = []
        for position in response:
            if symbols is None or self.safe_string(position, 'symbol') in symbols:
                result.append(self.parse_position_risk(position))

        return result

    def close_position(self, symbol, side=None, params={}):
        """
            Close an open position
            :see: https://docs.lmex.io/pages/futures.html#/operations/post-api-v2.1-order-close_position
            :param str symbol: Unified market symbol
            :param str|None side: 'buy' or 'sell' for closing a short or long position respectively
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: An order structure
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'type': 'MARKET',  # LMEX uses 'MARKET' for market orders
        }

        # LMEX requires positionId for hedge mode
        position_mode = self.safe_string(params, 'positionMode')
        if position_mode == 'HEDGE':
            if side is None:
                raise ArgumentsRequired(self.id + ' closePosition() requires a side parameter for hedge mode')
            position_id = self.safe_string(params, 'positionId')
            if position_id is None:
                raise ArgumentsRequired(self.id + ' closePosition() requires a positionId parameter for hedge mode')
            request['positionId'] = position_id
        elif side is not None:
            request['side'] = 'SELL' if side.upper() == 'BUY' else 'BUY'  # Reverse the side to close the position

        response = self.privatePostApiV21OrderClosePosition(self.extend(request, params))

        return self.parse_order(response)

    def fetch_leverage(self, symbol, params={}):
        """
            Fetch the set leverage for a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-leverage
            :param str symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A leverage structure
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.privateGetApiV21Leverage(self.extend(request, params))
        return self.parse_leverage(response)

    def set_leverage(self, leverage, symbol=None, params={}):
        """
            Set the level of leverage for a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/post-api-v2.1-leverage
            :param float leverage: The desired leverage, use 0 for cross margin
            :param str|None symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: Response from the exchange
        """
        self.load_markets()
        if symbol is None:
            raise ArgumentsRequired(self.id + ' setLeverage() requires a symbol argument')
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'leverage': leverage,
        }
        return self.privatePostApiV21Leverage(self.extend(request, params))

    def fetch_leverage_tiers(self, symbols=None, params={}):
        """
            Retrieve information on the maximum leverage, and maintenance margin for trades of varying trade sizes
            :see: https://docs.lmex.io/pages/futures.html#/operations/get-api-v2.1-leverage
            :param [str]|None symbols: A list of unified market symbols
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: A dictionary of leverage tiers structures, indexed by market symbols
        """
        self.load_markets()
        result = {}
        for symbol in symbols:
            market = self.market(symbol)
            request = {
                'symbol': market['id'],
            }
            response = self.privateGetApiV21Leverage(self.extend(request, params))
            result[symbol] = self.parse_leverage_tiers(response, market)
        return result

    def set_position_mode(self, hedged: bool, symbol=None, params={}):
        """
            Set hedged to True or False for a market
            :see: https://docs.lmex.io/pages/futures.html#/operations/post-api-v2.1-position_mode
            :param bool hedged: Set to True to use HEDGE_MODE, False for ONE_WAY
            :param str|None symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: Response from the exchange
        """
        hedgeMode = 'HEDGE' if hedged else 'ONE_WAY'
        request: dict = {
            'positionMode': hedgeMode,
            'symbol': symbol,
        }
        response = self.privatePostApiV21PositionMode(self.extend(request, params))
        # {
        #   "symbol": "string",
        #   "timestamp": 0,
        #   "status": "string",
        #   "type": "string",
        #   "message": "string"
        # }
        if 'success' in response and not response['success']:
            raise ExchangeError(self.id + ' setPositionMode() failed: ' + self.json(response))
        return response

    def set_margin_mode(self, marginMode, symbol=None, params={}):
        """
            Set margin mode to 'cross' or 'isolated'
            :see: https://docs.lmex.io/pages/futures.html#/operations/post-api-v2.1-leverage
            :param str marginMode: 'cross' or 'isolated'
            :param str symbol: Unified market symbol
            :param dict params: Extra parameters specific to the exchange API endpoint
            :returns dict: Response from the exchange
        """
        if symbol is None:
            raise ArgumentsRequired(self.id + ' setMarginMode() requires a symbol argument')

        self.load_markets()
        market = self.market(symbol)

        marginMode = marginMode.upper()
        if marginMode != 'CROSS' and marginMode != 'ISOLATED':
            raise BadRequest(self.id + ' setMarginMode() marginMode must be either "cross" or "isolated"')

        request = {
            'symbol': market['id'],
            'leverage': 0 if marginMode == 'CROSS' else None,  # 0 means maximum leverage for cross mode
            'marginMode': marginMode,
        }

        # LMEX uses the leverage endpoint to set margin mode
        response = self.privatePostApiV21Leverage(self.extend(request, params))

        return {
            'info': response,
            'type': marginMode.lower()
        }

# Parsing methods
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

    def parse_tickers(self, response, symbols=None):
        result = {}
        for ticker in response:
            parsed = self.parse_ticker(ticker)
            symbol = parsed['symbol']
            result[symbol] = parsed
        return self.filter_by_array(result, 'symbol', symbols)

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

    def parse_leverage(self, leverage):
        return {
            'info': leverage,
            'leverage': self.safe_number(leverage, 'leverage'),
        }

    def parse_funding_rate(self, fundingRate, market=None):
        data = self.safe_value(fundingRate, market['id'], [])
        latest = self.safe_value(data, 0, {})
        timestamp = self.safe_timestamp(latest, 'time')
        return {
            'info': fundingRate,
            'symbol': market['symbol'],
            'markPrice': None,
            'indexPrice': None,
            'interestRate': None,
            'estimatedSettlePrice': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'fundingRate': self.safe_number(latest, 'rate'),
            'fundingTimestamp': timestamp,
            'fundingDatetime': self.iso8601(timestamp),
            'nextFundingRate': None,
            'nextFundingTimestamp': None,
            'nextFundingDatetime': None,
            'previousFundingRate': None,
            'previousFundingTimestamp': None,
            'previousFundingDatetime': None,
        }

    def parse_order(self, order, market=None):
        order = self.safe_value(order, 0, order)  # LMEX returns an array with one order
        id = self.safe_string(order, 'orderID')
        timestamp = self.safe_integer(order, 'timestamp')
        symbol = self.safe_symbol(self.safe_string(order, 'symbol'), market)
        type_raw = self.safe_integer(order, 'orderType')
        type = 'limit' if type_raw == 76 else 'market' if type_raw == 77 else 'algo' if type_raw == 80 else 'unknown'
        side = self.safe_string_lower(order, 'side')
        price = self.safe_number(order, 'price')
        amount = self.safe_number(order, 'size')
        filled = self.safe_number_2(order, 'fillSize', 'filledSize')  # Handle both fillSize and filledSize
        remaining = self.safe_number(order, 'remainingSize')
        if remaining is None and amount is not None and filled is not None:
            remaining = amount - filled
        status_raw = self.safe_string(order, 'status')
        status = self.parse_order_status(
            int(status_raw) if status_raw is not None else self.safe_string(order, 'orderState'))
        average = self.safe_number_2(order, 'avgFillPrice', 'averageFillPrice')
        cost = self.safe_number(order, 'orderValue')
        if cost is None:
            if filled is not None and average is not None:
                cost = filled * average
            elif amount is not None and price is not None:
                cost = amount * price

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
            'postOnly': self.safe_value(order, 'postOnly'),
            'side': side,
            'price': price,
            'stopPrice': self.safe_number(order, 'triggerPrice'),
            'average': average,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'cost': cost,
            'trades': None,  # LMEX doesn't provide this in the order response
            'fee': None,  # LMEX doesn't provide this in the order response
            'info': order,
            'reduceOnly': self.safe_value(order, 'reduceOnly'),
            'triggerPrice': self.safe_number(order, 'triggerPrice'),
            'contract': self.safe_number(order, 'contractSize'),
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
            'STATUS_ACTIVE': 'open',
            'STATUS_INACTIVE': 'canceled',
        }
        if isinstance(status, str) and status.isdigit():
            status = int(status)
        return self.safe_string(statuses, status, 'unknown')

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

    def parse_leverage_tiers(self, response, market=None):
        leverage = self.safe_number(response, 'leverage')
        return [
            {
                'tier': 1,
                'currency': market['quote'],
                'minNotional': 0,
                'maxNotional': float('inf'),  # Assuming no upper limit
                'maintenanceMarginRate': None,  # LMEX doesn't provide this information
                'maxLeverage': leverage,
                'info': response,
            }
        ]

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

    def parse_open_interest(self, interest, market=None):
        """
        Parse the open interest returned by the exchange
        :param dict interest: open interest structure as returned by the exchange
        :param dict market: CCXT market
        """
        timestamp = self.milliseconds()
        symbol = self.safe_symbol(None, market)
        openInterestAmount = self.safe_number(interest, 'openInterest')
        openInterestValue = self.safe_number(interest, 'openInterestUSD')
        return {
            'symbol': symbol,
            'openInterestAmount': openInterestAmount,
            'openInterestValue': openInterestValue,
            'baseVolume': openInterestAmount,  # deprecated, use openInterestAmount instead
            'quoteVolume': openInterestValue,  # deprecated, use openInterestValue instead
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'info': interest,
        }

    def parse_position_risk(self, position, market=None):
        """
        Parse the position risk returned by the exchange
        :param dict position: position structure as returned by the exchange
        :param dict market: CCXT market
        """
        market_id = self.safe_string(position, 'symbol')
        market = self.safe_market(market_id, market)
        symbol = market['symbol']
        side = self.safe_string_lower(position, 'side')
        amount = self.safe_number(position, 'size')
        if side == 'sell':
            amount = -amount

        timestamp = self.safe_integer(position, 'timestamp')

        return {
            'info': position,
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'initialMargin': self.safe_number(position, 'orderValue'),
            'initialMarginPercentage': None,
            'maintenanceMargin': self.safe_number(position, 'totalMaintenanceMargin'),
            'maintenanceMarginPercentage': None,
            'entryPrice': self.safe_number(position, 'entryPrice'),
            'notional': self.safe_number(position, 'orderValue'),
            'leverage': self.safe_number(position, 'isolatedLeverage'),
            'unrealizedPnl': self.safe_number(position, 'unrealizedProfitLoss'),
            'contracts': abs(amount),
            'contractSize': self.safe_number(market, 'contractSize'),
            'marginRatio': None,
            'liquidationPrice': self.safe_number(position, 'liquidationPrice'),
            'markPrice': self.safe_number(position, 'markPrice'),
            'collateral': self.safe_number(position, 'orderValue'),
            'marginMode': 'isolated' if self.safe_number(position, 'isolatedLeverage') else 'cross',
            'side': 'long' if amount > 0 else 'short',
            'percentage': None,
            'hedged': self.safe_string(position, 'positionMode') == 'HEDGE',
            'delta': None,
            # Additional risk-related fields
            'liquidationPriceDistance': None,  # Not provided by LMEX
            'liquidationFundingRateDiff': None,  # Not provided by LMEX
            'adlRankIndicator': self.safe_integer(position, 'adlScoreBucket'),
            'currentLeverage': self.safe_number(position, 'currentLeverage'),
        }

# Request handling methods
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

# API-specific methods
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

    def privateGetApiV21Leverage(self, params={}):
        return self.request('api/v2.1/leverage', 'private', 'GET', params)

    def privateDeleteApiV21Order(self, params={}):
        path = 'api/v2.1/order'
        return self.request(path, 'private', 'DELETE', params, {}, None)  # Explicitly pass empty headers and body

    def privatePostApiV21PositionMode(self, params={}):
        return self.request('api/v2.1/position_mode', 'private', 'POST', params)

    def privatePostApiV21OrderClosePosition(self, params={}):
        return self.request('api/v2.1/order/close_position', 'private', 'POST', params)

    def privateGetApiV21RiskLimit(self, params={}):
        return self.request('api/v2.1/risk_limit', 'private', 'GET', params)

    def  privateGetApiV21UserFees(self, params={}):
        return self.request('api/v2.1/user/fees', 'private', 'GET', params)


