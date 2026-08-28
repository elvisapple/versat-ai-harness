# FastAPI Standard

- Request and response contracts MUST be explicit and versioned.
- Authentication and authorization MUST be enforced at the correct boundary.
- Blocking work MUST NOT run on the asynchronous request path without deliberate isolation.
- API errors MUST use consistent, non-sensitive responses.
