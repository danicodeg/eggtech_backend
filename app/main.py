from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.api.routes.client_router import router as client_router
from app.api.routes.user_router import router as user_router

app = FastAPI()
app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(client_router)
app.include_router(user_router)