
from datetime import date

from app import db
from app.models import Expense


def add_test_expenses(app):
    with app.app_context():
        expenses = [
            Expense(
                description="Lunch",
                amount=3000,
                category="Food",
                date=date(2026, 10, 9),
            ),
            Expense(
                description="Bus fare",
                amount=1000,
                category="Transport",
                date=date(2026, 10, 9),
            ),
            Expense(
                description="Groceries",
                amount=5000,
                category="Food",
                date=date(2026, 10, 8),
            ),
        ]

        db.session.add_all(expenses)
        db.session.commit()


def test_filter_displays_only_selected_category(client, app):
    add_test_expenses(app)

    response = client.get("/?category=Food")

    assert response.status_code == 200
    assert b"Lunch" in response.data
    assert b"Groceries" in response.data
    assert b"Bus fare" not in response.data


def test_all_categories_displays_all_expenses(client, app):
    add_test_expenses(app)

    response = client.get("/")

    assert response.status_code == 200
    assert b"Lunch" in response.data
    assert b"Bus fare" in response.data
    assert b"Groceries" in response.data


def test_filter_keeps_overall_total_unchanged(client, app):
    add_test_expenses(app)

    response = client.get("/?category=Food")

    assert response.status_code == 200
    assert b"9000.00" in response.data


def test_filter_with_no_matching_expenses(client, app):
    add_test_expenses(app)

    response = client.get("/?category=Health")

    assert response.status_code == 200
    assert b"Lunch" not in response.data
    assert b"Bus fare" not in response.data
    assert b"Groceries" not in response.data
