from fastapi import FastAPI

from components import some_business_logic

app = FastAPI()


@app.get('/api/v1/call')
async def main():
    results = some_business_logic()
    return results
