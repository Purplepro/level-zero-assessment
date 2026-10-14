from typing import Annotated
import uuid
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Query

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import ForeignKey, String, DateTime, func, URL
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
import os




DB_PASSWORD= os.environ.get("DB_PASSWORD")
DB_USERNAME= os.environ.get("DB_USERNAME")


class Base(DeclarativeBase):
    pass


class Job_DB(Base):
    __tablename__ = "jobs"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id")
    )
    name: Mapped[str] = mapped_column(String(30))
    phone:  Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(20), nullable=False)
    status: Mapped[str] = mapped_column(String(50))
    type: Mapped[str] = mapped_column(String(50))
    attempts: Mapped[int] = mapped_column(default=0)
    created_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
        )
    updated_on: Mapped[datetime] = mapped_column(                                                                                             
            DateTime(timezone=True),                                                                                                              
            server_default=func.now(),                                                                                                            
            onupdate=func.now()                                       
        )                    
    
postgres_file_name = "jobs_db"


database_url = URL.create(                                                                                                                    
        drivername="postgresql+asyncpg",                                                                                                          
        username="",
        password="",
        host="jobs_db",
        port=5432,
        database="jobs_db",
    )

engine = create_async_engine(
    database_url,
)