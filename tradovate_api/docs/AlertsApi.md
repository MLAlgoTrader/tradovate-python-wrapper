# swagger_client.AlertsApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_alert_signal_dependents**](AlertsApi.md#admin_alert_signal_dependents) | **GET** /adminAlertSignal/deps | 
[**admin_alert_signal_item**](AlertsApi.md#admin_alert_signal_item) | **GET** /adminAlertSignal/item | 
[**admin_alert_signal_items**](AlertsApi.md#admin_alert_signal_items) | **GET** /adminAlertSignal/items | 
[**admin_alert_signal_l_dependents**](AlertsApi.md#admin_alert_signal_l_dependents) | **GET** /adminAlertSignal/ldeps | 
[**admin_alert_signal_list**](AlertsApi.md#admin_alert_signal_list) | **GET** /adminAlertSignal/list | 
[**alert_dependents**](AlertsApi.md#alert_dependents) | **GET** /alert/deps | 
[**alert_item**](AlertsApi.md#alert_item) | **GET** /alert/item | 
[**alert_items**](AlertsApi.md#alert_items) | **GET** /alert/items | 
[**alert_l_dependents**](AlertsApi.md#alert_l_dependents) | **GET** /alert/ldeps | 
[**alert_list**](AlertsApi.md#alert_list) | **GET** /alert/list | 
[**alert_signal_dependents**](AlertsApi.md#alert_signal_dependents) | **GET** /alertSignal/deps | 
[**alert_signal_item**](AlertsApi.md#alert_signal_item) | **GET** /alertSignal/item | 
[**alert_signal_items**](AlertsApi.md#alert_signal_items) | **GET** /alertSignal/items | 
[**alert_signal_l_dependents**](AlertsApi.md#alert_signal_l_dependents) | **GET** /alertSignal/ldeps | 
[**alert_signal_list**](AlertsApi.md#alert_signal_list) | **GET** /alertSignal/list | 
[**complete_alert_signal**](AlertsApi.md#complete_alert_signal) | **POST** /adminAlertSignal/completealertsignal | 
[**create_alert**](AlertsApi.md#create_alert) | **POST** /alert/createalert | 
[**delete_alert**](AlertsApi.md#delete_alert) | **POST** /alert/deletealert | 
[**dismiss_alert**](AlertsApi.md#dismiss_alert) | **POST** /alert/dismissalert | 
[**mark_read_alert_signal**](AlertsApi.md#mark_read_alert_signal) | **POST** /alert/markreadalertsignal | 
[**modify_alert**](AlertsApi.md#modify_alert) | **POST** /alert/modifyalert | 
[**reset_alert**](AlertsApi.md#reset_alert) | **POST** /alert/resetalert | 
[**take_alert_signal_ownership**](AlertsApi.md#take_alert_signal_ownership) | **POST** /adminAlertSignal/takealertsignalownership | 

# **admin_alert_signal_dependents**
> list[AdminAlertSignal] admin_alert_signal_dependents(masterid)



Retrieves all entities of AdminAlertSignal type related to AdminAlert entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of AdminAlert entity

try:
    api_response = api_instance.admin_alert_signal_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->admin_alert_signal_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of AdminAlert entity | 

### Return type

[**list[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_item**
> AdminAlertSignal admin_alert_signal_item(id)



Retrieves an entity of AdminAlertSignal type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.admin_alert_signal_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->admin_alert_signal_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdminAlertSignal**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_items**
> list[AdminAlertSignal] admin_alert_signal_items(ids)



Retrieves multiple entities of AdminAlertSignal type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.admin_alert_signal_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->admin_alert_signal_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_l_dependents**
> list[AdminAlertSignal] admin_alert_signal_l_dependents(masterids)



Retrieves all entities of AdminAlertSignal type related to multiple entities of AdminAlert type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of AdminAlert entities

try:
    api_response = api_instance.admin_alert_signal_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->admin_alert_signal_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of AdminAlert entities | 

### Return type

[**list[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_alert_signal_list**
> list[AdminAlertSignal] admin_alert_signal_list()



Retrieves all entities of AdminAlertSignal type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.admin_alert_signal_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->admin_alert_signal_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdminAlertSignal]**](AdminAlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_dependents**
> list[Alert] alert_dependents(masterid)



Retrieves all entities of Alert type related to User entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of User entity

try:
    api_response = api_instance.alert_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity | 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_item**
> Alert alert_item(id)



Retrieves an entity of Alert type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.alert_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_items**
> list[Alert] alert_items(ids)



Retrieves multiple entities of Alert type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.alert_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_l_dependents**
> list[Alert] alert_l_dependents(masterids)



Retrieves all entities of Alert type related to multiple entities of User type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of User entities

try:
    api_response = api_instance.alert_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of User entities | 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_list**
> list[Alert] alert_list()



Retrieves all entities of Alert type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.alert_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_dependents**
> list[AlertSignal] alert_signal_dependents(masterid)



Retrieves all entities of AlertSignal type related to Alert entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Alert entity

try:
    api_response = api_instance.alert_signal_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_signal_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Alert entity | 

### Return type

[**list[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_item**
> AlertSignal alert_signal_item(id)



Retrieves an entity of AlertSignal type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.alert_signal_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_signal_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AlertSignal**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_items**
> list[AlertSignal] alert_signal_items(ids)



Retrieves multiple entities of AlertSignal type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.alert_signal_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_signal_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_l_dependents**
> list[AlertSignal] alert_signal_l_dependents(masterids)



Retrieves all entities of AlertSignal type related to multiple entities of Alert type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Alert entities

try:
    api_response = api_instance.alert_signal_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_signal_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Alert entities | 

### Return type

[**list[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_signal_list**
> list[AlertSignal] alert_signal_list()



Retrieves all entities of AlertSignal type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.alert_signal_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alert_signal_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertSignal]**](AlertSignal.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_alert_signal**
> AdminAlertSignalResponse complete_alert_signal(body)



### Silences an \"incomplete\" notification.  An \"Incomplete\" notification is one that has not yet been viewed by a user. Once a user has interacted with a notification it should be \"completed\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompleteAlertSignal() # CompleteAlertSignal | 

try:
    api_response = api_instance.complete_alert_signal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->complete_alert_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompleteAlertSignal**](CompleteAlertSignal.md)|  | 

### Return type

[**AdminAlertSignalResponse**](AdminAlertSignalResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> AlertResponse create_alert(body)



### Create an alert entity associated with the user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateAlert() # CreateAlert | 

try:
    api_response = api_instance.create_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAlert**](CreateAlert.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> AlertResponse delete_alert(body)



### Remove an alert entity associated with the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteAlert() # DeleteAlert | 

try:
    api_response = api_instance.delete_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAlert**](DeleteAlert.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dismiss_alert**
> AlertResponse dismiss_alert(body)



### Dismiss an alert for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DismissAlert() # DismissAlert | 

try:
    api_response = api_instance.dismiss_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->dismiss_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DismissAlert**](DismissAlert.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_read_alert_signal**
> AlertResponse mark_read_alert_signal(body)



### Mark an alert entity as 'read' for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkReadAlertSignal() # MarkReadAlertSignal | 

try:
    api_response = api_instance.mark_read_alert_signal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->mark_read_alert_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkReadAlertSignal**](MarkReadAlertSignal.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_alert**
> AlertResponse modify_alert(body)



### Change the parameters of an existing alert.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModifyAlert() # ModifyAlert | 

try:
    api_response = api_instance.modify_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->modify_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyAlert**](ModifyAlert.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_alert**
> AlertResponse reset_alert(body)



### Resets an alert.  You can use this method after an alert has been triggered to keep the alert and wait for the alert to be triggered again.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetAlert() # ResetAlert | 

try:
    api_response = api_instance.reset_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->reset_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetAlert**](ResetAlert.md)|  | 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_alert_signal_ownership**
> AdminAlertSignalResponse take_alert_signal_ownership(body)



### Internal. Can be used by B2B partners to mark an adminAlertSignal entity for further handling.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TakeAlertSignalOwnership() # TakeAlertSignalOwnership | 

try:
    api_response = api_instance.take_alert_signal_ownership(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->take_alert_signal_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TakeAlertSignalOwnership**](TakeAlertSignalOwnership.md)|  | 

### Return type

[**AdminAlertSignalResponse**](AdminAlertSignalResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

