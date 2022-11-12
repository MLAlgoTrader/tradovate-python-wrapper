# swagger_client.ChatApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_dependents**](ChatApi.md#chat_dependents) | **GET** /chat/deps | 
[**chat_item**](ChatApi.md#chat_item) | **GET** /chat/item | 
[**chat_items**](ChatApi.md#chat_items) | **GET** /chat/items | 
[**chat_l_dependents**](ChatApi.md#chat_l_dependents) | **GET** /chat/ldeps | 
[**chat_list**](ChatApi.md#chat_list) | **GET** /chat/list | 
[**chat_message_dependents**](ChatApi.md#chat_message_dependents) | **GET** /chatMessage/deps | 
[**chat_message_item**](ChatApi.md#chat_message_item) | **GET** /chatMessage/item | 
[**chat_message_items**](ChatApi.md#chat_message_items) | **GET** /chatMessage/items | 
[**chat_message_l_dependents**](ChatApi.md#chat_message_l_dependents) | **GET** /chatMessage/ldeps | 
[**close_chat**](ChatApi.md#close_chat) | **POST** /chat/closechat | 
[**mark_as_read_chat_message**](ChatApi.md#mark_as_read_chat_message) | **POST** /chat/markasreadchatmessage | 
[**post_chat_message**](ChatApi.md#post_chat_message) | **POST** /chat/postchatmessage | 

# **chat_dependents**
> list[Chat] chat_dependents(masterid)



Retrieves all entities of Chat type related to User entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of User entity

try:
    api_response = api_instance.chat_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of User entity | 

### Return type

[**list[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_item**
> Chat chat_item(id)



Retrieves an entity of Chat type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.chat_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Chat**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_items**
> list[Chat] chat_items(ids)



Retrieves multiple entities of Chat type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.chat_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_l_dependents**
> list[Chat] chat_l_dependents(masterids)



Retrieves all entities of Chat type related to multiple entities of User type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of User entities

try:
    api_response = api_instance.chat_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of User entities | 

### Return type

[**list[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_list**
> list[Chat] chat_list()



Retrieves all entities of Chat type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.chat_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Chat]**](Chat.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_dependents**
> list[ChatMessage] chat_message_dependents(masterid)



Retrieves all entities of ChatMessage type related to Chat entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
masterid = 789 # int | id of Chat entity

try:
    api_response = api_instance.chat_message_dependents(masterid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_message_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterid** | **int**| id of Chat entity | 

### Return type

[**list[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_item**
> ChatMessage chat_message_item(id)



Retrieves an entity of ChatMessage type by its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
id = 789 # int | 

try:
    api_response = api_instance.chat_message_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_message_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_items**
> list[ChatMessage] chat_message_items(ids)



Retrieves multiple entities of ChatMessage type by its ids

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | 

try:
    api_response = api_instance.chat_message_items(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_message_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_message_l_dependents**
> list[ChatMessage] chat_message_l_dependents(masterids)



Retrieves all entities of ChatMessage type related to multiple entities of Chat type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
masterids = [56] # list[int] | ids of Chat entities

try:
    api_response = api_instance.chat_message_l_dependents(masterids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_message_l_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **masterids** | [**list[int]**](int.md)| ids of Chat entities | 

### Return type

[**list[ChatMessage]**](ChatMessage.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_chat**
> ChatResponse close_chat(body)



### Close the chat context.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
body = swagger_client.CloseChat() # CloseChat | 

try:
    api_response = api_instance.close_chat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->close_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloseChat**](CloseChat.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_read_chat_message**
> ChatMessageResponse mark_as_read_chat_message(body)



### Marks a chat message as read.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarkAsReadChatMessage() # MarkAsReadChatMessage | 

try:
    api_response = api_instance.mark_as_read_chat_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->mark_as_read_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkAsReadChatMessage**](MarkAsReadChatMessage.md)|  | 

### Return type

[**ChatMessageResponse**](ChatMessageResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_chat_message**
> ChatMessageResponse post_chat_message(body)



### Post a chat message to a given chat's history.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostChatMessage() # PostChatMessage | 

try:
    api_response = api_instance.post_chat_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->post_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostChatMessage**](PostChatMessage.md)|  | 

### Return type

[**ChatMessageResponse**](ChatMessageResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

