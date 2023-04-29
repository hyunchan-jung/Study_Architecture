from fastapi import FastAPI

from components import some_business_logic, startup, shutdown

app = FastAPI()


@app.on_event('startup')
def startup_event():
    startup()


@app.on_event('shutdown')
def shutdown_event():
    shutdown()


@app.get('/')
async def main():
    results = some_business_logic()
    return results
