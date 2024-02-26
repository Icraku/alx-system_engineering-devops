# Designing Web Infrastructure

## 0. Simple_Web_Stack

### Insights Into This Infrastructure

- **Understanding a server.** <br />
    A server, whether hardware or software, facilitates functionalities for other programs or devices known as "clients".

- **Significance of domain names.** <br />
    Domain names aid users in navigating the Internet effectively. They serve as textual representations mapping to numeric IP addresses, enabling access to websites through client software.

- **The DNS record type for `www` in `www.foobar.com`.** <br />
    The DNS record for `www.foobar.com` is typically an A record. This can be verified using the command `dig www.foobar.com`. Note that results may vary, but for this infrastructure, an A record is utilized.
    An Address Mapping record (A Record) stores a hostname alongside its corresponding IPv4 address.

- **Understanding the web server's function.** <br />
    Web servers respond to client requests by serving web pages, operating primarily over the HTTP protocol.

- **Understanding the application server's role.** <br />
    Application servers grant clients access to business logic, enabling the generation of dynamic content essential for specialized functionality in businesses, services, or applications.

- **Understanding the purpose of databases.** <br />
    Databases store organized information that is easily accessible, updatable, and manageable.

- **Communication channels between server and client.** <br />
    Communication between servers and clients occurs over the internet network through the TCP/IP protocol suite.
  
## Issues with this Infrastructure

- **SPOF (Single Point Of Failure):**  
  The infrastructure suffers from a Single Point of Failure. If the server fails, the entire network collapses.

- **Downtime when maintenance is needed:**  
  Productivity is hindered during maintenance periods, such as when deploying new code that requires the web server to be restarted.

- **Inability to scale with high incoming traffic:**  
  Scaling the site for higher loads becomes challenging and unwieldy with this infrastructure.

