# swagger_client.ConfigurationApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_alert_find**](ConfigurationApi.md#admin_alert_find) | **GET** /adminAlert/find | 
[**admin_alert_item**](ConfigurationApi.md#admin_alert_item) | **GET** /adminAlert/item | 
[**admin_alert_items**](ConfigurationApi.md#admin_alert_items) | **GET** /adminAlert/items | 
[**admin_alert_list**](ConfigurationApi.md#admin_alert_list) | **GET** /adminAlert/list | 
[**admin_alert_suggest**](ConfigurationApi.md#admin_alert_suggest) | **GET** /adminAlert/suggest | 
[**clearing_house_find**](ConfigurationApi.md#clearing_house_find) | **GET** /clearingHouse/find | 
[**clearing_house_item**](ConfigurationApi.md#clearing_house_item) | **GET** /clearingHouse/item | 
[**clearing_house_items**](ConfigurationApi.md#clearing_house_items) | **GET** /clearingHouse/items | 
[**clearing_house_list**](ConfigurationApi.md#clearing_house_list) | **GET** /clearingHouse/list | 
[**clearing_house_suggest**](ConfigurationApi.md#clearing_house_suggest) | **GET** /clearingHouse/suggest | 
[**entitlement_item**](ConfigurationApi.md#entitlement_item) | **GET** /entitlement/item | 
[**entitlement_items**](ConfigurationApi.md#entitlement_items) | **GET** /entitlement/items | 
[**entitlement_list**](ConfigurationApi.md#entitlement_list) | **GET** /entitlement/list | 
[**order_strategy_type_find**](ConfigurationApi.md#order_strategy_type_find) | **GET** /orderStrategyType/find | 
[**order_strategy_type_item**](ConfigurationApi.md#order_strategy_type_item) | **GET** /orderStrategyType/item | 
[**order_strategy_type_items**](ConfigurationApi.md#order_strategy_type_items) | **GET** /orderStrategyType/items | 
[**order_strategy_type_list**](ConfigurationApi.md#order_strategy_type_list) | **GET** /orderStrategyType/list | 
[**order_strategy_type_suggest**](ConfigurationApi.md#order_strategy_type_suggest) | **GET** /orderStrategyType/suggest | 
[**property_find**](ConfigurationApi.md#property_find) | **GET** /property/find | 
[**property_item**](ConfigurationApi.md#property_item) | **GET** /property/item | 
[**property_items**](ConfigurationApi.md#property_items) | **GET** /property/items | 
[**property_list**](ConfigurationApi.md#property_list) | **GET** /property/list | 
[**property_suggest**](ConfigurationApi.md#property_suggest) | **GET** /property/suggest | 

# **admin_alert_find**
> AdminAlert admin_alert_find(name)



Retrieves an entity of AdminAlert type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.admin_alert_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->admin_alert_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**AdminAlert**](AdminAlert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_item**
> AdminAlert admin_alert_item(id)



Retrieves an entity of AdminAlert type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.admin_alert_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->admin_alert_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdminAlert**](AdminAlert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_items**
> list[AdminAlert] admin_alert_items(ids)



Retrieves multiple entities of AdminAlert type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.admin_alert_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->admin_alert_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[AdminAlert]**](AdminAlert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_list**
> list[AdminAlert] admin_alert_list()



Retrieves all entities of AdminAlert type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.admin_alert_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->admin_alert_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdminAlert]**](AdminAlert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_suggest**
> list[AdminAlert] admin_alert_suggest(t, l)



Retrieves entities of AdminAlert type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.admin_alert_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->admin_alert_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[AdminAlert]**](AdminAlert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clearing_house_find**
> ClearingHouse clearing_house_find(name)



Retrieves an entity of ClearingHouse type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.clearing_house_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->clearing_house_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ClearingHouse**](ClearingHouse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clearing_house_item**
> ClearingHouse clearing_house_item(id)



Retrieves an entity of ClearingHouse type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.clearing_house_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->clearing_house_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ClearingHouse**](ClearingHouse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clearing_house_items**
> list[ClearingHouse] clearing_house_items(ids)



Retrieves multiple entities of ClearingHouse type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.clearing_house_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->clearing_house_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ClearingHouse]**](ClearingHouse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clearing_house_list**
> list[ClearingHouse] clearing_house_list()



Retrieves all entities of ClearingHouse type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.clearing_house_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->clearing_house_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClearingHouse]**](ClearingHouse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clearing_house_suggest**
> list[ClearingHouse] clearing_house_suggest(t, l)



Retrieves entities of ClearingHouse type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.clearing_house_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->clearing_house_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[ClearingHouse]**](ClearingHouse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_item**
> Entitlement entitlement_item(id)



Retrieves an entity of Entitlement type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.entitlement_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->entitlement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_items**
> list[Entitlement] entitlement_items(ids)



Retrieves multiple entities of Entitlement type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.entitlement_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->entitlement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Entitlement]**](Entitlement.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_list**
> list[Entitlement] entitlement_list()



Retrieves all entities of Entitlement type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.entitlement_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->entitlement_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Entitlement]**](Entitlement.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_type_find**
> OrderStrategyType order_strategy_type_find(name)



Retrieves an entity of OrderStrategyType type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.order_strategy_type_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->order_strategy_type_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**OrderStrategyType**](OrderStrategyType.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_type_item**
> OrderStrategyType order_strategy_type_item(id)



Retrieves an entity of OrderStrategyType type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.order_strategy_type_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->order_strategy_type_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderStrategyType**](OrderStrategyType.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_type_items**
> list[OrderStrategyType] order_strategy_type_items(ids)



Retrieves multiple entities of OrderStrategyType type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.order_strategy_type_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->order_strategy_type_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[OrderStrategyType]**](OrderStrategyType.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_type_list**
> list[OrderStrategyType] order_strategy_type_list()



Retrieves all entities of OrderStrategyType type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_strategy_type_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->order_strategy_type_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrderStrategyType]**](OrderStrategyType.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_type_suggest**
> list[OrderStrategyType] order_strategy_type_suggest(t, l)



Retrieves entities of OrderStrategyType type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.order_strategy_type_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->order_strategy_type_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[OrderStrategyType]**](OrderStrategyType.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_find**
> ModelProperty property_find(name)



Retrieves an entity of Property type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.property_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->property_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_item**
> ModelProperty property_item(id)



Retrieves an entity of Property type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.property_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->property_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_items**
> list[ModelProperty] property_items(ids)



Retrieves multiple entities of Property type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.property_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->property_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_list**
> list[ModelProperty] property_list()



Retrieves all entities of Property type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.property_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->property_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_suggest**
> list[ModelProperty] property_suggest(t, l)



Retrieves entities of Property type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.property_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->property_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

