# IoArgoprojWorkflowV1alpha1GitArtifact

GitArtifact is the location of an git artifact

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | Branch is the branch to fetch when &#x60;SingleBranch&#x60; is enabled | [optional] 
**depth** | **int** | Depth specifies clones/fetches should be shallow and include the given number of commits from the branch tip | [optional] 
**disableSubmodules** | **bool** | DisableSubmodules disables submodules during git clone | [optional] 
**fetch** | **[str]** | Fetch specifies a number of refs that should be fetched before checkout | [optional] 
**insecureIgnoreHostKey** | **bool** | InsecureIgnoreHostKey disables SSH strict host key checking during git clone | [optional] 
**passwordSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**repo** | **str** | Repo is the git repository | 
**revision** | **str** | Revision is the git commit, tag, branch to checkout | [optional] 
**singleBranch** | **bool** | SingleBranch enables single branch clone, using the &#x60;branch&#x60; parameter | [optional] 
**sshPrivateKeySecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**usernameSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

