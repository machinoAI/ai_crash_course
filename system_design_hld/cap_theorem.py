"""
CAP Theorem: Choose 2 out of three:

    C: Consistency -> High consistency ->> Changes done in main DB must be consistent in its replicas
    A: Availability -> High Availability ->> System must be available to serve the requests.
    P: Partition Tolerance ->> Highly Partition tolerance

    - Imagine a scenario application X is reading data from Y and it's replicas from Z.
    - Any changes in Y must reflect in Z as Y and Z are connected.
    - Application X either can send request to Y or Z , should have same data.

    Trade-Offs:
     ->> CA: High consistency and high availability:
     ->> CP: High consistency and high Partition tolerant
     ->> AP: High availability and high Partition tolerant

     ->> CAP: Not possible

    Partition Tolerance is most important


"""