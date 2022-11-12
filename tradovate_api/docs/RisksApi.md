# swagger_client.RisksApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_risk_status_dependents**](RisksApi.md#account_risk_status_dependents) | **GET** /accountRiskStatus/deps | 
[**account_risk_status_item**](RisksApi.md#account_risk_status_item) | **GET** /accountRiskStatus/item | 
[**account_risk_status_items**](RisksApi.md#account_risk_status_items) | **GET** /accountRiskStatus/items | 
[**account_risk_status_l_dependents**](RisksApi.md#account_risk_status_l_dependents) | **GET** /accountRiskStatus/ldeps | 
[**account_risk_status_list**](RisksApi.md#account_risk_status_list) | **GET** /accountRiskStatus/list | 
[**contract_margin_dependents**](RisksApi.md#contract_margin_dependents) | **GET** /contractMargin/deps | 
[**contract_margin_item**](RisksApi.md#contract_margin_item) | **GET** /contractMargin/item | 
[**contract_margin_items**](RisksApi.md#contract_margin_items) | **GET** /contractMargin/items | 
[**contract_margin_l_dependents**](RisksApi.md#contract_margin_l_dependents) | **GET** /contractMargin/ldeps | 
[**delete_user_account_position_limit**](RisksApi.md#delete_user_account_position_limit) | **POST** /userAccountPositionLimit/deleteuseraccountpositionlimit | 
[**delete_user_account_risk_parameter**](RisksApi.md#delete_user_account_risk_parameter) | **POST** /userAccountPositionLimit/deleteuseraccountriskparameter | 
[**product_margin_dependents**](RisksApi.md#product_margin_dependents) | **GET** /productMargin/deps | 
[**product_margin_item**](RisksApi.md#product_margin_item) | **GET** /productMargin/item | 
[**product_margin_items**](RisksApi.md#product_margin_items) | **GET** /productMargin/items | 
[**product_margin_l_dependents**](RisksApi.md#product_margin_l_dependents) | **GET** /productMargin/ldeps | 
[**product_margin_list**](RisksApi.md#product_margin_list) | **GET** /productMargin/list | 
[**user_account_auto_liq_create**](RisksApi.md#user_account_auto_liq_create) | **POST** /userAccountAutoLiq/create | 
[**user_account_auto_liq_dependents**](RisksApi.md#user_account_auto_liq_dependents) | **GET** /userAccountAutoLiq/deps | 
[**user_account_auto_liq_item**](RisksApi.md#user_account_auto_liq_item) | **GET** /userAccountAutoLiq/item | 
[**user_account_auto_liq_items**](RisksApi.md#user_account_auto_liq_items) | **GET** /userAccountAutoLiq/items | 
[**user_account_auto_liq_l_dependents**](RisksApi.md#user_account_auto_liq_l_dependents) | **GET** /userAccountAutoLiq/ldeps | 
[**user_account_auto_liq_list**](RisksApi.md#user_account_auto_liq_list) | **GET** /userAccountAutoLiq/list | 
[**user_account_auto_liq_update**](RisksApi.md#user_account_auto_liq_update) | **POST** /userAccountAutoLiq/update | 
[**user_account_position_limit_create**](RisksApi.md#user_account_position_limit_create) | **POST** /userAccountPositionLimit/create | 
[**user_account_position_limit_dependents**](RisksApi.md#user_account_position_limit_dependents) | **GET** /userAccountPositionLimit/deps | 
[**user_account_position_limit_item**](RisksApi.md#user_account_position_limit_item) | **GET** /userAccountPositionLimit/item | 
[**user_account_position_limit_items**](RisksApi.md#user_account_position_limit_items) | **GET** /userAccountPositionLimit/items | 
[**user_account_position_limit_l_dependents**](RisksApi.md#user_account_position_limit_l_dependents) | **GET** /userAccountPositionLimit/ldeps | 
[**user_account_position_limit_update**](RisksApi.md#user_account_position_limit_update) | **POST** /userAccountPositionLimit/update | 
[**user_account_risk_parameter_create**](RisksApi.md#user_account_risk_parameter_create) | **POST** /userAccountRiskParameter/create | 
[**user_account_risk_parameter_dependents**](RisksApi.md#user_account_risk_parameter_dependents) | **GET** /userAccountRiskParameter/deps | 
[**user_account_risk_parameter_item**](RisksApi.md#user_account_risk_parameter_item) | **GET** /userAccountRiskParameter/item | 
[**user_account_risk_parameter_items**](RisksApi.md#user_account_risk_parameter_items) | **GET** /userAccountRiskParameter/items | 
[**user_account_risk_parameter_l_dependents**](RisksApi.md#user_account_risk_parameter_l_dependents) | **GET** /userAccountRiskParameter/ldeps | 
[**user_account_risk_parameter_update**](RisksApi.md#user_account_risk_parameter_update) | **POST** /userAccountRiskParameter/update | 

# **account_risk_status_dependents**
> list[AccountRiskStatus] account_risk_status_dependents(masterid)



Retrieves all entities of AccountRiskStatus type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.account_risk_status_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->account_risk_status_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[AccountRiskStatus]**](AccountRiskStatus.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_risk_status_item**
> AccountRiskStatus account_risk_status_item(id)



Retrieves an entity of AccountRiskStatus type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.account_risk_status_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->account_risk_status_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountRiskStatus**](AccountRiskStatus.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_risk_status_items**
> list[AccountRiskStatus] account_risk_status_items(ids)



Retrieves multiple entities of AccountRiskStatus type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.account_risk_status_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->account_risk_status_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[AccountRiskStatus]**](AccountRiskStatus.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_risk_status_l_dependents**
> list[AccountRiskStatus] account_risk_status_l_dependents(masterids)



Retrieves all entities of AccountRiskStatus type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.account_risk_status_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->account_risk_status_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[AccountRiskStatus]**](AccountRiskStatus.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_risk_status_list**
> list[AccountRiskStatus] account_risk_status_list()



Retrieves all entities of AccountRiskStatus type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.account_risk_status_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->account_risk_status_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AccountRiskStatus]**](AccountRiskStatus.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_dependents**
> list[ContractMargin] contract_margin_dependents(masterid)



Retrieves all entities of ContractMargin type related to Contract entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Contract entity

try:
    api_response = api_instance.contract_margin_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->contract_margin_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Contract entity | 

### Return type

[**list[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_item**
> ContractMargin contract_margin_item(id)



Retrieves an entity of ContractMargin type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.contract_margin_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->contract_margin_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContractMargin**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_items**
> list[ContractMargin] contract_margin_items(ids)



Retrieves multiple entities of ContractMargin type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.contract_margin_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->contract_margin_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_margin_l_dependents**
> list[ContractMargin] contract_margin_l_dependents(masterids)



Retrieves all entities of ContractMargin type related to multiple entities of Contract type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Contract entities

try:
    api_response = api_instance.contract_margin_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->contract_margin_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Contract entities | 

### Return type

[**list[ContractMargin]**](ContractMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_account_position_limit**
> DeleteResultResponse delete_user_account_position_limit(body)



### Remove an account position limit for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteUserAccountPositionLimit() # DeleteUserAccountPositionLimit | 

try:
    api_response = api_instance.delete_user_account_position_limit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->delete_user_account_position_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUserAccountPositionLimit**](DeleteUserAccountPositionLimit.md)|  | 

### Return type

[**DeleteResultResponse**](DeleteResultResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_account_risk_parameter**
> DeleteResultResponse delete_user_account_risk_parameter(body)



### Remove a Risk Setting parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteUserAccountRiskParameter() # DeleteUserAccountRiskParameter | 

try:
    api_response = api_instance.delete_user_account_risk_parameter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->delete_user_account_risk_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUserAccountRiskParameter**](DeleteUserAccountRiskParameter.md)|  | 

### Return type

[**DeleteResultResponse**](DeleteResultResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_dependents**
> list[ProductMargin] product_margin_dependents(masterid)



Retrieves all entities of ProductMargin type related to Product entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Product entity

try:
    api_response = api_instance.product_margin_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->product_margin_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Product entity | 

### Return type

[**list[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_item**
> ProductMargin product_margin_item(id)



Retrieves an entity of ProductMargin type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.product_margin_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->product_margin_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProductMargin**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_items**
> list[ProductMargin] product_margin_items(ids)



Retrieves multiple entities of ProductMargin type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.product_margin_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->product_margin_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_l_dependents**
> list[ProductMargin] product_margin_l_dependents(masterids)



Retrieves all entities of ProductMargin type related to multiple entities of Product type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Product entities

try:
    api_response = api_instance.product_margin_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->product_margin_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Product entities | 

### Return type

[**list[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_margin_list**
> list[ProductMargin] product_margin_list()



Retrieves all entities of ProductMargin type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.product_margin_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->product_margin_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductMargin]**](ProductMargin.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_create**
> UserAccountAutoLiq user_account_auto_liq_create(body)



Creates a new entity of UserAccountAutoLiq

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountAutoLiq() # UserAccountAutoLiq | 

try:
    api_response = api_instance.user_account_auto_liq_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountAutoLiq**](UserAccountAutoLiq.md)|  | 

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_dependents**
> list[UserAccountAutoLiq] user_account_auto_liq_dependents(masterid)



Retrieves all entities of UserAccountAutoLiq type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.user_account_auto_liq_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_item**
> UserAccountAutoLiq user_account_auto_liq_item(id)



Retrieves an entity of UserAccountAutoLiq type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.user_account_auto_liq_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_items**
> list[UserAccountAutoLiq] user_account_auto_liq_items(ids)



Retrieves multiple entities of UserAccountAutoLiq type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.user_account_auto_liq_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_l_dependents**
> list[UserAccountAutoLiq] user_account_auto_liq_l_dependents(masterids)



Retrieves all entities of UserAccountAutoLiq type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.user_account_auto_liq_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_list**
> list[UserAccountAutoLiq] user_account_auto_liq_list()



Retrieves all entities of UserAccountAutoLiq type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.user_account_auto_liq_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserAccountAutoLiq]**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_auto_liq_update**
> UserAccountAutoLiq user_account_auto_liq_update(body)



Updates an existing entity of UserAccountAutoLiq

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountAutoLiq() # UserAccountAutoLiq | 

try:
    api_response = api_instance.user_account_auto_liq_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_auto_liq_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountAutoLiq**](UserAccountAutoLiq.md)|  | 

### Return type

[**UserAccountAutoLiq**](UserAccountAutoLiq.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_create**
> UserAccountPositionLimit user_account_position_limit_create(body)



Creates a new entity of UserAccountPositionLimit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountPositionLimit() # UserAccountPositionLimit | 

try:
    api_response = api_instance.user_account_position_limit_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountPositionLimit**](UserAccountPositionLimit.md)|  | 

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_dependents**
> list[UserAccountPositionLimit] user_account_position_limit_dependents(masterid)



Retrieves all entities of UserAccountPositionLimit type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.user_account_position_limit_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_item**
> UserAccountPositionLimit user_account_position_limit_item(id)



Retrieves an entity of UserAccountPositionLimit type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.user_account_position_limit_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_items**
> list[UserAccountPositionLimit] user_account_position_limit_items(ids)



Retrieves multiple entities of UserAccountPositionLimit type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.user_account_position_limit_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_l_dependents**
> list[UserAccountPositionLimit] user_account_position_limit_l_dependents(masterids)



Retrieves all entities of UserAccountPositionLimit type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.user_account_position_limit_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[UserAccountPositionLimit]**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_position_limit_update**
> UserAccountPositionLimit user_account_position_limit_update(body)



Updates an existing entity of UserAccountPositionLimit

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountPositionLimit() # UserAccountPositionLimit | 

try:
    api_response = api_instance.user_account_position_limit_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_position_limit_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountPositionLimit**](UserAccountPositionLimit.md)|  | 

### Return type

[**UserAccountPositionLimit**](UserAccountPositionLimit.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_create**
> UserAccountRiskParameter user_account_risk_parameter_create(body)



Creates a new entity of UserAccountRiskParameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountRiskParameter() # UserAccountRiskParameter | 

try:
    api_response = api_instance.user_account_risk_parameter_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountRiskParameter**](UserAccountRiskParameter.md)|  | 

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_dependents**
> list[UserAccountRiskParameter] user_account_risk_parameter_dependents(masterid)



Retrieves all entities of UserAccountRiskParameter type related to UserAccountPositionLimit entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of UserAccountPositionLimit entity

try:
    api_response = api_instance.user_account_risk_parameter_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of UserAccountPositionLimit entity | 

### Return type

[**list[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_item**
> UserAccountRiskParameter user_account_risk_parameter_item(id)



Retrieves an entity of UserAccountRiskParameter type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.user_account_risk_parameter_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_items**
> list[UserAccountRiskParameter] user_account_risk_parameter_items(ids)



Retrieves multiple entities of UserAccountRiskParameter type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.user_account_risk_parameter_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_l_dependents**
> list[UserAccountRiskParameter] user_account_risk_parameter_l_dependents(masterids)



Retrieves all entities of UserAccountRiskParameter type related to multiple entities of UserAccountPositionLimit type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of UserAccountPositionLimit entities

try:
    api_response = api_instance.user_account_risk_parameter_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of UserAccountPositionLimit entities | 

### Return type

[**list[UserAccountRiskParameter]**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_risk_parameter_update**
> UserAccountRiskParameter user_account_risk_parameter_update(body)



Updates an existing entity of UserAccountRiskParameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RisksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAccountRiskParameter() # UserAccountRiskParameter | 

try:
    api_response = api_instance.user_account_risk_parameter_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->user_account_risk_parameter_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccountRiskParameter**](UserAccountRiskParameter.md)|  | 

### Return type

[**UserAccountRiskParameter**](UserAccountRiskParameter.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

