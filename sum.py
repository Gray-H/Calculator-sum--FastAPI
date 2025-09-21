from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/sum")
def get_sum(
    n1: float = Query(..., description="First number"),
    n2: float = Query(..., description="Second number")
):
    return {"result": n1 + n2}