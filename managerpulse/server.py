
import uvicorn

from managerpulse.app import app


def run():
    uvicorn.run(app=app, host="0.0.0.0", port=2000)
