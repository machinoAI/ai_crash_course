"""
1. What is Pydantic?

    - Pydantic is a Python library for data validation and data parsing using Python type hints.

    from pydantic import BaseModel

    class Todo(BaseModel):
        name: str
        completed: bool


2. What is Pydantic Response model ?

    - Suppose we define:

        class TodoResponse(BaseModel):
            id: int
            name: str
            completed: bool


        Then
        @app.get("/todos", response_mode = list[TodoResponse])
        def get_todos()
            return todos_list

    - We are telling FastAPI, The response from this api must confront to 'TodoResponse'







"""