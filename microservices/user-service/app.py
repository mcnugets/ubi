from fastapi import FastAPI as fapi

app = fapi()


@app.get('/api')
async def root():
    return {"message": "Hello World"}