"""
1. What is FastAPI ?

    - FastAPI is a Python web framework for building HTTP APIs.
    - The FastAPI layer exposes your Python functionality through HTTP.
    - FastAPI automatically converts dictionaries to JSON


    - Example:
        Frontend
           |
           | POST /chat
           ↓
        FastAPI
           |
           ├── Validate request
           ├── Authenticate user
           ├── Call RAG
           ├── Call LLM
           └── Return response


    from fastapi import FastAPI

    app = FastAPI()
    @app.post("/chat")

    def chat(question: str):
        return {
            "answer":"LLM Response"
        }

    Now another application can call: POST /Chat


2. What happens internally ?

    HTTP Request
         ↓
       Uvicorn
         ↓
       FastAPI
         ↓
    Route matching
         ↓
    Validation
         ↓
    Your Python function
         ↓
    Response serialization
         ↓
    HTTP Response


    - FastAPI: The web framework.
        app = FastAPI()

    - Uvicorn: The ASGI server that actually runs your application.
        uvicorn main:app --reload


    - Pydantic: Used primarily for data validation and serialization.

    - Starlette   → underlying web functionality

3. What is ASGI ?
    ASGI: Asynchronous Server Gateway Interface

    - ASGI is a standard interface between an asynchronous Python web server and a Python web application/framework.

    - Think of it like a contract.

                    ASGI interface
                         │
             ┌───────────┴───────────┐
             │                       │
          Uvicorn                FastAPI
          (server)              (application)


    - Uvicorn knows how to communicate with an ASGI application.
    - FastAPI is an ASGI-compatible application.


4. Why do we need ASGI?

    - Imagine, every python web framework have its own protocol,

        Server A ->> Framework A protocol
        Server B ->> Framework B protocol


        It will create a mess.

        Instead, ASGI defines a common interface, so multiple servers can potentially run ASGI applications.


        ASGI Servers Include:
            - Uvicorn
            - Hypercorn
            - Daphne

        And ASGI compatible framework includes:
            - FastAPI
            - Starlette
            - Django

        - Before ASGI, WSGI existed.
        WSGI = Web Server Gateway Interface


4. What exactly does uvicorn do ?

    - When you run uvicorn main:app --reload

    Uvicorn essentially does something like:

        Start server
            ↓
        Listen on port 8000
            ↓
        Receive HTTP request
            ↓
        Convert request into ASGI format
            ↓
        Call FastAPI application
            ↓
        Receive response
            ↓
        Convert response back to HTTP
            ↓
        Send response to client

    - So Uvicorn is not FastAPI.

    -            Your code
                   │
                   ▼
              FastAPI app
              (framework)
                   │
                   │ ASGI
                   ▼
                Uvicorn
                 (server)
                   │
                   ▼
                Network
                   │
                   ▼
                 Client



    - FastAPI is an ASGI application/framework.
    - Uvicorn is the ASGI server.

5. What does main:app mean?

        main
         ↓
        main.py

        app
         ↓
        app = FastAPI()

    - Start Uvicorn and use the app object from main.py as the ASGI application.


6. Mental model to memorize:

                CLIENT
                   │
                   │ HTTP
                   ▼
              ┌─────────┐
              │ Uvicorn │
              │ Server  │
              └────┬────┘
                   │
                  ASGI
                   │
                   ▼
            ┌─────────────┐
            │   FastAPI   │
            │ Application │
            └──────┬──────┘
                   │
                   ▼
             Your Python
                code


7. What is the difference between FastAPI, Uvicorn, and ASGI?

    - FastAPI is the web framework/application, Uvicorn is the ASGI server that runs it,
        and ASGI is the interface/standard that allows the server and application to communicate,
        including support for asynchronous workloads.




"""