"""
DESIGN: CURSOR-LIKE AI CODING ASSISTANT

1. USER INPUT

    Example:
    "Add authentication to this FastAPI application."

            ↓

2. AGENT / ORCHESTRATOR

    Responsibilities:
    - Understand task
    - Plan steps
    - Decide which tool to call
    - Read tool result
    - Decide next action
    - Stop when task is complete

            ↓

3. LLM

    Input:
    - User request
    - System instructions
    - Relevant code/context
    - Tool definitions
    - Previous tool results

    LLM outputs either:

        A. Final answer

    OR

        B. Tool call

        Example:
        search_code("authentication")


4. TOOLS

    Core tools:

        search_code()
        → semantic + exact code search

        read_file()
        → read relevant files

        edit_file()
        → modify/create files

        terminal()
        → run shell commands

        run_tests()
        → execute tests

        git_diff()
        → inspect changes

        git_status()
        → inspect repository state

        web_search()
        → external documentation/research

        MCP tools
        → GitHub, Jira, DB, Slack, cloud services, etc.

        Cursor explicitly supports codebase search, file operations, terminal,
        web access and MCP-based external tools.


5. TOOL-CALLING LOOP

    User task
       ↓
    LLM thinks
       ↓
    Choose tool
       ↓
    Tool executes
       ↓
    Tool result
       ↓
    LLM reads result
       ↓
    Choose next tool
       ↓
    ...
       ↓
    Final answer

    Example:

    search_code()
       ↓
    read_file()
       ↓
    edit_file()
       ↓
    run_tests()
       ↓
    test fails
       ↓
    read error
       ↓
    edit_file()
       ↓
    run_tests()
       ↓
    SUCCESS
       ↓
    Final response

    This loop is the CORE of a coding agent.


6. CODEBASE UNDERSTANDING / RETRIEVAL

    Before coding:

        Repository
           ↓
        File discovery
           ↓
        Exact search / grep
           +
        Semantic search
           ↓
        Relevant files/chunks
           ↓
        LLM context

    Cursor uses both exact search and semantic search; its semantic
    search retrieves code segments by meaning rather than only exact
    text matches.

    For large repos:

        Code
        → chunk/index
        → embeddings
        → vector retrieval
        → reranking
        → relevant context


7. CONTEXT ENGINE / CONTEXT WINDOW

Do NOT send the entire repository to the LLM.

    Build context from:
        - User request
        - Relevant files
        - Relevant code chunks
        - Current file
        - Git diff
        - Tool results
        - Conversation history
        - Rules/instructions

    Then:

        Context Manager
           ↓
        Select / compress / prioritize
           ↓
        LLM


8. AGENT TOOLS vs AGENTS

    The core Cursor Agent can itself perform the workflow.

    For complex tasks, use specialized subagents:

    Main Agent
     ├── Research Agent
     ├── Coding Agent
     ├── Test Agent
     └── Review Agent

    Example:

    Main Agent:
    "Implement OAuth."

    Research Agent:
    → inspect auth architecture

    Coding Agent:
    → modify files

    Test Agent:
    → run/create tests

    Review Agent:
    → inspect diff/security

    Cursor also exposes subagents/multi-agent concepts in its current
    agent tooling.


9. TOOL EXECUTION / SAFETY

    Never blindly allow:

        terminal("rm -rf ...")
        database mutations
        credential access
        network calls

        Use:

        Agent
         ↓
        Tool
         ↓
        Permission / policy check
         ↓
        Sandbox / approval
         ↓
        Execute

        Cursor currently provides run modes, sandboxing, allowlists and
        classifier-based review for higher-risk tool calls.


10. MEMORY / STATE

    Maintain:
        Conversation state
        Task state
        Agent state
        Tool results
        Git state

    Example:

    Task:
    "Fix authentication bug"

    State:
    - files discovered
    - hypothesis
    - changes made
    - tests passed
    - remaining work

    For long-running cloud agents:

    Task state
        → checkpoint
        → resume

    Cursor's Cloud Agents run in isolated VMs with the repository,
    dependencies, secrets/network access and test/command execution.


11. AUTOCOMPLETE vs AGENT

    These should be separate paths.

    AUTOCOMPLETE:

        keystroke
         ↓
        small context
         ↓
        fast model
         ↓
        suggestion

    Very latency sensitive.

    AGENT:

        task
         ↓
        planning
         ↓
        retrieval
         ↓
        many tool calls
         ↓
        edit
         ↓
        test
         ↓
        iterate

    Seconds/minutes are acceptable.

    Cursor distinguishes its autocomplete/Tab experience from the
    task-oriented Agent workflow.


12. REALISTIC END-TO-END FLOW

    User:
        "Add Redis caching to get_user()."

                ↓
        Main Agent
                ↓
        search_code("get_user")
                ↓
        read_file(user_service.py)
                ↓
        read_file(config.py)
                ↓
        LLM decides architecture
                ↓
        edit_file(user_service.py)
                ↓
        edit_file(config.py)
                ↓
        terminal("pytest")
                ↓
        FAIL
                ↓
        LLM reads failure
                ↓
        edit_file(...)
                ↓
        terminal("pytest")
                ↓
        PASS
                ↓
        git_diff()
                ↓
        Final response


13. PRODUCTION ARCHITECTURE

                    IDE
                     ↓
                API / Gateway
                     ↓
               Agent Service
                     ↓
               Agent Runtime
              /      |       \
             ↓       ↓        ↓
           LLM    Context    Tools
                    Engine    / \
                      ↓      File Terminal
                 Code Search    MCP
                    ↓
             Vector / Search Index
                    ↓
              Repository / Git

              Async Workers
                    ↓
             Indexing / Tests


14. MOST IMPORTANT DESIGN PRINCIPLE

    The LLM is NOT the whole product.

    Cursor-like system:

        LLM
        +
        Context Engine
        +
        Tool Layer
        +
        Agent Loop
        +
        Execution/Sandbox
        +
        Codebase Retrieval
        +
        State/Checkpoints
        +
        Evaluation


15. Notes:

    I'd build the coding assistant as an agent runtime around an LLM,
    rather than as a simple RAG chatbot. The agent receives a task,
    uses codebase search and semantic retrieval to understand the
    repository, and then iteratively calls tools such as file read,
    file edit, terminal and test execution.

    Each tool result goes back into the LLM context, allowing the model
    to decide the next action until the task is completed. Git provides
    the source-of-truth state, while a context engine selects only the
    relevant repository information instead of sending the whole repo
    to the model.

    For productions I'd separate low-latency autocomplete from the
    agent path, sandbox terminal execution, enforce tool permissions,
    limit agent loops, and evaluate task success, test pass rate,
    latency and cost.

"""