"""
1. Why Docker? What problem does it solve?

    - Docker provides a consistent, isolated runtime environment by packaging an application
        and its dependencies into an immutable image that can run consistently across environments.
2. Docker Image vs Container:

    Image: A read-only template/package.
        Python + application + dependencies
             ↓
          Image

    Container: A running instance of an image.
        Docker Image
             ↓
         ┌───┴────┐
         ↓        ↓
    Container  Container

    - Image = blueprint.
    - Container = running instance.

3. Why Kubernetes?
    - Docker can run containers, but imagine you have:
        - 100 containers
        - 10 services
        - multiple machines
        - traffic spikes
        - container failures

    - Managing them manually becomes difficult.
    - Kubernetes provides container orchestration.

    - It handles things like:
        - Deployment
        - Scaling
        - Restarting failed containers
        - Service discovery
        - Load balancing
        - Rolling updates
        - Health checks

                  Kubernetes Cluster
                         │
             ┌───────────┼───────────┐
             ↓           ↓           ↓
          Pod/API     Pod/API     Pod/API
             │           │           │
             └───────────┼───────────┘
                         ↓
                       Service
                         ↓
                     Load Balancer

4. Docker vs Kubernetes?

    - Docker is primarily used to build and run containers.
    - Kubernetes orchestrates containers across machines and manages deployment,
        scaling, networking, health checks and recovery.


 5. What happens if a Kubernetes Pod crashes?
    - Kubernetes detects the failed container/pod based on its desired state and attempts to
        restart or replace it depending on the controller managing it.

6. Explain a basic CI/CD pipeline.
    - Code is pushed to Git, Jenkins runs tests and quality/security checks,
        builds a Docker image, pushes it to a container registry, and deploys the image to Kubernetes.
        Deployment should include health checks and preferably a safe rollout/rollback strategy.

7. How would you deploy an ML/AI API?
            Git
             ↓
            Jenkins CI/CD
             ↓
            Docker
             ↓
            Container Registry
             ↓
            Kubernetes
             ↓
            FastAPI inference service
             ↓
            Model

    production flow: Git → Jenkins → Test → Docker Build → Registry → Kubernetes → Production

8. What is Jenkins?
    Jenkins is a CI/CD automation server.
    - Harness is an alternative of Jenkins for CI/CD pipeline.






"""