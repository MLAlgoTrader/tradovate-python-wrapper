# swagger_client.OrdersApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /order/cancelorder | 
[**command_dependents**](OrdersApi.md#command_dependents) | **GET** /command/deps | 
[**command_item**](OrdersApi.md#command_item) | **GET** /command/item | 
[**command_items**](OrdersApi.md#command_items) | **GET** /command/items | 
[**command_l_dependents**](OrdersApi.md#command_l_dependents) | **GET** /command/ldeps | 
[**command_list**](OrdersApi.md#command_list) | **GET** /command/list | 
[**command_report_dependents**](OrdersApi.md#command_report_dependents) | **GET** /commandReport/deps | 
[**command_report_item**](OrdersApi.md#command_report_item) | **GET** /commandReport/item | 
[**command_report_items**](OrdersApi.md#command_report_items) | **GET** /commandReport/items | 
[**command_report_l_dependents**](OrdersApi.md#command_report_l_dependents) | **GET** /commandReport/ldeps | 
[**command_report_list**](OrdersApi.md#command_report_list) | **GET** /commandReport/list | 
[**execution_report_dependents**](OrdersApi.md#execution_report_dependents) | **GET** /executionReport/deps | 
[**execution_report_find**](OrdersApi.md#execution_report_find) | **GET** /executionReport/find | 
[**execution_report_item**](OrdersApi.md#execution_report_item) | **GET** /executionReport/item | 
[**execution_report_items**](OrdersApi.md#execution_report_items) | **GET** /executionReport/items | 
[**execution_report_l_dependents**](OrdersApi.md#execution_report_l_dependents) | **GET** /executionReport/ldeps | 
[**execution_report_list**](OrdersApi.md#execution_report_list) | **GET** /executionReport/list | 
[**execution_report_suggest**](OrdersApi.md#execution_report_suggest) | **GET** /executionReport/suggest | 
[**fill_dependents**](OrdersApi.md#fill_dependents) | **GET** /fill/deps | 
[**fill_fee_dependents**](OrdersApi.md#fill_fee_dependents) | **GET** /fillFee/deps | 
[**fill_fee_item**](OrdersApi.md#fill_fee_item) | **GET** /fillFee/item | 
[**fill_fee_items**](OrdersApi.md#fill_fee_items) | **GET** /fillFee/items | 
[**fill_fee_l_dependents**](OrdersApi.md#fill_fee_l_dependents) | **GET** /fillFee/ldeps | 
[**fill_fee_list**](OrdersApi.md#fill_fee_list) | **GET** /fillFee/list | 
[**fill_item**](OrdersApi.md#fill_item) | **GET** /fill/item | 
[**fill_items**](OrdersApi.md#fill_items) | **GET** /fill/items | 
[**fill_l_dependents**](OrdersApi.md#fill_l_dependents) | **GET** /fill/ldeps | 
[**fill_list**](OrdersApi.md#fill_list) | **GET** /fill/list | 
[**interrupt_order_strategy**](OrdersApi.md#interrupt_order_strategy) | **POST** /orderStrategy/interruptorderstrategy | 
[**liquidate_position**](OrdersApi.md#liquidate_position) | **POST** /order/liquidateposition | 
[**modify_order**](OrdersApi.md#modify_order) | **POST** /order/modifyorder | 
[**modify_order_strategy**](OrdersApi.md#modify_order_strategy) | **POST** /orderStrategy/modifyorderstrategy | 
[**order_dependents**](OrdersApi.md#order_dependents) | **GET** /order/deps | 
[**order_item**](OrdersApi.md#order_item) | **GET** /order/item | 
[**order_items**](OrdersApi.md#order_items) | **GET** /order/items | 
[**order_l_dependents**](OrdersApi.md#order_l_dependents) | **GET** /order/ldeps | 
[**order_list**](OrdersApi.md#order_list) | **GET** /order/list | 
[**order_strategy_dependents**](OrdersApi.md#order_strategy_dependents) | **GET** /orderStrategy/deps | 
[**order_strategy_item**](OrdersApi.md#order_strategy_item) | **GET** /orderStrategy/item | 
[**order_strategy_items**](OrdersApi.md#order_strategy_items) | **GET** /orderStrategy/items | 
[**order_strategy_l_dependents**](OrdersApi.md#order_strategy_l_dependents) | **GET** /orderStrategy/ldeps | 
[**order_strategy_link_dependents**](OrdersApi.md#order_strategy_link_dependents) | **GET** /orderStrategyLink/deps | 
[**order_strategy_link_item**](OrdersApi.md#order_strategy_link_item) | **GET** /orderStrategyLink/item | 
[**order_strategy_link_items**](OrdersApi.md#order_strategy_link_items) | **GET** /orderStrategyLink/items | 
[**order_strategy_link_l_dependents**](OrdersApi.md#order_strategy_link_l_dependents) | **GET** /orderStrategyLink/ldeps | 
[**order_strategy_link_list**](OrdersApi.md#order_strategy_link_list) | **GET** /orderStrategyLink/list | 
[**order_strategy_list**](OrdersApi.md#order_strategy_list) | **GET** /orderStrategy/list | 
[**order_version_dependents**](OrdersApi.md#order_version_dependents) | **GET** /orderVersion/deps | 
[**order_version_item**](OrdersApi.md#order_version_item) | **GET** /orderVersion/item | 
[**order_version_items**](OrdersApi.md#order_version_items) | **GET** /orderVersion/items | 
[**order_version_l_dependents**](OrdersApi.md#order_version_l_dependents) | **GET** /orderVersion/ldeps | 
[**order_version_list**](OrdersApi.md#order_version_list) | **GET** /orderVersion/list | 
[**place_oco**](OrdersApi.md#place_oco) | **POST** /order/placeoco | 
[**place_order**](OrdersApi.md#place_order) | **POST** /order/placeorder | 
[**place_oso**](OrdersApi.md#place_oso) | **POST** /order/placeoso | 
[**start_order_strategy**](OrdersApi.md#start_order_strategy) | **POST** /orderStrategy/startorderstrategy | 

# **cancel_order**
> CommandResult cancel_order(body)



### Make a request to cancel an order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancelOrder() # CancelOrder | 

try:
    api_response = api_instance.cancel_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelOrder**](CancelOrder.md)|  | 

### Return type

[**CommandResult**](CommandResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_dependents**
> list[Command] command_dependents(masterid)



Retrieves all entities of Command type related to Order entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Order entity

try:
    api_response = api_instance.command_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity | 

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_item**
> Command command_item(id)



Retrieves an entity of Command type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.command_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Command**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_items**
> list[Command] command_items(ids)



Retrieves multiple entities of Command type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.command_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_l_dependents**
> list[Command] command_l_dependents(masterids)



Retrieves all entities of Command type related to multiple entities of Order type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Order entities

try:
    api_response = api_instance.command_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Order entities | 

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_list**
> list[Command] command_list()



Retrieves all entities of Command type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.command_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_dependents**
> list[CommandReport] command_report_dependents(masterid)



Retrieves all entities of CommandReport type related to Command entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Command entity

try:
    api_response = api_instance.command_report_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_report_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Command entity | 

### Return type

[**list[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_item**
> CommandReport command_report_item(id)



Retrieves an entity of CommandReport type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.command_report_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_report_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CommandReport**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_items**
> list[CommandReport] command_report_items(ids)



Retrieves multiple entities of CommandReport type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.command_report_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_report_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_l_dependents**
> list[CommandReport] command_report_l_dependents(masterids)



Retrieves all entities of CommandReport type related to multiple entities of Command type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Command entities

try:
    api_response = api_instance.command_report_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_report_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Command entities | 

### Return type

[**list[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_report_list**
> list[CommandReport] command_report_list()



Retrieves all entities of CommandReport type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.command_report_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->command_report_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CommandReport]**](CommandReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_dependents**
> list[ExecutionReport] execution_report_dependents(masterid)



Retrieves all entities of ExecutionReport type related to Command entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Command entity

try:
    api_response = api_instance.execution_report_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Command entity | 

### Return type

[**list[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_find**
> ExecutionReport execution_report_find(name)



Retrieves an entity of ExecutionReport type by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.execution_report_find(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ExecutionReport**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_item**
> ExecutionReport execution_report_item(id)



Retrieves an entity of ExecutionReport type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.execution_report_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExecutionReport**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_items**
> list[ExecutionReport] execution_report_items(ids)



Retrieves multiple entities of ExecutionReport type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.execution_report_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_l_dependents**
> list[ExecutionReport] execution_report_l_dependents(masterids)



Retrieves all entities of ExecutionReport type related to multiple entities of Command type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Command entities

try:
    api_response = api_instance.execution_report_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Command entities | 

### Return type

[**list[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_list**
> list[ExecutionReport] execution_report_list()



Retrieves all entities of ExecutionReport type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.execution_report_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution_report_suggest**
> list[ExecutionReport] execution_report_suggest(t, l)



Retrieves entities of ExecutionReport type filtered by an occurrence of a text in one of its fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
t = 't_example' # str | Text
l = 56 # int | Max number of entities

try:
    api_response = api_instance.execution_report_suggest(t, l)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->execution_report_suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **str**| Text | 
 **l** | **int**| Max number of entities | 

### Return type

[**list[ExecutionReport]**](ExecutionReport.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_dependents**
> list[Fill] fill_dependents(masterid)



Retrieves all entities of Fill type related to Order entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Order entity

try:
    api_response = api_instance.fill_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity | 

### Return type

[**list[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_dependents**
> list[FillFee] fill_fee_dependents(masterid)



Retrieves all entities of FillFee type related to Fill entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Fill entity

try:
    api_response = api_instance.fill_fee_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_fee_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Fill entity | 

### Return type

[**list[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_item**
> FillFee fill_fee_item(id)



Retrieves an entity of FillFee type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.fill_fee_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_fee_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FillFee**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_items**
> list[FillFee] fill_fee_items(ids)



Retrieves multiple entities of FillFee type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.fill_fee_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_fee_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_l_dependents**
> list[FillFee] fill_fee_l_dependents(masterids)



Retrieves all entities of FillFee type related to multiple entities of Fill type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Fill entities

try:
    api_response = api_instance.fill_fee_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_fee_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Fill entities | 

### Return type

[**list[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_fee_list**
> list[FillFee] fill_fee_list()



Retrieves all entities of FillFee type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.fill_fee_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_fee_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FillFee]**](FillFee.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_item**
> Fill fill_item(id)



Retrieves an entity of Fill type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.fill_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Fill**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_items**
> list[Fill] fill_items(ids)



Retrieves multiple entities of Fill type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.fill_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_l_dependents**
> list[Fill] fill_l_dependents(masterids)



Retrieves all entities of Fill type related to multiple entities of Order type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Order entities

try:
    api_response = api_instance.fill_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Order entities | 

### Return type

[**list[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_list**
> list[Fill] fill_list()



Retrieves all entities of Fill type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.fill_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->fill_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Fill]**](Fill.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interrupt_order_strategy**
> OrderStrategyStatusResponse interrupt_order_strategy(body)



### Stop a running multi-bracket strategy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterruptOrderStrategy() # InterruptOrderStrategy | 

try:
    api_response = api_instance.interrupt_order_strategy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->interrupt_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterruptOrderStrategy**](InterruptOrderStrategy.md)|  | 

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidate_position**
> PlaceOrderResult liquidate_position(body)



### Send a request to cancel orders for a specific contract and close that position for the given account. This request initiates the cancellation process of open orders for an existing position held by this account. > Note: This is a request to cancel orders and close a position, not a guarantee. Any operation could fail for a number of reasons, ranging from Exchange rejection to incorrect parameterization. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.LiquidatePosition() # LiquidatePosition | 

try:
    api_response = api_instance.liquidate_position(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->liquidate_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiquidatePosition**](LiquidatePosition.md)|  | 

### Return type

[**PlaceOrderResult**](PlaceOrderResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_order**
> CommandResult modify_order(body)



### Make a request to modify the parameters of an order. You can request changes to an order, such as the trigger price for a Stop or Limit order. > *Note*: This is no guarantee that the order can be modified in the way requests. Market, exchange and logical rules apply. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModifyOrder() # ModifyOrder | 

try:
    api_response = api_instance.modify_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->modify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyOrder**](ModifyOrder.md)|  | 

### Return type

[**CommandResult**](CommandResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_order_strategy**
> OrderStrategyStatusResponse modify_order_strategy(body)



### Modify an existing Order Strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModifyOrderStrategy() # ModifyOrderStrategy | 

try:
    api_response = api_instance.modify_order_strategy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->modify_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyOrderStrategy**](ModifyOrderStrategy.md)|  | 

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_dependents**
> list[Order] order_dependents(masterid)



Retrieves all entities of Order type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.order_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_item**
> Order order_item(id)



Retrieves an entity of Order type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.order_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Order**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_items**
> list[Order] order_items(ids)



Retrieves multiple entities of Order type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.order_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_l_dependents**
> list[Order] order_l_dependents(masterids)



Retrieves all entities of Order type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.order_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_list**
> list[Order] order_list()



Retrieves all entities of Order type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Order]**](Order.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_dependents**
> list[OrderStrategy] order_strategy_dependents(masterid)



Retrieves all entities of OrderStrategy type related to Account entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Account entity

try:
    api_response = api_instance.order_strategy_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Account entity | 

### Return type

[**list[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_item**
> OrderStrategy order_strategy_item(id)



Retrieves an entity of OrderStrategy type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.order_strategy_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderStrategy**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_items**
> list[OrderStrategy] order_strategy_items(ids)



Retrieves multiple entities of OrderStrategy type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.order_strategy_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_l_dependents**
> list[OrderStrategy] order_strategy_l_dependents(masterids)



Retrieves all entities of OrderStrategy type related to multiple entities of Account type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Account entities

try:
    api_response = api_instance.order_strategy_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Account entities | 

### Return type

[**list[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_dependents**
> list[OrderStrategyLink] order_strategy_link_dependents(masterid)



Retrieves all entities of OrderStrategyLink type related to OrderStrategy entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of OrderStrategy entity

try:
    api_response = api_instance.order_strategy_link_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_link_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of OrderStrategy entity | 

### Return type

[**list[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_item**
> OrderStrategyLink order_strategy_link_item(id)



Retrieves an entity of OrderStrategyLink type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.order_strategy_link_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_link_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderStrategyLink**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_items**
> list[OrderStrategyLink] order_strategy_link_items(ids)



Retrieves multiple entities of OrderStrategyLink type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.order_strategy_link_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_link_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_l_dependents**
> list[OrderStrategyLink] order_strategy_link_l_dependents(masterids)



Retrieves all entities of OrderStrategyLink type related to multiple entities of OrderStrategy type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of OrderStrategy entities

try:
    api_response = api_instance.order_strategy_link_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_link_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of OrderStrategy entities | 

### Return type

[**list[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_link_list**
> list[OrderStrategyLink] order_strategy_link_list()



Retrieves all entities of OrderStrategyLink type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_strategy_link_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_link_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrderStrategyLink]**](OrderStrategyLink.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_strategy_list**
> list[OrderStrategy] order_strategy_list()



Retrieves all entities of OrderStrategy type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_strategy_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_strategy_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrderStrategy]**](OrderStrategy.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_dependents**
> list[OrderVersion] order_version_dependents(masterid)



Retrieves all entities of OrderVersion type related to Order entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Order entity

try:
    api_response = api_instance.order_version_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_version_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Order entity | 

### Return type

[**list[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_item**
> OrderVersion order_version_item(id)



Retrieves an entity of OrderVersion type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.order_version_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_version_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderVersion**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_items**
> list[OrderVersion] order_version_items(ids)



Retrieves multiple entities of OrderVersion type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.order_version_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_version_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_l_dependents**
> list[OrderVersion] order_version_l_dependents(masterids)



Retrieves all entities of OrderVersion type related to multiple entities of Order type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Order entities

try:
    api_response = api_instance.order_version_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_version_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Order entities | 

### Return type

[**list[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_version_list**
> list[OrderVersion] order_version_list()



Retrieves all entities of OrderVersion type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.order_version_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_version_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrderVersion]**](OrderVersion.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_oco**
> PlaceOcoResult place_oco(body)



### Place a Order Cancels Order order strategy. OCO order strategies link 2 orders together such that if one order is filled, the other order is cancelled. You must provide an `other` parameter pertaining to the order linked to this one. The `other` must specify an `action` and an `orderType` which determines the other parameters that must be set. For example a Limit or Stop order must use the `price` parameter, but a Stop-Limit will require a `price` and a `stopPrice`. Below is an example of an OCO that either sells to take profit at 4200 points, or sells to stop loss at 4100 points.  ```js const URL = 'demo.tradovateapi.com/v1' const limit = {     action: 'Sell',     orderType: 'Limit',     price: 4200.00 } const oco = {     accountSpec: yourUserName,     accountId: yourAcctId,     action: \"Buy\",     symbol: \"MESM1\",     orderQty: 1,     orderType: \"Stop\",     price: 4100.00     isAutomated: true, //must be true if this isn't an order made directly by a human     other: limit }  const response = await fetch(URL + '/order/placeoco', {     method: 'POST',     headers: {         'Accept': 'application/json',         'Authorization': `Bearer ${myAccessToken}`,     },     body: JSON.stringify(oco) })  const json = await response.json() // { orderId: 0000000, ocoId: 0000000 } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlaceOCO() # PlaceOCO | 

try:
    api_response = api_instance.place_oco(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->place_oco: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceOCO**](PlaceOCO.md)|  | 

### Return type

[**PlaceOcoResult**](PlaceOcoResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> PlaceOrderResult place_order(body)



### Make a request to place an order.  Depending on the order type, the parameters vary. In the Trader application, you can see the details of placing a standard order ticket by adding the Order Ticket module to your workspace.  #### *Market Order* ```js const URL = 'demo.tradovateapi.com/v1' const body = {     accountSpec: yourUserName,     accountId: yourAcctId,     action: \"Buy\",     symbol: \"MYMM1\",     orderQty: 1,     orderType: \"Market\",     isAutomated: true //must be true if this isn't an order made directly by a human }  const response = await fetch(URL + '/order/placeorder', {     method: 'POST',     headers: {         'Accept': 'application/json',         'Authorization': `Bearer ${myAccessToken}`,     },     body: JSON.stringify(body) })  const json = await response.json() // { orderId: 0000000 }  ```  #### *Sell Limit* ```js const URL = 'demo.tradovateapi.com/v1' const body = {     accountSpec: yourUserName,     accountId: yourAcctId,     action: \"Sell\",     symbol: \"MYMM1\",     orderQty: 1,     orderType: \"Limit\",     price: 35000, //use for single value like limit or stop     isAutomated: true //must be true if this isn't an order made directly by a human }  const response = await fetch(URL + '/order/placeorder', {     method: 'POST',     headers: {         'Accept': 'application/json',         'Authorization': `Bearer ${myAccessToken}`,     },     body: JSON.stringify(body) })  const json = await response.json() // { orderId: 0000000 }  ``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlaceOrder() # PlaceOrder | 

try:
    api_response = api_instance.place_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->place_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceOrder**](PlaceOrder.md)|  | 

### Return type

[**PlaceOrderResult**](PlaceOrderResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_oso**
> PlaceOsoResult place_oso(body)



### Place an Order Sends Order order strategy. In the Trader application, the details of OSO orders can be viewed by adding the Order Ticket module to your workspace and selecting the Advanced workspace options with Brackets enabled. OSO orders allow for the most complex multi-bracket trading strategies. As an example, imagine MESM1 is trading around 4175.00 points. You want to place a Buy order for 4150.00 points, buying below market. We place an OSO to take profits at 4200.00 points. If the initial order is filled, the `bracket1` order will be sent. Below is an example in JavaScript:  ```js const URL = 'demo.tradovateapi.com/v1'  const oso = {     action: 'Sell',     orderType: 'Limit',     price: 4200.00, }  const initial = {     accountSpec: yourUserName,     accountId: yourAcctId,     action: \"Buy\",     symbol: \"MESM1\",     orderQty: 1,     orderType: \"Limit\",     price: 4150.00,     isAutomated: true //must be true if this isn't an order made directly by a human     bracket1: oso }  const response = await fetch(URL + '/order/placeOSO', {     method: 'POST',     headers: {         'Accept': 'application/json',         'Authorization': `Bearer ${myAccessToken}`,     },     body: JSON.stringify(initial) })  const json = await response.json() // { orderId: 0000000 } ```  >*Note:* If you specify both `bracket1` and `bracket2` the two orders will be linked as an OCO, where filling one will cancel the other.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlaceOSO() # PlaceOSO | 

try:
    api_response = api_instance.place_oso(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->place_oso: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceOSO**](PlaceOSO.md)|  | 

### Return type

[**PlaceOsoResult**](PlaceOsoResult.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_order_strategy**
> OrderStrategyStatusResponse start_order_strategy(body)



### Start a multi-bracket trading strategy. This endpoint is used with a WebSocket. You can create any number of brackets and add them to `brackets` field on the `params` object as a JSON string.  ```js  const URL = 'wss://demo.tradovateapi.com/v1/websocket'  const params = {     entryVersion: {         orderQty: 1,         orderType: \"Market\"     },     brackets: [{         qty: 1,         profitTarget: -30,         stopLoss: 15,         trailingStop: false     }] }  const body = {     accountId: myAcctId,     accountSpec: name,     symbol: 'MESM1',     action: 'Sell',     orderStrategyTypeId: 2, //2 is 'multibracket', we currently only offer this strategy but more may exist in the future.     params: JSON.stringify(params) }  const mySocket = new WebSocket(URL)  //authorize socket using your access token mySocket.onopen = function() {     mySocket.send(`authorize\\n0\\n\\n${accessToken}`) }  mySocket.send(`orderstrategy/startorderstrategy\\n4\\n\\n${JSON.stringify(body)}`)  ```  For more details about working with advanced order types, see [placeOrder](/#operation/placeOrder), [placeOCO](/#operation/placeOCO), and [placeOSO](/#operation/placeOSO).  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.StartOrderStrategy() # StartOrderStrategy | 

try:
    api_response = api_instance.start_order_strategy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->start_order_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartOrderStrategy**](StartOrderStrategy.md)|  | 

### Return type

[**OrderStrategyStatusResponse**](OrderStrategyStatusResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

