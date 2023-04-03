<?php

namespace ccxt\async\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class zb extends \ccxt\async\Exchange {
    public function spot_v1_public_get_markets($params = array()) {
        return $this->request('markets', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_ticker($params = array()) {
        return $this->request('ticker', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_allticker($params = array()) {
        return $this->request('allTicker', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_depth($params = array()) {
        return $this->request('depth', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_trades($params = array()) {
        return $this->request('trades', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_kline($params = array()) {
        return $this->request('kline', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_getgroupmarkets($params = array()) {
        return $this->request('getGroupMarkets', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_public_get_getfeeinfo($params = array()) {
        return $this->request('getFeeInfo', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spot_v1_private_get_order($params = array()) {
        return $this->request('order', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_ordermorev2($params = array()) {
        return $this->request('orderMoreV2', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_cancelorder($params = array()) {
        return $this->request('cancelOrder', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_cancelallordersafter($params = array()) {
        return $this->request('cancelAllOrdersAfter', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getorder($params = array()) {
        return $this->request('getOrder', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getorders($params = array()) {
        return $this->request('getOrders', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getordersnew($params = array()) {
        return $this->request('getOrdersNew', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getordersignoretradetype($params = array()) {
        return $this->request('getOrdersIgnoreTradeType', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getunfinishedordersignoretradetype($params = array()) {
        return $this->request('getUnfinishedOrdersIgnoreTradeType', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getfinishedandpartialorders($params = array()) {
        return $this->request('getFinishedAndPartialOrders', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getaccountinfo($params = array()) {
        return $this->request('getAccountInfo', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getuseraddress($params = array()) {
        return $this->request('getUserAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getpayinaddress($params = array()) {
        return $this->request('getPayinAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getwithdrawaddress($params = array()) {
        return $this->request('getWithdrawAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getwithdrawrecord($params = array()) {
        return $this->request('getWithdrawRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getchargerecord($params = array()) {
        return $this->request('getChargeRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getcnywithdrawrecord($params = array()) {
        return $this->request('getCnyWithdrawRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getcnychargerecord($params = array()) {
        return $this->request('getCnyChargeRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_withdraw($params = array()) {
        return $this->request('withdraw', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_addsubuser($params = array()) {
        return $this->request('addSubUser', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getsubuserlist($params = array()) {
        return $this->request('getSubUserList', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_dotransferfunds($params = array()) {
        return $this->request('doTransferFunds', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_createsubuserkey($params = array()) {
        return $this->request('createSubUserKey', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getleverassetsinfo($params = array()) {
        return $this->request('getLeverAssetsInfo', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getleverbills($params = array()) {
        return $this->request('getLeverBills', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_transferinlever($params = array()) {
        return $this->request('transferInLever', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_transferoutlever($params = array()) {
        return $this->request('transferOutLever', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_loan($params = array()) {
        return $this->request('loan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_cancelloan($params = array()) {
        return $this->request('cancelLoan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getloans($params = array()) {
        return $this->request('getLoans', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getloanrecords($params = array()) {
        return $this->request('getLoanRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_borrow($params = array()) {
        return $this->request('borrow', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_autoborrow($params = array()) {
        return $this->request('autoBorrow', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_repay($params = array()) {
        return $this->request('repay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_doallrepay($params = array()) {
        return $this->request('doAllRepay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getrepayments($params = array()) {
        return $this->request('getRepayments', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getfinancerecords($params = array()) {
        return $this->request('getFinanceRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_changeinvestmark($params = array()) {
        return $this->request('changeInvestMark', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_changeloop($params = array()) {
        return $this->request('changeLoop', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getcrossassets($params = array()) {
        return $this->request('getCrossAssets', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getcrossbills($params = array()) {
        return $this->request('getCrossBills', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_transferincross($params = array()) {
        return $this->request('transferInCross', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_transferoutcross($params = array()) {
        return $this->request('transferOutCross', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_docrossloan($params = array()) {
        return $this->request('doCrossLoan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_docrossrepay($params = array()) {
        return $this->request('doCrossRepay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spot_v1_private_get_getcrossrepayrecords($params = array()) {
        return $this->request('getCrossRepayRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function contract_v1_public_get_depth($params = array()) {
        return $this->request('depth', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_fundingrate($params = array()) {
        return $this->request('fundingRate', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_indexkline($params = array()) {
        return $this->request('indexKline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_indexprice($params = array()) {
        return $this->request('indexPrice', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_kline($params = array()) {
        return $this->request('kline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_markkline($params = array()) {
        return $this->request('markKline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_markprice($params = array()) {
        return $this->request('markPrice', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_ticker($params = array()) {
        return $this->request('ticker', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v1_public_get_trade($params = array()) {
        return $this->request('trade', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_allforceorders($params = array()) {
        return $this->request('allForceOrders', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_config_marketlist($params = array()) {
        return $this->request('config/marketList', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_toplongshortaccountratio($params = array()) {
        return $this->request('topLongShortAccountRatio', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_toplongshortpositionratio($params = array()) {
        return $this->request('topLongShortPositionRatio', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_fundingrate($params = array()) {
        return $this->request('fundingRate', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_public_get_premiumindex($params = array()) {
        return $this->request('premiumIndex', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contract_v2_private_get_fund_balance($params = array()) {
        return $this->request('Fund/balance', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_fund_getaccount($params = array()) {
        return $this->request('Fund/getAccount', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_fund_getbill($params = array()) {
        return $this->request('Fund/getBill', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_fund_getbilltypelist($params = array()) {
        return $this->request('Fund/getBillTypeList', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_fund_marginhistory($params = array()) {
        return $this->request('Fund/marginHistory', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_positions_getpositions($params = array()) {
        return $this->request('Positions/getPositions', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_positions_getnominalvalue($params = array()) {
        return $this->request('Positions/getNominalValue', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_positions_margininfo($params = array()) {
        return $this->request('Positions/marginInfo', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_setting_get($params = array()) {
        return $this->request('setting/get', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_getallorders($params = array()) {
        return $this->request('trade/getAllOrders', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_getorder($params = array()) {
        return $this->request('trade/getOrder', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_getorderalgos($params = array()) {
        return $this->request('trade/getOrderAlgos', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_gettradelist($params = array()) {
        return $this->request('trade/getTradeList', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_getundoneorders($params = array()) {
        return $this->request('trade/getUndoneOrders', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_get_trade_tradehistory($params = array()) {
        return $this->request('trade/tradeHistory', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contract_v2_private_post_activity_buyticket($params = array()) {
        return $this->request('activity/buyTicket', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_fund_transferfund($params = array()) {
        return $this->request('Fund/transferFund', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_positions_setmargincoins($params = array()) {
        return $this->request('Positions/setMarginCoins', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_positions_updateappendusdvalue($params = array()) {
        return $this->request('Positions/updateAppendUSDValue', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_positions_updatemargin($params = array()) {
        return $this->request('Positions/updateMargin', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_setting_setleverage($params = array()) {
        return $this->request('setting/setLeverage', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_setting_setpositionsmode($params = array()) {
        return $this->request('setting/setPositionsMode', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_batchorder($params = array()) {
        return $this->request('trade/batchOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_batchcancelorder($params = array()) {
        return $this->request('trade/batchCancelOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_cancelalgos($params = array()) {
        return $this->request('trade/cancelAlgos', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_cancelallorders($params = array()) {
        return $this->request('trade/cancelAllOrders', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_cancelorder($params = array()) {
        return $this->request('trade/cancelOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_order($params = array()) {
        return $this->request('trade/order', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_orderalgo($params = array()) {
        return $this->request('trade/orderAlgo', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contract_v2_private_post_trade_updateorderalgo($params = array()) {
        return $this->request('trade/updateOrderAlgo', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function spotV1PublicGetMarkets($params = array()) {
        return $this->request('markets', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetTicker($params = array()) {
        return $this->request('ticker', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetAllTicker($params = array()) {
        return $this->request('allTicker', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetDepth($params = array()) {
        return $this->request('depth', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetTrades($params = array()) {
        return $this->request('trades', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetKline($params = array()) {
        return $this->request('kline', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetGetGroupMarkets($params = array()) {
        return $this->request('getGroupMarkets', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PublicGetGetFeeInfo($params = array()) {
        return $this->request('getFeeInfo', array('spot', 'v1', 'public'), 'GET', $params);
    }
    public function spotV1PrivateGetOrder($params = array()) {
        return $this->request('order', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetOrderMoreV2($params = array()) {
        return $this->request('orderMoreV2', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetCancelOrder($params = array()) {
        return $this->request('cancelOrder', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetCancelAllOrdersAfter($params = array()) {
        return $this->request('cancelAllOrdersAfter', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetOrder($params = array()) {
        return $this->request('getOrder', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetOrders($params = array()) {
        return $this->request('getOrders', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetOrdersNew($params = array()) {
        return $this->request('getOrdersNew', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetOrdersIgnoreTradeType($params = array()) {
        return $this->request('getOrdersIgnoreTradeType', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetUnfinishedOrdersIgnoreTradeType($params = array()) {
        return $this->request('getUnfinishedOrdersIgnoreTradeType', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetFinishedAndPartialOrders($params = array()) {
        return $this->request('getFinishedAndPartialOrders', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetAccountInfo($params = array()) {
        return $this->request('getAccountInfo', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetUserAddress($params = array()) {
        return $this->request('getUserAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetPayinAddress($params = array()) {
        return $this->request('getPayinAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetWithdrawAddress($params = array()) {
        return $this->request('getWithdrawAddress', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetWithdrawRecord($params = array()) {
        return $this->request('getWithdrawRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetChargeRecord($params = array()) {
        return $this->request('getChargeRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetCnyWithdrawRecord($params = array()) {
        return $this->request('getCnyWithdrawRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetCnyChargeRecord($params = array()) {
        return $this->request('getCnyChargeRecord', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetWithdraw($params = array()) {
        return $this->request('withdraw', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetAddSubUser($params = array()) {
        return $this->request('addSubUser', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetSubUserList($params = array()) {
        return $this->request('getSubUserList', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetDoTransferFunds($params = array()) {
        return $this->request('doTransferFunds', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetCreateSubUserKey($params = array()) {
        return $this->request('createSubUserKey', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetLeverAssetsInfo($params = array()) {
        return $this->request('getLeverAssetsInfo', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetLeverBills($params = array()) {
        return $this->request('getLeverBills', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetTransferInLever($params = array()) {
        return $this->request('transferInLever', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetTransferOutLever($params = array()) {
        return $this->request('transferOutLever', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetLoan($params = array()) {
        return $this->request('loan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetCancelLoan($params = array()) {
        return $this->request('cancelLoan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetLoans($params = array()) {
        return $this->request('getLoans', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetLoanRecords($params = array()) {
        return $this->request('getLoanRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetBorrow($params = array()) {
        return $this->request('borrow', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetAutoBorrow($params = array()) {
        return $this->request('autoBorrow', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetRepay($params = array()) {
        return $this->request('repay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetDoAllRepay($params = array()) {
        return $this->request('doAllRepay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetRepayments($params = array()) {
        return $this->request('getRepayments', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetFinanceRecords($params = array()) {
        return $this->request('getFinanceRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetChangeInvestMark($params = array()) {
        return $this->request('changeInvestMark', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetChangeLoop($params = array()) {
        return $this->request('changeLoop', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetCrossAssets($params = array()) {
        return $this->request('getCrossAssets', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetCrossBills($params = array()) {
        return $this->request('getCrossBills', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetTransferInCross($params = array()) {
        return $this->request('transferInCross', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetTransferOutCross($params = array()) {
        return $this->request('transferOutCross', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetDoCrossLoan($params = array()) {
        return $this->request('doCrossLoan', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetDoCrossRepay($params = array()) {
        return $this->request('doCrossRepay', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function spotV1PrivateGetGetCrossRepayRecords($params = array()) {
        return $this->request('getCrossRepayRecords', array('spot', 'v1', 'private'), 'GET', $params);
    }
    public function contractV1PublicGetDepth($params = array()) {
        return $this->request('depth', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetFundingRate($params = array()) {
        return $this->request('fundingRate', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetIndexKline($params = array()) {
        return $this->request('indexKline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetIndexPrice($params = array()) {
        return $this->request('indexPrice', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetKline($params = array()) {
        return $this->request('kline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetMarkKline($params = array()) {
        return $this->request('markKline', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetMarkPrice($params = array()) {
        return $this->request('markPrice', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetTicker($params = array()) {
        return $this->request('ticker', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV1PublicGetTrade($params = array()) {
        return $this->request('trade', array('contract', 'v1', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetAllForceOrders($params = array()) {
        return $this->request('allForceOrders', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetConfigMarketList($params = array()) {
        return $this->request('config/marketList', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetTopLongShortAccountRatio($params = array()) {
        return $this->request('topLongShortAccountRatio', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetTopLongShortPositionRatio($params = array()) {
        return $this->request('topLongShortPositionRatio', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetFundingRate($params = array()) {
        return $this->request('fundingRate', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PublicGetPremiumIndex($params = array()) {
        return $this->request('premiumIndex', array('contract', 'v2', 'public'), 'GET', $params);
    }
    public function contractV2PrivateGetFundBalance($params = array()) {
        return $this->request('Fund/balance', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetFundGetAccount($params = array()) {
        return $this->request('Fund/getAccount', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetFundGetBill($params = array()) {
        return $this->request('Fund/getBill', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetFundGetBillTypeList($params = array()) {
        return $this->request('Fund/getBillTypeList', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetFundMarginHistory($params = array()) {
        return $this->request('Fund/marginHistory', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetPositionsGetPositions($params = array()) {
        return $this->request('Positions/getPositions', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetPositionsGetNominalValue($params = array()) {
        return $this->request('Positions/getNominalValue', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetPositionsMarginInfo($params = array()) {
        return $this->request('Positions/marginInfo', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetSettingGet($params = array()) {
        return $this->request('setting/get', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeGetAllOrders($params = array()) {
        return $this->request('trade/getAllOrders', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeGetOrder($params = array()) {
        return $this->request('trade/getOrder', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeGetOrderAlgos($params = array()) {
        return $this->request('trade/getOrderAlgos', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeGetTradeList($params = array()) {
        return $this->request('trade/getTradeList', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeGetUndoneOrders($params = array()) {
        return $this->request('trade/getUndoneOrders', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivateGetTradeTradeHistory($params = array()) {
        return $this->request('trade/tradeHistory', array('contract', 'v2', 'private'), 'GET', $params);
    }
    public function contractV2PrivatePostActivityBuyTicket($params = array()) {
        return $this->request('activity/buyTicket', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostFundTransferFund($params = array()) {
        return $this->request('Fund/transferFund', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostPositionsSetMarginCoins($params = array()) {
        return $this->request('Positions/setMarginCoins', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostPositionsUpdateAppendUSDValue($params = array()) {
        return $this->request('Positions/updateAppendUSDValue', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostPositionsUpdateMargin($params = array()) {
        return $this->request('Positions/updateMargin', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostSettingSetLeverage($params = array()) {
        return $this->request('setting/setLeverage', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostSettingSetPositionsMode($params = array()) {
        return $this->request('setting/setPositionsMode', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeBatchOrder($params = array()) {
        return $this->request('trade/batchOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeBatchCancelOrder($params = array()) {
        return $this->request('trade/batchCancelOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeCancelAlgos($params = array()) {
        return $this->request('trade/cancelAlgos', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeCancelAllOrders($params = array()) {
        return $this->request('trade/cancelAllOrders', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeCancelOrder($params = array()) {
        return $this->request('trade/cancelOrder', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeOrder($params = array()) {
        return $this->request('trade/order', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeOrderAlgo($params = array()) {
        return $this->request('trade/orderAlgo', array('contract', 'v2', 'private'), 'POST', $params);
    }
    public function contractV2PrivatePostTradeUpdateOrderAlgo($params = array()) {
        return $this->request('trade/updateOrderAlgo', array('contract', 'v2', 'private'), 'POST', $params);
    }
}