# IoArgoprojWorkflowV1alpha1HDFSArtifact

HDFSArtifact is the location of an HDFS artifact

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **[str]** | Addresses is accessible addresses of HDFS name nodes | [optional] 
**force** | **bool** | Force copies a file forcibly even if it exists | [optional] 
**hdfsUser** | **str** | HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used. | [optional] 
**krbCCacheSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krbConfigConfigMap** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**krbKeytabSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**krbRealm** | **str** | KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used. | [optional] 
**krbServicePrincipalName** | **str** | KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used. | [optional] 
**krbUsername** | **str** | KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used. | [optional] 
**path** | **str** | Path is a file path in HDFS | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

