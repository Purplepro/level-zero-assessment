# INITIAL_DESIGN.md

## Engineering Baseline Assessment — Job Processing API

**Status:** Initial reasoning / Pre-implementation  
**Purpose:** Document my independent understanding, assumptions, and early design decisions before building the system.

## 1. Understanding the Problem

I am building an API that allows services to submit jobs for asynchronous processing.

The API receives a job request, stores the job, and returns a response. The actual processing happens separately from the initial request.

A job could represent an operation such as:

- `crm.update`
- `invoice.created`
- `document.process`
- `customer.follow_up`

These are examples, not necessarily an exhaustive list of supported job types.

I clarified that the processing operations do not need to interact with real external services. For this assessment, the work can be simulated.

## 2. API Consumers and Assumptions

I am assuming this is an **internal API**, not a publicly exposed API.

Multiple internal services may use it to create and manage jobs.

Because multiple services are submitting jobs, I need to consider how the system identifies each service and determines which jobs belong to it.

### Initial Authentication Idea

I am considering giving each internal service its own bearer token.

My reasoning is that this would allow the API to identify which service is making a request and potentially restrict that service to accessing only its own jobs.

This is an initial design idea, not an implemented or validated authentication solution.

## 3. Data Privacy and PII

Some submitted jobs may contain personally identifiable information (PII), including:

- Email addresses
- Phone numbers
- Names

I initially considered whether the API should support looking up jobs using these fields.

However, I am leaning toward **not supporting lookups by email, phone number, or name**.

My reasoning:

- The API may receive jobs containing sensitive customer information.
- Multiple internal services will be using the same API.
- I want to avoid unnecessary exposure of customer information across services.
- The assessment does not require searching by these fields.

Instead, I am leaning toward using the job ID as the primary identifier for retrieving individual jobs.

I recognize that database indexing and exposing fields as searchable API parameters are different concerns. I have not made a final decision about database indexes.

## 4. Job Ownership and Access Boundaries

I am considering a model where each service can access only the jobs associated with that service.

The initial idea is:

1. Each service has its own bearer token.
2. The API identifies the service making the request.
3. Jobs are associated with the service that submitted them.
4. A service can retrieve or manage only its own jobs.

This is a proposed access model. I have not yet determined the implementation details or edge cases.

## 5. Job Types

I clarified that `crm.update` is an example and not necessarily the only job type the API can accept.

I have not yet decided whether the API will:

- Accept arbitrary valid job-type strings.
- Restrict job types to a predefined set.

That decision remains open.

## 6. Asynchronous Processing

My current understanding is that the API accepts and stores jobs, while a separate processing component performs the actual work.

I have not yet selected the implementation approach for asynchronous processing.

## 7. Design Decisions Still Outstanding

I have not yet worked through or documented my own decisions for:

- Database schema and relationships
- Framework selection
- Worker implementation
- Job state transitions
- Duplicate submission prevention
- Retry behavior
- Pagination and filtering
- Error handling
- Concurrency control
- Logging and observability
- Testing strategy
- Recovery after worker crashes
- Deployment and configuration

These are intentionally unresolved because I want to reason through them independently as part of the assessment.

## 8. AI Assistance Disclosure

This document was organized and formatted by ChatGPT using my prior discussion.

The original reasoning about internal API usage, per-service bearer tokens, service-specific job access, avoiding PII-based lookups, and using job IDs came from me.

ChatGPT clarified the assessment requirements and explained the distinction between database indexing and API searchability.

ChatGPT did not independently design the outstanding components listed above.

## 9. Current Progress

I have clarified several requirements and started considering privacy, authentication, and service isolation.

I have not yet completed my initial architecture or begun implementation.

This document is intended to preserve my early reasoning before further development.