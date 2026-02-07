import uuid
from sqlmodel import SQLModel, Field

class Tabungan(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4(), primary_key=True)
    nama: str = Field(default=None)
    jumlah: float = Field(default=0.0)
    descripsi: str = Field(default=None)