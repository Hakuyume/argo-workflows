# argo_workflows.SensorServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sensor**](SensorServiceApi.md#create_sensor) | **POST** /api/v1/sensors/{namespace} | 
[**delete_sensor**](SensorServiceApi.md#delete_sensor) | **DELETE** /api/v1/sensors/{namespace}/{name} | 
[**get_sensor**](SensorServiceApi.md#get_sensor) | **GET** /api/v1/sensors/{namespace}/{name} | 
[**list_sensors**](SensorServiceApi.md#list_sensors) | **GET** /api/v1/sensors/{namespace} | 
[**sensors_logs**](SensorServiceApi.md#sensors_logs) | **GET** /api/v1/stream/sensors/{namespace}/logs | 
[**update_sensor**](SensorServiceApi.md#update_sensor) | **PUT** /api/v1/sensors/{namespace}/{name} | 
[**watch_sensors**](SensorServiceApi.md#watch_sensors) | **GET** /api/v1/stream/sensors/{namespace} | 

# **create_sensor**
> IoArgoprojEventsV1alpha1Sensor create_sensor(namespacebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_sensor import IoArgoprojEventsV1alpha1Sensor
from argo_workflows.model.sensor_create_sensor_request import SensorCreateSensorRequest
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    body = SensorCreateSensorRequest(
        create_options=CreateOptions(
            dry_run=[
                "dry_run_example"
            ],
            field_manager="field_manager_example",
            field_validation="field_validation_example",
        ),
        namespace="namespace_example",
        sensor=IoArgoprojEventsV1alpha1Sensor(
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
            spec=IoArgoprojEventsV1alpha1SensorSpec(
                dependencies=[
                    IoArgoprojEventsV1alpha1EventDependency(
                        event_name="event_name_example",
                        event_source_name="event_source_name_example",
                        filters=IoArgoprojEventsV1alpha1EventDependencyFilter(
                            context=IoArgoprojEventsV1alpha1EventContext(
                                datacontenttype="datacontenttype_example",
                                id="id_example",
                                source="source_example",
                                specversion="specversion_example",
                                subject="subject_example",
                                time="1970-01-01T00:00:00.00Z",
                                type="type_example",
                            ),
                            data=[
                                IoArgoprojEventsV1alpha1DataFilter(
                                    comparator="comparator_example",
                                    path="path_example",
                                    template="template_example",
                                    type="type_example",
                                    value=[
                                        "value_example"
                                    ],
                                )
                            ],
                            data_logical_operator="data_logical_operator_example",
                            expr_logical_operator="expr_logical_operator_example",
                            exprs=[
                                IoArgoprojEventsV1alpha1ExprFilter(
                                    expr="expr_example",
                                    fields=[
                                        IoArgoprojEventsV1alpha1PayloadField(
                                            name="name_example",
                                            path="path_example",
                                        )
                                    ],
                                )
                            ],
                            time=IoArgoprojEventsV1alpha1TimeFilter(
                                start="start_example",
                                stop="stop_example",
                            ),
                        ),
                        filters_logical_operator="filters_logical_operator_example",
                        name="name_example",
                        transform=IoArgoprojEventsV1alpha1EventDependencyTransformer(
                            jq="jq_example",
                            script="script_example",
                        ),
                    )
                ],
                error_on_failed_round=True,
                event_bus_name="event_bus_name_example",
                replicas=1,
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
                                    config_map_key_ref=ConfigMapKeySelector(
                                        key="key_example",
                                        name="name_example",
                                        optional=True,
                                    ),
                                    field_ref=ObjectFieldSelector(
                                        api_version="api_version_example",
                                        field_path="field_path_example",
                                    ),
                                    resource_field_ref=ResourceFieldSelector(
                                        container_name="container_name_example",
                                        divisor="divisor_example",
                                        resource="resource_example",
                                    ),
                                    secret_key_ref=SecretKeySelector(
                                        key="key_example",
                                        name="name_example",
                                        optional=True,
                                    ),
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
                        annotations=dict(
                            "key": "key_example",
                        ),
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
                triggers=[
                    IoArgoprojEventsV1alpha1Trigger(
                        parameters=[
                            IoArgoprojEventsV1alpha1TriggerParameter(
                                dest="dest_example",
                                operation="operation_example",
                                src=IoArgoprojEventsV1alpha1TriggerParameterSource(
                                    context_key="context_key_example",
                                    context_template="context_template_example",
                                    data_key="data_key_example",
                                    data_template="data_template_example",
                                    dependency_name="dependency_name_example",
                                    value="value_example",
                                ),
                            )
                        ],
                        policy=IoArgoprojEventsV1alpha1TriggerPolicy(
                            k8s=IoArgoprojEventsV1alpha1K8SResourcePolicy(
                                backoff=IoArgoprojEventsV1alpha1Backoff(
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
                                error_on_backoff_timeout=True,
                                labels=dict(
                                    "key": "key_example",
                                ),
                            ),
                            status=IoArgoprojEventsV1alpha1StatusPolicy(
                                allow=[
                                    1
                                ],
                            ),
                        ),
                        rate_limit=IoArgoprojEventsV1alpha1RateLimit(
                            requests_per_unit=1,
                            unit="unit_example",
                        ),
                        retry_strategy=IoArgoprojEventsV1alpha1Backoff(),
                        template=IoArgoprojEventsV1alpha1TriggerTemplate(
                            argo_workflow=IoArgoprojEventsV1alpha1ArgoWorkflowTrigger(
                                operation="operation_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                source=IoArgoprojEventsV1alpha1ArtifactLocation(
                                    configmap=ConfigMapKeySelector(),
                                    file=IoArgoprojEventsV1alpha1FileArtifact(
                                        path="path_example",
                                    ),
                                    git=IoArgoprojEventsV1alpha1GitArtifact(
                                        branch="branch_example",
                                        clone_directory="clone_directory_example",
                                        creds=IoArgoprojEventsV1alpha1GitCreds(
                                            password=SecretKeySelector(),
                                            username=SecretKeySelector(),
                                        ),
                                        file_path="file_path_example",
                                        ref="ref_example",
                                        remote=IoArgoprojEventsV1alpha1GitRemoteConfig(
                                            name="name_example",
                                            urls=[
                                                "urls_example"
                                            ],
                                        ),
                                        ssh_key_secret=SecretKeySelector(),
                                        tag="tag_example",
                                        url="url_example",
                                    ),
                                    inline="inline_example",
                                    resource=IoArgoprojEventsV1alpha1Resource(
                                        value='YQ==',
                                    ),
                                    s3=IoArgoprojEventsV1alpha1S3Artifact(
                                        access_key=SecretKeySelector(),
                                        bucket=IoArgoprojEventsV1alpha1S3Bucket(
                                            key="key_example",
                                            name="name_example",
                                        ),
                                        endpoint="endpoint_example",
                                        events=[
                                            "events_example"
                                        ],
                                        filter=IoArgoprojEventsV1alpha1S3Filter(
                                            prefix="prefix_example",
                                            suffix="suffix_example",
                                        ),
                                        insecure=True,
                                        metadata=dict(),
                                        region="region_example",
                                        secret_key=SecretKeySelector(),
                                    ),
                                    url=IoArgoprojEventsV1alpha1URLArtifact(
                                        path="path_example",
                                        verify_cert=True,
                                    ),
                                ),
                            ),
                            aws_lambda=IoArgoprojEventsV1alpha1AWSLambdaTrigger(
                                access_key=SecretKeySelector(),
                                function_name="function_name_example",
                                invocation_type="invocation_type_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                region="region_example",
                                role_arn="role_arn_example",
                                secret_key=SecretKeySelector(),
                            ),
                            azure_event_hubs=IoArgoprojEventsV1alpha1AzureEventHubsTrigger(
                                fqdn="fqdn_example",
                                hub_name="hub_name_example",
                                parameters=[],
                                payload=[],
                                shared_access_key=SecretKeySelector(),
                                shared_access_key_name=SecretKeySelector(),
                            ),
                            conditions="conditions_example",
                            conditions_reset=[
                                IoArgoprojEventsV1alpha1ConditionsResetCriteria(
                                    by_time=IoArgoprojEventsV1alpha1ConditionsResetByTime(
                                        cron="cron_example",
                                        timezone="timezone_example",
                                    ),
                                )
                            ],
                            custom=IoArgoprojEventsV1alpha1CustomTrigger(
                                cert_secret=SecretKeySelector(),
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[],
                                secure=True,
                                server_name_override="server_name_override_example",
                                server_url="server_url_example",
                                spec=dict(
                                    "key": "key_example",
                                ),
                            ),
                            http=IoArgoprojEventsV1alpha1HTTPTrigger(
                                basic_auth=IoArgoprojEventsV1alpha1BasicAuth(
                                    password=SecretKeySelector(),
                                    username=SecretKeySelector(),
                                ),
                                headers=dict(
                                    "key": "key_example",
                                ),
                                method="method_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                secure_headers=[
                                    IoArgoprojEventsV1alpha1SecureHeader(
                                        name="name_example",
                                        value_from=IoArgoprojEventsV1alpha1ValueFromSource(
                                            config_map_key_ref=ConfigMapKeySelector(),
                                            secret_key_ref=SecretKeySelector(),
                                        ),
                                    )
                                ],
                                timeout="timeout_example",
                                tls=IoArgoprojEventsV1alpha1TLSConfig(
                                    ca_cert_secret=SecretKeySelector(),
                                    client_cert_secret=SecretKeySelector(),
                                    client_key_secret=SecretKeySelector(),
                                    insecure_skip_verify=True,
                                ),
                                url="url_example",
                            ),
                            k8s=IoArgoprojEventsV1alpha1StandardK8STrigger(
                                live_object=True,
                                operation="operation_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                patch_strategy="patch_strategy_example",
                                source=IoArgoprojEventsV1alpha1ArtifactLocation(),
                            ),
                            kafka=IoArgoprojEventsV1alpha1KafkaTrigger(
                                compress=True,
                                flush_frequency=1,
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                partition=1,
                                partitioning_key="partitioning_key_example",
                                payload=[],
                                required_acks=1,
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
                            log=IoArgoprojEventsV1alpha1LogTrigger(
                                interval_seconds="interval_seconds_example",
                            ),
                            name="name_example",
                            nats=IoArgoprojEventsV1alpha1NATSTrigger(
                                parameters=[],
                                payload=[],
                                subject="subject_example",
                                tls=IoArgoprojEventsV1alpha1TLSConfig(),
                                url="url_example",
                            ),
                            open_whisk=IoArgoprojEventsV1alpha1OpenWhiskTrigger(
                                action_name="action_name_example",
                                auth_token=SecretKeySelector(),
                                host="host_example",
                                namespace="namespace_example",
                                parameters=[],
                                payload=[],
                                version="version_example",
                            ),
                            pulsar=IoArgoprojEventsV1alpha1PulsarTrigger(
                                auth_token_secret=SecretKeySelector(),
                                connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                                parameters=[],
                                payload=[],
                                tls=IoArgoprojEventsV1alpha1TLSConfig(),
                                tls_allow_insecure_connection=True,
                                tls_trust_certs_secret=SecretKeySelector(),
                                tls_validate_hostname=True,
                                topic="topic_example",
                                url="url_example",
                            ),
                            slack=IoArgoprojEventsV1alpha1SlackTrigger(
                                channel="channel_example",
                                message="message_example",
                                parameters=[],
                                slack_token=SecretKeySelector(),
                            ),
                        ),
                    )
                ],
            ),
            status=IoArgoprojEventsV1alpha1SensorStatus(
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
    )
    try:
        api_response = api_instance.create_sensor(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->create_sensor: %s\n" % e)
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
[**SensorCreateSensorRequest**](SensorCreateSensorRequest.md) |  | 


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
[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md) |  | 


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



[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sensor**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_sensor(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_sensor(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->delete_sensor: %s\n" % e)

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
        api_response = api_instance.delete_sensor(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->delete_sensor: %s\n" % e)
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

# **get_sensor**
> IoArgoprojEventsV1alpha1Sensor get_sensor(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_sensor import IoArgoprojEventsV1alpha1Sensor
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_sensor(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->get_sensor: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'getOptions.resourceVersion': "getOptions.resourceVersion_example",
    }
    try:
        api_response = api_instance.get_sensor(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->get_sensor: %s\n" % e)
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


#### GetOptionsResourceVersionSchema

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
[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md) |  | 


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



[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sensors**
> IoArgoprojEventsV1alpha1SensorList list_sensors(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_sensor_list import IoArgoprojEventsV1alpha1SensorList
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_sensors(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->list_sensors: %s\n" % e)

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
        api_response = api_instance.list_sensors(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->list_sensors: %s\n" % e)
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
[**IoArgoprojEventsV1alpha1SensorList**](IoArgoprojEventsV1alpha1SensorList.md) |  | 


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



[**IoArgoprojEventsV1alpha1SensorList**](IoArgoprojEventsV1alpha1SensorList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sensors_logs(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.sensor_log_entry import SensorLogEntry
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.sensors_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->sensors_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'name': "name_example",
        'triggerName': "triggerName_example",
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
        api_response = api_instance.sensors_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->sensors_logs: %s\n" % e)
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
triggerName | TriggerNameSchema | | optional
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

#### TriggerNameSchema

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
**result** | [**SensorLogEntry**](SensorLogEntry.md) |  | [optional] 
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

# **update_sensor**
> IoArgoprojEventsV1alpha1Sensor update_sensor(namespacenamebody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_events_v1alpha1_sensor import IoArgoprojEventsV1alpha1Sensor
from argo_workflows.model.sensor_update_sensor_request import SensorUpdateSensorRequest
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    body = SensorUpdateSensorRequest(
        name="name_example",
        namespace="namespace_example",
        sensor=IoArgoprojEventsV1alpha1Sensor(
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
            spec=IoArgoprojEventsV1alpha1SensorSpec(
                dependencies=[
                    IoArgoprojEventsV1alpha1EventDependency(
                        event_name="event_name_example",
                        event_source_name="event_source_name_example",
                        filters=IoArgoprojEventsV1alpha1EventDependencyFilter(
                            context=IoArgoprojEventsV1alpha1EventContext(
                                datacontenttype="datacontenttype_example",
                                id="id_example",
                                source="source_example",
                                specversion="specversion_example",
                                subject="subject_example",
                                time="1970-01-01T00:00:00.00Z",
                                type="type_example",
                            ),
                            data=[
                                IoArgoprojEventsV1alpha1DataFilter(
                                    comparator="comparator_example",
                                    path="path_example",
                                    template="template_example",
                                    type="type_example",
                                    value=[
                                        "value_example"
                                    ],
                                )
                            ],
                            data_logical_operator="data_logical_operator_example",
                            expr_logical_operator="expr_logical_operator_example",
                            exprs=[
                                IoArgoprojEventsV1alpha1ExprFilter(
                                    expr="expr_example",
                                    fields=[
                                        IoArgoprojEventsV1alpha1PayloadField(
                                            name="name_example",
                                            path="path_example",
                                        )
                                    ],
                                )
                            ],
                            time=IoArgoprojEventsV1alpha1TimeFilter(
                                start="start_example",
                                stop="stop_example",
                            ),
                        ),
                        filters_logical_operator="filters_logical_operator_example",
                        name="name_example",
                        transform=IoArgoprojEventsV1alpha1EventDependencyTransformer(
                            jq="jq_example",
                            script="script_example",
                        ),
                    )
                ],
                error_on_failed_round=True,
                event_bus_name="event_bus_name_example",
                replicas=1,
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
                                    config_map_key_ref=ConfigMapKeySelector(
                                        key="key_example",
                                        name="name_example",
                                        optional=True,
                                    ),
                                    field_ref=ObjectFieldSelector(
                                        api_version="api_version_example",
                                        field_path="field_path_example",
                                    ),
                                    resource_field_ref=ResourceFieldSelector(
                                        container_name="container_name_example",
                                        divisor="divisor_example",
                                        resource="resource_example",
                                    ),
                                    secret_key_ref=SecretKeySelector(
                                        key="key_example",
                                        name="name_example",
                                        optional=True,
                                    ),
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
                        annotations=dict(
                            "key": "key_example",
                        ),
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
                triggers=[
                    IoArgoprojEventsV1alpha1Trigger(
                        parameters=[
                            IoArgoprojEventsV1alpha1TriggerParameter(
                                dest="dest_example",
                                operation="operation_example",
                                src=IoArgoprojEventsV1alpha1TriggerParameterSource(
                                    context_key="context_key_example",
                                    context_template="context_template_example",
                                    data_key="data_key_example",
                                    data_template="data_template_example",
                                    dependency_name="dependency_name_example",
                                    value="value_example",
                                ),
                            )
                        ],
                        policy=IoArgoprojEventsV1alpha1TriggerPolicy(
                            k8s=IoArgoprojEventsV1alpha1K8SResourcePolicy(
                                backoff=IoArgoprojEventsV1alpha1Backoff(
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
                                error_on_backoff_timeout=True,
                                labels=dict(
                                    "key": "key_example",
                                ),
                            ),
                            status=IoArgoprojEventsV1alpha1StatusPolicy(
                                allow=[
                                    1
                                ],
                            ),
                        ),
                        rate_limit=IoArgoprojEventsV1alpha1RateLimit(
                            requests_per_unit=1,
                            unit="unit_example",
                        ),
                        retry_strategy=IoArgoprojEventsV1alpha1Backoff(),
                        template=IoArgoprojEventsV1alpha1TriggerTemplate(
                            argo_workflow=IoArgoprojEventsV1alpha1ArgoWorkflowTrigger(
                                operation="operation_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                source=IoArgoprojEventsV1alpha1ArtifactLocation(
                                    configmap=ConfigMapKeySelector(),
                                    file=IoArgoprojEventsV1alpha1FileArtifact(
                                        path="path_example",
                                    ),
                                    git=IoArgoprojEventsV1alpha1GitArtifact(
                                        branch="branch_example",
                                        clone_directory="clone_directory_example",
                                        creds=IoArgoprojEventsV1alpha1GitCreds(
                                            password=SecretKeySelector(),
                                            username=SecretKeySelector(),
                                        ),
                                        file_path="file_path_example",
                                        ref="ref_example",
                                        remote=IoArgoprojEventsV1alpha1GitRemoteConfig(
                                            name="name_example",
                                            urls=[
                                                "urls_example"
                                            ],
                                        ),
                                        ssh_key_secret=SecretKeySelector(),
                                        tag="tag_example",
                                        url="url_example",
                                    ),
                                    inline="inline_example",
                                    resource=IoArgoprojEventsV1alpha1Resource(
                                        value='YQ==',
                                    ),
                                    s3=IoArgoprojEventsV1alpha1S3Artifact(
                                        access_key=SecretKeySelector(),
                                        bucket=IoArgoprojEventsV1alpha1S3Bucket(
                                            key="key_example",
                                            name="name_example",
                                        ),
                                        endpoint="endpoint_example",
                                        events=[
                                            "events_example"
                                        ],
                                        filter=IoArgoprojEventsV1alpha1S3Filter(
                                            prefix="prefix_example",
                                            suffix="suffix_example",
                                        ),
                                        insecure=True,
                                        metadata=dict(),
                                        region="region_example",
                                        secret_key=SecretKeySelector(),
                                    ),
                                    url=IoArgoprojEventsV1alpha1URLArtifact(
                                        path="path_example",
                                        verify_cert=True,
                                    ),
                                ),
                            ),
                            aws_lambda=IoArgoprojEventsV1alpha1AWSLambdaTrigger(
                                access_key=SecretKeySelector(),
                                function_name="function_name_example",
                                invocation_type="invocation_type_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                region="region_example",
                                role_arn="role_arn_example",
                                secret_key=SecretKeySelector(),
                            ),
                            azure_event_hubs=IoArgoprojEventsV1alpha1AzureEventHubsTrigger(
                                fqdn="fqdn_example",
                                hub_name="hub_name_example",
                                parameters=[],
                                payload=[],
                                shared_access_key=SecretKeySelector(),
                                shared_access_key_name=SecretKeySelector(),
                            ),
                            conditions="conditions_example",
                            conditions_reset=[
                                IoArgoprojEventsV1alpha1ConditionsResetCriteria(
                                    by_time=IoArgoprojEventsV1alpha1ConditionsResetByTime(
                                        cron="cron_example",
                                        timezone="timezone_example",
                                    ),
                                )
                            ],
                            custom=IoArgoprojEventsV1alpha1CustomTrigger(
                                cert_secret=SecretKeySelector(),
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[],
                                secure=True,
                                server_name_override="server_name_override_example",
                                server_url="server_url_example",
                                spec=dict(
                                    "key": "key_example",
                                ),
                            ),
                            http=IoArgoprojEventsV1alpha1HTTPTrigger(
                                basic_auth=IoArgoprojEventsV1alpha1BasicAuth(
                                    password=SecretKeySelector(),
                                    username=SecretKeySelector(),
                                ),
                                headers=dict(
                                    "key": "key_example",
                                ),
                                method="method_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                payload=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                secure_headers=[
                                    IoArgoprojEventsV1alpha1SecureHeader(
                                        name="name_example",
                                        value_from=IoArgoprojEventsV1alpha1ValueFromSource(
                                            config_map_key_ref=ConfigMapKeySelector(),
                                            secret_key_ref=SecretKeySelector(),
                                        ),
                                    )
                                ],
                                timeout="timeout_example",
                                tls=IoArgoprojEventsV1alpha1TLSConfig(
                                    ca_cert_secret=SecretKeySelector(),
                                    client_cert_secret=SecretKeySelector(),
                                    client_key_secret=SecretKeySelector(),
                                    insecure_skip_verify=True,
                                ),
                                url="url_example",
                            ),
                            k8s=IoArgoprojEventsV1alpha1StandardK8STrigger(
                                live_object=True,
                                operation="operation_example",
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                patch_strategy="patch_strategy_example",
                                source=IoArgoprojEventsV1alpha1ArtifactLocation(),
                            ),
                            kafka=IoArgoprojEventsV1alpha1KafkaTrigger(
                                compress=True,
                                flush_frequency=1,
                                parameters=[
                                    IoArgoprojEventsV1alpha1TriggerParameter()
                                ],
                                partition=1,
                                partitioning_key="partitioning_key_example",
                                payload=[],
                                required_acks=1,
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
                            log=IoArgoprojEventsV1alpha1LogTrigger(
                                interval_seconds="interval_seconds_example",
                            ),
                            name="name_example",
                            nats=IoArgoprojEventsV1alpha1NATSTrigger(
                                parameters=[],
                                payload=[],
                                subject="subject_example",
                                tls=IoArgoprojEventsV1alpha1TLSConfig(),
                                url="url_example",
                            ),
                            open_whisk=IoArgoprojEventsV1alpha1OpenWhiskTrigger(
                                action_name="action_name_example",
                                auth_token=SecretKeySelector(),
                                host="host_example",
                                namespace="namespace_example",
                                parameters=[],
                                payload=[],
                                version="version_example",
                            ),
                            pulsar=IoArgoprojEventsV1alpha1PulsarTrigger(
                                auth_token_secret=SecretKeySelector(),
                                connection_backoff=IoArgoprojEventsV1alpha1Backoff(),
                                parameters=[],
                                payload=[],
                                tls=IoArgoprojEventsV1alpha1TLSConfig(),
                                tls_allow_insecure_connection=True,
                                tls_trust_certs_secret=SecretKeySelector(),
                                tls_validate_hostname=True,
                                topic="topic_example",
                                url="url_example",
                            ),
                            slack=IoArgoprojEventsV1alpha1SlackTrigger(
                                channel="channel_example",
                                message="message_example",
                                parameters=[],
                                slack_token=SecretKeySelector(),
                            ),
                        ),
                    )
                ],
            ),
            status=IoArgoprojEventsV1alpha1SensorStatus(
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
    )
    try:
        api_response = api_instance.update_sensor(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->update_sensor: %s\n" % e)
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
[**SensorUpdateSensorRequest**](SensorUpdateSensorRequest.md) |  | 


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
[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md) |  | 


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



[**IoArgoprojEventsV1alpha1Sensor**](IoArgoprojEventsV1alpha1Sensor.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_sensors**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_sensors(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import sensor_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.sensor_sensor_watch_event import SensorSensorWatchEvent
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
    api_instance = sensor_service_api.SensorServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_sensors(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->watch_sensors: %s\n" % e)

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
        api_response = api_instance.watch_sensors(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling SensorServiceApi->watch_sensors: %s\n" % e)
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
**result** | [**SensorSensorWatchEvent**](SensorSensorWatchEvent.md) |  | [optional] 
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

