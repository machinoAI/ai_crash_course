"""
============================================================
SYSTEM DESIGN: PARKING LOT
============================================================

1. REQUIREMENTS
------------------------------------------------------------

Functional:
- Vehicle enters parking lot.
- Assign an appropriate parking spot.
- Generate parking ticket.
- Vehicle exits.
- Calculate parking fee.
- Free the parking spot.
- Show available spots.

Vehicle types:
- Bike
- Car
- Truck

Spot types:
- Bike spot
- Car spot
- Truck spot

Non-functional:
- Fast spot allocation
- Concurrent entry/exit handling
- Highly available
- Accurate availability/fee calculation


============================================================
2. HIGH-LEVEL ARCHITECTURE
============================================================

                    Customer
                       ↓
                Entry / Exit Gate
                       ↓
                Parking Service
                 /           \
                ↓             ↓
          Spot Manager     Payment Service
                ↓
           Parking DB
                ↓
          Redis (optional)


============================================================
3. DATA MODEL
------------------------------------------------------------

ParkingLot
- lot_id
- location

Floor
- floor_id
- lot_id

ParkingSpot
- spot_id
- floor_id
- spot_type
- status
- vehicle_id

Vehicle
- vehicle_id
- vehicle_type
- license_plate

Ticket
- ticket_id
- vehicle_id
- spot_id
- entry_time
- exit_time
- status

Payment
- payment_id
- ticket_id
- amount
- status


============================================================
4. VEHICLE → SPOT ALLOCATION
------------------------------------------------------------

Example:

Bike
  ↓
Bike Spot

Car
  ↓
Car Spot

Truck
  ↓
Truck Spot


If requirements allow larger vehicles to use smaller spots:

Truck → Truck only
Car   → Car / larger compatible spot
Bike  → Bike / compatible larger spot

This should be defined as a business rule.


============================================================
5. ENTRY FLOW
------------------------------------------------------------

Vehicle
   ↓
Entry Gate
   ↓
Identify vehicle
   ↓
Find available compatible spot
   ↓
Reserve / lock spot
   ↓
Create ticket
   ↓
Open gate


Example:

Car arrives
   ↓
Spot Manager
   ↓
Find FREE car spot #102
   ↓
Reserve #102
   ↓
Create Ticket T123


============================================================
6. EXIT FLOW
------------------------------------------------------------

Vehicle
   ↓
Exit Gate
   ↓
Find ticket
   ↓
Calculate duration
   ↓
Calculate fee
   ↓
Payment
   ↓
Mark ticket COMPLETED
   ↓
Free parking spot
   ↓
Open gate


============================================================
7. HOW DO WE FIND A FREE SPOT FAST?
------------------------------------------------------------

Naive:

Scan every spot:

Spot 1
Spot 2
Spot 3
...
Spot N

O(N) ❌

Better:

Maintain available spots by type.

Example:

FREE_CAR_SPOTS
→ Priority Queue / Set

FREE_BIKE_SPOTS
→ Set

FREE_TRUCK_SPOTS
→ Set

Then:

Get available car spot
→ O(log N) with priority queue
or approximately O(1) with suitable indexed/set design.


============================================================
8. WHICH SPOT SHOULD WE CHOOSE?
------------------------------------------------------------

Possible strategy:

Choose the lowest numbered available spot.

Example:

Available:
102, 105, 110

Assign:
102

Priority Queue:

       102
      /   \
    105   110

getMin() → 102


Why?

- Predictable
- Easy to implement
- Easy to explain


============================================================
9. CONCURRENCY — VERY IMPORTANT
------------------------------------------------------------

Two cars arrive simultaneously.

Both see:

Spot #102 = FREE

Without concurrency control:

Car A → gets #102
Car B → gets #102

❌ Double allocation


Solution:

Use atomic reservation / database transaction.

Example:

BEGIN

SELECT spot
WHERE spot_id = 102
AND status = 'FREE'
FOR UPDATE;

UPDATE parking_spot
SET status = 'OCCUPIED'
WHERE spot_id = 102;

COMMIT


Now only one transaction can reserve it.


Alternative:

Atomic update:

UPDATE parking_spot
SET status = 'OCCUPIED'
WHERE spot_id = 102
AND status = 'FREE';


If affected_rows = 1:
→ reservation succeeded

If affected_rows = 0:
→ someone else took it


============================================================
10. WHY NOT JUST REDIS?
------------------------------------------------------------

Redis can maintain:

available_spots:car → Set(102,105,110)

But the database should remain the durable source of truth.

A practical design can use:

Redis
→ fast availability lookup

DB
→ authoritative parking state

Need reconciliation if Redis and DB become inconsistent.


============================================================
11. FEE CALCULATION
------------------------------------------------------------

Example pricing:

Car:
₹50 first hour
₹20 each additional hour

Duration = 3 hours

Fee:

₹50 + ₹20 + ₹20
= ₹90


Better design:

PricingStrategy

calculateFee(
    vehicle_type,
    entry_time,
    exit_time
)


This keeps pricing logic separate from parking logic.


============================================================
12. PAYMENT
------------------------------------------------------------

Exit:

Ticket
  ↓
Fee Calculator
  ↓
Payment Service
  ↓
Payment Gateway
  ↓
SUCCESS
  ↓
Free spot


Important:

Do NOT free the spot before confirming successful payment
unless the business explicitly allows unpaid exit.


============================================================
13. SCALING
------------------------------------------------------------

Multiple parking lots:

                Parking Service
                 /     |      \
                ↓      ↓       ↓
              Lot 1  Lot 2   Lot N


Application servers should be stateless.

For very large systems:

- Partition by parking lot
- Cache availability
- Database indexing
- Read replicas for dashboards
- Event stream for analytics


============================================================
14. FAILURE HANDLING
------------------------------------------------------------

Payment fails:
→ Keep ticket active
→ Do not release spot

Spot reservation fails:
→ Try another available spot

Gate service fails:
→ Manual fallback / fail-safe procedure

DB unavailable:
→ Don't make uncertain reservations

Redis unavailable:
→ Fall back to DB if possible


============================================================
15. IMPORTANT APIs
------------------------------------------------------------

POST /parking/entry

Request:
{
  "vehicle_id": "V123",
  "vehicle_type": "CAR"
}

Response:
{
  "ticket_id": "T123",
  "spot_id": "102"
}


GET /parking/availability

Response:
{
  "car": 120,
  "bike": 80,
  "truck": 20
}


POST /parking/exit

Request:
{
  "ticket_id": "T123"
}


============================================================
16. KEY INTERVIEW TRADE-OFFS
------------------------------------------------------------

Simple system:
→ DB + application-level spot selection

High traffic:
→ Redis + DB

High contention:
→ Atomic DB update / row locking

Multiple parking lots:
→ Partition by lot_id

Complex pricing:
→ Strategy pattern / pricing service

Real-time availability:
→ Cache + event updates


Summary:
    I'd design the parking lot as a Spot Management service backed
    by a database. Each parking spot has a type and status, and
    vehicles are assigned to compatible free spots using an indexed
    set or priority queue rather than scanning all spots.

    At entry, I atomically reserve a free spot and create a ticket.
    At exit, I calculate the fee from entry and exit time, process
    payment, mark the ticket completed and release the spot.

    The important concurrency issue is preventing two vehicles from
    getting the same spot, so I'd use an atomic DB update or row-level
    locking. For large systems, I'd use Redis for fast availability
    lookups while keeping the database as the source of truth.

"""