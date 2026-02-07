from app.models.tabungan import Tabungan
from sqlmodel import select
from app.models.engine import get_db
from app.utils.query_params import standard_query_params
from app.schema.tabungan import TabunganResponse, TabunganRequest
from fastapi import APIRouter, Query, Header, Depends, status, HTTPException

tabungan_router = APIRouter(
    prefix="/api",
    tags=["Tabungan"],
)

@tabungan_router.get("/tabungan", status_code=status.HTTP_200_OK)
def get_tabungan(params = Depends(standard_query_params),db = Depends(get_db)):
    query = select(Tabungan)
    results = db.exec(query)
    tabungans = results.all()
    
    return tabungans