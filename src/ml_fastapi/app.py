from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import routers
from ml import get_ml_model
from middleware import BearerTokenHeaderForwarding


def setup_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(BearerTokenHeaderForwarding, auth_header_key='Authorization')


def setup_routers(app):
    app.include_router(routers.router)


def setup_ml_model(app):
    app.ml_model = get_ml_model()


def create_app():
    app = FastAPI()

    setup_routers(app)
    setup_middleware(app)
    setup_ml_model(app)

    return app
