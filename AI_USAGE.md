# AI Usage Log

This document tracks all AI interactions during the software engineering baseline assessment to provide an accurate record of AI assistance for reviewer evaluation.

---

## Interaction 1

**Timestamp:**  
2026-10-04 22:05:25 EDT

**My Prompt:**  
whats the python package name for flask?

**Your Contribution:**  
- Explained a concept: Clarified the PyPI package name and import name for Flask.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 2

**Timestamp:**  
2026-10-04 22:38:13 EDT

**My Prompt:**  
with the uv project should I put all of my coding files and folders in the src folder?

**Your Contribution:**  
- Explained a concept: Explained Python standard project conventions for the `src` layout in `uv`, distinguishing between application/package source code (inside `src/<package_name>/`) and root-level files like tests, configs, and documentation.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 3

**Timestamp:**  
2026-10-04 22:42:28 EDT

**My Prompt:**  
whats the command to turn on your venv?

**Your Contribution:**  
- Explained a concept: Provided shell commands to activate a virtual environment on macOS/zsh (`source .venv/bin/activate`) and explained the alternative `uv run` workflow.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 4

**Timestamp:**  
2026-10-05 23:14:25 EDT

**My Prompt:**  
hey when it comes to data classes, since I'm making a json structure I'm thinking the data structure should be rigid but what if I update the schema and by update I mean updating certain fields. Don't do things for me just lead me in the right direction

**Your Contribution:**  
- Explained a concept: Guided on schema evolution strategies (defaults, tolerant reader pattern, versioning), partial updates (separating create vs update schemas), and standard library dataclasses vs Pydantic in FastAPI.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 5

**Timestamp:**  
2026-10-07 23:10:24 EDT

**My Prompt:**  
is using the logging package for api status or response messages the industry standard or are return statements just used for that?

**Your Contribution:**  
- Explained a concept: Clarified the industry standard distinction between HTTP responses (client contract) and application logging (internal observability and diagnostics), explaining how they work together.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 6

**Timestamp:**  
2026-10-07 23:24:07 EDT

**My Prompt:**  
whats the purpoae of an operation_id for an api?

**Your Contribution:**  
- Explained a concept: Explained the purpose of OpenAPI `operationId` (SDK code generation, Swagger/Redoc deep linking, API gateway metrics) and how FastAPI generates and customizes it.

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 7

**Timestamp:**  
2026-10-08 21:55:19 EDT

**My Prompt:**  
I need to check if postgres is installed on my local machine. What is the command?

**Your Contribution:**  
- Provided commands: Provided macOS commands to check for PostgreSQL CLI/server binaries (`psql`, `postgres`), Homebrew packages/services (`brew list`, `brew services`), and port/connection status (`pg_isready`, `lsof`).

**Files Changed:**  
None

**Code Contribution:**  
None

## Interaction 8

**Timestamp:**  
2026-10-08 21:56:08 EDT

**My Prompt:**  
can you log my ai usage as well again looks like you forgot to update the AI_USAGE.md file

**Your Contribution:**  
- Documentation: Updated `AI_USAGE.md` with logs for interactions 4 through 8.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 9

**Timestamp:**  
2026-10-08 22:00:47 EDT

**My Prompt:**  
is there another way you can install postgres without using hombrew and downloading it on you laptop could you spin it up in a docker container?

**Your Contribution:**  
- Explained a concept: Explained running PostgreSQL inside a Docker container / Docker Compose as an alternative to native installation, detailing benefits (isolation, disposability, version management) and usage examples.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 10

**Timestamp:**  
2026-10-11 15:27:11 EDT

**My Prompt:**  
can you help me understand why I'm constantly faced with the error: service "db" refers to undefined volume pgdate: invalid compose project despite having the volum specified int he yml file?

**Your Contribution:**  
- Debugging assistance: Identified a naming discrepancy between the service volume mount (`pgdate`) and top-level volume definition (`pgdata`) in `docker-compose.yml`.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 11

**Timestamp:**  
2026-10-11 15:41:32 EDT

**My Prompt:**  
reading the fast api documentation, i can use sqlalchemy to create the schemas thats then interacting with postgres. Do I have that correct?

**Your Contribution:**  
- Explained a concept: Clarified the architectural roles in FastAPI between SQLAlchemy models (database tables/ORM interacting with PostgreSQL) and Pydantic schemas (data validation and API JSON request/response shapes).

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 12

**Timestamp:**  
2026-10-11 15:50:48 EDT

**My Prompt:**  
whats the meaning of this in sqlalchemy I was thinking we give ids foreign keys. Please help me understand the nuances here because the json schema for pulling the api has a id of uuid:
Mapped[int] = mapped_column(primary_key=True)

**Your Contribution:**  
- Explained a concept: Clarified the distinction between primary keys and foreign keys, explained SQLAlchemy 2.0 `Mapped` and `mapped_column` type annotations, and explained how to map UUID primary keys instead of integer IDs.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 13

**Timestamp:**  
2026-10-11 16:08:08 EDT

**My Prompt:**  
ok and then would the customer id be something like customer_id: Mapped[uuid.UUID] = mapped_column(
ForeignKey
    )?

**Your Contribution:**  
- Explained a concept: Confirmed and explained foreign key syntax in SQLAlchemy 2.0 (`ForeignKey("tablename.column")`), highlighting table name conventions, type matching, nullability, and ORM relationship mappings.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 14

**Timestamp:**  
2026-10-11 16:11:04 EDT

**My Prompt:**  
tell me about a sqlalchemy schema phone number field

**Your Contribution:**  
- Explained a concept: Outlined best practices for phone number fields in SQLAlchemy (storing as strings, character length considerations, E.164 normalization, indexing, and validating at the Pydantic schema layer).

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 15

**Timestamp:**  
2026-10-11 16:29:11 EDT

**My Prompt:**  
for Python Literals, whats the recommended data schema field? Additionally, what is the recommended field for created on and updated on? Lastly whats the recommended field for attempt. I know it should be an incremental integer but do we really need mappedcolumn for it. I was under the impression that mapped columns is for searching

**Your Contribution:**  
- Explained a concept: Clarified mapping Python `Literal` types (using `String` or `Enum`), best practices for `created_at`/`updated_at` timestamps with timezone support and server defaults, recommended modeling for an `attempt` counter, and corrected the misconception that `mapped_column` is for searching rather than defining table columns.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 16

**Timestamp:**  
2026-10-11 17:22:36 EDT

**My Prompt:**  
whats the difference between create_async_engine and create engine in sqlalchemy?

**Your Contribution:**  
- Explained a concept: Clarified the differences between `create_engine` (synchronous/blocking) and `create_async_engine` (asynchronous/non-blocking), including their drivers, session handling, event loop behavior, and usage patterns in FastAPI.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 17

**Timestamp:**  
2026-10-11 17:56:02 EDT

**My Prompt:**  
ok I need to understand how to create the engine, map the postgres url and add it to my yml which will then be recognized by my docker container. I don't want you to do it for me I want to understand the interconnections. SQL alchemy documentation is pretty bad so You can read db_schemas.py

**Your Contribution:**  
- Explained a concept: Clarified the interconnections between Docker Compose configuration, PostgreSQL container environment variables, and the SQLAlchemy connection URL in `create_async_engine`, detailing URL components, host resolution (`localhost` vs container network), and handling special characters in passwords.

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 18

**Timestamp:**  
2026-10-11 18:29:51 EDT

**My Prompt:**  
I'm only asking here because the sqlalchemy documentation really sucks like its hard to find methods I need but whats the sqlalchemy equivalent for session.add or just creating a new record when when a post request is made?

**Your Contribution:**  
- Explained a concept: Clarified that `session.add()` is indeed the SQLAlchemy method for staging new records, explained why `session.add` is synchronous even in async workflows, and walked through the full persistence cycle (`session.add` -> `await session.commit` -> `await session.refresh`).

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 19

**Timestamp:**  
2026-10-11 18:34:40 EDT

**My Prompt:**  
1. Instantiate your model with validated data                                                                                               
    new_job = Job_DB(                                                                                                                             
        name=payload.name,                                                                                                                        
        email=payload.email,                                                                                                                      
        phone=payload.phone,                                                                                                                      
        type=payload.type,                                                                                                                        
        status="pending",                                                                                                                         
        # ...                                                                                                                                     
    )                 


are you pertaining to my db schema or the api schema?

**Your Contribution:**  
- Explained a concept: Clarified that `Job_DB` is the database schema (SQLAlchemy model) being instantiated with values extracted from `payload`, which is the API schema (Pydantic model).

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None

## Interaction 20

**Timestamp:**  
2026-10-11 18:57:52 EDT

**My Prompt:**  
you see this created at connection in main.py? Would I need that if I already have the created_at schema as:

created_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
        )

**Your Contribution:**  
- Explained a concept: Clarified that manually passing `datetime.now()` in the route handler is unnecessary when `server_default=func.now()` is configured on the database model, and pointed out naming inconsistencies (`created_on` vs `created_at`).

**Files Changed:**  
- `AI_USAGE.md`

**Code Contribution:**  
None
