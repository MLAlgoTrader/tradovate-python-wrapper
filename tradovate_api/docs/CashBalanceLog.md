# CashBalanceLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | 
**timestamp** | **datetime** |  | 
**trade_date** | [**TradeDate**](TradeDate.md) |  | 
**currency_id** | **int** |  | 
**amount** | **float** |  | 
**realized_pn_l** | **float** |  | [optional] 
**week_realized_pn_l** | **float** |  | [optional] 
**cash_change_type** | **str** | AutomaticReconciliation, BrokerageFee, CancelledPairedTrade, CashSettlement, ClearingFee, Commission, DeskFee, EntitlementSubscription, ExchangeFee, FundTransaction, FundTransactionFee, IPFee, LiquidationFee, ManualAdjustment, MarketDataSubscription, NewSession, NfaFee, OptionsTrade, OrderRoutingFee, TradePaired, TradovateSubscription | 
**fill_pair_id** | **int** |  | [optional] 
**fill_id** | **int** |  | [optional] 
**fund_transaction_id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**delta** | **float** |  | 
**sender_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

