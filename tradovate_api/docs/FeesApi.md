# swagger_client.FeesApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_data_subscription_exchange_scope_find**](FeesApi.md#market_data_subscription_exchange_scope_find) | **GET** /marketDataSubscriptionExchangeScope/find | 
[**market_data_subscription_exchange_scope_item**](FeesApi.md#market_data_subscription_exchange_scope_item) | **GET** /marketDataSubscriptionExchangeScope/item | 
[**market_data_subscription_exchange_scope_items**](FeesApi.md#market_data_subscription_exchange_scope_items) | **GET** /marketDataSubscriptionExchangeScope/items | 
[**market_data_subscription_exchange_scope_list**](FeesApi.md#market_data_subscription_exchange_scope_list) | **GET** /marketDataSubscriptionExchangeScope/list | 
[**market_data_subscription_exchange_scope_suggest**](FeesApi.md#market_data_subscription_exchange_scope_suggest) | **GET** /marketDataSubscriptionExchangeScope/suggest | 
[**market_data_subscription_plan_find**](FeesApi.md#market_data_subscription_plan_find) | **GET** /marketDataSubscriptionPlan/find | 
[**market_data_subscription_plan_item**](FeesApi.md#market_data_subscription_plan_item) | **GET** /marketDataSubscriptionPlan/item | 
[**market_data_subscription_plan_items**](FeesApi.md#market_data_subscription_plan_items) | **GET** /marketDataSubscriptionPlan/items | 
[**market_data_subscription_plan_list**](FeesApi.md#market_data_subscription_plan_list) | **GET** /marketDataSubscriptionPlan/list | 
[**market_data_subscription_plan_suggest**](FeesApi.md#market_data_subscription_plan_suggest) | **GET** /marketDataSubscriptionPlan/suggest | 
[**tradovate_subscription_plan_find**](FeesApi.md#tradovate_subscription_plan_find) | **GET** /tradovateSubscriptionPlan/find | 
[**tradovate_subscription_plan_item**](FeesApi.md#tradovate_subscription_plan_item) | **GET** /tradovateSubscriptionPlan/item | 
[**tradovate_subscription_plan_items**](FeesApi.md#tradovate_subscription_plan_items) | **GET** /tradovateSubscriptionPlan/items | 
[**tradovate_subscription_plan_list**](FeesApi.md#tradovate_subscription_plan_list) | **GET** /tradovateSubscriptionPlan/list | 
[**tradovate_subscription_plan_suggest**](FeesApi.md#tradovate_subscription_plan_suggest) | **GET** /tradovateSubscriptionPlan/suggest | 

# **market_data_subscription_exchange_scope_find**
> MarketDataSubscriptionExchangeScope market_data_subscription_exchange_scope_find(name)



Retrieves an entity of MarketDataSubscriptionExchangeScope type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.market_data_subscription_exchange_scope_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_exchange_scope_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**MarketDataSubscriptionExchangeScope**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_item**
> MarketDataSubscriptionExchangeScope market_data_subscription_exchange_scope_item(id)



Retrieves an entity of MarketDataSubscriptionExchangeScope type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.market_data_subscription_exchange_scope_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_exchange_scope_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MarketDataSubscriptionExchangeScope**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_items**
> list[MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_items(ids)



Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.market_data_subscription_exchange_scope_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_exchange_scope_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_list**
> list[MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_list()



Retrieves all entities of MarketDataSubscriptionExchangeScope type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.market_data_subscription_exchange_scope_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_exchange_scope_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_exchange_scope_suggest**
> list[MarketDataSubscriptionExchangeScope] market_data_subscription_exchange_scope_suggest(t, l)



Retrieves entities of MarketDataSubscriptionExchangeScope type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.market_data_subscription_exchange_scope_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_exchange_scope_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[MarketDataSubscriptionExchangeScope]**](MarketDataSubscriptionExchangeScope.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_find**
> MarketDataSubscriptionPlan market_data_subscription_plan_find(name)



Retrieves an entity of MarketDataSubscriptionPlan type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.market_data_subscription_plan_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_plan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**MarketDataSubscriptionPlan**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_item**
> MarketDataSubscriptionPlan market_data_subscription_plan_item(id)



Retrieves an entity of MarketDataSubscriptionPlan type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.market_data_subscription_plan_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_plan_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MarketDataSubscriptionPlan**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_items**
> list[MarketDataSubscriptionPlan] market_data_subscription_plan_items(ids)



Retrieves multiple entities of MarketDataSubscriptionPlan type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.market_data_subscription_plan_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_plan_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_list**
> list[MarketDataSubscriptionPlan] market_data_subscription_plan_list()



Retrieves all entities of MarketDataSubscriptionPlan type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.market_data_subscription_plan_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_plan_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_data_subscription_plan_suggest**
> list[MarketDataSubscriptionPlan] market_data_subscription_plan_suggest(t, l)



Retrieves entities of MarketDataSubscriptionPlan type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.market_data_subscription_plan_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->market_data_subscription_plan_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[MarketDataSubscriptionPlan]**](MarketDataSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_find**
> TradovateSubscriptionPlan tradovate_subscription_plan_find(name)



Retrieves an entity of TradovateSubscriptionPlan type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.tradovate_subscription_plan_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->tradovate_subscription_plan_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**TradovateSubscriptionPlan**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_item**
> TradovateSubscriptionPlan tradovate_subscription_plan_item(id)



Retrieves an entity of TradovateSubscriptionPlan type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.tradovate_subscription_plan_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->tradovate_subscription_plan_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TradovateSubscriptionPlan**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_items**
> list[TradovateSubscriptionPlan] tradovate_subscription_plan_items(ids)



Retrieves multiple entities of TradovateSubscriptionPlan type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.tradovate_subscription_plan_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->tradovate_subscription_plan_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_list**
> list[TradovateSubscriptionPlan] tradovate_subscription_plan_list()



Retrieves all entities of TradovateSubscriptionPlan type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.tradovate_subscription_plan_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->tradovate_subscription_plan_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tradovate_subscription_plan_suggest**
> list[TradovateSubscriptionPlan] tradovate_subscription_plan_suggest(t, l)



Retrieves entities of TradovateSubscriptionPlan type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.tradovate_subscription_plan_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->tradovate_subscription_plan_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[TradovateSubscriptionPlan]**](TradovateSubscriptionPlan.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

