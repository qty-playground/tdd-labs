"""
Health check router for TDD Labs API.

This module provides health check endpoints for monitoring the application status.
All endpoints are grouped under the '/health' prefix with appropriate tags for
OpenAPI documentation.
"""

from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from typing import Literal

# Create router instance with proper configuration
router = APIRouter(
    prefix="/health",
    tags=["Health Check"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error"
        }
    }
)


class HealthResponse(BaseModel):
    """
    Health check response model.
    
    Attributes:
        status: Current health status of the application
        message: Descriptive message about the service state
        version: Application version information
    """
    status: Literal["healthy", "unhealthy"] = Field(
        ...,
        description="Health status indicator",
        example="healthy"
    )
    message: str = Field(
        ...,
        description="Human-readable status message",
        example="All systems operational"
    )
    version: str = Field(
        default="0.1.0",
        description="Application version",
        example="0.1.0"
    )


@router.get(
    "/",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Basic health check",
    description="Returns the basic health status of the application",
    response_description="Health status information",
    responses={
        status.HTTP_200_OK: {
            "description": "Service is healthy",
            "content": {
                "application/json": {
                    "example": {
                        "status": "healthy",
                        "message": "All systems operational",
                        "version": "0.1.0"
                    }
                }
            }
        }
    }
)
async def health_check():
    """
    Perform basic health check.
    
    Returns basic health status information including:
    - Current service status
    - Operational message
    - Application version
    
    Returns:
        HealthResponse: Health status information
    """
    return HealthResponse(
        status="healthy",
        message="All systems operational"
    )


@router.get(
    "/ready",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Readiness probe",
    description="Kubernetes-style readiness probe endpoint",
    response_description="Service readiness status"
)
async def readiness_check():
    """
    Check if the service is ready to accept requests.
    
    This endpoint is designed for Kubernetes readiness probes
    or load balancer health checks.
    
    Returns:
        HealthResponse: Readiness status information
    """
    return HealthResponse(
        status="healthy",
        message="Service ready to accept requests"
    )


@router.get(
    "/live",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Liveness probe",
    description="Kubernetes-style liveness probe endpoint",
    response_description="Service liveness status"
)
async def liveness_check():
    """
    Check if the service is alive and running.
    
    This endpoint is designed for Kubernetes liveness probes
    to determine if the container should be restarted.
    
    Returns:
        HealthResponse: Liveness status information
    """
    return HealthResponse(
        status="healthy",
        message="Service is alive and running"
    )