# Web Infrastructure Design

## 1. Distributed Web Infrastructure

### Specifics About This Infrastructure

- **Load Balancer Distribution Algorithm:** <br />
    The HAProxy load balancer utilizes the Round Robin distribution algorithm. This algorithm forwards client requests to each server in sequential order, resetting back to the top of the list for subsequent requests.

- **Setup Enabled by the Load Balancer:** <br />
    The HAProxy load balancer facilitates an Active-Passive setup, wherein at least two nodes exist but not all are active simultaneously. The passive (failover) server serves as a backup, ready to assume the primary role if the active server disconnects or fails. This differs from an Active-Active setup where multiple nodes actively run the same service concurrently.

- **Functioning of a Database Primary-Replica (Master-Slave) Cluster:** <br />
    In a Primary-Replica setup, one server acts as the Primary server, handling read/write requests, while the other acts as a Replica, capable only of processing read requests. Data synchronization between the Primary and Replica servers occurs whenever a write operation is executed on the Primary server.

- **Difference Between Primary and Replica Nodes Regarding the Application:** <br />
    The Primary node manages all write operations required by the site, while the Replica node handles read operations, reducing read traffic to the Primary node.

### Issues with this Infrastructure

- **Single Point Of Failure (SPOF):** <br />
    The failure of a server leads to the collapse of the entire network.

- **Security Issues:** <br />
    The infrastructure is vulnerable to malware and interception by third parties due to the absence of a firewall and HTTPS encryption.

- **Lack of Monitoring:** <br />
    Real-time assessment of server health and performance is not possible.
