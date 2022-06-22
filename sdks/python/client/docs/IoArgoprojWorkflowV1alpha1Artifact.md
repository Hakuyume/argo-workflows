# IoArgoprojWorkflowV1alpha1Artifact

Artifact indicates an artifact to place at a specified path

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive** | [**IoArgoprojWorkflowV1alpha1ArchiveStrategy**](IoArgoprojWorkflowV1alpha1ArchiveStrategy.md) |  | [optional] 
**archiveLogs** | **bool** | ArchiveLogs indicates if the container logs should be archived | [optional] 
**artifactGC** | [**IoArgoprojWorkflowV1alpha1ArtifactGC**](IoArgoprojWorkflowV1alpha1ArtifactGC.md) |  | [optional] 
**artifactory** | [**IoArgoprojWorkflowV1alpha1ArtifactoryArtifact**](IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.md) |  | [optional] 
**deleted** | **bool** | Has this been deleted? | [optional] 
**from** | **str** | From allows an artifact to reference an artifact from a previous step | [optional] 
**fromExpression** | **str** | FromExpression, if defined, is evaluated to specify the value for the artifact | [optional] 
**gcs** | [**IoArgoprojWorkflowV1alpha1GCSArtifact**](IoArgoprojWorkflowV1alpha1GCSArtifact.md) |  | [optional] 
**git** | [**IoArgoprojWorkflowV1alpha1GitArtifact**](IoArgoprojWorkflowV1alpha1GitArtifact.md) |  | [optional] 
**globalName** | **str** | GlobalName exports an output artifact to the global scope, making it available as &#x27;{{io.argoproj.workflow.v1alpha1.outputs.artifacts.XXXX}} and in workflow.status.outputs.artifacts | [optional] 
**hdfs** | [**IoArgoprojWorkflowV1alpha1HDFSArtifact**](IoArgoprojWorkflowV1alpha1HDFSArtifact.md) |  | [optional] 
**http** | [**IoArgoprojWorkflowV1alpha1HTTPArtifact**](IoArgoprojWorkflowV1alpha1HTTPArtifact.md) |  | [optional] 
**mode** | **int** | mode bits to use on this file, must be a value between 0 and 0777 set when loading input artifacts. | [optional] 
**name** | **str** | name of the artifact. must be unique within a template&#x27;s inputs/outputs. | 
**optional** | **bool** | Make Artifacts optional, if Artifacts doesn&#x27;t generate or exist | [optional] 
**oss** | [**IoArgoprojWorkflowV1alpha1OSSArtifact**](IoArgoprojWorkflowV1alpha1OSSArtifact.md) |  | [optional] 
**path** | **str** | Path is the container path to the artifact | [optional] 
**raw** | [**IoArgoprojWorkflowV1alpha1RawArtifact**](IoArgoprojWorkflowV1alpha1RawArtifact.md) |  | [optional] 
**recurseMode** | **bool** | If mode is set, apply the permission recursively into the artifact if it is a folder | [optional] 
**s3** | [**IoArgoprojWorkflowV1alpha1S3Artifact**](IoArgoprojWorkflowV1alpha1S3Artifact.md) |  | [optional] 
**subPath** | **str** | SubPath allows an artifact to be sourced from a subpath within the specified source | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

