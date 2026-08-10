from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class todo(BaseModel):
    name: str
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    name: str
    completed: bool




todos_list = [
    {
        "id": 1,
        "name" : "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "name": "Learn Async",
        "completed": False
    },
    {
        "id": 3,
        "name": "Build LLM from Scratch",
        "completed": False
    },
]

app = FastAPI()

@app.get("/todos", response_model = TodoResponse)
def get_todos():
    return todos_list

@app.post("/todos", response_model = TodoResponse)
def create_todos(todo:todo):
    new_todo = {
            "id": len(todos_list)+1,
            "name": todo.name,
            "completed": todo.completed
        }

    todos_list.append(new_todo)

    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):

    for todo in todos_list:
        if todo_id == todos_list["id"]:
            todos_list.remove(todo)
            return {"message":"Todo deleted"}

    raise HTTPException(
        status_code=404,
        detail= "Todo not found"
    )


class TodoUpdate(BaseModel):
    name: str
    completed: bool


@app.put("/todos/{todo_id}", response_model = TodoResponse)
def update_todo(todo_id:int, todo:TodoUpdate):

    for existing_todo in todos_list:

        if existing_todo["id"]==todo_id:
            existing_todo["name"] = TodoUpdate.name
            existing_todo["completed"] = TodoUpdate.completed

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )


class TodoPatch(BaseModel):
    name: str |None = None
    completed: bool| None = None


@app.patch("/todos/{todo_id}", response_model = TodoResponse)
def patch_todo(todo_id:int, todo:TodoPatch):

    for existing_todo in todos_list:

        if existing_todo["id"] ==todo_id:

            if "name" in todo:
                existing_todo["name"] = TodoPatch.name

            if "completed" in todo:
                existing_todo["completed"] = TodoPatch.completed

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )