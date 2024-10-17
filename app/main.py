from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.api.routes.suppliers_router import router as suppliers_router
from app.api.routes.client_router import router as client_router
from app.api.routes.user_router import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Cambia esto por la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(client_router)
app.include_router(user_router)
app.include_router(suppliers_router)