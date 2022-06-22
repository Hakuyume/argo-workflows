# ScaleIOVolumeSource

ScaleIOVolumeSource represents a persistent ScaleIO volume

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fsType** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot;. | [optional] 
**gateway** | **str** | The host address of the ScaleIO API Gateway. | 
**protectionDomain** | **str** | The name of the ScaleIO Protection Domain for the configured storage. | [optional] 
**readOnly** | **bool** | Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secretRef** | [**LocalObjectReference**](LocalObjectReference.md) |  | 
**sslEnabled** | **bool** | Flag to enable/disable SSL communication with Gateway, default false | [optional] 
**storageMode** | **str** | Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. | [optional] 
**storagePool** | **str** | The ScaleIO Storage Pool associated with the protection domain. | [optional] 
**system** | **str** | The name of the storage system as configured in ScaleIO. | 
**volumeName** | **str** | The name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

