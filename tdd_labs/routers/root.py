"""
Root router for TDD Labs API.

This module provides the root endpoint and basic API information.
It serves as the entry point for API navigation and provides
essential metadata about the service.
"""

from fastapi import APIRouter, status
from pydantic import BaseModel, Field

# Create router instance for root endpoints
router = APIRouter(
    tags=["Root"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error"
        }
    }
)


class RootResponse(BaseModel):
    """
    Root endpoint response model.
    
    Provides basic API information and navigation links for clients
    to discover available endpoints and documentation.
    
    Attributes:
        message: Welcome message for the API
        version: Current API version
        docs_url: URL to OpenAPI documentation
        health_url: URL to health check endpoints
    """
    message: str = Field(
        ...,
        description="Welcome message",
        example="Welcome to TDD Labs API"
    )
    version: str = Field(
        ...,
        description="API version",
        example="0.1.0"
    )
    docs_url: str = Field(
        ...,
        description="OpenAPI documentation URL",
        example="/docs"
    )
    health_url: str = Field(
        ...,
        description="Health check endpoint URL",
        example="/health"
    )


@router.get(
    "/",
    response_model=RootResponse,
    status_code=status.HTTP_200_OK,
    summary="API Root",
    description="Root endpoint providing API information and navigation",
    response_description="API information and navigation links",
    responses={
        status.HTTP_200_OK: {
            "description": "API information and navigation links",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Welcome to TDD Labs API",
                        "version": "0.1.0",
                        "docs_url": "/docs",
                        "health_url": "/health"
                    }
                }
            }
        }
    }
)
async def root():
    """
    API root endpoint.
    
    Provides basic information about the API including:
    - Welcome message
    - API version information
    - Documentation URLs
    - Key endpoint navigation links
    
    This endpoint serves as the main entry point for API discovery
    and provides clients with essential information to navigate
    the available services.
    
    Returns:
        RootResponse: API information and navigation links
    """
    return RootResponse(
        message="Welcome to TDD Labs API",
        version="0.1.0",
        docs_url="/docs",
        health_url="/health"
    )