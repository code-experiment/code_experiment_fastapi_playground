# TODO:  Possibly think of a fixture that is autouse that creates a user with a todo
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from app.database import Base, get_db
from app.main import app
from app.schemas import TodoCreate, UserCreate
from app.crud import create_user, create_todo


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def credentials():
    return {'username': "test1", 'password': "test1"}


@pytest.fixture
def create_single_user(session: Session, credentials: dict):
    new_user = UserCreate(**credentials)
    return create_user(session, new_user)


@pytest.fixture
def create_single_todo(session: Session, create_single_user):
    new_todo = TodoCreate(title="Buy Milk", complete=False)
    return create_todo(db=session, todo=new_todo, user_id=create_single_user.id)


@pytest.fixture
def login(create_single_user, client, credentials):
    url = '/login'
    payload = {
        "username": credentials.get('username'),
        "password": credentials.get('password')
    }

    response = client.post(url, data=payload)
    return response.json()
