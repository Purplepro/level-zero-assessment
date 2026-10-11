from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Literal


@dataclass
class Job(BaseModel):
    """Class for creating, updating, and keeping record of jobs.
    """
    id: UUID
    customer_id: UUID
    name: str
    email: str
    phone: str
    status: Literal["pending", "processing", "completed", "failed"]
    type: Literal["crm.update", "invoice.created", "document.process", "customer.follow_up"]
    attempts: int
    created_on: datetime
    updated_on: datetime

    
    