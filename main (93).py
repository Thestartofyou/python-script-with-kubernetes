from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()

# List all pods in the default namespace
print("Listing pods:")
pod_list = v1.list_namespaced_pod(namespace="default")
for pod in pod_list.items:
    print(f"- {pod.metadata.name}")

# Create a deployment
print("Creating a deployment...")
deployment = client.V1Deployment()
deployment.metadata = client.V1ObjectMeta(name="my-deployment")
deployment.spec = client.V1DeploymentSpec(
    replicas=3,
    selector=client.V1LabelSelector(
        match_labels={"app": "my-app"}
    ),
    template=client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="my-container",
                    image="nginx:latest"
                )
            ]
        )
    )
)

v1.create_namespaced_deployment(namespace="default", body=deployment)
print("Deployment created successfully!")
