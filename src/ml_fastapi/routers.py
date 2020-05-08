from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()

@router.get('/')
async def read_root(request: Request):
    return "ML serving with fastapi"


@router.get('api/predict')
async def predict_number(request: Request):
    model = request.app.ml_model
    return model.predict('bla')

