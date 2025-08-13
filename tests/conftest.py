import pytest
from fastapi.testclient import TestClient

# from tdd_labs.main import app
# from tdd_labs.repositories.user_repository import InMemoryUserRepository  
# from tdd_labs.repositories.session_repository import InMemorySessionRepository
# from tdd_labs.web.dependencies import get_user_repository, get_session_repository


@pytest.fixture
def test_client():
    """Provide a test client for FastAPI with fresh repositories for each test."""
    # Create a minimal FastAPI app for testing when main app doesn't exist yet
    from tdd_labs.main import app
    
    # Example dependency overrides - uncomment and modify as needed:
    # user_repo = InMemoryUserRepository()
    # session_repo = InMemorySessionRepository()
    
    # Override dependencies with in-memory implementations
    # app.dependency_overrides[get_user_repository] = lambda: user_repo
    # app.dependency_overrides[get_session_repository] = lambda: session_repo
    
    # Add more dependency overrides here as needed:
    # app.dependency_overrides[get_auth_service] = lambda: MockAuthService()
    # app.dependency_overrides[get_email_service] = lambda: MockEmailService()
    
    client = TestClient(app)
    
    yield client
    
    # Clean up dependency overrides after each test
    app.dependency_overrides.clear()


@pytest.fixture
def authenticated_client(test_client):
    """Provide a test client with an authenticated user session."""
    # Example setup - uncomment and modify as needed:
    
    # Create a test user
    # user_data = {
    #     "email": "testuser@example.com", 
    #     "password": "testpassword123"
    # }
    
    # Register the user
    # response = test_client.post("/auth/register", json=user_data)
    # assert response.status_code == 201
    
    # Login to get authentication
    # login_response = test_client.post("/auth/login", json=user_data)
    # assert login_response.status_code == 200
    
    # Extract token or session info
    # auth_data = login_response.json()
    # token = auth_data.get("access_token")
    
    # Add authorization header to client
    # test_client.headers.update({"Authorization": f"Bearer {token}"})
    
    # yield test_client
    
    # Placeholder until authentication is implemented
    pass