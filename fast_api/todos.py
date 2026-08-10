from fastapi import FastAPI, HTTPException

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

@app.get("/todos")
def get_todos():
    return todos_list

@app.post("/todos")
def create_todos(todo:dict):
    new_todo = {
            "id": len(todos_list)+1,
            "name": todo["name"],
            "completed": False
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


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, todo:dict):

    for existing_todo in todos_list:

        if existing_todo["id"]==todo_id:
            existing_todo["name"] = todo["name"]
            existing_todo["completed"] = todo["completed"]

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )


@app.patch("/todos/{todo_id}")
def patch_todo(todo_id:int, todo:dict):

    for existing_todo in todos_list:

        if existing_todo["id"] ==todo_id:

            if "name" in todo:
                existing_todo["name"] = todo["name"]

            if "completed" in todo:
                existing_todo["completed"] = todo["completed"]

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )