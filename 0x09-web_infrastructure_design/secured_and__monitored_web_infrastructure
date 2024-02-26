# Web Infrastructure Design

## 2. Secured and Monitored Web Infrastructure

### Specifics About This Infrastructure

- **Purpose of Firewalls:** <br />
    Firewalls monitor and filter incoming and outgoing network traffic based on established security policies within an organization.

- **Reason for Serving Traffic over HTTPS:** <br />
    HTTPS, an advanced and secure version of the HTTP protocol, incorporates SSL encryption for data protection.
    An SSL certificate authenticates the website's identity and establishes a secure channel for communication between the website and the client.

- **Role of Monitoring:** <br />
    Monitoring tracks the health, metrics, and performance of web servers to ensure optimal functioning.

- **Data Collection Methods for Monitoring Tools:** <br />
    - Web servers are monitored for user load, security, and speed.
    - Application servers are monitored for server availability and responsiveness.
    - Storage servers are monitored for availability, capacity, delay, and data loss.

### Issues with this Infrastructure

- **Terminating SSL at the Load Balancer Level:** <br />
    Terminating SSL at the load balancer exposes traffic between the load balancer and the server, making it susceptible to data theft, session hijacking, and man-in-the-middle (MitM) attacks.

- **Single MySQL Server Accepting Writes:** <br />
    Relying on only one MySQL server capable of accepting writes poses a risk. Some transactions committed on the master may not be available on the slave if the master fails.

- **Uniformity in Server Components:** <br />
    Having servers with identical components (database, web server, and application server) may lead to issues. Sharing server resources (disk usage, memory, CPU) between the web site and database can result in slower performance compared to dedicated resources.
