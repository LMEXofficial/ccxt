namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


public partial class kraken
{
    /// <summary>
    /// retrieves data on all markets for kraken
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getTradableAssetPairs"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> an array of objects representing market data.</returns>
    public async Task<List<MarketInterface>> FetchMarkets(Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchMarkets(parameters);
        return ((IList<object>)res).Select(item => new MarketInterface(item)).ToList<MarketInterface>();
    }
    /// <summary>
    /// the latest known information on the availability of the exchange API
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/api/docs/rest-api/get-system-status/"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [status structure]{@link https://docs.ccxt.com/#/?id=exchange-status-structure}.</returns>
    public async Task<Dictionary<string, object>> FetchStatus(Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchStatus(parameters);
        return ((Dictionary<string, object>)res);
    }
    /// <summary>
    /// fetch the trading fees for a market
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getTradeVolume"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [fee structure]{@link https://docs.ccxt.com/#/?id=fee-structure}.</returns>
    public async Task<TradingFeeInterface> FetchTradingFee(string symbol, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchTradingFee(symbol, parameters);
        return new TradingFeeInterface(res);
    }
    /// <summary>
    /// fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getOrderBook"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum amount of order book entries to return
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> A dictionary of [order book structures]{@link https://docs.ccxt.com/#/?id=order-book-structure} indexed by market symbols.</returns>
    public async Task<OrderBook> FetchOrderBook(string symbol, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchOrderBook(symbol, limit, parameters);
        return new OrderBook(res);
    }
    /// <summary>
    /// fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getTickerInformation"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a dictionary of [ticker structures]{@link https://docs.ccxt.com/#/?id=ticker-structure}.</returns>
    public async Task<Tickers> FetchTickers(List<String> symbols = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchTickers(symbols, parameters);
        return new Tickers(res);
    }
    /// <summary>
    /// fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getTickerInformation"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [ticker structure]{@link https://docs.ccxt.com/#/?id=ticker-structure}.</returns>
    public async Task<Ticker> FetchTicker(string symbol, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchTicker(symbol, parameters);
        return new Ticker(res);
    }
    /// <summary>
    /// fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getOHLCData"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : timestamp in ms of the earliest candle to fetch
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum amount of candles to fetch
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.paginate</term>
    /// <description>
    /// boolean : default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>int[][]</term> A list of candles ordered as timestamp, open, high, low, close, volume.</returns>
    public async Task<List<OHLCV>> FetchOHLCV(string symbol, string timeframe = "1m", Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchOHLCV(symbol, timeframe, since, limit, parameters);
        return ((IList<object>)res).Select(item => new OHLCV(item)).ToList<OHLCV>();
    }
    /// <summary>
    /// fetch the history of changes, actions done by the user or operations that altered the balance of the user
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getLedgers"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>code</term>
    /// <description>
    /// string : unified currency code, default is undefined
    /// </description>
    /// </item>
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : timestamp in ms of the earliest ledger entry, default is undefined
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : max number of ledger entries to return, default is undefined
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.until</term>
    /// <description>
    /// int : timestamp in ms of the latest ledger entry
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.end</term>
    /// <description>
    /// int : timestamp in seconds of the latest ledger entry
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [ledger structure]{@link https://docs.ccxt.com/#/?id=ledger-structure}.</returns>
    public async Task<List<LedgerEntry>> FetchLedger(string code = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchLedger(code, since, limit, parameters);
        return ((IList<object>)res).Select(item => new LedgerEntry(item)).ToList<LedgerEntry>();
    }
    public async Task<List<LedgerEntry>> FetchLedgerEntriesByIds(object ids, string code = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchLedgerEntriesByIds(ids, code, parameters);
        return ((IList<object>)res).Select(item => new LedgerEntry(item)).ToList<LedgerEntry>();
    }
    public async Task<LedgerEntry> FetchLedgerEntry(string id, string code = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchLedgerEntry(id, code, parameters);
        return new LedgerEntry(res);
    }
    /// <summary>
    /// get the list of most recent trades for a particular symbol
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getRecentTrades"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : timestamp in ms of the earliest trade to fetch
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum amount of trades to fetch
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>Trade[]</term> a list of [trade structures]{@link https://docs.ccxt.com/#/?id=public-trades}.</returns>
    public async Task<List<Trade>> FetchTrades(string symbol, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchTrades(symbol, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Trade(item)).ToList<Trade>();
    }
    /// <summary>
    /// query for balance and get the amount of funds available for trading or funds locked in orders
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getExtendedBalance"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [balance structure]{@link https://docs.ccxt.com/#/?id=balance-structure}.</returns>
    public async Task<Balances> FetchBalance(Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchBalance(parameters);
        return new Balances(res);
    }
    /// <summary>
    /// create a market order by providing the symbol, side and cost
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/addOrder"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> CreateMarketOrderWithCost(string symbol, string side, double cost, Dictionary<string, object> parameters = null)
    {
        var res = await this.createMarketOrderWithCost(symbol, side, cost, parameters);
        return new Order(res);
    }
    /// <summary>
    /// create a market buy order by providing the symbol, side and cost
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/addOrder"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> CreateMarketBuyOrderWithCost(string symbol, double cost, Dictionary<string, object> parameters = null)
    {
        var res = await this.createMarketBuyOrderWithCost(symbol, cost, parameters);
        return new Order(res);
    }
    /// <summary>
    /// create a trade order
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/addOrder"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>price</term>
    /// <description>
    /// float : the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.postOnly</term>
    /// <description>
    /// bool : if true, the order will only be posted to the order book and not executed immediately
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.reduceOnly</term>
    /// <description>
    /// bool : *margin only* indicates if this order is to reduce the size of a position
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.stopLossPrice</term>
    /// <description>
    /// float : *margin only* the price that a stop loss order is triggered at
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.takeProfitPrice</term>
    /// <description>
    /// float : *margin only* the price that a take profit order is triggered at
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trailingAmount</term>
    /// <description>
    /// string : *margin only* the quote amount to trail away from the current market price
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trailingLimitAmount</term>
    /// <description>
    /// string : *margin only* the quote amount away from the trailingAmount
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.offset</term>
    /// <description>
    /// string : *margin only* '+' or '-' whether you want the trailingLimitAmount value to be positive or negative, default is negative '-'
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trigger</term>
    /// <description>
    /// string : *margin only* the activation price type, 'last' or 'index', default is 'last'
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> CreateOrder(string symbol, string type, string side, double amount, double? price2 = 0, Dictionary<string, object> parameters = null)
    {
        var price = price2 == 0 ? null : (object)price2;
        var res = await this.createOrder(symbol, type, side, amount, price, parameters);
        return new Order(res);
    }
    /// <summary>
    /// edit a trade order
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/editOrder"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>price</term>
    /// <description>
    /// float : the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.stopLossPrice</term>
    /// <description>
    /// float : *margin only* the price that a stop loss order is triggered at
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.takeProfitPrice</term>
    /// <description>
    /// float : *margin only* the price that a take profit order is triggered at
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trailingAmount</term>
    /// <description>
    /// string : *margin only* the quote price away from the current market price
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trailingLimitAmount</term>
    /// <description>
    /// string : *margin only* the quote amount away from the trailingAmount
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.offset</term>
    /// <description>
    /// string : *margin only* '+' or '-' whether you want the trailingLimitAmount value to be positive or negative, default is negative '-'
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.trigger</term>
    /// <description>
    /// string : *margin only* the activation price type, 'last' or 'index', default is 'last'
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> EditOrder(string id, string symbol, string type, string side, double? amount2 = 0, double? price2 = 0, Dictionary<string, object> parameters = null)
    {
        var amount = amount2 == 0 ? null : (object)amount2;
        var price = price2 == 0 ? null : (object)price2;
        var res = await this.editOrder(id, symbol, type, side, amount, price, parameters);
        return new Order(res);
    }
    /// <summary>
    /// fetches information on an order made by the user
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getOrdersInfo"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> An [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> FetchOrder(string id, string symbol = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchOrder(id, symbol, parameters);
        return new Order(res);
    }
    /// <summary>
    /// fetch all the trades made from a single order
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getTradesInfo"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch trades for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of trades to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [trade structures]{@link https://docs.ccxt.com/#/?id=trade-structure}.</returns>
    public async Task<List<Trade>> FetchOrderTrades(string id, string symbol = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchOrderTrades(id, symbol, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Trade(item)).ToList<Trade>();
    }
    /// <summary>
    /// fetch orders by the list of order id
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getClosedOrders"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the kraken api endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<List<Dictionary<string, object>>> FetchOrdersByIds(object ids, string symbol = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchOrdersByIds(ids, symbol, parameters);
        return ((IList<object>)res).Select(item => (item as Dictionary<string, object>)).ToList();
    }
    /// <summary>
    /// fetch all trades made by the user
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getTradeHistory"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch trades for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of trades structures to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.until</term>
    /// <description>
    /// int : timestamp in ms of the latest trade entry
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.end</term>
    /// <description>
    /// int : timestamp in seconds of the latest trade entry
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>Trade[]</term> a list of [trade structures]{@link https://docs.ccxt.com/#/?id=trade-structure}.</returns>
    public async Task<List<Trade>> FetchMyTrades(string symbol = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchMyTrades(symbol, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Trade(item)).ToList<Trade>();
    }
    /// <summary>
    /// cancels an open order
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/cancelOrder"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> An [order structure]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<Order> CancelOrder(string id, string symbol = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.cancelOrder(id, symbol, parameters);
        return new Order(res);
    }
    /// <summary>
    /// cancel multiple orders
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/cancelOrderBatch"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an list of [order structures]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<List<Order>> CancelOrders(object ids, string symbol = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.cancelOrders(ids, symbol, parameters);
        return ((IList<object>)res).Select(item => new Order(item)).ToList<Order>();
    }
    /// <summary>
    /// cancel all open orders
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/cancelAllOrders"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [order structures]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<List<Order>> CancelAllOrders(string symbol = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.cancelAllOrders(symbol, parameters);
        return ((IList<object>)res).Select(item => new Order(item)).ToList<Order>();
    }
    /// <summary>
    /// dead man's switch, cancel all orders after the given timeout
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Trading/operation/cancelAllOrdersAfter"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> the api result.</returns>
    public async Task<Dictionary<string, object>> CancelAllOrdersAfter(Int64 timeout, Dictionary<string, object> parameters = null)
    {
        var res = await this.cancelAllOrdersAfter(timeout, parameters);
        return ((Dictionary<string, object>)res);
    }
    /// <summary>
    /// fetch all unfilled currently open orders
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getOpenOrders"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch open orders for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of  open orders structures to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>Order[]</term> a list of [order structures]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<List<Order>> FetchOpenOrders(string symbol = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchOpenOrders(symbol, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Order(item)).ToList<Order>();
    }
    /// <summary>
    /// fetches information on multiple closed orders made by the user
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getClosedOrders"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch orders for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of order structures to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.until</term>
    /// <description>
    /// int : timestamp in ms of the latest entry
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>Order[]</term> a list of [order structures]{@link https://docs.ccxt.com/#/?id=order-structure}.</returns>
    public async Task<List<Order>> FetchClosedOrders(string symbol = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchClosedOrders(symbol, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Order(item)).ToList<Order>();
    }
    /// <summary>
    /// fetch all deposits made to an account
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/getStatusRecentDeposits"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch deposits for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of deposits structures to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.until</term>
    /// <description>
    /// int : timestamp in ms of the latest transaction entry
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.end</term>
    /// <description>
    /// int : timestamp in seconds of the latest transaction entry
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [transaction structures]{@link https://docs.ccxt.com/#/?id=transaction-structure}.</returns>
    public async Task<List<Transaction>> FetchDeposits(string code = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchDeposits(code, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Transaction(item)).ToList<Transaction>();
    }
    /// <summary>
    /// fetches the current integer timestamp in milliseconds from the exchange server
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Spot-Market-Data/operation/getServerTime"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>int</term> the current integer timestamp in milliseconds from the exchange server.</returns>
    public async Task<Int64> FetchTime(Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchTime(parameters);
        return (Int64)res;
    }
    /// <summary>
    /// fetch all withdrawals made from an account
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/getStatusRecentWithdrawals"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>since</term>
    /// <description>
    /// int : the earliest time in ms to fetch withdrawals for
    /// </description>
    /// </item>
    /// <item>
    /// <term>limit</term>
    /// <description>
    /// int : the maximum number of withdrawals structures to retrieve
    /// </description>
    /// </item>
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.until</term>
    /// <description>
    /// int : timestamp in ms of the latest transaction entry
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.end</term>
    /// <description>
    /// int : timestamp in seconds of the latest transaction entry
    /// </description>
    /// </item>
    /// <item>
    /// <term>params.paginate</term>
    /// <description>
    /// boolean : default false, when true will automatically paginate by calling this endpoint multiple times
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [transaction structures]{@link https://docs.ccxt.com/#/?id=transaction-structure}.</returns>
    public async Task<List<Transaction>> FetchWithdrawals(string code = null, Int64? since2 = 0, Int64? limit2 = 0, Dictionary<string, object> parameters = null)
    {
        var since = since2 == 0 ? null : (object)since2;
        var limit = limit2 == 0 ? null : (object)limit2;
        var res = await this.fetchWithdrawals(code, since, limit, parameters);
        return ((IList<object>)res).Select(item => new Transaction(item)).ToList<Transaction>();
    }
    /// <summary>
    /// create a currency deposit address
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/getDepositAddresses"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [address structure]{@link https://docs.ccxt.com/#/?id=address-structure}.</returns>
    public async Task<Dictionary<string, object>> CreateDepositAddress(string code, Dictionary<string, object> parameters = null)
    {
        var res = await this.createDepositAddress(code, parameters);
        return ((Dictionary<string, object>)res);
    }
    /// <summary>
    /// fetch deposit methods for a currency associated with this account
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/getDepositMethods"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the kraken api endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> of deposit methods.</returns>
    public async Task<Dictionary<string, object>> FetchDepositMethods(string code, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchDepositMethods(code, parameters);
        return ((Dictionary<string, object>)res);
    }
    /// <summary>
    /// fetch the deposit address for a currency associated with this account
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/getDepositAddresses"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> an [address structure]{@link https://docs.ccxt.com/#/?id=address-structure}.</returns>
    public async Task<Dictionary<string, object>> FetchDepositAddress(string code, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchDepositAddress(code, parameters);
        return ((Dictionary<string, object>)res);
    }
    /// <summary>
    /// make a withdrawal
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Funding/operation/withdrawFunds"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object</term> a [transaction structure]{@link https://docs.ccxt.com/#/?id=transaction-structure}.</returns>
    public async Task<Transaction> Withdraw(string code, double amount, string address, object tag = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.withdraw(code, amount, address, tag, parameters);
        return new Transaction(res);
    }
    /// <summary>
    /// fetch all open positions
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/Account-Data/operation/getOpenPositions"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : extra parameters specific to the exchange API endpoint
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>object[]</term> a list of [position structure]{@link https://docs.ccxt.com/#/?id=position-structure}.</returns>
    public async Task<List<Position>> FetchPositions(List<String> symbols = null, Dictionary<string, object> parameters = null)
    {
        var res = await this.fetchPositions(symbols, parameters);
        return ((IList<object>)res).Select(item => new Position(item)).ToList<Position>();
    }
    public async Task<TransferEntry> TransferOut(string code, object amount, Dictionary<string, object> parameters = null)
    {
        var res = await this.transferOut(code, amount, parameters);
        return new TransferEntry(res);
    }
    /// <summary>
    /// transfers currencies between sub-accounts (only spot->swap direction is supported)
    /// </summary>
    /// <remarks>
    /// See <see href="https://docs.kraken.com/rest/#tag/User-Funding/operation/walletTransfer"/>  <br/>
    /// <list type="table">
    /// <item>
    /// <term>params</term>
    /// <description>
    /// object : Exchange specific parameters
    /// </description>
    /// </item>
    /// </list>
    /// </remarks>
    /// <returns> <term>undefined</term> undefined.</returns>
    public async Task<TransferEntry> Transfer(string code, double amount, string fromAccount, string toAccount, Dictionary<string, object> parameters = null)
    {
        var res = await this.transfer(code, amount, fromAccount, toAccount, parameters);
        return new TransferEntry(res);
    }
}
