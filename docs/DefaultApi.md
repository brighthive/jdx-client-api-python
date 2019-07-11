# openapi_client.DefaultApi

All URIs are relative to *https://jdx-api.brighthive.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**framework_recommendations_post**](DefaultApi.md#framework_recommendations_post) | **POST** /framework-recommendations | Get framework recommendations based on the uploaded job descripton and context.
[**framework_selections_post**](DefaultApi.md#framework_selections_post) | **POST** /framework-selections | The user indicates what frameworks they selected
[**generate_job_schema_plus_post**](DefaultApi.md#generate_job_schema_plus_post) | **POST** /generate-job-schema-plus | Generate JobSchema+
[**get_score_post**](DefaultApi.md#get_score_post) | **POST** /get-score | Provides a scored based on how much metadata you provide and the quality of that data.
[**health_get**](DefaultApi.md#health_get) | **GET** /health | Health Check
[**match_table_post**](DefaultApi.md#match_table_post) | **POST** /match-table | Get the match table associated with the provided &#x60;pipelineID&#x60;
[**preview_post**](DefaultApi.md#preview_post) | **POST** /preview | Get preview of job description with tagged matches.
[**upload_job_description_context_post**](DefaultApi.md#upload_job_description_context_post) | **POST** /upload-job-description-context | Provide job description context (e.g metadata) on the job description
[**upload_job_description_file_post**](DefaultApi.md#upload_job_description_file_post) | **POST** /upload-job-description-file | Upload a raw job description file.
[**user_actions_post**](DefaultApi.md#user_actions_post) | **POST** /user-actions | Provide the user responses as a list of user actions


# **framework_recommendations_post**
> FrameworkRecommendationResponse framework_recommendations_post(request=request)

Get framework recommendations based on the uploaded job descripton and context.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
request = openapi_client.Request() # Request | Get framework-recommendations for a given Pipeline ID. (optional)

try:
    # Get framework recommendations based on the uploaded job descripton and context.
    api_response = api_instance.framework_recommendations_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->framework_recommendations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)| Get framework-recommendations for a given Pipeline ID. | [optional] 

### Return type

[**FrameworkRecommendationResponse**](FrameworkRecommendationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a list of frameworks, including competencies, occupation and industries, that the user may choose from (one or more). |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **framework_selections_post**
> Response framework_selections_post(framework_selection_request=framework_selection_request)

The user indicates what frameworks they selected

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
framework_selection_request = openapi_client.FrameworkSelectionRequest() # FrameworkSelectionRequest | framework selections (optional)

try:
    # The user indicates what frameworks they selected
    api_response = api_instance.framework_selections_post(framework_selection_request=framework_selection_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->framework_selections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **framework_selection_request** | [**FrameworkSelectionRequest**](FrameworkSelectionRequest.md)| framework selections | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored the context object associated with &#x60;pipelineID&#x60; |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_job_schema_plus_post**
> GenerateJobSchemaPlusResponse generate_job_schema_plus_post(request=request)

Generate JobSchema+

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
request = openapi_client.Request() # Request | Generate JobSchema+ from a given pipeline_id (optional)

try:
    # Generate JobSchema+
    api_response = api_instance.generate_job_schema_plus_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_job_schema_plus_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)| Generate JobSchema+ from a given pipeline_id | [optional] 

### Return type

[**GenerateJobSchemaPlusResponse**](GenerateJobSchemaPlusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JobSchema+ file |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_post**
> PipelineScoreResponse get_score_post(request=request)

Provides a scored based on how much metadata you provide and the quality of that data.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
request = openapi_client.Request() # Request | Get score for a given Pipeline ID. (optional)

try:
    # Provides a scored based on how much metadata you provide and the quality of that data.
    api_response = api_instance.get_score_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_score_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)| Get score for a given Pipeline ID. | [optional] 

### Return type

[**PipelineScoreResponse**](PipelineScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a score for your pipeline work. |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_get**
> HealthResponse health_get()

Health Check

The health check endpoint can be used to check if the API is up. If the API is running it will return a 200 OK response.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    # Health Check
    api_response = api_instance.health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API is up! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_table_post**
> MatchTableResponse match_table_post(match_table_request=match_table_request)

Get the match table associated with the provided `pipelineID`

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
match_table_request = openapi_client.MatchTableRequest() # MatchTableRequest | Get framework-recommendations for a given Pipeline ID. (optional)

try:
    # Get the match table associated with the provided `pipelineID`
    api_response = api_instance.match_table_post(match_table_request=match_table_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->match_table_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_table_request** | [**MatchTableRequest**](MatchTableRequest.md)| Get framework-recommendations for a given Pipeline ID. | [optional] 

### Return type

[**MatchTableResponse**](MatchTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a match table with &#x60;uuid&#x60; references along with a json-ld object. The json-ld object contains &#x60;uuid&#x60;&#39;s that reference into the match table, for instance, containing a list of possble competencies that the user should be asked to choose among, reject or approve one of. |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_post**
> PreviewResponse preview_post(request=request)

Get preview of job description with tagged matches.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
request = openapi_client.Request() # Request | Get preview of job description wth tagged matches. (optional)

try:
    # Get preview of job description with tagged matches.
    api_response = api_instance.preview_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->preview_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)| Get preview of job description wth tagged matches. | [optional] 

### Return type

[**PreviewResponse**](PreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a chunked job description with matches that refer to the given paragraph chunks. |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_description_context_post**
> JobDescriptionContextResponse upload_job_description_context_post(job_description_context_request=job_description_context_request)

Provide job description context (e.g metadata) on the job description

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
job_description_context_request = openapi_client.JobDescriptionContextRequest() # JobDescriptionContextRequest | job description context (optional)

try:
    # Provide job description context (e.g metadata) on the job description
    api_response = api_instance.upload_job_description_context_post(job_description_context_request=job_description_context_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_description_context_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_description_context_request** | [**JobDescriptionContextRequest**](JobDescriptionContextRequest.md)| job description context | [optional] 

### Return type

[**JobDescriptionContextResponse**](JobDescriptionContextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored the context object associated with &#x60;pipelineID&#x60; |  -  |
**400** | Bad Request |  -  |
**404** | Pipeline was not found |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |
**503** | Service is down |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_description_file_post**
> RawJobDescriptionResponse upload_job_description_file_post(file=file)

Upload a raw job description file.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
file = '/path/to/file' # file | The file to upload (optional)

try:
    # Upload a raw job description file.
    api_response = api_instance.upload_job_description_file_post(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_job_description_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to upload | [optional] 

### Return type

[**RawJobDescriptionResponse**](RawJobDescriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created. A pipeline was created and the provided job description was converted to text and attached to the pipeline. |  -  |
**400** | Bad Request |  -  |
**422** | Validation error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_actions_post**
> Response user_actions_post(user_action_request=user_action_request)

Provide the user responses as a list of user actions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
user_action_request = openapi_client.UserActionRequest() # UserActionRequest | Contains a list of user responses (optional)

try:
    # Provide the user responses as a list of user actions
    api_response = api_instance.user_actions_post(user_action_request=user_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_actions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_action_request** | [**UserActionRequest**](UserActionRequest.md)| Contains a list of user responses | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user actions response object |  -  |
**422** | Validation error. |  -  |
**400** | Bad Request error |  -  |
**415** | Unsupported media type |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

