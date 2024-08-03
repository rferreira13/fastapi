from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Te amo amor da minha vida"}
