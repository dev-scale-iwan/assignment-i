from pydantic import BaseModel

class TabunganRequest(BaseModel):
    nama: str
    jumlah: float | None = None   
    description: str | None = None
    
    
class TabunganResponse(BaseModel):
    id: str
    nama: str
    jumlah: float | None = None
    description: str | None = None

