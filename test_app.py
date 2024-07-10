from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is named 'app'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import  get_db
from models import Todo

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the dependency to use the testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Initialize the test client
client = TestClient(app)

def test_add_todo():
    # Define test data
    test_title = "Test Todo"
    # obj = Todo()
    # Make a POST request to the /add endpoint
    response = client.post(
        "/add",
        data={"title": test_title}
    )

    # Assert the response status code
    assert response.status_code == 200  # HTTP 303 SEE OTHER

# Clean up: remove the dependency override after tests
def cleanup_override():
    app.dependency_overrides.clear()

# Ensure cleanup happens after the test
def teardown_function():
    cleanup_override()
