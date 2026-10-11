# Project Architecture

## Python Package and Project Manager
- This project uses UV as its Python package and project manager.

### What it replaces:
- Package Management: Pip and pip-tools
- Environment management: virtualenv
- Python version management: pyenv
- Project and dependency management
- Running isolated tools
- Publishing packages

## Common Commands
```bash
uv init
```
```bash
uv add <package>
```
```bash
uv run <script.py>
```
```bash
uv sync
```
```bash
uv python3 install <version>
```

# How it works

## Job Processing API

- The API accepts tasks that needs to be processed asynchronously. Once the jobs are recieved, the API stores them in a relational database, processes them, and allows another system to check their status. The API Validates the request made to it, creates a persistent job, and rerurns the appropriate response.

## API operations

### POST /jobs

When making a post request, the accepted payload structure example is:

```json
{
    "customer_id": "cus_123",
    "first_name": "Elisa",
    "email": "customer@example.com",
    "type": "crm.update"

}
```

### GET /jobs/{job_id}


### GET  /jobs


### POST /jobs/{job_id}/retry

## Method Examples:

- `invoice.created`
- `customer.follow_up`
- `document.process`
- `crm.update`



# How to Run

- The is an API that allows .....
