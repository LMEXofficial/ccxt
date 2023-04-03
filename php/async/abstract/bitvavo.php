<?php

namespace ccxt\async\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class bitvavo extends \ccxt\async\Exchange {
    public function public_get_time($params = array()) {
        return $this->request('time', 'public', 'GET', $params);
    }
    public function public_get_markets($params = array()) {
        return $this->request('markets', 'public', 'GET', $params);
    }
    public function public_get_assets($params = array()) {
        return $this->request('assets', 'public', 'GET', $params);
    }
    public function public_get_market_book($params = array()) {
        return $this->request('{market}/book', 'public', 'GET', $params);
    }
    public function public_get_market_trades($params = array()) {
        return $this->request('{market}/trades', 'public', 'GET', $params);
    }
    public function public_get_market_candles($params = array()) {
        return $this->request('{market}/candles', 'public', 'GET', $params);
    }
    public function public_get_ticker_price($params = array()) {
        return $this->request('ticker/price', 'public', 'GET', $params);
    }
    public function public_get_ticker_book($params = array()) {
        return $this->request('ticker/book', 'public', 'GET', $params);
    }
    public function public_get_ticker_24h($params = array()) {
        return $this->request('ticker/24h', 'public', 'GET', $params);
    }
    public function private_get_account($params = array()) {
        return $this->request('account', 'private', 'GET', $params);
    }
    public function private_get_order($params = array()) {
        return $this->request('order', 'private', 'GET', $params);
    }
    public function private_get_orders($params = array()) {
        return $this->request('orders', 'private', 'GET', $params);
    }
    public function private_get_ordersopen($params = array()) {
        return $this->request('ordersOpen', 'private', 'GET', $params);
    }
    public function private_get_trades($params = array()) {
        return $this->request('trades', 'private', 'GET', $params);
    }
    public function private_get_balance($params = array()) {
        return $this->request('balance', 'private', 'GET', $params);
    }
    public function private_get_deposit($params = array()) {
        return $this->request('deposit', 'private', 'GET', $params);
    }
    public function private_get_deposithistory($params = array()) {
        return $this->request('depositHistory', 'private', 'GET', $params);
    }
    public function private_get_withdrawalhistory($params = array()) {
        return $this->request('withdrawalHistory', 'private', 'GET', $params);
    }
    public function private_post_order($params = array()) {
        return $this->request('order', 'private', 'POST', $params);
    }
    public function private_post_withdrawal($params = array()) {
        return $this->request('withdrawal', 'private', 'POST', $params);
    }
    public function private_put_order($params = array()) {
        return $this->request('order', 'private', 'PUT', $params);
    }
    public function private_delete_order($params = array()) {
        return $this->request('order', 'private', 'DELETE', $params);
    }
    public function private_delete_orders($params = array()) {
        return $this->request('orders', 'private', 'DELETE', $params);
    }
    public function publicGetTime($params = array()) {
        return $this->request('time', 'public', 'GET', $params);
    }
    public function publicGetMarkets($params = array()) {
        return $this->request('markets', 'public', 'GET', $params);
    }
    public function publicGetAssets($params = array()) {
        return $this->request('assets', 'public', 'GET', $params);
    }
    public function publicGetMarketBook($params = array()) {
        return $this->request('{market}/book', 'public', 'GET', $params);
    }
    public function publicGetMarketTrades($params = array()) {
        return $this->request('{market}/trades', 'public', 'GET', $params);
    }
    public function publicGetMarketCandles($params = array()) {
        return $this->request('{market}/candles', 'public', 'GET', $params);
    }
    public function publicGetTickerPrice($params = array()) {
        return $this->request('ticker/price', 'public', 'GET', $params);
    }
    public function publicGetTickerBook($params = array()) {
        return $this->request('ticker/book', 'public', 'GET', $params);
    }
    public function publicGetTicker24h($params = array()) {
        return $this->request('ticker/24h', 'public', 'GET', $params);
    }
    public function privateGetAccount($params = array()) {
        return $this->request('account', 'private', 'GET', $params);
    }
    public function privateGetOrder($params = array()) {
        return $this->request('order', 'private', 'GET', $params);
    }
    public function privateGetOrders($params = array()) {
        return $this->request('orders', 'private', 'GET', $params);
    }
    public function privateGetOrdersOpen($params = array()) {
        return $this->request('ordersOpen', 'private', 'GET', $params);
    }
    public function privateGetTrades($params = array()) {
        return $this->request('trades', 'private', 'GET', $params);
    }
    public function privateGetBalance($params = array()) {
        return $this->request('balance', 'private', 'GET', $params);
    }
    public function privateGetDeposit($params = array()) {
        return $this->request('deposit', 'private', 'GET', $params);
    }
    public function privateGetDepositHistory($params = array()) {
        return $this->request('depositHistory', 'private', 'GET', $params);
    }
    public function privateGetWithdrawalHistory($params = array()) {
        return $this->request('withdrawalHistory', 'private', 'GET', $params);
    }
    public function privatePostOrder($params = array()) {
        return $this->request('order', 'private', 'POST', $params);
    }
    public function privatePostWithdrawal($params = array()) {
        return $this->request('withdrawal', 'private', 'POST', $params);
    }
    public function privatePutOrder($params = array()) {
        return $this->request('order', 'private', 'PUT', $params);
    }
    public function privateDeleteOrder($params = array()) {
        return $this->request('order', 'private', 'DELETE', $params);
    }
    public function privateDeleteOrders($params = array()) {
        return $this->request('orders', 'private', 'DELETE', $params);
    }
}