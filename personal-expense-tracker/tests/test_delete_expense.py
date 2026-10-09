
from datetime import date

from app import db
from app.models import Expense


def create_expense(app):
    with app.app_context():
        expense = Expense(
            description="Lunch",
            amount=3000,
            category="Food",
            date=date(2026, 10, 9),
        )
        db.session.add(expense)
        db.session.commit()
        expense_id = expense.id

    return expense_id


def test_delete_expense_removes_record(client, app):
    expense_id = create_expense(app)

    response = client.post(f"/delete/{expense_id}")

    assert response.status_code == 302

    with app.app_context():
        expense = db.session.get(Expense, expense_id)
        assert expense is None


def test_deleted_expense_no_longer_appears_on_home_page(client, app):
    expense_id = create_expense(app)

    client.post(f"/delete/{expense_id}")

    response = client.get("/")

    assert response.status_code == 200
    assert b"Lunch" not in response.data


def test_delete_unknown_expense_returns_404(client):
    response = client.post("/delete/999999")

    assert response.status_code == 404


def test_delete_requires_post(client, app):
    expense_id = create_expense(app)

    response = client.get(f"/delete/{expense_id}")

    assert response.status_code == 405

    with app.app_context():
        expense = db.session.get(Expense, expense_id)
        assert expense is not None
