
from datetime import date

from app import db
from app.models import Expense


def test_total_expenses_displays_sum_of_all_expenses(client, app):
    with app.app_context():
        expenses = [
            Expense(
                description="Lunch",
                amount=3000,
                category="Food",
                date=date(2026, 10, 9),
            ),
            Expense(
                description="Transport",
                amount=1500,
                category="Transport",
                date=date(2026, 10, 9),
            ),
        ]
        db.session.add_all(expenses)
        db.session.commit()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Total Expenses" in response.data
    assert b"4500.00" in response.data


def test_total_expenses_is_zero_when_no_expenses(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"0.00" in response.data
