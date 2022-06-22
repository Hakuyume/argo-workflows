# ExecAction

ExecAction describes a \"run in container\" action.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **[str]** | Command is the command line to execute inside the container, the working directory for the command  is root (&#x27;/&#x27;) in the container&#x27;s filesystem. The command is simply exec&#x27;d, it is not run inside a shell, so traditional shell instructions (&#x27;|&#x27;, etc) won&#x27;t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

