# argo_workflows.WorkflowServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowServiceApi.md#create_workflow) | **POST** /api/v1/workflows/{namespace} | 
[**delete_workflow**](WorkflowServiceApi.md#delete_workflow) | **DELETE** /api/v1/workflows/{namespace}/{name} | 
[**get_workflow**](WorkflowServiceApi.md#get_workflow) | **GET** /api/v1/workflows/{namespace}/{name} | 
[**lint_workflow**](WorkflowServiceApi.md#lint_workflow) | **POST** /api/v1/workflows/{namespace}/lint | 
[**list_workflows**](WorkflowServiceApi.md#list_workflows) | **GET** /api/v1/workflows/{namespace} | 
[**pod_logs**](WorkflowServiceApi.md#pod_logs) | **GET** /api/v1/workflows/{namespace}/{name}/{podName}/log | DEPRECATED: Cannot work via HTTP if podName is an empty string. Use WorkflowLogs.
[**resubmit_workflow**](WorkflowServiceApi.md#resubmit_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/resubmit | 
[**resume_workflow**](WorkflowServiceApi.md#resume_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/resume | 
[**retry_workflow**](WorkflowServiceApi.md#retry_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/retry | 
[**set_workflow**](WorkflowServiceApi.md#set_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/set | 
[**stop_workflow**](WorkflowServiceApi.md#stop_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/stop | 
[**submit_workflow**](WorkflowServiceApi.md#submit_workflow) | **POST** /api/v1/workflows/{namespace}/submit | 
[**suspend_workflow**](WorkflowServiceApi.md#suspend_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/suspend | 
[**terminate_workflow**](WorkflowServiceApi.md#terminate_workflow) | **PUT** /api/v1/workflows/{namespace}/{name}/terminate | 
[**watch_events**](WorkflowServiceApi.md#watch_events) | **GET** /api/v1/stream/events/{namespace} | 
[**watch_workflows**](WorkflowServiceApi.md#watch_workflows) | **GET** /api/v1/workflow-events/{namespace} | 
[**workflow_logs**](WorkflowServiceApi.md#workflow_logs) | **GET** /api/v1/workflows/{namespace}/{name}/log | 

# **create_workflow**
> IoArgoprojWorkflowV1alpha1Workflow create_workflow(namespacebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_create_request import IoArgoprojWorkflowV1alpha1WorkflowCreateRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowCreateRequest(
        create_options=CreateOptions(
            dry_run=[
                "dry_run_example"
            ],
            field_manager="field_manager_example",
            field_validation="field_validation_example",
        ),
        instance_id="instance_id_example",
        namespace="namespace_example",
        server_dry_run=True,
        workflow=IoArgoprojWorkflowV1alpha1Workflow(
            api_version="api_version_example",
            kind="kind_example",
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
            spec=IoArgoprojWorkflowV1alpha1WorkflowSpec(
                active_deadline_seconds=1,
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
                archive_logs=True,
                arguments=IoArgoprojWorkflowV1alpha1Arguments(
                    artifacts=[
                        IoArgoprojWorkflowV1alpha1Artifact(
                            archive=IoArgoprojWorkflowV1alpha1ArchiveStrategy(
                                _none=dict(),
                                tar=IoArgoprojWorkflowV1alpha1TarStrategy(
                                    compression_level=1,
                                ),
                                zip=dict(),
                            ),
                            archive_logs=True,
                            artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(
                                strategy="strategy_example",
                            ),
                            artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(
                                password_secret=SecretKeySelector(
                                    key="key_example",
                                    name="name_example",
                                    optional=True,
                                ),
                                url="url_example",
                                username_secret=SecretKeySelector(),
                            ),
                            deleted=True,
                            _from="_from_example",
                            from_expression="from_expression_example",
                            gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(
                                bucket="bucket_example",
                                key="key_example",
                                service_account_key_secret=SecretKeySelector(),
                            ),
                            git=IoArgoprojWorkflowV1alpha1GitArtifact(
                                branch="branch_example",
                                depth=1,
                                disable_submodules=True,
                                fetch=[
                                    "fetch_example"
                                ],
                                insecure_ignore_host_key=True,
                                password_secret=SecretKeySelector(),
                                repo="repo_example",
                                revision="revision_example",
                                single_branch=True,
                                ssh_private_key_secret=SecretKeySelector(),
                                username_secret=SecretKeySelector(),
                            ),
                            global_name="global_name_example",
                            hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(
                                addresses=[
                                    "addresses_example"
                                ],
                                force=True,
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
                                path="path_example",
                            ),
                            http=IoArgoprojWorkflowV1alpha1HTTPArtifact(
                                auth=IoArgoprojWorkflowV1alpha1HTTPAuth(
                                    basic_auth=IoArgoprojWorkflowV1alpha1BasicAuth(
                                        password_secret=SecretKeySelector(),
                                        username_secret=SecretKeySelector(),
                                    ),
                                    client_cert=IoArgoprojWorkflowV1alpha1ClientCertAuth(
                                        client_cert_secret=SecretKeySelector(),
                                        client_key_secret=SecretKeySelector(),
                                    ),
                                    oauth2=IoArgoprojWorkflowV1alpha1OAuth2Auth(
                                        client_id_secret=SecretKeySelector(),
                                        client_secret_secret=SecretKeySelector(),
                                        endpoint_params=[
                                            IoArgoprojWorkflowV1alpha1OAuth2EndpointParam(
                                                key="key_example",
                                                value="value_example",
                                            )
                                        ],
                                        scopes=[
                                            "scopes_example"
                                        ],
                                        token_url_secret=SecretKeySelector(),
                                    ),
                                ),
                                headers=[
                                    IoArgoprojWorkflowV1alpha1Header(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                url="url_example",
                            ),
                            mode=1,
                            name="name_example",
                            optional=True,
                            oss=IoArgoprojWorkflowV1alpha1OSSArtifact(
                                access_key_secret=SecretKeySelector(),
                                bucket="bucket_example",
                                create_bucket_if_not_present=True,
                                endpoint="endpoint_example",
                                key="key_example",
                                lifecycle_rule=IoArgoprojWorkflowV1alpha1OSSLifecycleRule(
                                    mark_deletion_after_days=1,
                                    mark_infrequent_access_after_days=1,
                                ),
                                secret_key_secret=SecretKeySelector(),
                                security_token="security_token_example",
                            ),
                            path="path_example",
                            raw=IoArgoprojWorkflowV1alpha1RawArtifact(
                                data="data_example",
                            ),
                            recurse_mode=True,
                            s3=IoArgoprojWorkflowV1alpha1S3Artifact(
                                access_key_secret=SecretKeySelector(),
                                bucket="bucket_example",
                                create_bucket_if_not_present=IoArgoprojWorkflowV1alpha1CreateS3BucketOptions(
                                    object_locking=True,
                                ),
                                encryption_options=IoArgoprojWorkflowV1alpha1S3EncryptionOptions(
                                    enable_encryption=True,
                                    kms_encryption_context="kms_encryption_context_example",
                                    kms_key_id="kms_key_id_example",
                                    server_side_customer_key_secret=SecretKeySelector(),
                                ),
                                endpoint="endpoint_example",
                                insecure=True,
                                key="key_example",
                                region="region_example",
                                role_arn="role_arn_example",
                                secret_key_secret=SecretKeySelector(),
                                use_sdk_creds=True,
                            ),
                            sub_path="sub_path_example",
                        )
                    ],
                    parameters=[
                        IoArgoprojWorkflowV1alpha1Parameter(
                            default="default_example",
                            description="description_example",
                            enum=[
                                "enum_example"
                            ],
                            global_name="global_name_example",
                            name="name_example",
                            value="value_example",
                            value_from=IoArgoprojWorkflowV1alpha1ValueFrom(
                                config_map_key_ref=ConfigMapKeySelector(),
                                default="default_example",
                                event="event_example",
                                expression="expression_example",
                                jq_filter="jq_filter_example",
                                json_path="json_path_example",
                                parameter="parameter_example",
                                path="path_example",
                                supplied=dict(),
                            ),
                        )
                    ],
                ),
                artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(),
                artifact_repository_ref=IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef(
                    config_map="config_map_example",
                    key="key_example",
                ),
                automount_service_account_token=True,
                dns_config=PodDNSConfig(
                    nameservers=[
                        "nameservers_example"
                    ],
                    options=[
                        PodDNSConfigOption(
                            name="name_example",
                            value="value_example",
                        )
                    ],
                    searches=[
                        "searches_example"
                    ],
                ),
                dns_policy="dns_policy_example",
                entrypoint="entrypoint_example",
                executor=IoArgoprojWorkflowV1alpha1ExecutorConfig(
                    service_account_name="service_account_name_example",
                ),
                hooks=dict(
                    "key": IoArgoprojWorkflowV1alpha1LifecycleHook(
                        arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                        expression="expression_example",
                        template="template_example",
                        template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(
                            cluster_scope=True,
                            name="name_example",
                            template="template_example",
                        ),
                    ),
                ),
                host_aliases=[
                    HostAlias(
                        hostnames=[
                            "hostnames_example"
                        ],
                        ip="ip_example",
                    )
                ],
                host_network=True,
                image_pull_secrets=[
                    LocalObjectReference(
                        name="name_example",
                    )
                ],
                metrics=IoArgoprojWorkflowV1alpha1Metrics(
                    prometheus=[
                        IoArgoprojWorkflowV1alpha1Prometheus(
                            counter=IoArgoprojWorkflowV1alpha1Counter(
                                value="value_example",
                            ),
                            gauge=IoArgoprojWorkflowV1alpha1Gauge(
                                realtime=True,
                                value="value_example",
                            ),
                            help="help_example",
                            histogram=IoArgoprojWorkflowV1alpha1Histogram(
                                buckets=[
                                    3.14
                                ],
                                value="value_example",
                            ),
                            labels=[
                                IoArgoprojWorkflowV1alpha1MetricLabel(
                                    key="key_example",
                                    value="value_example",
                                )
                            ],
                            name="name_example",
                            when="when_example",
                        )
                    ],
                ),
                node_selector=dict(
                    "key": "key_example",
                ),
                on_exit="on_exit_example",
                parallelism=1,
                pod_disruption_budget=IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec(
                    max_unavailable="max_unavailable_example",
                    min_available="min_available_example",
                    selector=LabelSelector(),
                ),
                pod_gc=IoArgoprojWorkflowV1alpha1PodGC(
                    label_selector=LabelSelector(),
                    strategy="strategy_example",
                ),
                pod_metadata=IoArgoprojWorkflowV1alpha1Metadata(
                    annotations=dict(
                        "key": "key_example",
                    ),
                    labels=dict(),
                ),
                pod_priority=1,
                pod_priority_class_name="pod_priority_class_name_example",
                pod_spec_patch="pod_spec_patch_example",
                priority=1,
                retry_strategy=IoArgoprojWorkflowV1alpha1RetryStrategy(
                    affinity=IoArgoprojWorkflowV1alpha1RetryAffinity(
                        node_anti_affinity=dict(),
                    ),
                    backoff=IoArgoprojWorkflowV1alpha1Backoff(
                        duration="duration_example",
                        factor="factor_example",
                        max_duration="max_duration_example",
                    ),
                    expression="expression_example",
                    limit="limit_example",
                    retry_policy="retry_policy_example",
                ),
                scheduler_name="scheduler_name_example",
                security_context=PodSecurityContext(
                    fs_group=1,
                    fs_group_change_policy="fs_group_change_policy_example",
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
                    supplemental_groups=[
                        1
                    ],
                    sysctls=[
                        Sysctl(
                            name="name_example",
                            value="value_example",
                        )
                    ],
                    windows_options=WindowsSecurityContextOptions(
                        gmsa_credential_spec="gmsa_credential_spec_example",
                        gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                        host_process=True,
                        run_as_user_name="run_as_user_name_example",
                    ),
                ),
                service_account_name="service_account_name_example",
                shutdown="shutdown_example",
                suspend=True,
                synchronization=IoArgoprojWorkflowV1alpha1Synchronization(
                    mutex=IoArgoprojWorkflowV1alpha1Mutex(
                        name="name_example",
                    ),
                    semaphore=IoArgoprojWorkflowV1alpha1SemaphoreRef(
                        config_map_key_ref=ConfigMapKeySelector(),
                    ),
                ),
                template_defaults=IoArgoprojWorkflowV1alpha1Template(
                    active_deadline_seconds="active_deadline_seconds_example",
                    affinity=Affinity(),
                    archive_location=IoArgoprojWorkflowV1alpha1ArtifactLocation(
                        archive_logs=True,
                        artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(),
                        gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(),
                        git=IoArgoprojWorkflowV1alpha1GitArtifact(),
                        hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(),
                        http=IoArgoprojWorkflowV1alpha1HTTPArtifact(),
                        oss=IoArgoprojWorkflowV1alpha1OSSArtifact(),
                        raw=IoArgoprojWorkflowV1alpha1RawArtifact(),
                        s3=IoArgoprojWorkflowV1alpha1S3Artifact(),
                    ),
                    automount_service_account_token=True,
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
                            se_linux_options=SELinuxOptions(),
                            seccomp_profile=SeccompProfile(),
                            windows_options=WindowsSecurityContextOptions(),
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
                    container_set=IoArgoprojWorkflowV1alpha1ContainerSetTemplate(
                        containers=[
                            IoArgoprojWorkflowV1alpha1ContainerNode(
                                args=[],
                                command=[],
                                dependencies=[],
                                env=[],
                                env_from=[],
                                image="image_example",
                                image_pull_policy="image_pull_policy_example",
                                lifecycle=Lifecycle(),
                                liveness_probe=Probe(),
                                name="name_example",
                                ports=[],
                                readiness_probe=Probe(),
                                resources=ResourceRequirements(),
                                security_context=SecurityContext(),
                                startup_probe=Probe(),
                                stdin=True,
                                stdin_once=True,
                                termination_message_path="termination_message_path_example",
                                termination_message_policy="termination_message_policy_example",
                                tty=True,
                                volume_devices=[],
                                volume_mounts=[],
                                working_dir="working_dir_example",
                            )
                        ],
                        retry_strategy=IoArgoprojWorkflowV1alpha1ContainerSetRetryStrategy(
                            duration="duration_example",
                            retries="retries_example",
                        ),
                        volume_mounts=[
                            VolumeMount()
                        ],
                    ),
                    daemon=True,
                    dag=IoArgoprojWorkflowV1alpha1DAGTemplate(
                        fail_fast=True,
                        target="target_example",
                        tasks=[
                            IoArgoprojWorkflowV1alpha1DAGTask(
                                arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                                continue_on=IoArgoprojWorkflowV1alpha1ContinueOn(
                                    error=True,
                                    failed=True,
                                ),
                                dependencies=[
                                    "dependencies_example"
                                ],
                                depends="depends_example",
                                hooks=dict(
                                    "key": IoArgoprojWorkflowV1alpha1LifecycleHook(),
                                ),
                                inline=IoArgoprojWorkflowV1alpha1Template(),
                                name="name_example",
                                on_exit="on_exit_example",
                                template="template_example",
                                template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                                when="when_example",
                                with_items=[
                                    dict()
                                ],
                                with_param="with_param_example",
                                with_sequence=IoArgoprojWorkflowV1alpha1Sequence(
                                    count="count_example",
                                    end="end_example",
                                    format="format_example",
                                    start="start_example",
                                ),
                            )
                        ],
                    ),
                    data=IoArgoprojWorkflowV1alpha1Data(
                        source=IoArgoprojWorkflowV1alpha1DataSource(
                            artifact_paths=IoArgoprojWorkflowV1alpha1ArtifactPaths(
                                archive=IoArgoprojWorkflowV1alpha1ArchiveStrategy(),
                                archive_logs=True,
                                artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(),
                                artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(),
                                deleted=True,
                                _from="_from_example",
                                from_expression="from_expression_example",
                                gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(),
                                git=IoArgoprojWorkflowV1alpha1GitArtifact(),
                                global_name="global_name_example",
                                hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(),
                                http=IoArgoprojWorkflowV1alpha1HTTPArtifact(),
                                mode=1,
                                name="name_example",
                                optional=True,
                                oss=IoArgoprojWorkflowV1alpha1OSSArtifact(),
                                path="path_example",
                                raw=IoArgoprojWorkflowV1alpha1RawArtifact(),
                                recurse_mode=True,
                                s3=IoArgoprojWorkflowV1alpha1S3Artifact(),
                                sub_path="sub_path_example",
                            ),
                        ),
                        transformation=[
                            IoArgoprojWorkflowV1alpha1TransformationStep(
                                expression="expression_example",
                            )
                        ],
                    ),
                    executor=IoArgoprojWorkflowV1alpha1ExecutorConfig(),
                    fail_fast=True,
                    host_aliases=[
                        HostAlias()
                    ],
                    http=IoArgoprojWorkflowV1alpha1HTTP(
                        body="body_example",
                        headers=[
                            IoArgoprojWorkflowV1alpha1HTTPHeader(
                                name="name_example",
                                value="value_example",
                                value_from=IoArgoprojWorkflowV1alpha1HTTPHeaderSource(
                                    secret_key_ref=SecretKeySelector(),
                                ),
                            )
                        ],
                        insecure_skip_verify=True,
                        method="method_example",
                        success_condition="success_condition_example",
                        timeout_seconds=1,
                        url="url_example",
                    ),
                    init_containers=[
                        IoArgoprojWorkflowV1alpha1UserContainer(
                            args=[],
                            command=[],
                            env=[],
                            env_from=[],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=Lifecycle(),
                            liveness_probe=Probe(),
                            mirror_volume_mounts=True,
                            name="name_example",
                            ports=[],
                            readiness_probe=Probe(),
                            resources=ResourceRequirements(),
                            security_context=SecurityContext(),
                            startup_probe=Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[],
                            volume_mounts=[],
                            working_dir="working_dir_example",
                        )
                    ],
                    inputs=IoArgoprojWorkflowV1alpha1Inputs(
                        artifacts=[
                            IoArgoprojWorkflowV1alpha1Artifact()
                        ],
                        parameters=[
                            IoArgoprojWorkflowV1alpha1Parameter()
                        ],
                    ),
                    memoize=IoArgoprojWorkflowV1alpha1Memoize(
                        cache=IoArgoprojWorkflowV1alpha1Cache(
                            config_map=ConfigMapKeySelector(),
                        ),
                        key="key_example",
                        max_age="max_age_example",
                    ),
                    metadata=IoArgoprojWorkflowV1alpha1Metadata(),
                    metrics=IoArgoprojWorkflowV1alpha1Metrics(),
                    name="name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    outputs=IoArgoprojWorkflowV1alpha1Outputs(
                        artifacts=[
                            IoArgoprojWorkflowV1alpha1Artifact()
                        ],
                        exit_code="exit_code_example",
                        parameters=[
                            IoArgoprojWorkflowV1alpha1Parameter()
                        ],
                        result="result_example",
                    ),
                    parallelism=1,
                    plugin=dict(),
                    pod_spec_patch="pod_spec_patch_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    resource=IoArgoprojWorkflowV1alpha1ResourceTemplate(
                        action="action_example",
                        failure_condition="failure_condition_example",
                        flags=[
                            "flags_example"
                        ],
                        manifest="manifest_example",
                        manifest_from=IoArgoprojWorkflowV1alpha1ManifestFrom(
                            artifact=IoArgoprojWorkflowV1alpha1Artifact(),
                        ),
                        merge_strategy="merge_strategy_example",
                        set_owner_reference=True,
                        success_condition="success_condition_example",
                    ),
                    retry_strategy=IoArgoprojWorkflowV1alpha1RetryStrategy(),
                    scheduler_name="scheduler_name_example",
                    script=IoArgoprojWorkflowV1alpha1ScriptTemplate(
                        args=[],
                        command=[],
                        env=[],
                        env_from=[],
                        image="image_example",
                        image_pull_policy="image_pull_policy_example",
                        lifecycle=Lifecycle(),
                        liveness_probe=Probe(),
                        name="name_example",
                        ports=[],
                        readiness_probe=Probe(),
                        resources=ResourceRequirements(),
                        security_context=SecurityContext(),
                        source="source_example",
                        startup_probe=Probe(),
                        stdin=True,
                        stdin_once=True,
                        termination_message_path="termination_message_path_example",
                        termination_message_policy="termination_message_policy_example",
                        tty=True,
                        volume_devices=[],
                        volume_mounts=[],
                        working_dir="working_dir_example",
                    ),
                    security_context=PodSecurityContext(),
                    service_account_name="service_account_name_example",
                    sidecars=[
                        IoArgoprojWorkflowV1alpha1UserContainer()
                    ],
                    steps=[
                        IoArgoprojWorkflowV1alpha1ParallelSteps([
                            IoArgoprojWorkflowV1alpha1WorkflowStep(
                                arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                                continue_on=IoArgoprojWorkflowV1alpha1ContinueOn(),
                                hooks=dict(),
                                inline=IoArgoprojWorkflowV1alpha1Template(),
                                name="name_example",
                                on_exit="on_exit_example",
                                template="template_example",
                                template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                                when="when_example",
                                with_items=[
                                    dict()
                                ],
                                with_param="with_param_example",
                                with_sequence=IoArgoprojWorkflowV1alpha1Sequence(),
                            )
                        ])
                    ],
                    suspend=IoArgoprojWorkflowV1alpha1SuspendTemplate(
                        duration="duration_example",
                    ),
                    synchronization=IoArgoprojWorkflowV1alpha1Synchronization(),
                    timeout="timeout_example",
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
                templates=[
                    IoArgoprojWorkflowV1alpha1Template()
                ],
                tolerations=[],
                ttl_strategy=IoArgoprojWorkflowV1alpha1TTLStrategy(
                    seconds_after_completion=1,
                    seconds_after_failure=1,
                    seconds_after_success=1,
                ),
                volume_claim_gc=IoArgoprojWorkflowV1alpha1VolumeClaimGC(
                    strategy="strategy_example",
                ),
                volume_claim_templates=[
                    PersistentVolumeClaim(
                        api_version="api_version_example",
                        kind="kind_example",
                        metadata=ObjectMeta(),
                        spec=PersistentVolumeClaimSpec(),
                        status=PersistentVolumeClaimStatus(
                            access_modes=[
                                "access_modes_example"
                            ],
                            allocated_resources=dict(
                                "key": "key_example",
                            ),
                            capacity=dict(
                                "key": "key_example",
                            ),
                            conditions=[
                                PersistentVolumeClaimCondition(
                                    last_probe_time="1970-01-01T00:00:00.00Z",
                                    last_transition_time="1970-01-01T00:00:00.00Z",
                                    message="message_example",
                                    reason="reason_example",
                                    status="status_example",
                                    type="FileSystemResizePending",
                                )
                            ],
                            phase="Bound",
                            resize_status="resize_status_example",
                        ),
                    )
                ],
                volumes=[
                    Volume()
                ],
                workflow_metadata=IoArgoprojWorkflowV1alpha1WorkflowMetadata(
                    annotations=dict(),
                    labels=dict(),
                    labels_from=dict(
                        "key": IoArgoprojWorkflowV1alpha1LabelValueFrom(
                            expression="expression_example",
                        ),
                    ),
                ),
                workflow_template_ref=IoArgoprojWorkflowV1alpha1WorkflowTemplateRef(
                    cluster_scope=True,
                    name="name_example",
                ),
            ),
            status=IoArgoprojWorkflowV1alpha1WorkflowStatus(
                artifact_repository_ref=IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus(
                    artifact_repository=IoArgoprojWorkflowV1alpha1ArtifactRepository(
                        archive_logs=True,
                        artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifactRepository(
                            password_secret=SecretKeySelector(),
                            repo_url="repo_url_example",
                            username_secret=SecretKeySelector(),
                        ),
                        gcs=IoArgoprojWorkflowV1alpha1GCSArtifactRepository(
                            bucket="bucket_example",
                            key_format="key_format_example",
                            service_account_key_secret=SecretKeySelector(),
                        ),
                        hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifactRepository(
                            addresses=[],
                            force=True,
                            hdfs_user="hdfs_user_example",
                            krb_c_cache_secret=SecretKeySelector(),
                            krb_config_config_map=ConfigMapKeySelector(),
                            krb_keytab_secret=SecretKeySelector(),
                            krb_realm="krb_realm_example",
                            krb_service_principal_name="krb_service_principal_name_example",
                            krb_username="krb_username_example",
                            path_format="path_format_example",
                        ),
                        oss=IoArgoprojWorkflowV1alpha1OSSArtifactRepository(
                            access_key_secret=SecretKeySelector(),
                            bucket="bucket_example",
                            create_bucket_if_not_present=True,
                            endpoint="endpoint_example",
                            key_format="key_format_example",
                            lifecycle_rule=IoArgoprojWorkflowV1alpha1OSSLifecycleRule(),
                            secret_key_secret=SecretKeySelector(),
                            security_token="security_token_example",
                        ),
                        s3=IoArgoprojWorkflowV1alpha1S3ArtifactRepository(
                            access_key_secret=SecretKeySelector(),
                            bucket="bucket_example",
                            create_bucket_if_not_present=IoArgoprojWorkflowV1alpha1CreateS3BucketOptions(),
                            encryption_options=IoArgoprojWorkflowV1alpha1S3EncryptionOptions(),
                            endpoint="endpoint_example",
                            insecure=True,
                            key_format="key_format_example",
                            key_prefix="key_prefix_example",
                            region="region_example",
                            role_arn="role_arn_example",
                            secret_key_secret=SecretKeySelector(),
                            use_sdk_creds=True,
                        ),
                    ),
                    config_map="config_map_example",
                    default=True,
                    key="key_example",
                    namespace="namespace_example",
                ),
                compressed_nodes="compressed_nodes_example",
                conditions=[
                    IoArgoprojWorkflowV1alpha1Condition(
                        message="message_example",
                        status="status_example",
                        type="type_example",
                    )
                ],
                estimated_duration=1,
                finished_at="1970-01-01T00:00:00.00Z",
                message="message_example",
                nodes=dict(
                    "key": IoArgoprojWorkflowV1alpha1NodeStatus(
                        boundary_id="boundary_id_example",
                        children=[
                            "children_example"
                        ],
                        daemoned=True,
                        display_name="display_name_example",
                        estimated_duration=1,
                        finished_at="1970-01-01T00:00:00.00Z",
                        host_node_name="host_node_name_example",
                        id="id_example",
                        inputs=IoArgoprojWorkflowV1alpha1Inputs(),
                        memoization_status=IoArgoprojWorkflowV1alpha1MemoizationStatus(
                            cache_name="cache_name_example",
                            hit=True,
                            key="key_example",
                        ),
                        message="message_example",
                        name="name_example",
                        outbound_nodes=[
                            "outbound_nodes_example"
                        ],
                        outputs=IoArgoprojWorkflowV1alpha1Outputs(),
                        phase="phase_example",
                        pod_ip="pod_ip_example",
                        progress="progress_example",
                        resources_duration=dict(
                            "key": 1,
                        ),
                        started_at="1970-01-01T00:00:00.00Z",
                        synchronization_status=IoArgoprojWorkflowV1alpha1NodeSynchronizationStatus(
                            waiting="waiting_example",
                        ),
                        template_name="template_name_example",
                        template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                        template_scope="template_scope_example",
                        type="type_example",
                    ),
                ),
                offload_node_status_version="offload_node_status_version_example",
                outputs=IoArgoprojWorkflowV1alpha1Outputs(),
                persistent_volume_claims=[
                    Volume()
                ],
                phase="phase_example",
                progress="progress_example",
                resources_duration=dict(
                    "key": 1,
                ),
                started_at="1970-01-01T00:00:00.00Z",
                stored_templates=dict(
                    "key": IoArgoprojWorkflowV1alpha1Template(),
                ),
                stored_workflow_template_spec=IoArgoprojWorkflowV1alpha1WorkflowSpec(),
                synchronization=IoArgoprojWorkflowV1alpha1SynchronizationStatus(
                    mutex=IoArgoprojWorkflowV1alpha1MutexStatus(
                        holding=[
                            IoArgoprojWorkflowV1alpha1MutexHolding(
                                holder="holder_example",
                                mutex="mutex_example",
                            )
                        ],
                        waiting=[
                            IoArgoprojWorkflowV1alpha1MutexHolding()
                        ],
                    ),
                    semaphore=IoArgoprojWorkflowV1alpha1SemaphoreStatus(
                        holding=[
                            IoArgoprojWorkflowV1alpha1SemaphoreHolding(
                                holders=[
                                    "holders_example"
                                ],
                                semaphore="semaphore_example",
                            )
                        ],
                        waiting=[
                            IoArgoprojWorkflowV1alpha1SemaphoreHolding()
                        ],
                    ),
                ),
            ),
        ),
    )
    try:
        api_response = api_instance.create_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->create_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowCreateRequest**](IoArgoprojWorkflowV1alpha1WorkflowCreateRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_workflow(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_workflow(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->delete_workflow: %s\n" % e)

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
        api_response = api_instance.delete_workflow(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->delete_workflow: %s\n" % e)
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

# **get_workflow**
> IoArgoprojWorkflowV1alpha1Workflow get_workflow(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_workflow(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'getOptions.resourceVersion': "getOptions.resourceVersion_example",
        'fields': "fields_example",
    }
    try:
        api_response = api_instance.get_workflow(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->get_workflow: %s\n" % e)
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
getOptions.resourceVersion | GetOptionsResourceVersionSchema | | optional
fields | FieldsSchema | | optional


#### GetOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### FieldsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lint_workflow**
> IoArgoprojWorkflowV1alpha1Workflow lint_workflow(namespacebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_lint_request import IoArgoprojWorkflowV1alpha1WorkflowLintRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowLintRequest(
        namespace="namespace_example",
        workflow=IoArgoprojWorkflowV1alpha1Workflow(
            api_version="api_version_example",
            kind="kind_example",
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
            spec=IoArgoprojWorkflowV1alpha1WorkflowSpec(
                active_deadline_seconds=1,
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
                archive_logs=True,
                arguments=IoArgoprojWorkflowV1alpha1Arguments(
                    artifacts=[
                        IoArgoprojWorkflowV1alpha1Artifact(
                            archive=IoArgoprojWorkflowV1alpha1ArchiveStrategy(
                                _none=dict(),
                                tar=IoArgoprojWorkflowV1alpha1TarStrategy(
                                    compression_level=1,
                                ),
                                zip=dict(),
                            ),
                            archive_logs=True,
                            artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(
                                strategy="strategy_example",
                            ),
                            artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(
                                password_secret=SecretKeySelector(
                                    key="key_example",
                                    name="name_example",
                                    optional=True,
                                ),
                                url="url_example",
                                username_secret=SecretKeySelector(),
                            ),
                            deleted=True,
                            _from="_from_example",
                            from_expression="from_expression_example",
                            gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(
                                bucket="bucket_example",
                                key="key_example",
                                service_account_key_secret=SecretKeySelector(),
                            ),
                            git=IoArgoprojWorkflowV1alpha1GitArtifact(
                                branch="branch_example",
                                depth=1,
                                disable_submodules=True,
                                fetch=[
                                    "fetch_example"
                                ],
                                insecure_ignore_host_key=True,
                                password_secret=SecretKeySelector(),
                                repo="repo_example",
                                revision="revision_example",
                                single_branch=True,
                                ssh_private_key_secret=SecretKeySelector(),
                                username_secret=SecretKeySelector(),
                            ),
                            global_name="global_name_example",
                            hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(
                                addresses=[
                                    "addresses_example"
                                ],
                                force=True,
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
                                path="path_example",
                            ),
                            http=IoArgoprojWorkflowV1alpha1HTTPArtifact(
                                auth=IoArgoprojWorkflowV1alpha1HTTPAuth(
                                    basic_auth=IoArgoprojWorkflowV1alpha1BasicAuth(
                                        password_secret=SecretKeySelector(),
                                        username_secret=SecretKeySelector(),
                                    ),
                                    client_cert=IoArgoprojWorkflowV1alpha1ClientCertAuth(
                                        client_cert_secret=SecretKeySelector(),
                                        client_key_secret=SecretKeySelector(),
                                    ),
                                    oauth2=IoArgoprojWorkflowV1alpha1OAuth2Auth(
                                        client_id_secret=SecretKeySelector(),
                                        client_secret_secret=SecretKeySelector(),
                                        endpoint_params=[
                                            IoArgoprojWorkflowV1alpha1OAuth2EndpointParam(
                                                key="key_example",
                                                value="value_example",
                                            )
                                        ],
                                        scopes=[
                                            "scopes_example"
                                        ],
                                        token_url_secret=SecretKeySelector(),
                                    ),
                                ),
                                headers=[
                                    IoArgoprojWorkflowV1alpha1Header(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                url="url_example",
                            ),
                            mode=1,
                            name="name_example",
                            optional=True,
                            oss=IoArgoprojWorkflowV1alpha1OSSArtifact(
                                access_key_secret=SecretKeySelector(),
                                bucket="bucket_example",
                                create_bucket_if_not_present=True,
                                endpoint="endpoint_example",
                                key="key_example",
                                lifecycle_rule=IoArgoprojWorkflowV1alpha1OSSLifecycleRule(
                                    mark_deletion_after_days=1,
                                    mark_infrequent_access_after_days=1,
                                ),
                                secret_key_secret=SecretKeySelector(),
                                security_token="security_token_example",
                            ),
                            path="path_example",
                            raw=IoArgoprojWorkflowV1alpha1RawArtifact(
                                data="data_example",
                            ),
                            recurse_mode=True,
                            s3=IoArgoprojWorkflowV1alpha1S3Artifact(
                                access_key_secret=SecretKeySelector(),
                                bucket="bucket_example",
                                create_bucket_if_not_present=IoArgoprojWorkflowV1alpha1CreateS3BucketOptions(
                                    object_locking=True,
                                ),
                                encryption_options=IoArgoprojWorkflowV1alpha1S3EncryptionOptions(
                                    enable_encryption=True,
                                    kms_encryption_context="kms_encryption_context_example",
                                    kms_key_id="kms_key_id_example",
                                    server_side_customer_key_secret=SecretKeySelector(),
                                ),
                                endpoint="endpoint_example",
                                insecure=True,
                                key="key_example",
                                region="region_example",
                                role_arn="role_arn_example",
                                secret_key_secret=SecretKeySelector(),
                                use_sdk_creds=True,
                            ),
                            sub_path="sub_path_example",
                        )
                    ],
                    parameters=[
                        IoArgoprojWorkflowV1alpha1Parameter(
                            default="default_example",
                            description="description_example",
                            enum=[
                                "enum_example"
                            ],
                            global_name="global_name_example",
                            name="name_example",
                            value="value_example",
                            value_from=IoArgoprojWorkflowV1alpha1ValueFrom(
                                config_map_key_ref=ConfigMapKeySelector(),
                                default="default_example",
                                event="event_example",
                                expression="expression_example",
                                jq_filter="jq_filter_example",
                                json_path="json_path_example",
                                parameter="parameter_example",
                                path="path_example",
                                supplied=dict(),
                            ),
                        )
                    ],
                ),
                artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(),
                artifact_repository_ref=IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef(
                    config_map="config_map_example",
                    key="key_example",
                ),
                automount_service_account_token=True,
                dns_config=PodDNSConfig(
                    nameservers=[
                        "nameservers_example"
                    ],
                    options=[
                        PodDNSConfigOption(
                            name="name_example",
                            value="value_example",
                        )
                    ],
                    searches=[
                        "searches_example"
                    ],
                ),
                dns_policy="dns_policy_example",
                entrypoint="entrypoint_example",
                executor=IoArgoprojWorkflowV1alpha1ExecutorConfig(
                    service_account_name="service_account_name_example",
                ),
                hooks=dict(
                    "key": IoArgoprojWorkflowV1alpha1LifecycleHook(
                        arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                        expression="expression_example",
                        template="template_example",
                        template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(
                            cluster_scope=True,
                            name="name_example",
                            template="template_example",
                        ),
                    ),
                ),
                host_aliases=[
                    HostAlias(
                        hostnames=[
                            "hostnames_example"
                        ],
                        ip="ip_example",
                    )
                ],
                host_network=True,
                image_pull_secrets=[
                    LocalObjectReference(
                        name="name_example",
                    )
                ],
                metrics=IoArgoprojWorkflowV1alpha1Metrics(
                    prometheus=[
                        IoArgoprojWorkflowV1alpha1Prometheus(
                            counter=IoArgoprojWorkflowV1alpha1Counter(
                                value="value_example",
                            ),
                            gauge=IoArgoprojWorkflowV1alpha1Gauge(
                                realtime=True,
                                value="value_example",
                            ),
                            help="help_example",
                            histogram=IoArgoprojWorkflowV1alpha1Histogram(
                                buckets=[
                                    3.14
                                ],
                                value="value_example",
                            ),
                            labels=[
                                IoArgoprojWorkflowV1alpha1MetricLabel(
                                    key="key_example",
                                    value="value_example",
                                )
                            ],
                            name="name_example",
                            when="when_example",
                        )
                    ],
                ),
                node_selector=dict(
                    "key": "key_example",
                ),
                on_exit="on_exit_example",
                parallelism=1,
                pod_disruption_budget=IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec(
                    max_unavailable="max_unavailable_example",
                    min_available="min_available_example",
                    selector=LabelSelector(),
                ),
                pod_gc=IoArgoprojWorkflowV1alpha1PodGC(
                    label_selector=LabelSelector(),
                    strategy="strategy_example",
                ),
                pod_metadata=IoArgoprojWorkflowV1alpha1Metadata(
                    annotations=dict(
                        "key": "key_example",
                    ),
                    labels=dict(),
                ),
                pod_priority=1,
                pod_priority_class_name="pod_priority_class_name_example",
                pod_spec_patch="pod_spec_patch_example",
                priority=1,
                retry_strategy=IoArgoprojWorkflowV1alpha1RetryStrategy(
                    affinity=IoArgoprojWorkflowV1alpha1RetryAffinity(
                        node_anti_affinity=dict(),
                    ),
                    backoff=IoArgoprojWorkflowV1alpha1Backoff(
                        duration="duration_example",
                        factor="factor_example",
                        max_duration="max_duration_example",
                    ),
                    expression="expression_example",
                    limit="limit_example",
                    retry_policy="retry_policy_example",
                ),
                scheduler_name="scheduler_name_example",
                security_context=PodSecurityContext(
                    fs_group=1,
                    fs_group_change_policy="fs_group_change_policy_example",
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
                    supplemental_groups=[
                        1
                    ],
                    sysctls=[
                        Sysctl(
                            name="name_example",
                            value="value_example",
                        )
                    ],
                    windows_options=WindowsSecurityContextOptions(
                        gmsa_credential_spec="gmsa_credential_spec_example",
                        gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                        host_process=True,
                        run_as_user_name="run_as_user_name_example",
                    ),
                ),
                service_account_name="service_account_name_example",
                shutdown="shutdown_example",
                suspend=True,
                synchronization=IoArgoprojWorkflowV1alpha1Synchronization(
                    mutex=IoArgoprojWorkflowV1alpha1Mutex(
                        name="name_example",
                    ),
                    semaphore=IoArgoprojWorkflowV1alpha1SemaphoreRef(
                        config_map_key_ref=ConfigMapKeySelector(),
                    ),
                ),
                template_defaults=IoArgoprojWorkflowV1alpha1Template(
                    active_deadline_seconds="active_deadline_seconds_example",
                    affinity=Affinity(),
                    archive_location=IoArgoprojWorkflowV1alpha1ArtifactLocation(
                        archive_logs=True,
                        artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(),
                        gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(),
                        git=IoArgoprojWorkflowV1alpha1GitArtifact(),
                        hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(),
                        http=IoArgoprojWorkflowV1alpha1HTTPArtifact(),
                        oss=IoArgoprojWorkflowV1alpha1OSSArtifact(),
                        raw=IoArgoprojWorkflowV1alpha1RawArtifact(),
                        s3=IoArgoprojWorkflowV1alpha1S3Artifact(),
                    ),
                    automount_service_account_token=True,
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
                            se_linux_options=SELinuxOptions(),
                            seccomp_profile=SeccompProfile(),
                            windows_options=WindowsSecurityContextOptions(),
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
                    container_set=IoArgoprojWorkflowV1alpha1ContainerSetTemplate(
                        containers=[
                            IoArgoprojWorkflowV1alpha1ContainerNode(
                                args=[],
                                command=[],
                                dependencies=[],
                                env=[],
                                env_from=[],
                                image="image_example",
                                image_pull_policy="image_pull_policy_example",
                                lifecycle=Lifecycle(),
                                liveness_probe=Probe(),
                                name="name_example",
                                ports=[],
                                readiness_probe=Probe(),
                                resources=ResourceRequirements(),
                                security_context=SecurityContext(),
                                startup_probe=Probe(),
                                stdin=True,
                                stdin_once=True,
                                termination_message_path="termination_message_path_example",
                                termination_message_policy="termination_message_policy_example",
                                tty=True,
                                volume_devices=[],
                                volume_mounts=[],
                                working_dir="working_dir_example",
                            )
                        ],
                        retry_strategy=IoArgoprojWorkflowV1alpha1ContainerSetRetryStrategy(
                            duration="duration_example",
                            retries="retries_example",
                        ),
                        volume_mounts=[
                            VolumeMount()
                        ],
                    ),
                    daemon=True,
                    dag=IoArgoprojWorkflowV1alpha1DAGTemplate(
                        fail_fast=True,
                        target="target_example",
                        tasks=[
                            IoArgoprojWorkflowV1alpha1DAGTask(
                                arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                                continue_on=IoArgoprojWorkflowV1alpha1ContinueOn(
                                    error=True,
                                    failed=True,
                                ),
                                dependencies=[
                                    "dependencies_example"
                                ],
                                depends="depends_example",
                                hooks=dict(
                                    "key": IoArgoprojWorkflowV1alpha1LifecycleHook(),
                                ),
                                inline=IoArgoprojWorkflowV1alpha1Template(),
                                name="name_example",
                                on_exit="on_exit_example",
                                template="template_example",
                                template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                                when="when_example",
                                with_items=[
                                    dict()
                                ],
                                with_param="with_param_example",
                                with_sequence=IoArgoprojWorkflowV1alpha1Sequence(
                                    count="count_example",
                                    end="end_example",
                                    format="format_example",
                                    start="start_example",
                                ),
                            )
                        ],
                    ),
                    data=IoArgoprojWorkflowV1alpha1Data(
                        source=IoArgoprojWorkflowV1alpha1DataSource(
                            artifact_paths=IoArgoprojWorkflowV1alpha1ArtifactPaths(
                                archive=IoArgoprojWorkflowV1alpha1ArchiveStrategy(),
                                archive_logs=True,
                                artifact_gc=IoArgoprojWorkflowV1alpha1ArtifactGC(),
                                artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(),
                                deleted=True,
                                _from="_from_example",
                                from_expression="from_expression_example",
                                gcs=IoArgoprojWorkflowV1alpha1GCSArtifact(),
                                git=IoArgoprojWorkflowV1alpha1GitArtifact(),
                                global_name="global_name_example",
                                hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifact(),
                                http=IoArgoprojWorkflowV1alpha1HTTPArtifact(),
                                mode=1,
                                name="name_example",
                                optional=True,
                                oss=IoArgoprojWorkflowV1alpha1OSSArtifact(),
                                path="path_example",
                                raw=IoArgoprojWorkflowV1alpha1RawArtifact(),
                                recurse_mode=True,
                                s3=IoArgoprojWorkflowV1alpha1S3Artifact(),
                                sub_path="sub_path_example",
                            ),
                        ),
                        transformation=[
                            IoArgoprojWorkflowV1alpha1TransformationStep(
                                expression="expression_example",
                            )
                        ],
                    ),
                    executor=IoArgoprojWorkflowV1alpha1ExecutorConfig(),
                    fail_fast=True,
                    host_aliases=[
                        HostAlias()
                    ],
                    http=IoArgoprojWorkflowV1alpha1HTTP(
                        body="body_example",
                        headers=[
                            IoArgoprojWorkflowV1alpha1HTTPHeader(
                                name="name_example",
                                value="value_example",
                                value_from=IoArgoprojWorkflowV1alpha1HTTPHeaderSource(
                                    secret_key_ref=SecretKeySelector(),
                                ),
                            )
                        ],
                        insecure_skip_verify=True,
                        method="method_example",
                        success_condition="success_condition_example",
                        timeout_seconds=1,
                        url="url_example",
                    ),
                    init_containers=[
                        IoArgoprojWorkflowV1alpha1UserContainer(
                            args=[],
                            command=[],
                            env=[],
                            env_from=[],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=Lifecycle(),
                            liveness_probe=Probe(),
                            mirror_volume_mounts=True,
                            name="name_example",
                            ports=[],
                            readiness_probe=Probe(),
                            resources=ResourceRequirements(),
                            security_context=SecurityContext(),
                            startup_probe=Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[],
                            volume_mounts=[],
                            working_dir="working_dir_example",
                        )
                    ],
                    inputs=IoArgoprojWorkflowV1alpha1Inputs(
                        artifacts=[
                            IoArgoprojWorkflowV1alpha1Artifact()
                        ],
                        parameters=[
                            IoArgoprojWorkflowV1alpha1Parameter()
                        ],
                    ),
                    memoize=IoArgoprojWorkflowV1alpha1Memoize(
                        cache=IoArgoprojWorkflowV1alpha1Cache(
                            config_map=ConfigMapKeySelector(),
                        ),
                        key="key_example",
                        max_age="max_age_example",
                    ),
                    metadata=IoArgoprojWorkflowV1alpha1Metadata(),
                    metrics=IoArgoprojWorkflowV1alpha1Metrics(),
                    name="name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    outputs=IoArgoprojWorkflowV1alpha1Outputs(
                        artifacts=[
                            IoArgoprojWorkflowV1alpha1Artifact()
                        ],
                        exit_code="exit_code_example",
                        parameters=[
                            IoArgoprojWorkflowV1alpha1Parameter()
                        ],
                        result="result_example",
                    ),
                    parallelism=1,
                    plugin=dict(),
                    pod_spec_patch="pod_spec_patch_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    resource=IoArgoprojWorkflowV1alpha1ResourceTemplate(
                        action="action_example",
                        failure_condition="failure_condition_example",
                        flags=[
                            "flags_example"
                        ],
                        manifest="manifest_example",
                        manifest_from=IoArgoprojWorkflowV1alpha1ManifestFrom(
                            artifact=IoArgoprojWorkflowV1alpha1Artifact(),
                        ),
                        merge_strategy="merge_strategy_example",
                        set_owner_reference=True,
                        success_condition="success_condition_example",
                    ),
                    retry_strategy=IoArgoprojWorkflowV1alpha1RetryStrategy(),
                    scheduler_name="scheduler_name_example",
                    script=IoArgoprojWorkflowV1alpha1ScriptTemplate(
                        args=[],
                        command=[],
                        env=[],
                        env_from=[],
                        image="image_example",
                        image_pull_policy="image_pull_policy_example",
                        lifecycle=Lifecycle(),
                        liveness_probe=Probe(),
                        name="name_example",
                        ports=[],
                        readiness_probe=Probe(),
                        resources=ResourceRequirements(),
                        security_context=SecurityContext(),
                        source="source_example",
                        startup_probe=Probe(),
                        stdin=True,
                        stdin_once=True,
                        termination_message_path="termination_message_path_example",
                        termination_message_policy="termination_message_policy_example",
                        tty=True,
                        volume_devices=[],
                        volume_mounts=[],
                        working_dir="working_dir_example",
                    ),
                    security_context=PodSecurityContext(),
                    service_account_name="service_account_name_example",
                    sidecars=[
                        IoArgoprojWorkflowV1alpha1UserContainer()
                    ],
                    steps=[
                        IoArgoprojWorkflowV1alpha1ParallelSteps([
                            IoArgoprojWorkflowV1alpha1WorkflowStep(
                                arguments=IoArgoprojWorkflowV1alpha1Arguments(),
                                continue_on=IoArgoprojWorkflowV1alpha1ContinueOn(),
                                hooks=dict(),
                                inline=IoArgoprojWorkflowV1alpha1Template(),
                                name="name_example",
                                on_exit="on_exit_example",
                                template="template_example",
                                template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                                when="when_example",
                                with_items=[
                                    dict()
                                ],
                                with_param="with_param_example",
                                with_sequence=IoArgoprojWorkflowV1alpha1Sequence(),
                            )
                        ])
                    ],
                    suspend=IoArgoprojWorkflowV1alpha1SuspendTemplate(
                        duration="duration_example",
                    ),
                    synchronization=IoArgoprojWorkflowV1alpha1Synchronization(),
                    timeout="timeout_example",
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
                templates=[
                    IoArgoprojWorkflowV1alpha1Template()
                ],
                tolerations=[],
                ttl_strategy=IoArgoprojWorkflowV1alpha1TTLStrategy(
                    seconds_after_completion=1,
                    seconds_after_failure=1,
                    seconds_after_success=1,
                ),
                volume_claim_gc=IoArgoprojWorkflowV1alpha1VolumeClaimGC(
                    strategy="strategy_example",
                ),
                volume_claim_templates=[
                    PersistentVolumeClaim(
                        api_version="api_version_example",
                        kind="kind_example",
                        metadata=ObjectMeta(),
                        spec=PersistentVolumeClaimSpec(),
                        status=PersistentVolumeClaimStatus(
                            access_modes=[
                                "access_modes_example"
                            ],
                            allocated_resources=dict(
                                "key": "key_example",
                            ),
                            capacity=dict(
                                "key": "key_example",
                            ),
                            conditions=[
                                PersistentVolumeClaimCondition(
                                    last_probe_time="1970-01-01T00:00:00.00Z",
                                    last_transition_time="1970-01-01T00:00:00.00Z",
                                    message="message_example",
                                    reason="reason_example",
                                    status="status_example",
                                    type="FileSystemResizePending",
                                )
                            ],
                            phase="Bound",
                            resize_status="resize_status_example",
                        ),
                    )
                ],
                volumes=[
                    Volume()
                ],
                workflow_metadata=IoArgoprojWorkflowV1alpha1WorkflowMetadata(
                    annotations=dict(),
                    labels=dict(),
                    labels_from=dict(
                        "key": IoArgoprojWorkflowV1alpha1LabelValueFrom(
                            expression="expression_example",
                        ),
                    ),
                ),
                workflow_template_ref=IoArgoprojWorkflowV1alpha1WorkflowTemplateRef(
                    cluster_scope=True,
                    name="name_example",
                ),
            ),
            status=IoArgoprojWorkflowV1alpha1WorkflowStatus(
                artifact_repository_ref=IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus(
                    artifact_repository=IoArgoprojWorkflowV1alpha1ArtifactRepository(
                        archive_logs=True,
                        artifactory=IoArgoprojWorkflowV1alpha1ArtifactoryArtifactRepository(
                            password_secret=SecretKeySelector(),
                            repo_url="repo_url_example",
                            username_secret=SecretKeySelector(),
                        ),
                        gcs=IoArgoprojWorkflowV1alpha1GCSArtifactRepository(
                            bucket="bucket_example",
                            key_format="key_format_example",
                            service_account_key_secret=SecretKeySelector(),
                        ),
                        hdfs=IoArgoprojWorkflowV1alpha1HDFSArtifactRepository(
                            addresses=[],
                            force=True,
                            hdfs_user="hdfs_user_example",
                            krb_c_cache_secret=SecretKeySelector(),
                            krb_config_config_map=ConfigMapKeySelector(),
                            krb_keytab_secret=SecretKeySelector(),
                            krb_realm="krb_realm_example",
                            krb_service_principal_name="krb_service_principal_name_example",
                            krb_username="krb_username_example",
                            path_format="path_format_example",
                        ),
                        oss=IoArgoprojWorkflowV1alpha1OSSArtifactRepository(
                            access_key_secret=SecretKeySelector(),
                            bucket="bucket_example",
                            create_bucket_if_not_present=True,
                            endpoint="endpoint_example",
                            key_format="key_format_example",
                            lifecycle_rule=IoArgoprojWorkflowV1alpha1OSSLifecycleRule(),
                            secret_key_secret=SecretKeySelector(),
                            security_token="security_token_example",
                        ),
                        s3=IoArgoprojWorkflowV1alpha1S3ArtifactRepository(
                            access_key_secret=SecretKeySelector(),
                            bucket="bucket_example",
                            create_bucket_if_not_present=IoArgoprojWorkflowV1alpha1CreateS3BucketOptions(),
                            encryption_options=IoArgoprojWorkflowV1alpha1S3EncryptionOptions(),
                            endpoint="endpoint_example",
                            insecure=True,
                            key_format="key_format_example",
                            key_prefix="key_prefix_example",
                            region="region_example",
                            role_arn="role_arn_example",
                            secret_key_secret=SecretKeySelector(),
                            use_sdk_creds=True,
                        ),
                    ),
                    config_map="config_map_example",
                    default=True,
                    key="key_example",
                    namespace="namespace_example",
                ),
                compressed_nodes="compressed_nodes_example",
                conditions=[
                    IoArgoprojWorkflowV1alpha1Condition(
                        message="message_example",
                        status="status_example",
                        type="type_example",
                    )
                ],
                estimated_duration=1,
                finished_at="1970-01-01T00:00:00.00Z",
                message="message_example",
                nodes=dict(
                    "key": IoArgoprojWorkflowV1alpha1NodeStatus(
                        boundary_id="boundary_id_example",
                        children=[
                            "children_example"
                        ],
                        daemoned=True,
                        display_name="display_name_example",
                        estimated_duration=1,
                        finished_at="1970-01-01T00:00:00.00Z",
                        host_node_name="host_node_name_example",
                        id="id_example",
                        inputs=IoArgoprojWorkflowV1alpha1Inputs(),
                        memoization_status=IoArgoprojWorkflowV1alpha1MemoizationStatus(
                            cache_name="cache_name_example",
                            hit=True,
                            key="key_example",
                        ),
                        message="message_example",
                        name="name_example",
                        outbound_nodes=[
                            "outbound_nodes_example"
                        ],
                        outputs=IoArgoprojWorkflowV1alpha1Outputs(),
                        phase="phase_example",
                        pod_ip="pod_ip_example",
                        progress="progress_example",
                        resources_duration=dict(
                            "key": 1,
                        ),
                        started_at="1970-01-01T00:00:00.00Z",
                        synchronization_status=IoArgoprojWorkflowV1alpha1NodeSynchronizationStatus(
                            waiting="waiting_example",
                        ),
                        template_name="template_name_example",
                        template_ref=IoArgoprojWorkflowV1alpha1TemplateRef(),
                        template_scope="template_scope_example",
                        type="type_example",
                    ),
                ),
                offload_node_status_version="offload_node_status_version_example",
                outputs=IoArgoprojWorkflowV1alpha1Outputs(),
                persistent_volume_claims=[
                    Volume()
                ],
                phase="phase_example",
                progress="progress_example",
                resources_duration=dict(
                    "key": 1,
                ),
                started_at="1970-01-01T00:00:00.00Z",
                stored_templates=dict(
                    "key": IoArgoprojWorkflowV1alpha1Template(),
                ),
                stored_workflow_template_spec=IoArgoprojWorkflowV1alpha1WorkflowSpec(),
                synchronization=IoArgoprojWorkflowV1alpha1SynchronizationStatus(
                    mutex=IoArgoprojWorkflowV1alpha1MutexStatus(
                        holding=[
                            IoArgoprojWorkflowV1alpha1MutexHolding(
                                holder="holder_example",
                                mutex="mutex_example",
                            )
                        ],
                        waiting=[
                            IoArgoprojWorkflowV1alpha1MutexHolding()
                        ],
                    ),
                    semaphore=IoArgoprojWorkflowV1alpha1SemaphoreStatus(
                        holding=[
                            IoArgoprojWorkflowV1alpha1SemaphoreHolding(
                                holders=[
                                    "holders_example"
                                ],
                                semaphore="semaphore_example",
                            )
                        ],
                        waiting=[
                            IoArgoprojWorkflowV1alpha1SemaphoreHolding()
                        ],
                    ),
                ),
            ),
        ),
    )
    try:
        api_response = api_instance.lint_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->lint_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowLintRequest**](IoArgoprojWorkflowV1alpha1WorkflowLintRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> IoArgoprojWorkflowV1alpha1WorkflowList list_workflows(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_list import IoArgoprojWorkflowV1alpha1WorkflowList
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_workflows(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflows: %s\n" % e)

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
        'fields': "fields_example",
    }
    try:
        api_response = api_instance.list_workflows(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->list_workflows: %s\n" % e)
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
fields | FieldsSchema | | optional


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

#### FieldsSchema

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
[**IoArgoprojWorkflowV1alpha1WorkflowList**](IoArgoprojWorkflowV1alpha1WorkflowList.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1WorkflowList**](IoArgoprojWorkflowV1alpha1WorkflowList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pod_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pod_logs(namespacenamepod_name)

DEPRECATED: Cannot work via HTTP if podName is an empty string. Use WorkflowLogs.

### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_log_entry import IoArgoprojWorkflowV1alpha1LogEntry
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
        'podName': "podName_example",
    }
    query_params = {
    }
    try:
        # DEPRECATED: Cannot work via HTTP if podName is an empty string. Use WorkflowLogs.
        api_response = api_instance.pod_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->pod_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
        'podName': "podName_example",
    }
    query_params = {
        'logOptions.container': "logOptions.container_example",
        'logOptions.follow': True,
        'logOptions.previous': True,
        'logOptions.sinceSeconds': "logOptions.sinceSeconds_example",
        'logOptions.sinceTime.seconds': "logOptions.sinceTime.seconds_example",
        'logOptions.sinceTime.nanos': 1,
        'logOptions.timestamps': True,
        'logOptions.tailLines': "logOptions.tailLines_example",
        'logOptions.limitBytes': "logOptions.limitBytes_example",
        'logOptions.insecureSkipTLSVerifyBackend': True,
        'grep': "grep_example",
        'selector': "selector_example",
    }
    try:
        # DEPRECATED: Cannot work via HTTP if podName is an empty string. Use WorkflowLogs.
        api_response = api_instance.pod_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->pod_logs: %s\n" % e)
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
logOptions.container | LogOptionsContainerSchema | | optional
logOptions.follow | LogOptionsFollowSchema | | optional
logOptions.previous | LogOptionsPreviousSchema | | optional
logOptions.sinceSeconds | LogOptionsSinceSecondsSchema | | optional
logOptions.sinceTime.seconds | LogOptionsSinceTimeSecondsSchema | | optional
logOptions.sinceTime.nanos | LogOptionsSinceTimeNanosSchema | | optional
logOptions.timestamps | LogOptionsTimestampsSchema | | optional
logOptions.tailLines | LogOptionsTailLinesSchema | | optional
logOptions.limitBytes | LogOptionsLimitBytesSchema | | optional
logOptions.insecureSkipTLSVerifyBackend | LogOptionsInsecureSkipTLSVerifyBackendSchema | | optional
grep | GrepSchema | | optional
selector | SelectorSchema | | optional


#### LogOptionsContainerSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsFollowSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsPreviousSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsSinceSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsSinceTimeSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsSinceTimeNanosSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### LogOptionsTimestampsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsTailLinesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsLimitBytesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsInsecureSkipTLSVerifyBackendSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### GrepSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 
podName | PodNameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodNameSchema

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
**result** | [**IoArgoprojWorkflowV1alpha1LogEntry**](IoArgoprojWorkflowV1alpha1LogEntry.md) |  | [optional] 
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

# **resubmit_workflow**
> IoArgoprojWorkflowV1alpha1Workflow resubmit_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_resubmit_request import IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest(
        memoized=True,
        name="name_example",
        namespace="namespace_example",
    )
    try:
        api_response = api_instance.resubmit_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->resubmit_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest**](IoArgoprojWorkflowV1alpha1WorkflowResubmitRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_workflow**
> IoArgoprojWorkflowV1alpha1Workflow resume_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_resume_request import IoArgoprojWorkflowV1alpha1WorkflowResumeRequest
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowResumeRequest(
        name="name_example",
        namespace="namespace_example",
        node_field_selector="node_field_selector_example",
    )
    try:
        api_response = api_instance.resume_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->resume_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowResumeRequest**](IoArgoprojWorkflowV1alpha1WorkflowResumeRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_workflow**
> IoArgoprojWorkflowV1alpha1Workflow retry_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_retry_request import IoArgoprojWorkflowV1alpha1WorkflowRetryRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowRetryRequest(
        name="name_example",
        namespace="namespace_example",
        node_field_selector="node_field_selector_example",
        restart_successful=True,
    )
    try:
        api_response = api_instance.retry_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->retry_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowRetryRequest**](IoArgoprojWorkflowV1alpha1WorkflowRetryRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_workflow**
> IoArgoprojWorkflowV1alpha1Workflow set_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_set_request import IoArgoprojWorkflowV1alpha1WorkflowSetRequest
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowSetRequest(
        message="message_example",
        name="name_example",
        namespace="namespace_example",
        node_field_selector="node_field_selector_example",
        output_parameters="output_parameters_example",
        phase="phase_example",
    )
    try:
        api_response = api_instance.set_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->set_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowSetRequest**](IoArgoprojWorkflowV1alpha1WorkflowSetRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_workflow**
> IoArgoprojWorkflowV1alpha1Workflow stop_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_stop_request import IoArgoprojWorkflowV1alpha1WorkflowStopRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowStopRequest(
        message="message_example",
        name="name_example",
        namespace="namespace_example",
        node_field_selector="node_field_selector_example",
    )
    try:
        api_response = api_instance.stop_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->stop_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowStopRequest**](IoArgoprojWorkflowV1alpha1WorkflowStopRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_workflow**
> IoArgoprojWorkflowV1alpha1Workflow submit_workflow(namespacebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_submit_request import IoArgoprojWorkflowV1alpha1WorkflowSubmitRequest
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowSubmitRequest(
        namespace="namespace_example",
        resource_kind="resource_kind_example",
        resource_name="resource_name_example",
        submit_options=IoArgoprojWorkflowV1alpha1SubmitOpts(
            annotations="annotations_example",
            dry_run=True,
            entry_point="entry_point_example",
            generate_name="generate_name_example",
            labels="labels_example",
            name="name_example",
            owner_reference=OwnerReference(
                api_version="api_version_example",
                block_owner_deletion=True,
                controller=True,
                kind="kind_example",
                name="name_example",
                uid="uid_example",
            ),
            parameters=[
                "parameters_example"
            ],
            pod_priority_class_name="pod_priority_class_name_example",
            priority=1,
            server_dry_run=True,
            service_account="service_account_example",
        ),
    )
    try:
        api_response = api_instance.submit_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->submit_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowSubmitRequest**](IoArgoprojWorkflowV1alpha1WorkflowSubmitRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_workflow**
> IoArgoprojWorkflowV1alpha1Workflow suspend_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_suspend_request import IoArgoprojWorkflowV1alpha1WorkflowSuspendRequest
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowSuspendRequest(
        name="name_example",
        namespace="namespace_example",
    )
    try:
        api_response = api_instance.suspend_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->suspend_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowSuspendRequest**](IoArgoprojWorkflowV1alpha1WorkflowSuspendRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_workflow**
> IoArgoprojWorkflowV1alpha1Workflow terminate_workflow(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_terminate_request import IoArgoprojWorkflowV1alpha1WorkflowTerminateRequest
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = IoArgoprojWorkflowV1alpha1WorkflowTerminateRequest(
        name="name_example",
        namespace="namespace_example",
    )
    try:
        api_response = api_instance.terminate_workflow(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->terminate_workflow: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowTerminateRequest**](IoArgoprojWorkflowV1alpha1WorkflowTerminateRequest.md) |  | 


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
[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1Workflow**](IoArgoprojWorkflowV1alpha1Workflow.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_events**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_events(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from argo_workflows.model.event import Event
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_events: %s\n" % e)

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
        api_response = api_instance.watch_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_events: %s\n" % e)
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
**result** | [**Event**](Event.md) |  | [optional] 
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

# **watch_workflows**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_workflows(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_watch_event import IoArgoprojWorkflowV1alpha1WorkflowWatchEvent
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_workflows(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflows: %s\n" % e)

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
        'fields': "fields_example",
    }
    try:
        api_response = api_instance.watch_workflows(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->watch_workflows: %s\n" % e)
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
fields | FieldsSchema | | optional


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

#### FieldsSchema

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
**result** | [**IoArgoprojWorkflowV1alpha1WorkflowWatchEvent**](IoArgoprojWorkflowV1alpha1WorkflowWatchEvent.md) |  | [optional] 
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

# **workflow_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} workflow_logs(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import workflow_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_log_entry import IoArgoprojWorkflowV1alpha1LogEntry
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
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.workflow_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'podName': "podName_example",
        'logOptions.container': "logOptions.container_example",
        'logOptions.follow': True,
        'logOptions.previous': True,
        'logOptions.sinceSeconds': "logOptions.sinceSeconds_example",
        'logOptions.sinceTime.seconds': "logOptions.sinceTime.seconds_example",
        'logOptions.sinceTime.nanos': 1,
        'logOptions.timestamps': True,
        'logOptions.tailLines': "logOptions.tailLines_example",
        'logOptions.limitBytes': "logOptions.limitBytes_example",
        'logOptions.insecureSkipTLSVerifyBackend': True,
        'grep': "grep_example",
        'selector': "selector_example",
    }
    try:
        api_response = api_instance.workflow_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_logs: %s\n" % e)
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
podName | PodNameSchema | | optional
logOptions.container | LogOptionsContainerSchema | | optional
logOptions.follow | LogOptionsFollowSchema | | optional
logOptions.previous | LogOptionsPreviousSchema | | optional
logOptions.sinceSeconds | LogOptionsSinceSecondsSchema | | optional
logOptions.sinceTime.seconds | LogOptionsSinceTimeSecondsSchema | | optional
logOptions.sinceTime.nanos | LogOptionsSinceTimeNanosSchema | | optional
logOptions.timestamps | LogOptionsTimestampsSchema | | optional
logOptions.tailLines | LogOptionsTailLinesSchema | | optional
logOptions.limitBytes | LogOptionsLimitBytesSchema | | optional
logOptions.insecureSkipTLSVerifyBackend | LogOptionsInsecureSkipTLSVerifyBackendSchema | | optional
grep | GrepSchema | | optional
selector | SelectorSchema | | optional


#### PodNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsContainerSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsFollowSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsPreviousSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsSinceSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsSinceTimeSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsSinceTimeNanosSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### LogOptionsTimestampsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### LogOptionsTailLinesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsLimitBytesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LogOptionsInsecureSkipTLSVerifyBackendSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### GrepSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

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
**result** | [**IoArgoprojWorkflowV1alpha1LogEntry**](IoArgoprojWorkflowV1alpha1LogEntry.md) |  | [optional] 
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

