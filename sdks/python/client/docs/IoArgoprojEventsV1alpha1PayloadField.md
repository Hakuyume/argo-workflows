# IoArgoprojEventsV1alpha1PayloadField

PayloadField binds a value at path within the event payload against a name.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name acts as key that holds the value at the path. | [optional] 
**path** | **str** | Path is the JSONPath of the event&#x27;s (JSON decoded) data key Path is a series of keys separated by a dot. A key may contain wildcard characters &#x27;*&#x27; and &#x27;?&#x27;. To access an array value use the index as the key. The dot and wildcard characters can be escaped with &#x27;\\\\&#x27;. See https://github.com/tidwall/gjson#path-syntax for more information on how to use this. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

