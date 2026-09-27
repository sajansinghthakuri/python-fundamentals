# Display deployment configuration.


def deploy_config(**config):
    for key, value in config.items():
        print(f"{key}: {value}")


deploy_config(
    service="api",
    environment="production",
    replicas=3,
)
