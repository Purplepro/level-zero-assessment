from fastapi import FastAPI, APIRouter
from fastapi.routing import APIRoute

from typing import Dict, List
from datetime import datetime

from level_zero_assessment.api_schemas import Job

from level_zero_assessment.db_schemas import Job_DB

def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

router = APIRouter()



@app.post("/jobs/", status_code=201, tags=["jobs"])
async def create_job(job: Job):
    """Creates an object of job details

    Returns:
        _type_: Dict
    """
    
    new_job = Job_DB(
        name = job.name,
        email = job.email,
        phone = job.phone,
        type = job.type,
        status = "pending",
    )
    
    return {
        "message": "Job Created!",
        "payload": Dict[new_job]
    }

@app.get("/jobs/", status_code=201, tags=["jobs"])
async def get_jobs(job: List[Job]):
    """Retrieves list of jobs.

    Args:
        job (Job): job details
    """
    return job


job_id = Job.id

@app.get(f"/jobs/{job_id}")
async def read_item(job_id: int):
    return {"job_id": str(job_id),
            "data": Job
            }
    


"""
POST /jobs/{job_id}/retry

The above needs to be an internal retry not a public endpoint retry.

PATCH

"""