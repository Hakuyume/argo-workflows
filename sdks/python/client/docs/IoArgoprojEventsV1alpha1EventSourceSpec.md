# IoArgoprojEventsV1alpha1EventSourceSpec

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amqp** | **{str: (IoArgoprojEventsV1alpha1AMQPEventSource,)}** |  | [optional] 
**azureEventsHub** | **{str: (IoArgoprojEventsV1alpha1AzureEventsHubEventSource,)}** |  | [optional] 
**bitbucket** | **{str: (IoArgoprojEventsV1alpha1BitbucketEventSource,)}** |  | [optional] 
**bitbucketserver** | **{str: (IoArgoprojEventsV1alpha1BitbucketServerEventSource,)}** |  | [optional] 
**calendar** | **{str: (IoArgoprojEventsV1alpha1CalendarEventSource,)}** |  | [optional] 
**emitter** | **{str: (IoArgoprojEventsV1alpha1EmitterEventSource,)}** |  | [optional] 
**eventBusName** | **str** |  | [optional] 
**file** | **{str: (IoArgoprojEventsV1alpha1FileEventSource,)}** |  | [optional] 
**generic** | **{str: (IoArgoprojEventsV1alpha1GenericEventSource,)}** |  | [optional] 
**github** | **{str: (IoArgoprojEventsV1alpha1GithubEventSource,)}** |  | [optional] 
**gitlab** | **{str: (IoArgoprojEventsV1alpha1GitlabEventSource,)}** |  | [optional] 
**hdfs** | **{str: (IoArgoprojEventsV1alpha1HDFSEventSource,)}** |  | [optional] 
**kafka** | **{str: (IoArgoprojEventsV1alpha1KafkaEventSource,)}** |  | [optional] 
**minio** | **{str: (IoArgoprojEventsV1alpha1S3Artifact,)}** |  | [optional] 
**mqtt** | **{str: (IoArgoprojEventsV1alpha1MQTTEventSource,)}** |  | [optional] 
**nats** | **{str: (IoArgoprojEventsV1alpha1NATSEventsSource,)}** |  | [optional] 
**nsq** | **{str: (IoArgoprojEventsV1alpha1NSQEventSource,)}** |  | [optional] 
**pubSub** | **{str: (IoArgoprojEventsV1alpha1PubSubEventSource,)}** |  | [optional] 
**pulsar** | **{str: (IoArgoprojEventsV1alpha1PulsarEventSource,)}** |  | [optional] 
**redis** | **{str: (IoArgoprojEventsV1alpha1RedisEventSource,)}** |  | [optional] 
**replicas** | **int** |  | [optional] 
**resource** | **{str: (IoArgoprojEventsV1alpha1ResourceEventSource,)}** |  | [optional] 
**service** | [**IoArgoprojEventsV1alpha1Service**](IoArgoprojEventsV1alpha1Service.md) |  | [optional] 
**slack** | **{str: (IoArgoprojEventsV1alpha1SlackEventSource,)}** |  | [optional] 
**sns** | **{str: (IoArgoprojEventsV1alpha1SNSEventSource,)}** |  | [optional] 
**sqs** | **{str: (IoArgoprojEventsV1alpha1SQSEventSource,)}** |  | [optional] 
**storageGrid** | **{str: (IoArgoprojEventsV1alpha1StorageGridEventSource,)}** |  | [optional] 
**stripe** | **{str: (IoArgoprojEventsV1alpha1StripeEventSource,)}** |  | [optional] 
**template** | [**IoArgoprojEventsV1alpha1Template**](IoArgoprojEventsV1alpha1Template.md) |  | [optional] 
**webhook** | **{str: (IoArgoprojEventsV1alpha1WebhookContext,)}** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

