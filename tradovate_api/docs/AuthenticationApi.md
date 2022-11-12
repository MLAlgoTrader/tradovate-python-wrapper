# swagger_client.AuthenticationApi

All URIs are relative to *https://demo.tradovateapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token_request**](AuthenticationApi.md#access_token_request) | **POST** /auth/accesstokenrequest | 
[**me**](AuthenticationApi.md#me) | **GET** /auth/me | 
[**o_auth_token**](AuthenticationApi.md#o_auth_token) | **POST** /auth/oauthtoken | 
[**renew_access_token**](AuthenticationApi.md#renew_access_token) | **GET** /auth/renewaccesstoken | 

# **access_token_request**
> AccessTokenResponse access_token_request(body)



#### Request an access token using your user credentials and API Key.   See the [Access](/#tag/Access) section for more details. For a comprehensive guide on how to acquire and use an access token in the JavaScript language, see out [JavaScript tutorial](https://github.com/tradovate/example-api-js) repository. For usage examples using the C# language, see the [C# example](https://github.com/tradovate/example-api-csharp-trading) repository.  ### Acquiring an Access Token  ```js const URL = 'https://live.tradovateapi.com/v1'  const credentials = {     name:       \"Your credentials here\",     password:   \"Your credentials here\",     appId:      \"Sample App\",     appVersion: \"1.0\",     cid:        0,     sec:        \"Your API secret here\" }  async function getAccessToken() {     let response = await fetch(URL + '/auth/accessTokenRequest', {         method: 'POST',         headers: {             'Content-Type': 'application/json'         }     })     let result = await response.json()     return result // { accessToken, mdAccessToken, userId, ... } }  //...  async function main() {     const { accessToken, mdAccessToken, userId } = await getAccessToken()      //use access token } ```  ### Using an Access Token  ```js //use the Authorization: Bearer schema in API POST and GET requests  //simple /account/list endpoint requires no body or query async function getAccounts() {     let response = await fetch(URL + '/account/list', {         method: 'GET',         headers: {             'Content-Type': 'application/json',             Authorization: `Bearer ${accessToken}` //Access Token use in HTTP requests         }     })     let result = await response.json()     return result }  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AccessTokenRequest() # AccessTokenRequest | 

try:
    api_response = api_instance.access_token_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->access_token_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenRequest**](AccessTokenRequest.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> OAuthMeResponse me()



### Shows Basic user data for the calling user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthMeResponse**](OAuthMeResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_token**
> OAuthTokenResponse o_auth_token(body)



### Used to exchange your OAuth code for an access token. Using the OAuth authorization delegation flow, we can send a request to verify that our users are who they say they are. For more information on using OAuth with the Tradovate API see our [OAuth JavaScript tutorial](https://github.com/tradovate/example-api-oauth).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.OAuthToken() # OAuthToken | 

try:
    api_response = api_instance.o_auth_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthToken**](OAuthToken.md)|  | 

### Return type

[**OAuthTokenResponse**](OAuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_access_token**
> AccessTokenResponse renew_access_token()



### Request a renewal for an existing access token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.renew_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->renew_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[bearer_access_token](../README.md#bearer_access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

