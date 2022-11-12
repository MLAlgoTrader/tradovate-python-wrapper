# swagger_client.ContractLibraryApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_dependents**](ContractLibraryApi.md#contract_dependents) | **GET** /contract/deps | 
[**contract_find**](ContractLibraryApi.md#contract_find) | **GET** /contract/find | 
[**contract_group_find**](ContractLibraryApi.md#contract_group_find) | **GET** /contractGroup/find | 
[**contract_group_item**](ContractLibraryApi.md#contract_group_item) | **GET** /contractGroup/item | 
[**contract_group_items**](ContractLibraryApi.md#contract_group_items) | **GET** /contractGroup/items | 
[**contract_group_list**](ContractLibraryApi.md#contract_group_list) | **GET** /contractGroup/list | 
[**contract_group_suggest**](ContractLibraryApi.md#contract_group_suggest) | **GET** /contractGroup/suggest | 
[**contract_item**](ContractLibraryApi.md#contract_item) | **GET** /contract/item | 
[**contract_items**](ContractLibraryApi.md#contract_items) | **GET** /contract/items | 
[**contract_l_dependents**](ContractLibraryApi.md#contract_l_dependents) | **GET** /contract/ldeps | 
[**contract_maturity_dependents**](ContractLibraryApi.md#contract_maturity_dependents) | **GET** /contractMaturity/deps | 
[**contract_maturity_item**](ContractLibraryApi.md#contract_maturity_item) | **GET** /contractMaturity/item | 
[**contract_maturity_items**](ContractLibraryApi.md#contract_maturity_items) | **GET** /contractMaturity/items | 
[**contract_maturity_l_dependents**](ContractLibraryApi.md#contract_maturity_l_dependents) | **GET** /contractMaturity/ldeps | 
[**contract_suggest**](ContractLibraryApi.md#contract_suggest) | **GET** /contract/suggest | 
[**currency_find**](ContractLibraryApi.md#currency_find) | **GET** /currency/find | 
[**currency_item**](ContractLibraryApi.md#currency_item) | **GET** /currency/item | 
[**currency_items**](ContractLibraryApi.md#currency_items) | **GET** /currency/items | 
[**currency_list**](ContractLibraryApi.md#currency_list) | **GET** /currency/list | 
[**currency_rate_dependents**](ContractLibraryApi.md#currency_rate_dependents) | **GET** /currencyRate/deps | 
[**currency_rate_item**](ContractLibraryApi.md#currency_rate_item) | **GET** /currencyRate/item | 
[**currency_rate_items**](ContractLibraryApi.md#currency_rate_items) | **GET** /currencyRate/items | 
[**currency_rate_l_dependents**](ContractLibraryApi.md#currency_rate_l_dependents) | **GET** /currencyRate/ldeps | 
[**currency_rate_list**](ContractLibraryApi.md#currency_rate_list) | **GET** /currencyRate/list | 
[**currency_suggest**](ContractLibraryApi.md#currency_suggest) | **GET** /currency/suggest | 
[**exchange_find**](ContractLibraryApi.md#exchange_find) | **GET** /exchange/find | 
[**exchange_item**](ContractLibraryApi.md#exchange_item) | **GET** /exchange/item | 
[**exchange_items**](ContractLibraryApi.md#exchange_items) | **GET** /exchange/items | 
[**exchange_list**](ContractLibraryApi.md#exchange_list) | **GET** /exchange/list | 
[**exchange_suggest**](ContractLibraryApi.md#exchange_suggest) | **GET** /exchange/suggest | 
[**get_product_fee_params**](ContractLibraryApi.md#get_product_fee_params) | **POST** /contract/getproductfeeparams | 
[**product_dependents**](ContractLibraryApi.md#product_dependents) | **GET** /product/deps | 
[**product_find**](ContractLibraryApi.md#product_find) | **GET** /product/find | 
[**product_item**](ContractLibraryApi.md#product_item) | **GET** /product/item | 
[**product_items**](ContractLibraryApi.md#product_items) | **GET** /product/items | 
[**product_l_dependents**](ContractLibraryApi.md#product_l_dependents) | **GET** /product/ldeps | 
[**product_list**](ContractLibraryApi.md#product_list) | **GET** /product/list | 
[**product_session_dependents**](ContractLibraryApi.md#product_session_dependents) | **GET** /productSession/deps | 
[**product_session_item**](ContractLibraryApi.md#product_session_item) | **GET** /productSession/item | 
[**product_session_items**](ContractLibraryApi.md#product_session_items) | **GET** /productSession/items | 
[**product_session_l_dependents**](ContractLibraryApi.md#product_session_l_dependents) | **GET** /productSession/ldeps | 
[**product_suggest**](ContractLibraryApi.md#product_suggest) | **GET** /product/suggest | 
[**roll_contract**](ContractLibraryApi.md#roll_contract) | **POST** /contract/rollcontract | 
[**spread_definition_item**](ContractLibraryApi.md#spread_definition_item) | **GET** /spreadDefinition/item | 
[**spread_definition_items**](ContractLibraryApi.md#spread_definition_items) | **GET** /spreadDefinition/items | 

# **contract_dependents**
> list[Contract] contract_dependents(masterid)



Retrieves all entities of Contract type related to ContractMaturity entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of ContractMaturity entity

try:
    api_response = api_instance.contract_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of ContractMaturity entity | 

### Return type

[**list[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_find**
> Contract contract_find(name)



Retrieves an entity of Contract type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.contract_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Contract**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_find**
> ContractGroup contract_group_find(name)



Retrieves an entity of ContractGroup type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.contract_group_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_group_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ContractGroup**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_item**
> ContractGroup contract_group_item(id)



Retrieves an entity of ContractGroup type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.contract_group_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_group_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContractGroup**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_items**
> list[ContractGroup] contract_group_items(ids)



Retrieves multiple entities of ContractGroup type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.contract_group_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_group_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_list**
> list[ContractGroup] contract_group_list()



Retrieves all entities of ContractGroup type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.contract_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_group_suggest**
> list[ContractGroup] contract_group_suggest(t, l)



Retrieves entities of ContractGroup type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.contract_group_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_group_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[ContractGroup]**](ContractGroup.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_item**
> Contract contract_item(id)



Retrieves an entity of Contract type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.contract_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Contract**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_items**
> list[Contract] contract_items(ids)



Retrieves multiple entities of Contract type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.contract_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_l_dependents**
> list[Contract] contract_l_dependents(masterids)



Retrieves all entities of Contract type related to multiple entities of ContractMaturity type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of ContractMaturity entities

try:
    api_response = api_instance.contract_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of ContractMaturity entities | 

### Return type

[**list[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_dependents**
> list[ContractMaturity] contract_maturity_dependents(masterid)



Retrieves all entities of ContractMaturity type related to Product entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Product entity

try:
    api_response = api_instance.contract_maturity_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_maturity_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity | 

### Return type

[**list[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_item**
> ContractMaturity contract_maturity_item(id)



Retrieves an entity of ContractMaturity type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.contract_maturity_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_maturity_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContractMaturity**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_items**
> list[ContractMaturity] contract_maturity_items(ids)



Retrieves multiple entities of ContractMaturity type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.contract_maturity_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_maturity_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_maturity_l_dependents**
> list[ContractMaturity] contract_maturity_l_dependents(masterids)



Retrieves all entities of ContractMaturity type related to multiple entities of Product type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Product entities

try:
    api_response = api_instance.contract_maturity_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_maturity_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Product entities | 

### Return type

[**list[ContractMaturity]**](ContractMaturity.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_suggest**
> list[Contract] contract_suggest(t, l)



Retrieves entities of Contract type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.contract_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->contract_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[Contract]**](Contract.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_find**
> Currency currency_find(name)



Retrieves an entity of Currency type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.currency_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Currency**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_item**
> Currency currency_item(id)



Retrieves an entity of Currency type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.currency_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Currency**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_items**
> list[Currency] currency_items(ids)



Retrieves multiple entities of Currency type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.currency_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_list**
> list[Currency] currency_list()



Retrieves all entities of Currency type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.currency_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_dependents**
> list[CurrencyRate] currency_rate_dependents(masterid)



Retrieves all entities of CurrencyRate type related to Currency entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Currency entity

try:
    api_response = api_instance.currency_rate_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_rate_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Currency entity | 

### Return type

[**list[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_item**
> CurrencyRate currency_rate_item(id)



Retrieves an entity of CurrencyRate type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.currency_rate_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CurrencyRate**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_items**
> list[CurrencyRate] currency_rate_items(ids)



Retrieves multiple entities of CurrencyRate type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.currency_rate_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_rate_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_l_dependents**
> list[CurrencyRate] currency_rate_l_dependents(masterids)



Retrieves all entities of CurrencyRate type related to multiple entities of Currency type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Currency entities

try:
    api_response = api_instance.currency_rate_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_rate_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Currency entities | 

### Return type

[**list[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_rate_list**
> list[CurrencyRate] currency_rate_list()



Retrieves all entities of CurrencyRate type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.currency_rate_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_rate_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CurrencyRate]**](CurrencyRate.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_suggest**
> list[Currency] currency_suggest(t, l)



Retrieves entities of Currency type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.currency_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->currency_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[Currency]**](Currency.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_find**
> Exchange exchange_find(name)



Retrieves an entity of Exchange type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.exchange_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->exchange_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Exchange**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_item**
> Exchange exchange_item(id)



Retrieves an entity of Exchange type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.exchange_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->exchange_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Exchange**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_items**
> list[Exchange] exchange_items(ids)



Retrieves multiple entities of Exchange type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.exchange_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->exchange_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_list**
> list[Exchange] exchange_list()



Retrieves all entities of Exchange type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.exchange_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->exchange_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_suggest**
> list[Exchange] exchange_suggest(t, l)



Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.exchange_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->exchange_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[Exchange]**](Exchange.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_fee_params**
> ProductFeeParamsResponse get_product_fee_params(body)



### Query the a product's fee parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetProductFeeParams() # GetProductFeeParams | 

try:
    api_response = api_instance.get_product_fee_params(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->get_product_fee_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetProductFeeParams**](GetProductFeeParams.md)|  | 

### Return type

[**ProductFeeParamsResponse**](ProductFeeParamsResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_dependents**
> list[Product] product_dependents(masterid)



Retrieves all entities of Product type related to Exchange entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Exchange entity

try:
    api_response = api_instance.product_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Exchange entity | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_find**
> Product product_find(name)



Retrieves an entity of Product type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.product_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_item**
> Product product_item(id)



Retrieves an entity of Product type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.product_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_items**
> list[Product] product_items(ids)



Retrieves multiple entities of Product type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.product_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_l_dependents**
> list[Product] product_l_dependents(masterids)



Retrieves all entities of Product type related to multiple entities of Exchange type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Exchange entities

try:
    api_response = api_instance.product_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Exchange entities | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_list**
> list[Product] product_list()



Retrieves all entities of Product type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.product_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_dependents**
> list[ProductSession] product_session_dependents(masterid)



Retrieves all entities of ProductSession type related to Product entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Product entity

try:
    api_response = api_instance.product_session_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_session_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity | 

### Return type

[**list[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_item**
> ProductSession product_session_item(id)



Retrieves an entity of ProductSession type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.product_session_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_session_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProductSession**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_items**
> list[ProductSession] product_session_items(ids)



Retrieves multiple entities of ProductSession type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.product_session_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_session_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_session_l_dependents**
> list[ProductSession] product_session_l_dependents(masterids)



Retrieves all entities of ProductSession type related to multiple entities of Product type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Product entities

try:
    api_response = api_instance.product_session_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_session_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Product entities | 

### Return type

[**list[ProductSession]**](ProductSession.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_suggest**
> list[Product] product_suggest(t, l)



Retrieves entities of Product type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.product_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->product_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roll_contract**
> RollContractResponse roll_contract(body)



### Request the best upcoming maturity date for a given contract.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
body = swagger_client.RollContract() # RollContract | 

try:
    api_response = api_instance.roll_contract(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->roll_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RollContract**](RollContract.md)|  | 

### Return type

[**RollContractResponse**](RollContractResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spread_definition_item**
> SpreadDefinition spread_definition_item(id)



Retrieves an entity of SpreadDefinition type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.spread_definition_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->spread_definition_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SpreadDefinition**](SpreadDefinition.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spread_definition_items**
> list[SpreadDefinition] spread_definition_items(ids)



Retrieves multiple entities of SpreadDefinition type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ContractLibraryApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.spread_definition_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractLibraryApi->spread_definition_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[SpreadDefinition]**](SpreadDefinition.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

