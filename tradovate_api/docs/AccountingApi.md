# swagger_client.AccountingApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_dependents**](AccountingApi.md#account_dependents) | **GET** /account/deps | 
[**account_find**](AccountingApi.md#account_find) | **GET** /account/find | 
[**account_item**](AccountingApi.md#account_item) | **GET** /account/item | 
[**account_items**](AccountingApi.md#account_items) | **GET** /account/items | 
[**account_l_dependents**](AccountingApi.md#account_l_dependents) | **GET** /account/ldeps | 
[**account_list**](AccountingApi.md#account_list) | **GET** /account/list | 
[**account_suggest**](AccountingApi.md#account_suggest) | **GET** /account/suggest | 
[**cash_balance_dependents**](AccountingApi.md#cash_balance_dependents) | **GET** /cashBalance/deps | 
[**cash_balance_item**](AccountingApi.md#cash_balance_item) | **GET** /cashBalance/item | 
[**cash_balance_items**](AccountingApi.md#cash_balance_items) | **GET** /cashBalance/items | 
[**cash_balance_l_dependents**](AccountingApi.md#cash_balance_l_dependents) | **GET** /cashBalance/ldeps | 
[**cash_balance_list**](AccountingApi.md#cash_balance_list) | **GET** /cashBalance/list | 
[**cash_balance_log_dependents**](AccountingApi.md#cash_balance_log_dependents) | **GET** /cashBalanceLog/deps | 
[**cash_balance_log_item**](AccountingApi.md#cash_balance_log_item) | **GET** /cashBalanceLog/item | 
[**cash_balance_log_items**](AccountingApi.md#cash_balance_log_items) | **GET** /cashBalanceLog/items | 
[**cash_balance_log_l_dependents**](AccountingApi.md#cash_balance_log_l_dependents) | **GET** /cashBalanceLog/ldeps | 
[**get_cash_balance_snapshot**](AccountingApi.md#get_cash_balance_snapshot) | **POST** /cashBalance/getcashbalancesnapshot | 
[**margin_snapshot_dependents**](AccountingApi.md#margin_snapshot_dependents) | **GET** /marginSnapshot/deps | 
[**margin_snapshot_item**](AccountingApi.md#margin_snapshot_item) | **GET** /marginSnapshot/item | 
[**margin_snapshot_items**](AccountingApi.md#margin_snapshot_items) | **GET** /marginSnapshot/items | 
[**margin_snapshot_l_dependents**](AccountingApi.md#margin_snapshot_l_dependents) | **GET** /marginSnapshot/ldeps | 
[**margin_snapshot_list**](AccountingApi.md#margin_snapshot_list) | **GET** /marginSnapshot/list | 
[**trading_permission_dependents**](AccountingApi.md#trading_permission_dependents) | **GET** /tradingPermission/deps | 
[**trading_permission_item**](AccountingApi.md#trading_permission_item) | **GET** /tradingPermission/item | 
[**trading_permission_items**](AccountingApi.md#trading_permission_items) | **GET** /tradingPermission/items | 
[**trading_permission_l_dependents**](AccountingApi.md#trading_permission_l_dependents) | **GET** /tradingPermission/ldeps | 
[**trading_permission_list**](AccountingApi.md#trading_permission_list) | **GET** /tradingPermission/list | 

# **account_dependents**
> list[Account] account_dependents(masterid)



Retrieves all entities of Account type related to User entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of User entity

try:
    api_response = api_instance.account_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_find**
> Account account_find(name)



Retrieves an entity of Account type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.account_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_item**
> Account account_item(id)



Retrieves an entity of Account type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.account_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_items**
> list[Account] account_items(ids)



Retrieves multiple entities of Account type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.account_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_l_dependents**
> list[Account] account_l_dependents(masterids)



Retrieves all entities of Account type related to multiple entities of User type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of User entities

try:
    api_response = api_instance.account_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of User entities | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_list**
> list[Account] account_list()



Retrieves all entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.account_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_suggest**
> list[Account] account_suggest(t, l)



Retrieves entities of Account type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.account_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->account_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_dependents**
> list[CashBalance] cash_balance_dependents(masterid)



Retrieves all entities of CashBalance type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.cash_balance_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_item**
> CashBalance cash_balance_item(id)



Retrieves an entity of CashBalance type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.cash_balance_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CashBalance**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_items**
> list[CashBalance] cash_balance_items(ids)



Retrieves multiple entities of CashBalance type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.cash_balance_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_l_dependents**
> list[CashBalance] cash_balance_l_dependents(masterids)



Retrieves all entities of CashBalance type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.cash_balance_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_list**
> list[CashBalance] cash_balance_list()



Retrieves all entities of CashBalance type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.cash_balance_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CashBalance]**](CashBalance.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_dependents**
> list[CashBalanceLog] cash_balance_log_dependents(masterid)



Retrieves all entities of CashBalanceLog type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.cash_balance_log_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_log_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_item**
> CashBalanceLog cash_balance_log_item(id)



Retrieves an entity of CashBalanceLog type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.cash_balance_log_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_log_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CashBalanceLog**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_items**
> list[CashBalanceLog] cash_balance_log_items(ids)



Retrieves multiple entities of CashBalanceLog type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.cash_balance_log_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_log_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_balance_log_l_dependents**
> list[CashBalanceLog] cash_balance_log_l_dependents(masterids)



Retrieves all entities of CashBalanceLog type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.cash_balance_log_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->cash_balance_log_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[CashBalanceLog]**](CashBalanceLog.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_balance_snapshot**
> CashBalanceSnapshot get_cash_balance_snapshot(body)



### Get a snapshot of an account's current cash balance. > *Note*: Using this endpoint many times in succession is an anti-pattern. If you need to check a `cashBalance` in real-time, instead use a WebSocket connected to the standard Tradovate WebSocket URL and initialize a real-time user data subscription via the `user/syncrequest` endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetCashBalanceSnapshot() # GetCashBalanceSnapshot | 

try:
    api_response = api_instance.get_cash_balance_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_cash_balance_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetCashBalanceSnapshot**](GetCashBalanceSnapshot.md)|  | 

### Return type

[**CashBalanceSnapshot**](CashBalanceSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_dependents**
> list[MarginSnapshot] margin_snapshot_dependents(masterid)



Retrieves all entities of MarginSnapshot type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.margin_snapshot_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->margin_snapshot_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_item**
> MarginSnapshot margin_snapshot_item(id)



Retrieves an entity of MarginSnapshot type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.margin_snapshot_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->margin_snapshot_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MarginSnapshot**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_items**
> list[MarginSnapshot] margin_snapshot_items(ids)



Retrieves multiple entities of MarginSnapshot type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.margin_snapshot_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->margin_snapshot_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_l_dependents**
> list[MarginSnapshot] margin_snapshot_l_dependents(masterids)



Retrieves all entities of MarginSnapshot type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.margin_snapshot_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->margin_snapshot_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **margin_snapshot_list**
> list[MarginSnapshot] margin_snapshot_list()



Retrieves all entities of MarginSnapshot type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.margin_snapshot_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->margin_snapshot_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarginSnapshot]**](MarginSnapshot.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_dependents**
> list[TradingPermission] trading_permission_dependents(masterid)



Retrieves all entities of TradingPermission type related to User entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of User entity

try:
    api_response = api_instance.trading_permission_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->trading_permission_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity | 

### Return type

[**list[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_item**
> TradingPermission trading_permission_item(id)



Retrieves an entity of TradingPermission type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.trading_permission_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->trading_permission_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TradingPermission**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_items**
> list[TradingPermission] trading_permission_items(ids)



Retrieves multiple entities of TradingPermission type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.trading_permission_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->trading_permission_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_l_dependents**
> list[TradingPermission] trading_permission_l_dependents(masterids)



Retrieves all entities of TradingPermission type related to multiple entities of User type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of User entities

try:
    api_response = api_instance.trading_permission_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->trading_permission_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of User entities | 

### Return type

[**list[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trading_permission_list**
> list[TradingPermission] trading_permission_list()



Retrieves all entities of TradingPermission type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountingApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.trading_permission_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->trading_permission_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TradingPermission]**](TradingPermission.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

