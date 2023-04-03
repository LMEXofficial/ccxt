<?php

namespace ccxt\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class timex extends \ccxt\Exchange {
    public function addressbook_get_me($params = array()) {
        return $this->request('me', 'addressbook', 'GET', $params);
    }
    public function addressbook_post($params = array()) {
        return $this->request('', 'addressbook', 'POST', $params);
    }
    public function addressbook_post_id_id($params = array()) {
        return $this->request('id/{id}', 'addressbook', 'POST', $params);
    }
    public function addressbook_post_id_id_remove($params = array()) {
        return $this->request('id/{id}/remove', 'addressbook', 'POST', $params);
    }
    public function custody_get_credentials($params = array()) {
        return $this->request('credentials', 'custody', 'GET', $params);
    }
    public function custody_get_credentials_h_hash($params = array()) {
        return $this->request('credentials/h/{hash}', 'custody', 'GET', $params);
    }
    public function custody_get_credentials_k_key($params = array()) {
        return $this->request('credentials/k/{key}', 'custody', 'GET', $params);
    }
    public function custody_get_credentials_me($params = array()) {
        return $this->request('credentials/me', 'custody', 'GET', $params);
    }
    public function custody_get_credentials_me_address($params = array()) {
        return $this->request('credentials/me/address', 'custody', 'GET', $params);
    }
    public function custody_get_deposit_addresses($params = array()) {
        return $this->request('deposit-addresses', 'custody', 'GET', $params);
    }
    public function custody_get_deposit_addresses_h_hash($params = array()) {
        return $this->request('deposit-addresses/h/{hash}', 'custody', 'GET', $params);
    }
    public function history_get_orders($params = array()) {
        return $this->request('orders', 'history', 'GET', $params);
    }
    public function history_get_orders_details($params = array()) {
        return $this->request('orders/details', 'history', 'GET', $params);
    }
    public function history_get_orders_export_csv($params = array()) {
        return $this->request('orders/export/csv', 'history', 'GET', $params);
    }
    public function history_get_trades($params = array()) {
        return $this->request('trades', 'history', 'GET', $params);
    }
    public function history_get_trades_export_csv($params = array()) {
        return $this->request('trades/export/csv', 'history', 'GET', $params);
    }
    public function currencies_get_a_address($params = array()) {
        return $this->request('a/{address}', 'currencies', 'GET', $params);
    }
    public function currencies_get_i_id($params = array()) {
        return $this->request('i/{id}', 'currencies', 'GET', $params);
    }
    public function currencies_get_s_symbol($params = array()) {
        return $this->request('s/{symbol}', 'currencies', 'GET', $params);
    }
    public function currencies_post_perform($params = array()) {
        return $this->request('perform', 'currencies', 'POST', $params);
    }
    public function currencies_post_prepare($params = array()) {
        return $this->request('prepare', 'currencies', 'POST', $params);
    }
    public function currencies_post_remove_perform($params = array()) {
        return $this->request('remove/perform', 'currencies', 'POST', $params);
    }
    public function currencies_post_s_symbol_remove_prepare($params = array()) {
        return $this->request('s/{symbol}/remove/prepare', 'currencies', 'POST', $params);
    }
    public function currencies_post_s_symbol_update_perform($params = array()) {
        return $this->request('s/{symbol}/update/perform', 'currencies', 'POST', $params);
    }
    public function currencies_post_s_symbol_update_prepare($params = array()) {
        return $this->request('s/{symbol}/update/prepare', 'currencies', 'POST', $params);
    }
    public function manager_get_deposits($params = array()) {
        return $this->request('deposits', 'manager', 'GET', $params);
    }
    public function manager_get_transfers($params = array()) {
        return $this->request('transfers', 'manager', 'GET', $params);
    }
    public function manager_get_withdrawals($params = array()) {
        return $this->request('withdrawals', 'manager', 'GET', $params);
    }
    public function markets_get_i_id($params = array()) {
        return $this->request('i/{id}', 'markets', 'GET', $params);
    }
    public function markets_get_s_symbol($params = array()) {
        return $this->request('s/{symbol}', 'markets', 'GET', $params);
    }
    public function markets_post_perform($params = array()) {
        return $this->request('perform', 'markets', 'POST', $params);
    }
    public function markets_post_prepare($params = array()) {
        return $this->request('prepare', 'markets', 'POST', $params);
    }
    public function markets_post_remove_perform($params = array()) {
        return $this->request('remove/perform', 'markets', 'POST', $params);
    }
    public function markets_post_s_symbol_remove_prepare($params = array()) {
        return $this->request('s/{symbol}/remove/prepare', 'markets', 'POST', $params);
    }
    public function markets_post_s_symbol_update_perform($params = array()) {
        return $this->request('s/{symbol}/update/perform', 'markets', 'POST', $params);
    }
    public function markets_post_s_symbol_update_prepare($params = array()) {
        return $this->request('s/{symbol}/update/prepare', 'markets', 'POST', $params);
    }
    public function public_get_candles($params = array()) {
        return $this->request('candles', 'public', 'GET', $params);
    }
    public function public_get_currencies($params = array()) {
        return $this->request('currencies', 'public', 'GET', $params);
    }
    public function public_get_markets($params = array()) {
        return $this->request('markets', 'public', 'GET', $params);
    }
    public function public_get_orderbook($params = array()) {
        return $this->request('orderbook', 'public', 'GET', $params);
    }
    public function public_get_orderbook_raw($params = array()) {
        return $this->request('orderbook/raw', 'public', 'GET', $params);
    }
    public function public_get_orderbook_v2($params = array()) {
        return $this->request('orderbook/v2', 'public', 'GET', $params);
    }
    public function public_get_tickers($params = array()) {
        return $this->request('tickers', 'public', 'GET', $params);
    }
    public function public_get_trades($params = array()) {
        return $this->request('trades', 'public', 'GET', $params);
    }
    public function statistics_get_address($params = array()) {
        return $this->request('address', 'statistics', 'GET', $params);
    }
    public function trading_get_balances($params = array()) {
        return $this->request('balances', 'trading', 'GET', $params);
    }
    public function trading_get_fees($params = array()) {
        return $this->request('fees', 'trading', 'GET', $params);
    }
    public function trading_get_orders($params = array()) {
        return $this->request('orders', 'trading', 'GET', $params);
    }
    public function trading_post_orders($params = array()) {
        return $this->request('orders', 'trading', 'POST', $params);
    }
    public function trading_post_orders_json($params = array()) {
        return $this->request('orders/json', 'trading', 'POST', $params);
    }
    public function trading_put_orders($params = array()) {
        return $this->request('orders', 'trading', 'PUT', $params);
    }
    public function trading_put_orders_json($params = array()) {
        return $this->request('orders/json', 'trading', 'PUT', $params);
    }
    public function trading_delete_orders($params = array()) {
        return $this->request('orders', 'trading', 'DELETE', $params);
    }
    public function trading_delete_orders_json($params = array()) {
        return $this->request('orders/json', 'trading', 'DELETE', $params);
    }
    public function tradingview_get_config($params = array()) {
        return $this->request('config', 'tradingview', 'GET', $params);
    }
    public function tradingview_get_history($params = array()) {
        return $this->request('history', 'tradingview', 'GET', $params);
    }
    public function tradingview_get_symbol_info($params = array()) {
        return $this->request('symbol_info', 'tradingview', 'GET', $params);
    }
    public function tradingview_get_time($params = array()) {
        return $this->request('time', 'tradingview', 'GET', $params);
    }
    public function addressbookGetMe($params = array()) {
        return $this->request('me', 'addressbook', 'GET', $params);
    }
    public function addressbookPost($params = array()) {
        return $this->request('', 'addressbook', 'POST', $params);
    }
    public function addressbookPostIdId($params = array()) {
        return $this->request('id/{id}', 'addressbook', 'POST', $params);
    }
    public function addressbookPostIdIdRemove($params = array()) {
        return $this->request('id/{id}/remove', 'addressbook', 'POST', $params);
    }
    public function custodyGetCredentials($params = array()) {
        return $this->request('credentials', 'custody', 'GET', $params);
    }
    public function custodyGetCredentialsHHash($params = array()) {
        return $this->request('credentials/h/{hash}', 'custody', 'GET', $params);
    }
    public function custodyGetCredentialsKKey($params = array()) {
        return $this->request('credentials/k/{key}', 'custody', 'GET', $params);
    }
    public function custodyGetCredentialsMe($params = array()) {
        return $this->request('credentials/me', 'custody', 'GET', $params);
    }
    public function custodyGetCredentialsMeAddress($params = array()) {
        return $this->request('credentials/me/address', 'custody', 'GET', $params);
    }
    public function custodyGetDepositAddresses($params = array()) {
        return $this->request('deposit-addresses', 'custody', 'GET', $params);
    }
    public function custodyGetDepositAddressesHHash($params = array()) {
        return $this->request('deposit-addresses/h/{hash}', 'custody', 'GET', $params);
    }
    public function historyGetOrders($params = array()) {
        return $this->request('orders', 'history', 'GET', $params);
    }
    public function historyGetOrdersDetails($params = array()) {
        return $this->request('orders/details', 'history', 'GET', $params);
    }
    public function historyGetOrdersExportCsv($params = array()) {
        return $this->request('orders/export/csv', 'history', 'GET', $params);
    }
    public function historyGetTrades($params = array()) {
        return $this->request('trades', 'history', 'GET', $params);
    }
    public function historyGetTradesExportCsv($params = array()) {
        return $this->request('trades/export/csv', 'history', 'GET', $params);
    }
    public function currenciesGetAAddress($params = array()) {
        return $this->request('a/{address}', 'currencies', 'GET', $params);
    }
    public function currenciesGetIId($params = array()) {
        return $this->request('i/{id}', 'currencies', 'GET', $params);
    }
    public function currenciesGetSSymbol($params = array()) {
        return $this->request('s/{symbol}', 'currencies', 'GET', $params);
    }
    public function currenciesPostPerform($params = array()) {
        return $this->request('perform', 'currencies', 'POST', $params);
    }
    public function currenciesPostPrepare($params = array()) {
        return $this->request('prepare', 'currencies', 'POST', $params);
    }
    public function currenciesPostRemovePerform($params = array()) {
        return $this->request('remove/perform', 'currencies', 'POST', $params);
    }
    public function currenciesPostSSymbolRemovePrepare($params = array()) {
        return $this->request('s/{symbol}/remove/prepare', 'currencies', 'POST', $params);
    }
    public function currenciesPostSSymbolUpdatePerform($params = array()) {
        return $this->request('s/{symbol}/update/perform', 'currencies', 'POST', $params);
    }
    public function currenciesPostSSymbolUpdatePrepare($params = array()) {
        return $this->request('s/{symbol}/update/prepare', 'currencies', 'POST', $params);
    }
    public function managerGetDeposits($params = array()) {
        return $this->request('deposits', 'manager', 'GET', $params);
    }
    public function managerGetTransfers($params = array()) {
        return $this->request('transfers', 'manager', 'GET', $params);
    }
    public function managerGetWithdrawals($params = array()) {
        return $this->request('withdrawals', 'manager', 'GET', $params);
    }
    public function marketsGetIId($params = array()) {
        return $this->request('i/{id}', 'markets', 'GET', $params);
    }
    public function marketsGetSSymbol($params = array()) {
        return $this->request('s/{symbol}', 'markets', 'GET', $params);
    }
    public function marketsPostPerform($params = array()) {
        return $this->request('perform', 'markets', 'POST', $params);
    }
    public function marketsPostPrepare($params = array()) {
        return $this->request('prepare', 'markets', 'POST', $params);
    }
    public function marketsPostRemovePerform($params = array()) {
        return $this->request('remove/perform', 'markets', 'POST', $params);
    }
    public function marketsPostSSymbolRemovePrepare($params = array()) {
        return $this->request('s/{symbol}/remove/prepare', 'markets', 'POST', $params);
    }
    public function marketsPostSSymbolUpdatePerform($params = array()) {
        return $this->request('s/{symbol}/update/perform', 'markets', 'POST', $params);
    }
    public function marketsPostSSymbolUpdatePrepare($params = array()) {
        return $this->request('s/{symbol}/update/prepare', 'markets', 'POST', $params);
    }
    public function publicGetCandles($params = array()) {
        return $this->request('candles', 'public', 'GET', $params);
    }
    public function publicGetCurrencies($params = array()) {
        return $this->request('currencies', 'public', 'GET', $params);
    }
    public function publicGetMarkets($params = array()) {
        return $this->request('markets', 'public', 'GET', $params);
    }
    public function publicGetOrderbook($params = array()) {
        return $this->request('orderbook', 'public', 'GET', $params);
    }
    public function publicGetOrderbookRaw($params = array()) {
        return $this->request('orderbook/raw', 'public', 'GET', $params);
    }
    public function publicGetOrderbookV2($params = array()) {
        return $this->request('orderbook/v2', 'public', 'GET', $params);
    }
    public function publicGetTickers($params = array()) {
        return $this->request('tickers', 'public', 'GET', $params);
    }
    public function publicGetTrades($params = array()) {
        return $this->request('trades', 'public', 'GET', $params);
    }
    public function statisticsGetAddress($params = array()) {
        return $this->request('address', 'statistics', 'GET', $params);
    }
    public function tradingGetBalances($params = array()) {
        return $this->request('balances', 'trading', 'GET', $params);
    }
    public function tradingGetFees($params = array()) {
        return $this->request('fees', 'trading', 'GET', $params);
    }
    public function tradingGetOrders($params = array()) {
        return $this->request('orders', 'trading', 'GET', $params);
    }
    public function tradingPostOrders($params = array()) {
        return $this->request('orders', 'trading', 'POST', $params);
    }
    public function tradingPostOrdersJson($params = array()) {
        return $this->request('orders/json', 'trading', 'POST', $params);
    }
    public function tradingPutOrders($params = array()) {
        return $this->request('orders', 'trading', 'PUT', $params);
    }
    public function tradingPutOrdersJson($params = array()) {
        return $this->request('orders/json', 'trading', 'PUT', $params);
    }
    public function tradingDeleteOrders($params = array()) {
        return $this->request('orders', 'trading', 'DELETE', $params);
    }
    public function tradingDeleteOrdersJson($params = array()) {
        return $this->request('orders/json', 'trading', 'DELETE', $params);
    }
    public function tradingviewGetConfig($params = array()) {
        return $this->request('config', 'tradingview', 'GET', $params);
    }
    public function tradingviewGetHistory($params = array()) {
        return $this->request('history', 'tradingview', 'GET', $params);
    }
    public function tradingviewGetSymbolInfo($params = array()) {
        return $this->request('symbol_info', 'tradingview', 'GET', $params);
    }
    public function tradingviewGetTime($params = array()) {
        return $this->request('time', 'tradingview', 'GET', $params);
    }
}