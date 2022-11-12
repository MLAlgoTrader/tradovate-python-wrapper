# swagger_client.PositionsApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fill_pair_dependents**](PositionsApi.md#fill_pair_dependents) | **GET** /fillPair/deps | 
[**fill_pair_item**](PositionsApi.md#fill_pair_item) | **GET** /fillPair/item | 
[**fill_pair_items**](PositionsApi.md#fill_pair_items) | **GET** /fillPair/items | 
[**fill_pair_l_dependents**](PositionsApi.md#fill_pair_l_dependents) | **GET** /fillPair/ldeps | 
[**fill_pair_list**](PositionsApi.md#fill_pair_list) | **GET** /fillPair/list | 
[**position_dependents**](PositionsApi.md#position_dependents) | **GET** /position/deps | 
[**position_find**](PositionsApi.md#position_find) | **GET** /position/find | 
[**position_item**](PositionsApi.md#position_item) | **GET** /position/item | 
[**position_items**](PositionsApi.md#position_items) | **GET** /position/items | 
[**position_l_dependents**](PositionsApi.md#position_l_dependents) | **GET** /position/ldeps | 
[**position_list**](PositionsApi.md#position_list) | **GET** /position/list | 

# **fill_pair_dependents**
> list[FillPair] fill_pair_dependents(masterid)



Retrieves all entities of FillPair type related to Position entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Position entity

try:
    api_response = api_instance.fill_pair_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->fill_pair_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Position entity | 

### Return type

[**list[FillPair]**](FillPair.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_pair_item**
> FillPair fill_pair_item(id)



Retrieves an entity of FillPair type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.fill_pair_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->fill_pair_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FillPair**](FillPair.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_pair_items**
> list[FillPair] fill_pair_items(ids)



Retrieves multiple entities of FillPair type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.fill_pair_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->fill_pair_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[FillPair]**](FillPair.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_pair_l_dependents**
> list[FillPair] fill_pair_l_dependents(masterids)



Retrieves all entities of FillPair type related to multiple entities of Position type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Position entities

try:
    api_response = api_instance.fill_pair_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->fill_pair_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Position entities | 

### Return type

[**list[FillPair]**](FillPair.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_pair_list**
> list[FillPair] fill_pair_list()



Retrieves all entities of FillPair type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.fill_pair_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->fill_pair_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FillPair]**](FillPair.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_dependents**
> list[Position] position_dependents(masterid)



Retrieves all entities of Position type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.position_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_find**
> Position position_find(name)



Retrieves an entity of Position type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.position_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Position**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_item**
> Position position_item(id)



Retrieves an entity of Position type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.position_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Position**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_items**
> list[Position] position_items(ids)



Retrieves multiple entities of Position type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.position_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_l_dependents**
> list[Position] position_l_dependents(masterids)



Retrieves all entities of Position type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.position_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_list**
> list[Position] position_list()



Retrieves all entities of Position type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.PositionsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.position_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->position_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Position]**](Position.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

