from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


class AdditionInput(BaseModel):
    number1: int
    number2: int


@app.get("/", response_class=HTMLResponse)
async def read_form():
    return """
        <form method="post">
            <input type="number" name="number1" placeholder="Enter first number">
            <input type="number" name="number2" placeholder="Enter second number">
            <input type="submit" value="Add">
        </form>
    """


@app.post("/")
async def add(number1: int = Form(...), number2: int = Form(...)):
    result = number1 + number2
    return f"Result: {result}"
