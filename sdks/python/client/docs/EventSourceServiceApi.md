# argo_workflows.EventSourceServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_source**](EventSourceServiceApi.md#create_event_source) | **POST** /api/v1/event-sources/{namespace} | 
[**delete_event_source**](EventSourceServiceApi.md#delete_event_source) | **DELETE** /api/v1/event-sources/{namespace}/{name} | 
[**event_sources_logs**](EventSourceServiceApi.md#event_sources_logs) | **GET** /api/v1/stream/event-sources/{namespace}/logs | 
[**get_event_source**](EventSourceServiceApi.md#get_event_source) | **GET** /api/v1/event-sources/{namespace}/{name} | 
[**list_event_sources**](EventSourceServiceApi.md#list_event_sources) | **GET** /api/v1/event-sources/{namespace} | 
[**update_event_source**](EventSourceServiceApi.md#update_event_source) | **PUT** /api/v1/event-sources/{namespace}/{name} | 
[**watch_event_sources**](EventSourceServiceApi.md#watch_event_sources) | **GET** /api/v1/stream/event-sources/{namespace} | 

# **create_event_source**
> IoArgoprojEventsV1alpha1EventSource create_event_source(namespacebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_event_source import IoArgoprojEventsV1alpha1EventSource
from argo_workflows.model.eventsource_create_event_source_request import EventsourceCreateEventSourceRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    body = EventsourceCreateEventSourceRequest(
        event_source=IoArgoprojEventsV1alpha1EventSource(
            metadata=ObjectMeta(
                annotations=dict(
                    "key": "key_example",
                ),
                cluster_name="cluster_name_example",
                creation_timestamp="1970-01-01T00:00:00.00Z",
                deletion_grace_period_seconds=1,
                deletion_timestamp="1970-01-01T00:00:00.00Z",
                finalizers=[
                    "finalizers_example"
                ],
                generate_name="generate_name_example",
                generation=1,
                labels=dict(
                    "key": "key_example",
                ),
                managed_fields=[
                    ManagedFieldsEntry(
                        api_version="api_version_example",
                        fields_type="fields_type_example",
                        fields_v1=dict(),
                        manager="manager_example",
                        operation="operation_example",
                        subresource="subresource_example",
                        time="1970-01-01T00:00:00.00Z",
                    )
                ],
                name="name_example",
                namespace="namespace_example",
                owner_references=[
                    OwnerReference(
                        api_version="api_version_example",
                        block_owner_deletion=True,
                        controller=True,
                        kind="kind_example",
                        name="name_example",
                        uid="uid_example",
                    )
                ],
                resource_version="resource_version_example",
                self_link="self_link_example",
                uid="uid_example",
            ),
            spec=IoArgoprojEventsV1alpha1EventSourceSpec(
                amqp=dict(
                    "key": IoArgoprojEventsV1alpha1AMQPEventSource(
                        auth=IoArgoprojEventsV1alpha1BasicAuth(
                            password=SecretKeySelector(
                                key="key_example",
                                name="name_example",
                                optional=True,
                            ),
                            username=SecretKeySelector(),
                        ),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(
                            duration=IoArgoprojEventsV1alpha1Int64OrString(
                                int64_val="int64_val_example",
                                str_val="str_val_example",
                                type="type_example",
                            ),
                            factor=IoArgoprojEventsV1alpha1Amount(
                                value='YQ==',
                            ),
                            jitter=IoArgoprojEventsV1alpha1Amount(),
                            steps=1,
                        ),
                        consume=IoArgoprojEventsV1alpha1AMQPConsumeConfig(
                            auto_ack=True,
                            consumer_tag="consumer_tag_example",
                            exclusive=True,
                            no_local=True,
                            no_wait=True,
                        ),
                        exchange_declare=IoArgoprojEventsV1alpha1AMQPExchangeDeclareConfig(
                            auto_delete=True,
                            durable=True,
                            internal=True,
                            no_wait=True,
                        ),
                        exchange_name="exchange_name_example",
                        exchange_type="exchange_type_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(
                            expression="expression_example",
                        ),
                        json_body=True,
                        metadata=dict(
                            "key": "key_example",
                        ),
                        queue_bind=IoArgoprojEventsV1alpha1AMQPQueueBindConfig(
                            no_wait=True,
                        ),
                        queue_declare=IoArgoprojEventsV1alpha1AMQPQueueDeclareConfig(
                            arguments="arguments_example",
                            auto_delete=True,
                            durable=True,
                            exclusive=True,
                            name="name_example",
                            no_wait=True,
                        ),
                        routing_key="routing_key_example",
                        tls=IoArgoprojEventsV1alpha1TLSConfig(
                            ca_cert_secret=SecretKeySelector(),
                            client_cert_secret=SecretKeySelector(),
                            client_key_secret=SecretKeySelector(),
                            insecure_skip_verify=True,
                        ),
                        url="url_example",
                        url_secret=SecretKeySelector(),
                    ),
                ),
                azure_events_hub=dict(
                    "key": IoArgoprojEventsV1alpha1AzureEventsHubEventSource(
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        fqdn="fqdn_example",
                        hub_name="hub_name_example",
                        metadata=dict(),
                        shared_access_key=SecretKeySelector(),
                        shared_access_key_name=SecretKeySelector(),
                    ),
                ),
                bitbucket=dict(
                    "key": IoArgoprojEventsV1alpha1BitbucketEventSource(
                        auth=IoArgoprojEventsV1alpha1BitbucketAuth(
                            basic=IoArgoprojEventsV1alpha1BitbucketBasicAuth(
                                password=SecretKeySelector(),
                                username=SecretKeySelector(),
                            ),
                            token=SecretKeySelector(),
                        ),
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(
                            "key": "key_example",
                        ),
                        owner="owner_example",
                        project_key="project_key_example",
                        repository_slug="repository_slug_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(
                            auth_secret=SecretKeySelector(),
                            endpoint="endpoint_example",
                            metadata=dict(),
                            method="method_example",
                            port="port_example",
                            server_cert_secret=SecretKeySelector(),
                            server_key_secret=SecretKeySelector(),
                            url="url_example",
                        ),
                    ),
                ),
                bitbucketserver=dict(
                    "key": IoArgoprojEventsV1alpha1BitbucketServerEventSource(
                        access_token=SecretKeySelector(),
                        bitbucketserver_base_url="bitbucketserver_base_url_example",
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        project_key="project_key_example",
                        repositories=[
                            IoArgoprojEventsV1alpha1BitbucketServerRepository(
                                project_key="project_key_example",
                                repository_slug="repository_slug_example",
                            )
                        ],
                        repository_slug="repository_slug_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                        webhook_secret=SecretKeySelector(),
                    ),
                ),
                calendar=dict(
                    "key": IoArgoprojEventsV1alpha1CalendarEventSource(
                        exclusion_dates=[
                            "exclusion_dates_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        interval="interval_example",
                        metadata=dict(),
                        persistence=IoArgoprojEventsV1alpha1EventPersistence(
                            catchup=IoArgoprojEventsV1alpha1CatchupConfiguration(
                                enabled=True,
                                max_duration="max_duration_example",
                            ),
                            config_map=IoArgoprojEventsV1alpha1ConfigMapPersistence(
                                create_if_not_exist=True,
                                name="name_example",
                            ),
                        ),
                        schedule="schedule_example",
                        timezone="timezone_example",
                    ),
                ),
                emitter=dict(
                    "key": IoArgoprojEventsV1alpha1EmitterEventSource(
                        broker="broker_example",
                        channel_key="channel_key_example",
                        channel_name="channel_name_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        password=SecretKeySelector(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        username=SecretKeySelector(),
                    ),
                ),
                event_bus_name="event_bus_name_example",
                file=dict(
                    "key": IoArgoprojEventsV1alpha1FileEventSource(
                        event_type="event_type_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        polling=True,
                        watch_path_config=IoArgoprojEventsV1alpha1WatchPathConfig(
                            directory="directory_example",
                            path="path_example",
                            path_regexp="path_regexp_example",
                        ),
                    ),
                ),
                generic=dict(
                    "key": IoArgoprojEventsV1alpha1GenericEventSource(
                        auth_secret=SecretKeySelector(),
                        config="config_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        insecure=True,
                        json_body=True,
                        metadata=dict(),
                        url="url_example",
                    ),
                ),
                github=dict(
                    "key": IoArgoprojEventsV1alpha1GithubEventSource(
                        active=True,
                        api_token=SecretKeySelector(),
                        content_type="content_type_example",
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        github_app=IoArgoprojEventsV1alpha1GithubAppCreds(
                            app_id="app_id_example",
                            installation_id="installation_id_example",
                            private_key=SecretKeySelector(),
                        ),
                        github_base_url="github_base_url_example",
                        github_upload_url="github_upload_url_example",
                        id="id_example",
                        insecure=True,
                        metadata=dict(),
                        organizations=[
                            "organizations_example"
                        ],
                        owner="owner_example",
                        repositories=[
                            IoArgoprojEventsV1alpha1OwnedRepositories(
                                names=[
                                    "names_example"
                                ],
                                owner="owner_example",
                            )
                        ],
                        repository="repository_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                        webhook_secret=SecretKeySelector(),
                    ),
                ),
                gitlab=dict(
                    "key": IoArgoprojEventsV1alpha1GitlabEventSource(
                        access_token=SecretKeySelector(),
                        delete_hook_on_finish=True,
                        enable_ssl_verification=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        gitlab_base_url="gitlab_base_url_example",
                        metadata=dict(),
                        project_id="project_id_example",
                        projects=[
                            "projects_example"
                        ],
                        secret_token=SecretKeySelector(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                hdfs=dict(
                    "key": IoArgoprojEventsV1alpha1HDFSEventSource(
                        addresses=[
                            "addresses_example"
                        ],
                        check_interval="check_interval_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        hdfs_user="hdfs_user_example",
                        krb_c_cache_secret=SecretKeySelector(),
                        krb_config_config_map=ConfigMapKeySelector(
                            key="key_example",
                            name="name_example",
                            optional=True,
                        ),
                        krb_keytab_secret=SecretKeySelector(),
                        krb_realm="krb_realm_example",
                        krb_service_principal_name="krb_service_principal_name_example",
                        krb_username="krb_username_example",
                        metadata=dict(),
                        type="type_example",
                        watch_path_config=IoArgoprojEventsV1alpha1WatchPathConfig(),
                    ),
                ),
                kafka=dict(
                    "key": IoArgoprojEventsV1alpha1KafkaEventSource(
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        consumer_group=IoArgoprojEventsV1alpha1KafkaConsumerGroup(
                            group_name="group_name_example",
                            oldest=True,
                            rebalance_strategy="rebalance_strategy_example",
                        ),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        limit_events_per_second="limit_events_per_second_example",
                        metadata=dict(),
                        partition="partition_example",
                        sasl=IoArgoprojEventsV1alpha1SASLConfig(
                            mechanism="mechanism_example",
                            password=SecretKeySelector(),
                            user=SecretKeySelector(),
                        ),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                        url="url_example",
                        version="version_example",
                    ),
                ),
                minio=dict(
                    "key": IoArgoprojEventsV1alpha1S3Artifact(
                        access_key=SecretKeySelector(),
                        bucket=IoArgoprojEventsV1alpha1S3Bucket(
                            key="key_example",
                            name="name_example",
                        ),
                        endpoint="endpoint_example",
                        events=[],
                        filter=IoArgoprojEventsV1alpha1S3Filter(
                            prefix="prefix_example",
                            suffix="suffix_example",
                        ),
                        insecure=True,
                        metadata=dict(
                            "key": "key_example",
                        ),
                        region="region_example",
                        secret_key=SecretKeySelector(),
                    ),
                ),
                mqtt=dict(
                    "key": IoArgoprojEventsV1alpha1MQTTEventSource(
                        client_id="client_id_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                        url="url_example",
                    ),
                ),
                nats=dict(
                    "key": IoArgoprojEventsV1alpha1NATSEventsSource(
                        auth=IoArgoprojEventsV1alpha1NATSAuth(
                            basic=IoArgoprojEventsV1alpha1BasicAuth(),
                            credential=SecretKeySelector(),
                            nkey=SecretKeySelector(),
                            token=SecretKeySelector(),
                        ),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        subject="subject_example",
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        url="url_example",
                    ),
                ),
                nsq=dict(
                    "key": IoArgoprojEventsV1alpha1NSQEventSource(
                        channel="channel_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        host_address="host_address_example",
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                    ),
                ),
                pub_sub=dict(
                    "key": IoArgoprojEventsV1alpha1PubSubEventSource(
                        credential_secret=SecretKeySelector(),
                        delete_subscription_on_finish=True,
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        project_id="project_id_example",
                        subscription_id="subscription_id_example",
                        topic="topic_example",
                        topic_project_id="topic_project_id_example",
                    ),
                ),
                pulsar=dict(
                    "key": IoArgoprojEventsV1alpha1PulsarEventSource(
                        auth_token_secret=SecretKeySelector(),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        tls_allow_insecure_connection=True,
                        tls_trust_certs_secret=SecretKeySelector(),
                        tls_validate_hostname=True,
                        topics=[
                            "topics_example"
                        ],
                        type="type_example",
                        url="url_example",
                    ),
                ),
                redis=dict(
                    "key": IoArgoprojEventsV1alpha1RedisEventSource(
                        channels=[],
                        db=1,
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        host_address="host_address_example",
                        metadata=dict(),
                        namespace="namespace_example",
                        password=SecretKeySelector(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                    ),
                ),
                replicas=1,
                resource=dict(
                    "key": IoArgoprojEventsV1alpha1ResourceEventSource(
                        event_types=[
                            "event_types_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1ResourceFilter(
                            after_start=True,
                            created_by="1970-01-01T00:00:00.00Z",
                            fields=[
                                IoArgoprojEventsV1alpha1Selector(
                                    key="key_example",
                                    operation="operation_example",
                                    value="value_example",
                                )
                            ],
                            labels=[
                                IoArgoprojEventsV1alpha1Selector()
                            ],
                            prefix="prefix_example",
                        ),
                        group_version_resource=GroupVersionResource(
                            group="group_example",
                            resource="resource_example",
                            version="version_example",
                        ),
                        metadata=dict(),
                        namespace="namespace_example",
                    ),
                ),
                service=IoArgoprojEventsV1alpha1Service(
                    cluster_ip="cluster_ip_example",
                    ports=[
                        ServicePort(
                            app_protocol="app_protocol_example",
                            name="name_example",
                            node_port=1,
                            port=1,
                            protocol="SCTP",
                            target_port="target_port_example",
                        )
                    ],
                ),
                slack=dict(
                    "key": IoArgoprojEventsV1alpha1SlackEventSource(
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        signing_secret=SecretKeySelector(),
                        token=SecretKeySelector(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                sns=dict(
                    "key": IoArgoprojEventsV1alpha1SNSEventSource(
                        access_key=SecretKeySelector(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        region="region_example",
                        role_arn="role_arn_example",
                        secret_key=SecretKeySelector(),
                        topic_arn="topic_arn_example",
                        validate_signature=True,
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                sqs=dict(
                    "key": IoArgoprojEventsV1alpha1SQSEventSource(
                        access_key=SecretKeySelector(),
                        dlq=True,
                        endpoint="endpoint_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        queue="queue_example",
                        queue_account_id="queue_account_id_example",
                        region="region_example",
                        role_arn="role_arn_example",
                        secret_key=SecretKeySelector(),
                        wait_time_seconds="wait_time_seconds_example",
                    ),
                ),
                storage_grid=dict(
                    "key": IoArgoprojEventsV1alpha1StorageGridEventSource(
                        api_url="api_url_example",
                        auth_token=SecretKeySelector(),
                        bucket="bucket_example",
                        events=[],
                        filter=IoArgoprojEventsV1alpha1StorageGridFilter(
                            prefix="prefix_example",
                            suffix="suffix_example",
                        ),
                        metadata=dict(),
                        region="region_example",
                        topic_arn="topic_arn_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                stripe=dict(
                    "key": IoArgoprojEventsV1alpha1StripeEventSource(
                        api_key=SecretKeySelector(),
                        create_webhook=True,
                        event_filter=[
                            "event_filter_example"
                        ],
                        metadata=dict(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                template=IoArgoprojEventsV1alpha1Template(
                    affinity=Affinity(
                        node_affinity=NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                PreferredSchedulingTerm(
                                    preference=NodeSelectorTerm(
                                        match_expressions=[
                                            NodeSelectorRequirement(
                                                key="key_example",
                                                operator="DoesNotExist",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=NodeSelector(
                                node_selector_terms=[
                                    NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                WeightedPodAffinityTerm(
                                    pod_affinity_term=PodAffinityTerm(
                                        label_selector=LabelSelector(
                                            match_expressions=[
                                                LabelSelectorRequirement(
                                                    key="key_example",
                                                    operator="operator_example",
                                                    values=[
                                                        "values_example"
                                                    ],
                                                )
                                            ],
                                            match_labels=dict(
                                                "key": "key_example",
                                            ),
                                        ),
                                        namespace_selector=LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                PodAffinityTerm()
                            ],
                        ),
                    ),
                    container=Container(
                        args=[
                            "args_example"
                        ],
                        command=[
                            "command_example"
                        ],
                        env=[
                            EnvVar(
                                name="name_example",
                                value="value_example",
                                value_from=EnvVarSource(
                                    config_map_key_ref=ConfigMapKeySelector(),
                                    field_ref=ObjectFieldSelector(
                                        api_version="api_version_example",
                                        field_path="field_path_example",
                                    ),
                                    resource_field_ref=ResourceFieldSelector(
                                        container_name="container_name_example",
                                        divisor="divisor_example",
                                        resource="resource_example",
                                    ),
                                    secret_key_ref=SecretKeySelector(),
                                ),
                            )
                        ],
                        env_from=[
                            EnvFromSource(
                                config_map_ref=ConfigMapEnvSource(
                                    name="name_example",
                                    optional=True,
                                ),
                                prefix="prefix_example",
                                secret_ref=SecretEnvSource(
                                    name="name_example",
                                    optional=True,
                                ),
                            )
                        ],
                        image="image_example",
                        image_pull_policy="Always",
                        lifecycle=Lifecycle(
                            post_start=LifecycleHandler(
                                _exec=ExecAction(
                                    command=[
                                        "command_example"
                                    ],
                                ),
                                http_get=HTTPGetAction(
                                    host="host_example",
                                    http_headers=[
                                        HTTPHeader(
                                            name="name_example",
                                            value="value_example",
                                        )
                                    ],
                                    path="path_example",
                                    port="port_example",
                                    scheme="HTTP",
                                ),
                                tcp_socket=TCPSocketAction(
                                    host="host_example",
                                    port="port_example",
                                ),
                            ),
                            pre_stop=LifecycleHandler(),
                        ),
                        liveness_probe=Probe(
                            _exec=ExecAction(),
                            failure_threshold=1,
                            grpc=GRPCAction(
                                port=1,
                                service="service_example",
                            ),
                            http_get=HTTPGetAction(),
                            initial_delay_seconds=1,
                            period_seconds=1,
                            success_threshold=1,
                            tcp_socket=TCPSocketAction(),
                            termination_grace_period_seconds=1,
                            timeout_seconds=1,
                        ),
                        name="name_example",
                        ports=[
                            ContainerPort(
                                container_port=1,
                                host_ip="host_ip_example",
                                host_port=1,
                                name="name_example",
                                protocol="SCTP",
                            )
                        ],
                        readiness_probe=Probe(),
                        resources=ResourceRequirements(
                            limits=dict(
                                "key": "key_example",
                            ),
                            requests=dict(
                                "key": "key_example",
                            ),
                        ),
                        security_context=SecurityContext(
                            allow_privilege_escalation=True,
                            capabilities=Capabilities(
                                add=[
                                    "add_example"
                                ],
                                drop=[
                                    "drop_example"
                                ],
                            ),
                            privileged=True,
                            proc_mount="proc_mount_example",
                            read_only_root_filesystem=True,
                            run_as_group=1,
                            run_as_non_root=True,
                            run_as_user=1,
                            se_linux_options=SELinuxOptions(
                                level="level_example",
                                role="role_example",
                                type="type_example",
                                user="user_example",
                            ),
                            seccomp_profile=SeccompProfile(
                                localhost_profile="localhost_profile_example",
                                type="Localhost",
                            ),
                            windows_options=WindowsSecurityContextOptions(
                                gmsa_credential_spec="gmsa_credential_spec_example",
                                gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                host_process=True,
                                run_as_user_name="run_as_user_name_example",
                            ),
                        ),
                        startup_probe=Probe(),
                        stdin=True,
                        stdin_once=True,
                        termination_message_path="termination_message_path_example",
                        termination_message_policy="FallbackToLogsOnError",
                        tty=True,
                        volume_devices=[
                            VolumeDevice(
                                device_path="device_path_example",
                                name="name_example",
                            )
                        ],
                        volume_mounts=[
                            VolumeMount(
                                mount_path="mount_path_example",
                                mount_propagation="mount_propagation_example",
                                name="name_example",
                                read_only=True,
                                sub_path="sub_path_example",
                                sub_path_expr="sub_path_expr_example",
                            )
                        ],
                        working_dir="working_dir_example",
                    ),
                    image_pull_secrets=[
                        LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    metadata=IoArgoprojEventsV1alpha1Metadata(
                        annotations=dict(),
                        labels=dict(),
                    ),
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    security_context=PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=SELinuxOptions(),
                        seccomp_profile=SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=WindowsSecurityContextOptions(),
                    ),
                    service_account_name="service_account_name_example",
                    tolerations=[
                        Toleration(
                            effect="NoExecute",
                            key="key_example",
                            operator="Equal",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    volumes=[
                        Volume(
                            aws_elastic_block_store=AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    DownwardAPIVolumeFile(
                                        field_ref=ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=EphemeralVolumeSource(
                                volume_claim_template=PersistentVolumeClaimTemplate(
                                    metadata=ObjectMeta(),
                                    spec=PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
                                        data_source_ref=TypedLocalObjectReference(),
                                        resources=ResourceRequirements(),
                                        selector=LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                            ),
                            flocker=FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    VolumeProjection(
                                        config_map=ConfigMapProjection(
                                            items=[],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=DownwardAPIProjection(
                                            items=[
                                                DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=SecretProjection(
                                            items=[
                                                KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=SecretVolumeSource(
                                default_mode=1,
                                items=[],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
                webhook=dict(
                    "key": IoArgoprojEventsV1alpha1WebhookContext(),
                ),
            ),
            status=IoArgoprojEventsV1alpha1EventSourceStatus(
                status=IoArgoprojEventsV1alpha1Status(
                    conditions=[
                        IoArgoprojEventsV1alpha1Condition(
                            last_transition_time="1970-01-01T00:00:00.00Z",
                            message="message_example",
                            reason="reason_example",
                            status="status_example",
                            type="type_example",
                        )
                    ],
                ),
            ),
        ),
        namespace="namespace_example",
    )
    try:
        api_response = api_instance.create_event_source(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->create_event_source: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EventsourceCreateEventSourceRequest**](EventsourceCreateEventSourceRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_source**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_event_source(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_event_source(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->delete_event_source: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'deleteOptions.gracePeriodSeconds': "deleteOptions.gracePeriodSeconds_example",
        'deleteOptions.preconditions.uid': "deleteOptions.preconditions.uid_example",
        'deleteOptions.preconditions.resourceVersion': "deleteOptions.preconditions.resourceVersion_example",
        'deleteOptions.orphanDependents': True,
        'deleteOptions.propagationPolicy': "deleteOptions.propagationPolicy_example",
        'deleteOptions.dryRun': [
        "deleteOptions.dryRun_example"
    ],
    }
    try:
        api_response = api_instance.delete_event_source(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->delete_event_source: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deleteOptions.gracePeriodSeconds | DeleteOptionsGracePeriodSecondsSchema | | optional
deleteOptions.preconditions.uid | DeleteOptionsPreconditionsUidSchema | | optional
deleteOptions.preconditions.resourceVersion | DeleteOptionsPreconditionsResourceVersionSchema | | optional
deleteOptions.orphanDependents | DeleteOptionsOrphanDependentsSchema | | optional
deleteOptions.propagationPolicy | DeleteOptionsPropagationPolicySchema | | optional
deleteOptions.dryRun | DeleteOptionsDryRunSchema | | optional


#### DeleteOptionsGracePeriodSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsPreconditionsUidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsPreconditionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsOrphanDependentsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### DeleteOptionsPropagationPolicySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsDryRunSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_sources_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} event_sources_logs(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.eventsource_log_entry import EventsourceLogEntry
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.event_sources_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->event_sources_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'name': "name_example",
        'eventSourceType': "eventSourceType_example",
        'eventName': "eventName_example",
        'grep': "grep_example",
        'podLogOptions.container': "podLogOptions.container_example",
        'podLogOptions.follow': True,
        'podLogOptions.previous': True,
        'podLogOptions.sinceSeconds': "podLogOptions.sinceSeconds_example",
        'podLogOptions.sinceTime.seconds': "podLogOptions.sinceTime.seconds_example",
        'podLogOptions.sinceTime.nanos': 1,
        'podLogOptions.timestamps': True,
        'podLogOptions.tailLines': "podLogOptions.tailLines_example",
        'podLogOptions.limitBytes': "podLogOptions.limitBytes_example",
        'podLogOptions.insecureSkipTLSVerifyBackend': True,
    }
    try:
        api_response = api_instance.event_sources_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->event_sources_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
eventSourceType | EventSourceTypeSchema | | optional
eventName | EventNameSchema | | optional
grep | GrepSchema | | optional
podLogOptions.container | PodLogOptionsContainerSchema | | optional
podLogOptions.follow | PodLogOptionsFollowSchema | | optional
podLogOptions.previous | PodLogOptionsPreviousSchema | | optional
podLogOptions.sinceSeconds | PodLogOptionsSinceSecondsSchema | | optional
podLogOptions.sinceTime.seconds | PodLogOptionsSinceTimeSecondsSchema | | optional
podLogOptions.sinceTime.nanos | PodLogOptionsSinceTimeNanosSchema | | optional
podLogOptions.timestamps | PodLogOptionsTimestampsSchema | | optional
podLogOptions.tailLines | PodLogOptionsTailLinesSchema | | optional
podLogOptions.limitBytes | PodLogOptionsLimitBytesSchema | | optional
podLogOptions.insecureSkipTLSVerifyBackend | PodLogOptionsInsecureSkipTLSVerifyBackendSchema | | optional


#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EventSourceTypeSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EventNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### GrepSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsContainerSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsFollowSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsPreviousSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsSinceSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsSinceTimeSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsSinceTimeNanosSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### PodLogOptionsTimestampsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsTailLinesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsLimitBytesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsInsecureSkipTLSVerifyBackendSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.(streaming responses)
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**EventsourceLogEntry**](EventsourceLogEntry.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_source**
> IoArgoprojEventsV1alpha1EventSource get_event_source(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_event_source import IoArgoprojEventsV1alpha1EventSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    try:
        api_response = api_instance.get_event_source(
            path_params=path_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->get_event_source: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_sources**
> IoArgoprojEventsV1alpha1EventSourceList list_event_sources(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_event_source_list import IoArgoprojEventsV1alpha1EventSourceList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_event_sources(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->list_event_sources: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'listOptions.labelSelector': "listOptions.labelSelector_example",
        'listOptions.fieldSelector': "listOptions.fieldSelector_example",
        'listOptions.watch': True,
        'listOptions.allowWatchBookmarks': True,
        'listOptions.resourceVersion': "listOptions.resourceVersion_example",
        'listOptions.resourceVersionMatch': "listOptions.resourceVersionMatch_example",
        'listOptions.timeoutSeconds': "listOptions.timeoutSeconds_example",
        'listOptions.limit': "listOptions.limit_example",
        'listOptions.continue': "listOptions.continue_example",
    }
    try:
        api_response = api_instance.list_event_sources(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->list_event_sources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
listOptions.labelSelector | ListOptionsLabelSelectorSchema | | optional
listOptions.fieldSelector | ListOptionsFieldSelectorSchema | | optional
listOptions.watch | ListOptionsWatchSchema | | optional
listOptions.allowWatchBookmarks | ListOptionsAllowWatchBookmarksSchema | | optional
listOptions.resourceVersion | ListOptionsResourceVersionSchema | | optional
listOptions.resourceVersionMatch | ListOptionsResourceVersionMatchSchema | | optional
listOptions.timeoutSeconds | ListOptionsTimeoutSecondsSchema | | optional
listOptions.limit | ListOptionsLimitSchema | | optional
listOptions.continue | ListOptionsContinueSchema | | optional


#### ListOptionsLabelSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsFieldSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsWatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsAllowWatchBookmarksSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsResourceVersionMatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsTimeoutSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsContinueSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IoArgoprojEventsV1alpha1EventSourceList**](IoArgoprojEventsV1alpha1EventSourceList.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**IoArgoprojEventsV1alpha1EventSourceList**](IoArgoprojEventsV1alpha1EventSourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_source**
> IoArgoprojEventsV1alpha1EventSource update_event_source(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_event_source import IoArgoprojEventsV1alpha1EventSource
from argo_workflows.model.eventsource_update_event_source_request import EventsourceUpdateEventSourceRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = EventsourceUpdateEventSourceRequest(
        event_source=IoArgoprojEventsV1alpha1EventSource(
            metadata=ObjectMeta(
                annotations=dict(
                    "key": "key_example",
                ),
                cluster_name="cluster_name_example",
                creation_timestamp="1970-01-01T00:00:00.00Z",
                deletion_grace_period_seconds=1,
                deletion_timestamp="1970-01-01T00:00:00.00Z",
                finalizers=[
                    "finalizers_example"
                ],
                generate_name="generate_name_example",
                generation=1,
                labels=dict(
                    "key": "key_example",
                ),
                managed_fields=[
                    ManagedFieldsEntry(
                        api_version="api_version_example",
                        fields_type="fields_type_example",
                        fields_v1=dict(),
                        manager="manager_example",
                        operation="operation_example",
                        subresource="subresource_example",
                        time="1970-01-01T00:00:00.00Z",
                    )
                ],
                name="name_example",
                namespace="namespace_example",
                owner_references=[
                    OwnerReference(
                        api_version="api_version_example",
                        block_owner_deletion=True,
                        controller=True,
                        kind="kind_example",
                        name="name_example",
                        uid="uid_example",
                    )
                ],
                resource_version="resource_version_example",
                self_link="self_link_example",
                uid="uid_example",
            ),
            spec=IoArgoprojEventsV1alpha1EventSourceSpec(
                amqp=dict(
                    "key": IoArgoprojEventsV1alpha1AMQPEventSource(
                        auth=IoArgoprojEventsV1alpha1BasicAuth(
                            password=SecretKeySelector(
                                key="key_example",
                                name="name_example",
                                optional=True,
                            ),
                            username=SecretKeySelector(),
                        ),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(
                            duration=IoArgoprojEventsV1alpha1Int64OrString(
                                int64_val="int64_val_example",
                                str_val="str_val_example",
                                type="type_example",
                            ),
                            factor=IoArgoprojEventsV1alpha1Amount(
                                value='YQ==',
                            ),
                            jitter=IoArgoprojEventsV1alpha1Amount(),
                            steps=1,
                        ),
                        consume=IoArgoprojEventsV1alpha1AMQPConsumeConfig(
                            auto_ack=True,
                            consumer_tag="consumer_tag_example",
                            exclusive=True,
                            no_local=True,
                            no_wait=True,
                        ),
                        exchange_declare=IoArgoprojEventsV1alpha1AMQPExchangeDeclareConfig(
                            auto_delete=True,
                            durable=True,
                            internal=True,
                            no_wait=True,
                        ),
                        exchange_name="exchange_name_example",
                        exchange_type="exchange_type_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(
                            expression="expression_example",
                        ),
                        json_body=True,
                        metadata=dict(
                            "key": "key_example",
                        ),
                        queue_bind=IoArgoprojEventsV1alpha1AMQPQueueBindConfig(
                            no_wait=True,
                        ),
                        queue_declare=IoArgoprojEventsV1alpha1AMQPQueueDeclareConfig(
                            arguments="arguments_example",
                            auto_delete=True,
                            durable=True,
                            exclusive=True,
                            name="name_example",
                            no_wait=True,
                        ),
                        routing_key="routing_key_example",
                        tls=IoArgoprojEventsV1alpha1TLSConfig(
                            ca_cert_secret=SecretKeySelector(),
                            client_cert_secret=SecretKeySelector(),
                            client_key_secret=SecretKeySelector(),
                            insecure_skip_verify=True,
                        ),
                        url="url_example",
                        url_secret=SecretKeySelector(),
                    ),
                ),
                azure_events_hub=dict(
                    "key": IoArgoprojEventsV1alpha1AzureEventsHubEventSource(
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        fqdn="fqdn_example",
                        hub_name="hub_name_example",
                        metadata=dict(),
                        shared_access_key=SecretKeySelector(),
                        shared_access_key_name=SecretKeySelector(),
                    ),
                ),
                bitbucket=dict(
                    "key": IoArgoprojEventsV1alpha1BitbucketEventSource(
                        auth=IoArgoprojEventsV1alpha1BitbucketAuth(
                            basic=IoArgoprojEventsV1alpha1BitbucketBasicAuth(
                                password=SecretKeySelector(),
                                username=SecretKeySelector(),
                            ),
                            token=SecretKeySelector(),
                        ),
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(
                            "key": "key_example",
                        ),
                        owner="owner_example",
                        project_key="project_key_example",
                        repository_slug="repository_slug_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(
                            auth_secret=SecretKeySelector(),
                            endpoint="endpoint_example",
                            metadata=dict(),
                            method="method_example",
                            port="port_example",
                            server_cert_secret=SecretKeySelector(),
                            server_key_secret=SecretKeySelector(),
                            url="url_example",
                        ),
                    ),
                ),
                bitbucketserver=dict(
                    "key": IoArgoprojEventsV1alpha1BitbucketServerEventSource(
                        access_token=SecretKeySelector(),
                        bitbucketserver_base_url="bitbucketserver_base_url_example",
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        project_key="project_key_example",
                        repositories=[
                            IoArgoprojEventsV1alpha1BitbucketServerRepository(
                                project_key="project_key_example",
                                repository_slug="repository_slug_example",
                            )
                        ],
                        repository_slug="repository_slug_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                        webhook_secret=SecretKeySelector(),
                    ),
                ),
                calendar=dict(
                    "key": IoArgoprojEventsV1alpha1CalendarEventSource(
                        exclusion_dates=[
                            "exclusion_dates_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        interval="interval_example",
                        metadata=dict(),
                        persistence=IoArgoprojEventsV1alpha1EventPersistence(
                            catchup=IoArgoprojEventsV1alpha1CatchupConfiguration(
                                enabled=True,
                                max_duration="max_duration_example",
                            ),
                            config_map=IoArgoprojEventsV1alpha1ConfigMapPersistence(
                                create_if_not_exist=True,
                                name="name_example",
                            ),
                        ),
                        schedule="schedule_example",
                        timezone="timezone_example",
                    ),
                ),
                emitter=dict(
                    "key": IoArgoprojEventsV1alpha1EmitterEventSource(
                        broker="broker_example",
                        channel_key="channel_key_example",
                        channel_name="channel_name_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        password=SecretKeySelector(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        username=SecretKeySelector(),
                    ),
                ),
                event_bus_name="event_bus_name_example",
                file=dict(
                    "key": IoArgoprojEventsV1alpha1FileEventSource(
                        event_type="event_type_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        polling=True,
                        watch_path_config=IoArgoprojEventsV1alpha1WatchPathConfig(
                            directory="directory_example",
                            path="path_example",
                            path_regexp="path_regexp_example",
                        ),
                    ),
                ),
                generic=dict(
                    "key": IoArgoprojEventsV1alpha1GenericEventSource(
                        auth_secret=SecretKeySelector(),
                        config="config_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        insecure=True,
                        json_body=True,
                        metadata=dict(),
                        url="url_example",
                    ),
                ),
                github=dict(
                    "key": IoArgoprojEventsV1alpha1GithubEventSource(
                        active=True,
                        api_token=SecretKeySelector(),
                        content_type="content_type_example",
                        delete_hook_on_finish=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        github_app=IoArgoprojEventsV1alpha1GithubAppCreds(
                            app_id="app_id_example",
                            installation_id="installation_id_example",
                            private_key=SecretKeySelector(),
                        ),
                        github_base_url="github_base_url_example",
                        github_upload_url="github_upload_url_example",
                        id="id_example",
                        insecure=True,
                        metadata=dict(),
                        organizations=[
                            "organizations_example"
                        ],
                        owner="owner_example",
                        repositories=[
                            IoArgoprojEventsV1alpha1OwnedRepositories(
                                names=[
                                    "names_example"
                                ],
                                owner="owner_example",
                            )
                        ],
                        repository="repository_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                        webhook_secret=SecretKeySelector(),
                    ),
                ),
                gitlab=dict(
                    "key": IoArgoprojEventsV1alpha1GitlabEventSource(
                        access_token=SecretKeySelector(),
                        delete_hook_on_finish=True,
                        enable_ssl_verification=True,
                        events=[
                            "events_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        gitlab_base_url="gitlab_base_url_example",
                        metadata=dict(),
                        project_id="project_id_example",
                        projects=[
                            "projects_example"
                        ],
                        secret_token=SecretKeySelector(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                hdfs=dict(
                    "key": IoArgoprojEventsV1alpha1HDFSEventSource(
                        addresses=[
                            "addresses_example"
                        ],
                        check_interval="check_interval_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        hdfs_user="hdfs_user_example",
                        krb_c_cache_secret=SecretKeySelector(),
                        krb_config_config_map=ConfigMapKeySelector(
                            key="key_example",
                            name="name_example",
                            optional=True,
                        ),
                        krb_keytab_secret=SecretKeySelector(),
                        krb_realm="krb_realm_example",
                        krb_service_principal_name="krb_service_principal_name_example",
                        krb_username="krb_username_example",
                        metadata=dict(),
                        type="type_example",
                        watch_path_config=IoArgoprojEventsV1alpha1WatchPathConfig(),
                    ),
                ),
                kafka=dict(
                    "key": IoArgoprojEventsV1alpha1KafkaEventSource(
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        consumer_group=IoArgoprojEventsV1alpha1KafkaConsumerGroup(
                            group_name="group_name_example",
                            oldest=True,
                            rebalance_strategy="rebalance_strategy_example",
                        ),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        limit_events_per_second="limit_events_per_second_example",
                        metadata=dict(),
                        partition="partition_example",
                        sasl=IoArgoprojEventsV1alpha1SASLConfig(
                            mechanism="mechanism_example",
                            password=SecretKeySelector(),
                            user=SecretKeySelector(),
                        ),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                        url="url_example",
                        version="version_example",
                    ),
                ),
                minio=dict(
                    "key": IoArgoprojEventsV1alpha1S3Artifact(
                        access_key=SecretKeySelector(),
                        bucket=IoArgoprojEventsV1alpha1S3Bucket(
                            key="key_example",
                            name="name_example",
                        ),
                        endpoint="endpoint_example",
                        events=[],
                        filter=IoArgoprojEventsV1alpha1S3Filter(
                            prefix="prefix_example",
                            suffix="suffix_example",
                        ),
                        insecure=True,
                        metadata=dict(
                            "key": "key_example",
                        ),
                        region="region_example",
                        secret_key=SecretKeySelector(),
                    ),
                ),
                mqtt=dict(
                    "key": IoArgoprojEventsV1alpha1MQTTEventSource(
                        client_id="client_id_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                        url="url_example",
                    ),
                ),
                nats=dict(
                    "key": IoArgoprojEventsV1alpha1NATSEventsSource(
                        auth=IoArgoprojEventsV1alpha1NATSAuth(
                            basic=IoArgoprojEventsV1alpha1BasicAuth(),
                            credential=SecretKeySelector(),
                            nkey=SecretKeySelector(),
                            token=SecretKeySelector(),
                        ),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        subject="subject_example",
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        url="url_example",
                    ),
                ),
                nsq=dict(
                    "key": IoArgoprojEventsV1alpha1NSQEventSource(
                        channel="channel_example",
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        host_address="host_address_example",
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        topic="topic_example",
                    ),
                ),
                pub_sub=dict(
                    "key": IoArgoprojEventsV1alpha1PubSubEventSource(
                        credential_secret=SecretKeySelector(),
                        delete_subscription_on_finish=True,
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        project_id="project_id_example",
                        subscription_id="subscription_id_example",
                        topic="topic_example",
                        topic_project_id="topic_project_id_example",
                    ),
                ),
                pulsar=dict(
                    "key": IoArgoprojEventsV1alpha1PulsarEventSource(
                        auth_token_secret=SecretKeySelector(),
                        connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                        tls_allow_insecure_connection=True,
                        tls_trust_certs_secret=SecretKeySelector(),
                        tls_validate_hostname=True,
                        topics=[
                            "topics_example"
                        ],
                        type="type_example",
                        url="url_example",
                    ),
                ),
                redis=dict(
                    "key": IoArgoprojEventsV1alpha1RedisEventSource(
                        channels=[],
                        db=1,
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        host_address="host_address_example",
                        metadata=dict(),
                        namespace="namespace_example",
                        password=SecretKeySelector(),
                        tls=IoArgoprojEventsV1alpha1TLSConfig(),
                    ),
                ),
                replicas=1,
                resource=dict(
                    "key": IoArgoprojEventsV1alpha1ResourceEventSource(
                        event_types=[
                            "event_types_example"
                        ],
                        filter=IoArgoprojEventsV1alpha1ResourceFilter(
                            after_start=True,
                            created_by="1970-01-01T00:00:00.00Z",
                            fields=[
                                IoArgoprojEventsV1alpha1Selector(
                                    key="key_example",
                                    operation="operation_example",
                                    value="value_example",
                                )
                            ],
                            labels=[
                                IoArgoprojEventsV1alpha1Selector()
                            ],
                            prefix="prefix_example",
                        ),
                        group_version_resource=GroupVersionResource(
                            group="group_example",
                            resource="resource_example",
                            version="version_example",
                        ),
                        metadata=dict(),
                        namespace="namespace_example",
                    ),
                ),
                service=IoArgoprojEventsV1alpha1Service(
                    cluster_ip="cluster_ip_example",
                    ports=[
                        ServicePort(
                            app_protocol="app_protocol_example",
                            name="name_example",
                            node_port=1,
                            port=1,
                            protocol="SCTP",
                            target_port="target_port_example",
                        )
                    ],
                ),
                slack=dict(
                    "key": IoArgoprojEventsV1alpha1SlackEventSource(
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        signing_secret=SecretKeySelector(),
                        token=SecretKeySelector(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                sns=dict(
                    "key": IoArgoprojEventsV1alpha1SNSEventSource(
                        access_key=SecretKeySelector(),
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        metadata=dict(),
                        region="region_example",
                        role_arn="role_arn_example",
                        secret_key=SecretKeySelector(),
                        topic_arn="topic_arn_example",
                        validate_signature=True,
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                sqs=dict(
                    "key": IoArgoprojEventsV1alpha1SQSEventSource(
                        access_key=SecretKeySelector(),
                        dlq=True,
                        endpoint="endpoint_example",
                        filter=IoArgoprojEventsV1alpha1EventSourceFilter(),
                        json_body=True,
                        metadata=dict(),
                        queue="queue_example",
                        queue_account_id="queue_account_id_example",
                        region="region_example",
                        role_arn="role_arn_example",
                        secret_key=SecretKeySelector(),
                        wait_time_seconds="wait_time_seconds_example",
                    ),
                ),
                storage_grid=dict(
                    "key": IoArgoprojEventsV1alpha1StorageGridEventSource(
                        api_url="api_url_example",
                        auth_token=SecretKeySelector(),
                        bucket="bucket_example",
                        events=[],
                        filter=IoArgoprojEventsV1alpha1StorageGridFilter(
                            prefix="prefix_example",
                            suffix="suffix_example",
                        ),
                        metadata=dict(),
                        region="region_example",
                        topic_arn="topic_arn_example",
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                stripe=dict(
                    "key": IoArgoprojEventsV1alpha1StripeEventSource(
                        api_key=SecretKeySelector(),
                        create_webhook=True,
                        event_filter=[
                            "event_filter_example"
                        ],
                        metadata=dict(),
                        webhook=IoArgoprojEventsV1alpha1WebhookContext(),
                    ),
                ),
                template=IoArgoprojEventsV1alpha1Template(
                    affinity=Affinity(
                        node_affinity=NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                PreferredSchedulingTerm(
                                    preference=NodeSelectorTerm(
                                        match_expressions=[
                                            NodeSelectorRequirement(
                                                key="key_example",
                                                operator="DoesNotExist",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=NodeSelector(
                                node_selector_terms=[
                                    NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                WeightedPodAffinityTerm(
                                    pod_affinity_term=PodAffinityTerm(
                                        label_selector=LabelSelector(
                                            match_expressions=[
                                                LabelSelectorRequirement(
                                                    key="key_example",
                                                    operator="operator_example",
                                                    values=[
                                                        "values_example"
                                                    ],
                                                )
                                            ],
                                            match_labels=dict(
                                                "key": "key_example",
                                            ),
                                        ),
                                        namespace_selector=LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                PodAffinityTerm()
                            ],
                        ),
                    ),
                    container=Container(
                        args=[
                            "args_example"
                        ],
                        command=[
                            "command_example"
                        ],
                        env=[
                            EnvVar(
                                name="name_example",
                                value="value_example",
                                value_from=EnvVarSource(
                                    config_map_key_ref=ConfigMapKeySelector(),
                                    field_ref=ObjectFieldSelector(
                                        api_version="api_version_example",
                                        field_path="field_path_example",
                                    ),
                                    resource_field_ref=ResourceFieldSelector(
                                        container_name="container_name_example",
                                        divisor="divisor_example",
                                        resource="resource_example",
                                    ),
                                    secret_key_ref=SecretKeySelector(),
                                ),
                            )
                        ],
                        env_from=[
                            EnvFromSource(
                                config_map_ref=ConfigMapEnvSource(
                                    name="name_example",
                                    optional=True,
                                ),
                                prefix="prefix_example",
                                secret_ref=SecretEnvSource(
                                    name="name_example",
                                    optional=True,
                                ),
                            )
                        ],
                        image="image_example",
                        image_pull_policy="Always",
                        lifecycle=Lifecycle(
                            post_start=LifecycleHandler(
                                _exec=ExecAction(
                                    command=[
                                        "command_example"
                                    ],
                                ),
                                http_get=HTTPGetAction(
                                    host="host_example",
                                    http_headers=[
                                        HTTPHeader(
                                            name="name_example",
                                            value="value_example",
                                        )
                                    ],
                                    path="path_example",
                                    port="port_example",
                                    scheme="HTTP",
                                ),
                                tcp_socket=TCPSocketAction(
                                    host="host_example",
                                    port="port_example",
                                ),
                            ),
                            pre_stop=LifecycleHandler(),
                        ),
                        liveness_probe=Probe(
                            _exec=ExecAction(),
                            failure_threshold=1,
                            grpc=GRPCAction(
                                port=1,
                                service="service_example",
                            ),
                            http_get=HTTPGetAction(),
                            initial_delay_seconds=1,
                            period_seconds=1,
                            success_threshold=1,
                            tcp_socket=TCPSocketAction(),
                            termination_grace_period_seconds=1,
                            timeout_seconds=1,
                        ),
                        name="name_example",
                        ports=[
                            ContainerPort(
                                container_port=1,
                                host_ip="host_ip_example",
                                host_port=1,
                                name="name_example",
                                protocol="SCTP",
                            )
                        ],
                        readiness_probe=Probe(),
                        resources=ResourceRequirements(
                            limits=dict(
                                "key": "key_example",
                            ),
                            requests=dict(
                                "key": "key_example",
                            ),
                        ),
                        security_context=SecurityContext(
                            allow_privilege_escalation=True,
                            capabilities=Capabilities(
                                add=[
                                    "add_example"
                                ],
                                drop=[
                                    "drop_example"
                                ],
                            ),
                            privileged=True,
                            proc_mount="proc_mount_example",
                            read_only_root_filesystem=True,
                            run_as_group=1,
                            run_as_non_root=True,
                            run_as_user=1,
                            se_linux_options=SELinuxOptions(
                                level="level_example",
                                role="role_example",
                                type="type_example",
                                user="user_example",
                            ),
                            seccomp_profile=SeccompProfile(
                                localhost_profile="localhost_profile_example",
                                type="Localhost",
                            ),
                            windows_options=WindowsSecurityContextOptions(
                                gmsa_credential_spec="gmsa_credential_spec_example",
                                gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                host_process=True,
                                run_as_user_name="run_as_user_name_example",
                            ),
                        ),
                        startup_probe=Probe(),
                        stdin=True,
                        stdin_once=True,
                        termination_message_path="termination_message_path_example",
                        termination_message_policy="FallbackToLogsOnError",
                        tty=True,
                        volume_devices=[
                            VolumeDevice(
                                device_path="device_path_example",
                                name="name_example",
                            )
                        ],
                        volume_mounts=[
                            VolumeMount(
                                mount_path="mount_path_example",
                                mount_propagation="mount_propagation_example",
                                name="name_example",
                                read_only=True,
                                sub_path="sub_path_example",
                                sub_path_expr="sub_path_expr_example",
                            )
                        ],
                        working_dir="working_dir_example",
                    ),
                    image_pull_secrets=[
                        LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    metadata=IoArgoprojEventsV1alpha1Metadata(
                        annotations=dict(),
                        labels=dict(),
                    ),
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    security_context=PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=SELinuxOptions(),
                        seccomp_profile=SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=WindowsSecurityContextOptions(),
                    ),
                    service_account_name="service_account_name_example",
                    tolerations=[
                        Toleration(
                            effect="NoExecute",
                            key="key_example",
                            operator="Equal",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    volumes=[
                        Volume(
                            aws_elastic_block_store=AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    DownwardAPIVolumeFile(
                                        field_ref=ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=EphemeralVolumeSource(
                                volume_claim_template=PersistentVolumeClaimTemplate(
                                    metadata=ObjectMeta(),
                                    spec=PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
                                        data_source_ref=TypedLocalObjectReference(),
                                        resources=ResourceRequirements(),
                                        selector=LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                            ),
                            flocker=FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    VolumeProjection(
                                        config_map=ConfigMapProjection(
                                            items=[],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=DownwardAPIProjection(
                                            items=[
                                                DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=SecretProjection(
                                            items=[
                                                KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=SecretVolumeSource(
                                default_mode=1,
                                items=[],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
                webhook=dict(
                    "key": IoArgoprojEventsV1alpha1WebhookContext(),
                ),
            ),
            status=IoArgoprojEventsV1alpha1EventSourceStatus(
                status=IoArgoprojEventsV1alpha1Status(
                    conditions=[
                        IoArgoprojEventsV1alpha1Condition(
                            last_transition_time="1970-01-01T00:00:00.00Z",
                            message="message_example",
                            reason="reason_example",
                            status="status_example",
                            type="type_example",
                        )
                    ],
                ),
            ),
        ),
        name="name_example",
        namespace="namespace_example",
    )
    try:
        api_response = api_instance.update_event_source(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->update_event_source: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EventsourceUpdateEventSourceRequest**](EventsourceUpdateEventSourceRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**IoArgoprojEventsV1alpha1EventSource**](IoArgoprojEventsV1alpha1EventSource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_event_sources**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_event_sources(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_source_service_api
from argo_workflows.model.eventsource_event_source_watch_event import EventsourceEventSourceWatchEvent
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = event_source_service_api.EventSourceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_event_sources(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->watch_event_sources: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'listOptions.labelSelector': "listOptions.labelSelector_example",
        'listOptions.fieldSelector': "listOptions.fieldSelector_example",
        'listOptions.watch': True,
        'listOptions.allowWatchBookmarks': True,
        'listOptions.resourceVersion': "listOptions.resourceVersion_example",
        'listOptions.resourceVersionMatch': "listOptions.resourceVersionMatch_example",
        'listOptions.timeoutSeconds': "listOptions.timeoutSeconds_example",
        'listOptions.limit': "listOptions.limit_example",
        'listOptions.continue': "listOptions.continue_example",
    }
    try:
        api_response = api_instance.watch_event_sources(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventSourceServiceApi->watch_event_sources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
listOptions.labelSelector | ListOptionsLabelSelectorSchema | | optional
listOptions.fieldSelector | ListOptionsFieldSelectorSchema | | optional
listOptions.watch | ListOptionsWatchSchema | | optional
listOptions.allowWatchBookmarks | ListOptionsAllowWatchBookmarksSchema | | optional
listOptions.resourceVersion | ListOptionsResourceVersionSchema | | optional
listOptions.resourceVersionMatch | ListOptionsResourceVersionMatchSchema | | optional
listOptions.timeoutSeconds | ListOptionsTimeoutSecondsSchema | | optional
listOptions.limit | ListOptionsLimitSchema | | optional
listOptions.continue | ListOptionsContinueSchema | | optional


#### ListOptionsLabelSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsFieldSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsWatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsAllowWatchBookmarksSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsResourceVersionMatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsTimeoutSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsContinueSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.(streaming responses)
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**EventsourceEventSourceWatchEvent**](EventsourceEventSourceWatchEvent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

