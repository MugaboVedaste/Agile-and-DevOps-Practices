
import pytest

from app import create_app, db
from app.models import Expense


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"My Expenses" in response.data


def test_add_expense_page_loads(client):
    response = client.get("/add")

    assert response.status_code == 200
    assert b"Add a New Expense" in response.data


def test_add_valid_expense(client, app):
    response = client.post("/add", data={
        "description": "Lunch",
        "amount": "3000",
        "category": "Food",
        "date": "2026-10-09",
    })

    assert response.status_code == 302

    with app.app_context():
        expense = db.session.execute(
            db.select(Expense).filter_by(description="Lunch")
        ).scalar_one_or_none()

        assert expense is not None
        assert expense.amount == 3000.0
        assert expense.category == "Food"


def test_invalid_amount_is_rejected(client, app):
    response = client.post("/add", data={
        "description": "Lunch",
        "amount": "-100",
        "category": "Food",
        "date": "2026-10-09",
    })

    assert response.status_code == 200
    assert b"valid date and an amount greater than zero" in response.data

    with app.app_context():
        assert db.session.execute(
            db.select(Expense)
        ).scalars().all() == []


def test_saved_expense_appears_on_home_page(client):
    client.post("/add", data={
        "description": "Bus fare",
        "amount": "500",
        "category": "Transport",
        "date": "2026-10-09",
    })

    response = client.get("/")

    assert response.status_code == 200
    assert b"Bus fare" in response.data
    assert b"Transport" in response.data
