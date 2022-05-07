# Web application with Identity and Access Management
## Project for Service Oriented Architectures Security (SOASec) course at University of Milan.
This web app lets the user login and see a different image depending on his roles to simulate different privileges.

The project consists of 4 Docker containers: the web application written in Python using the Flask framework, where the user can login via the Keycloak IAM server with OpenID Connect, and Nginx as a reverse proxy which is the endpoint for TLS using Let’s Encrypt certificates. The fourth container is the PostgreSQL database for Keycloak.

It has been deployed to a Linux server following security best practices as much as possible.