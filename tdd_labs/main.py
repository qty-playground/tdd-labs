"""
TDD Labs FastAPI Application.

This is the main FastAPI application for Test-Driven Development experiments.
The application follows a modular router-based architecture where all endpoints
are organized in separate router modules and included in the main app.

Architecture:
- Main app configuration and middleware setup
- Router modules in tdd_labs.routers package
- Each functional area has its own router module
- Comprehensive OpenAPI documentation
"""

from fastapi import FastAPI

from .routers import health, root

# Application metadata
APP_TITLE = "TDD Labs API"
APP_DESCRIPTION = """
TDD Labs API - A comprehensive FastAPI application for Test-Driven Development experiments.

## Features

* **Health Monitoring**: Comprehensive health check endpoints
* **Modular Architecture**: Router-based endpoint organization
* **OpenAPI Documentation**: Auto-generated API documentation
* **Type Safety**: Full Pydantic model validation

## API Organization

All endpoints are organized into logical modules:
- Health checks under `/health`
- Additional modules can be easily added

"""
APP_VERSION = "0.1.0"

# FastAPI application instance with comprehensive configuration
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "TDD Labs Team",
        "url": "https://github.com/your-username/tdd-labs",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


# Include all router modules
app.include_router(
    root.router
)

app.include_router(
    health.router
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)