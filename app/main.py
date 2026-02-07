from app.router.tabungan import tabungan_router
from fastapi import FastAPI
from app.core.setting import settings
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(tabungan_router)

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
