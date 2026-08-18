"""
DATABASE INDEXING:

1. What are the 3 fundamental questions behind Database Indexing?

- Database Indexing = a technique used by a DBMS to locate rows efficiently instead of scanning the entire table.
- The 3 questions are:
  1. How is table data physically stored?

  2. What types of indexes exist?
        - Clustered Index
        - Non-Clustered / Secondary Index

  3. What data structure is used for indexing?
    - B-Tree / B+ Tree


2. How is a table physically stored?

    - The table shown as rows and columns is only a logical representation.
    - DBMS physically stores table data inside Data Pages.

    - Data Page = logical unit of storage managed by the DBMS.
    - Typical size = 8 KB, although this can vary by database engine.

    - An 8 KB page contains:

      ┌─────────────────────────────┐
      │ Header                      │
      │ Metadata                    │
      ├─────────────────────────────┤
      │                             │
      │ Data Records                │
      │ Row 1                       │
      │ Row 2                       │
      │ Row 3                       │
      │ ...                         │
      │                             │
      ├─────────────────────────────┤
      │ Offset Array                │
      └─────────────────────────────┘

    1. Header = contains metadata such as page number, checksum and free space.
    2. Data Records = actual table rows.
    3. Offset Array = pointers indicating where each row starts inside the page.

    - For an 8 KB page:
      - Total = 8192 bytes
          - Header = 96 bytes
          - Data area = 8060 bytes
          - Offset array = 36 bytes


3. How many rows can fit into a Data Page?

    - If one row = 64 bytes:

      Rows per page = 8060 / 64
                    ≈ 125 rows

    - Therefore, approximately 125 rows can fit into one 8 KB page.


4. What is a Data Block?

    - Data Block = physical storage unit used by the underlying OS/storage system for I/O.
    - Data Pages are managed by the DBMS.
    - Data Blocks are managed by the physical storage/OS layer.

    - Data Pages may be physically scattered across storage.

      Data Page 1 → Data Block 1
      Data Page 2 → Data Block 100
      Data Page 3 → Data Block 25

    - Therefore, the DBMS maintains a mapping:

      Data Page ID → Physical Data Block Address


5. What happens when there is NO index?

    Example:

      SELECT * FROM Employee
      WHERE Employee_ID = 35;

    - Full Table Scan = scanning the table row-by-row/page-by-page to find the required record.

      Page 1 → Search
         ↓
      Page 2 → Search
         ↓
      Page 3 → Search
         ↓
        ...
         ↓
      Page N → Search

    - DBMS may need to inspect every page.
    - Worst-case complexity = O(N).
    - N = number of rows being searched.
    - Large tables make this expensive because of disk I/O.


6. How does an index improve search?

    - Index = additional data structure that helps the DBMS quickly locate required data.
    - The DBMS commonly uses a B+ Tree for indexing.

      Without Index:

      Query → Full Table Scan → O(N)

      With B+ Tree:

      Query → B+ Tree → Target → O(log N)

    - B+ Tree keeps the search tree balanced, making search, insertion and deletion approximately O(log N).


7. What is a B-Tree?

    - B-Tree = balanced multi-way search tree used as the foundation for understanding database indexing.

    - M-order B-Tree:
      - Maximum children per node = M
      - Maximum keys per node = M - 1

    - Example: 3-order B-Tree

              [K1 | K2]
              /   |   \
           < K1  K1-K2  >= K2

    - Left pointer → keys smaller than K1.
    - Middle pointer → keys between K1 and K2.
    - Right pointer → keys greater than or equal to K2.


8. What happens when a B-Tree node overflows?

    - Overflow = a node contains more keys than its allowed capacity.

    - Process:

      Insert key
          ↓
      Node becomes full
          ↓
      Insert another key
          ↓
      Overflow
          ↓
      Split node
          ↓
      Promote middle key to parent

    - If the parent also overflows, splitting can propagate upward.
    - If the root splits, a new root is created.


9. What is a B+ Tree?

    - B+ Tree = a balanced tree optimized for database indexing and range searches.

    - Important characteristics:
      - Internal nodes → routing/search information.
      - Leaf nodes → actual indexed values + pointers to data.
      - All leaf nodes are linked.
      - Tree remains balanced.

      Root
        │
        ▼
      Internal Nodes
        │
        ▼
      Leaf → Leaf → Leaf → Leaf
              └──────────────→

    - Linked leaves make sequential/range queries efficient.


10. Why are linked leaf nodes important in a B+ Tree?

    - Range Query = query that retrieves values within a range.

    Example:

      SELECT *
      FROM Employee
      WHERE Employee_ID BETWEEN 10 AND 50;

    - DBMS:
      1. Finds the leaf containing 10.
      2. Follows the linked leaf nodes.
      3. Reads keys until 50.

    - It does not need to repeatedly navigate from the root for every value.


11. What is the difference between B-Tree and B+ Tree?

    - B-Tree:
      - Data/search values can exist in internal and leaf nodes.
      - Leaf nodes do not necessarily form a linked sequence.

    - B+ Tree:
      - Actual indexed values/data references are stored at leaf level.
      - Internal nodes primarily act as routing information.
      - Leaf nodes are linked.
      - Better suited for database range scans.


12. How does a B+ Tree connect to actual table data?

    - Each indexed key in a leaf node has a reference/pointer to where the actual row is stored.

      B+ Tree
          │
          ▼
      Key = 35
          │
          ▼
      Data Page 5
          │
          ▼
      Physical Data Block
          │
          ▼
      Actual Row

    - Therefore:

      Index Key → Leaf → Data Page → Physical Storage → Row


13. What happens when a Data Page becomes full?

    - Page Split = creating a new page and redistributing rows when an existing page cannot accommodate another row.

    Example:

      Maximum rows/page = 3

      Page 1:
      [19 | 25 | 30]    ← FULL

      Insert 17
           ↓
      Page 1 is full
           ↓
      Create Page 2
           ↓
      Redistribute rows

      Page 1: [17 | 19]
      Page 2: [25 | 30]

    - B+ Tree pointers are updated to point to the correct page.
    - The new page is also mapped to its physical storage block.


14. What is a Clustered Index?

    - Clustered Index = index where the table's row storage follows the logical ordering of the index key.

    - Important points:
      - Data is organized according to the clustered key.
      - Only ONE clustered index can exist per table.
      - The lecture describes the Primary Key as receiving the clustered index by default.
      - The page's offset array can maintain the ordered access to rows within the page.

    Example:

      Clustered Key: Employee_ID

      101
      102
      103
      104
      105
       ↓
      Data organized according to Employee_ID


15. Why can there be only one Clustered Index?

    - Because the table's data can have only one physical/clustered ordering at a time.

    - Example:

      If data is clustered by Employee_ID:

      101 → 102 → 103 → 104

      It cannot simultaneously have a different physical ordering such as:

      Alice → Bob → Charlie → David


16. What happens if there is no Primary Key?

    - The DBMS can internally create a hidden sequential/unique identifier.
    - This internal identifier can be used to manage the clustered data layout.


17. Why can changing the Primary/Clustered Key be expensive?

    - Changing the clustering key may require:
      - Rebuilding the existing B+ Tree.
      - Rearranging data pages.
      - Reshuffling rows according to the new ordering.
      - Rewriting large amounts of data.

    - Therefore, changing the clustered key on a massive table can be expensive.


18. What is a Non-Clustered Index?

    - Non-Clustered Index = separate index structure whose ordering does not determine the physical ordering of table rows.

    - Example:

      Employee table
           │
           ├── Clustered Index → Employee_ID
           │
           ├── Non-Clustered → Name
           │
           ├── Non-Clustered → Email
           │
           └── Non-Clustered → Age, City

    - Each non-clustered index has its own B+ Tree.
    - Its leaf nodes point to the clustered key or a Data Page + Row Offset.
    - Multiple non-clustered indexes can exist on one table.


19. Clustered vs Non-Clustered Index

  Clustered Index
  - Determines/controls the ordered organization of table data.
  - Only one per table.
  - Data and index organization are closely connected.

  Non-Clustered Index
  - Separate B+ Tree structure.
  - Does not determine table's physical ordering.
  - Multiple indexes can exist.
  - Leaf nodes point toward the actual row through the clustered key/page location.


20. Why shouldn't we create an index on every column?

    - Indexes improve read/search performance but create write and storage overhead.

    - Storage overhead:
      - Every index requires its own index pages.

    - Insert overhead:
      - New rows must be added to every relevant index.

    - Update overhead:
      - Changes to indexed values require index updates.

    - Delete overhead:
      - Corresponding index entries must be removed.

    - Page split overhead:
      - Data-page splits can occur.
      - Index-page splits can also occur.

    - Therefore:

      More indexes
          ↓
      Faster reads
          +
      More storage
          +
      Slower writes


21. What is the complete flow of an indexed query?

    Example:

      SELECT *
      FROM Employees
      WHERE Employee_ID = 35;

      Query
        ↓
      B+ Tree Root
        ↓
      Internal Nodes
        ↓
      Leaf Node containing 35
        ↓
      Data Page ID
        ↓
      Page → Physical Block mapping
        ↓
      Load Data Page
        ↓
      Offset Array
        ↓
      Exact Row
        ↓
      Return Result

    - Step 1 → Load the required B+ Tree/index page.
    - Step 2 → Traverse the B+ Tree.
    - Step 3 → Reach the leaf containing key 35.
    - Step 4 → Obtain the target Data Page ID.
    - Step 5 → Resolve the Data Page to its physical block.
    - Step 6 → Load that page into memory.
    - Step 7 → Use the Offset Array to locate the exact row.
    - Step 8 → Return the record.


22. Why is the indexed query much faster?

    - Without index:

      Query → Scan many/all pages → Search rows

      Complexity ≈ O(N)

    - With B+ Tree:

      Query → Tree traversal → Target page → Target row

      Complexity ≈ O(log N)

    - The DBMS avoids scanning millions of rows and performs targeted I/O instead.


23. What are the most important terms to remember?

    - Data Page = logical storage unit managed by DBMS.
    - Data Block = physical storage unit handled by OS/storage.
    - Offset Array = pointers used to locate rows inside a page.
    - Index = structure that speeds up data lookup.
    - B-Tree = balanced multi-way search tree.
    - B+ Tree = balanced index tree with data references at leaves and linked leaves.
    - Full Table Scan = scanning the table to find matching rows.
    - Clustered Index = index associated with the ordered organization of table data.
    - Non-Clustered Index = separate index structure independent of table's physical ordering.
    - Page Split = splitting a full page into multiple pages.
    - Range Query = query that retrieves values within a specified range.


24. What is the complete mental model of Database Indexing?

          TABLE
            ↓
          Data Pages
            ↓
          Physical Data Blocks

          B+ Tree
            ↓
          Root
            ↓
          Internal Nodes
            ↓
          Leaf Nodes
            ↓
          Data Page Pointer
            ↓
          Data Page
            ↓
          Offset Array
            ↓
          Exact Row


25. What should I say in an interview if asked "Explain Database Indexing"?

    - Database indexing is a technique used to avoid full table scans and make data retrieval faster.
    - The DBMS stores table data in pages and uses a B+ Tree to index frequently queried columns.
    - The B+ Tree navigates from the root to the appropriate leaf, where the key and reference to the data are found.
    - The DBMS then loads the required data page and locates the exact row.
    - This changes lookup from approximately O(N) scanning to O(log N) tree traversal.
    - Clustered indexes organize table data around the indexed key, while non-clustered indexes maintain separate index structures.
    - The trade-off is that indexes consume storage and increase INSERT/UPDATE/DELETE cost.

"""