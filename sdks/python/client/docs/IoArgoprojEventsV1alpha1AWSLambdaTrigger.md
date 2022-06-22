# IoArgoprojEventsV1alpha1AWSLambdaTrigger

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**functionName** | **str** | FunctionName refers to the name of the function to invoke. | [optional] 
**invocationType** | **str** | Choose from the following options.     * RequestResponse (default) - Invoke the function synchronously. Keep    the connection open until the function returns a response or times out.    The API response includes the function response and additional data.     * Event - Invoke the function asynchronously. Send events that fail multiple    times to the function&#x27;s dead-letter queue (if it&#x27;s configured). The API    response only includes a status code.     * DryRun - Validate parameter values and verify that the user or role    has permission to invoke the function. +optional | [optional] 
**parameters** | **[IoArgoprojEventsV1alpha1TriggerParameter]** |  | [optional] 
**payload** | **[IoArgoprojEventsV1alpha1TriggerParameter]** | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**region** | **str** |  | [optional] 
**roleARN** | **str** |  | [optional] 
**secretKey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

