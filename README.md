# Web application with Identity and Access Management
## Project for Service Oriented Architectures Security (SOASec) course at University of Milan.
This web app lets the user login and see a different image depending on his roles to simulate different privileges.

## How it is composed
The project consists of 4 Docker containers:
* A web application written in Python using the Flask framework, running on the gunicorn web server
* A [Keycloak](https://www.keycloak.org/) IAM server to which the user can login with the OpenID Connect protocol via the web application
* The PostgreSQL database for Keycloak
* Nginx as a reverse proxy for both the web app and keycloak, which is also the endpoint for TLS using Let's Encrypt Certificates.


It has been deployed to a Linux server running on a [Linode](https://www.linode.com/) machine following security best practices, the server also scored an A+ on the [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) test.
