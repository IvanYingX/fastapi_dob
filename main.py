import fastapi
import uvicorn

from api import dob_api
from views import home

api = fastapi.FastAPI()


def configure_routing():
    api.include_router(home.router)
    api.include_router(dob_api.router)


if __name__ == '__main__':
    configure_routing()
    uvicorn.run(api, port=8008, host='127.0.0.1')