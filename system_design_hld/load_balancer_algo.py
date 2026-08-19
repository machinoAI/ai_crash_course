"""
1. WHAT IS A LOAD BALANCER?
------------------------------------------------------------

Load Balancer (LB) =
Distributes incoming requests across multiple servers.

Client
  ↓
Load Balancer
  ├──→ Server 1
  ├──→ Server 2
  └──→ Server 3

Goals:
- Prevent one server from being overloaded
- Improve availability
- Scale horizontally
- Route traffic intelligently


============================================================
2. L4 vs L7 LOAD BALANCER
============================================================

L4 = Transport Layer

Routes traffic using:
- IP address
- Port
- TCP/UDP information

Does NOT understand HTTP request details.

Example:
Client → L4 LB → Server


L7 = Application Layer

Understands:
- HTTP/HTTPS
- URL/path
- HTTP headers
- Cookies
- Hostname

Example:

/api/users  → User Service
/api/orders → Order Service


Memory:

L4 → "Where is the connection going?"
L7 → "What is the request asking for?"


============================================================
3. ROUND ROBIN
============================================================

Requests are distributed sequentially.

Servers:
A, B, C

Requests:

R1 → A
R2 → B
R3 → C
R4 → A
R5 → B
R6 → C


Best for:
- Servers with similar capacity
- Simple workloads

Problem:
Does not consider server capacity or current load.


============================================================
4. WEIGHTED ROUND ROBIN
============================================================

Each server gets a weight based on capacity.

Example:

A = weight 3
B = weight 2
C = weight 1

Approximate distribution:

A → 3 requests
B → 2 requests
C → 1 request

Then repeat.

Best for:
Servers with different capacities.

Example:
A = 16 CPU
B = 8 CPU
C = 4 CPU

Give A a higher weight.


============================================================
5. IP HASH
============================================================

Uses client IP to determine the server.

Example:

hash(client_IP) % number_of_servers

Same client IP
      ↓
Usually same server


Example:

User A → Server 2
User A → Server 2
User A → Server 2

Useful when:
- Session affinity/stickiness is required
- Session data is stored locally

Problem:
If servers are added/removed, mappings can change.

Consistent hashing can reduce remapping in some designs.


============================================================
6. LEAST CONNECTION
============================================================

Send request to the server with the fewest active connections.

Example:

Server A → 10 connections
Server B → 4 connections
Server C → 7 connections

New request:

→ Server B


Better than Round Robin when:
Requests have different execution times.


============================================================
7. WEIGHTED LEAST CONNECTION
============================================================

Combines:
- Current connections
- Server capacity/weight

Example:

A = powerful → weight 3
B = medium   → weight 2
C = weak     → weight 1

The LB chooses the server based on
connections relative to capacity.

Best for:
Heterogeneous servers + varying traffic.


============================================================
8. LEAST RESPONSE TIME
============================================================

Routes traffic to the server with the best response time,
usually considering current connections/load as well.

Example:

A → 120 ms
B → 40 ms
C → 80 ms

New request:

→ Server B


Best when:
- Server performance varies
- Latency is important

Problem:
Response time can fluctuate, so LB needs monitoring/recent metrics.


============================================================
9. QUICK COMPARISON
============================================================

Algorithm              Main Idea
------------------------------------------------------------
Round Robin            A → B → C → A

Weighted Round Robin   More traffic to stronger servers

IP Hash                Same client → usually same server

Least Connection      Fewest active connections

Weighted Least Conn.  Fewest connections relative to capacity

Least Response Time   Prefer fastest/lowest-latency server


============================================================
10. WHICH ONE SHOULD I CHOOSE?
============================================================

Similar servers:
→ Round Robin

Different server capacities:
→ Weighted Round Robin

Need session affinity:
→ IP Hash

Long-running / variable requests:
→ Least Connection

Different capacity + variable workload:
→ Weighted Least Connection

Latency-sensitive system:
→ Least Response Time


============================================================
MEMORY TRICK
============================================================

ROUND ROBIN
→ "Take turns"

WEIGHTED ROUND ROBIN
→ "Take turns, but stronger server gets more"

IP HASH
→ "Same client → same server"

LEAST CONNECTION
→ "Go where fewer people are"

WEIGHTED LEAST CONNECTION
→ "Go where load is lowest relative to capacity"

LEAST RESPONSE TIME
→ "Go where response is fastest"


============================================================
30-SECOND:
============================================================

"A load balancer distributes traffic across multiple backend
servers. L4 operates at the transport layer using IP and port,
while L7 understands application-level information such as HTTP
paths and headers.

For routing, Round Robin is suitable for similar servers,
Weighted Round Robin for different capacities, IP Hash when
session affinity is needed, Least Connection for variable-length
requests, Weighted Least Connection for heterogeneous servers,
and Least Response Time for latency-sensitive workloads."

"""