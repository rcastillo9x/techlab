from fastapi import FastAPI

app=FastAPI()

@app.get("/api/check")
def get_check():
    return {"service":"up"}
