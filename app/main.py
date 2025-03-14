from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


from app.api.routes.bill_router import router as bill_router
from app.api.routes.products_router import router as products_router
from app.api.routes.production_router import router as production_router
from app.api.routes.suppliers_router import router as suppliers_router
from app.api.routes.client_router import router as client_router
from app.api.routes.user_router import router as user_router
from app.api.routes.dashboard_router import router as dashboard_router
from app.api.routes.shed_router import router as shed_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  #  la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(client_router)
app.include_router(user_router)
app.include_router(suppliers_router)
app.include_router(production_router)
app.include_router(products_router)
app.include_router(bill_router)
app.include_router(dashboard_router)
app.include_router(shed_router)
