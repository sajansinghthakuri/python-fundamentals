# Demonstrate local and global scope.

environment = "production"


def deploy():
    service = "api"  # Local variable
    print(f"Deploying {service} to {environment}")


deploy()

print(environment)
