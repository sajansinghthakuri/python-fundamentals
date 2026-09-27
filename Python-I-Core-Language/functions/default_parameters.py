# Use a default environment when none is provided.


def deploy(service, environment="production"):
    print(f"Deploying {service} to {environment}")


deploy("api")
deploy("api", "staging")
