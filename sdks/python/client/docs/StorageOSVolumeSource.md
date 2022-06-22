# StorageOSVolumeSource

Represents a StorageOS persistent volume resource.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fsType** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**readOnly** | **bool** | Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secretRef** | [**LocalObjectReference**](LocalObjectReference.md) |  | [optional] 
**volumeName** | **str** | VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. | [optional] 
**volumeNamespace** | **str** | VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod&#x27;s namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to \&quot;default\&quot; if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

