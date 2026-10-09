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


def test_edit_page_displays_existing_expense(client, app):
    expense_id = create_expense(app)

    response = client.get(f"/edit/{expense_id}")

    assert response.status_code == 200
    assert b"Lunch" in response.data
    assert b"3000" in response.data


def test_edit_expense_updates_existing_record(client, app):
    expense_id = create_expense(app)

    response = client.post(
        f"/edit/{expense_id}",
        data={
            "description": "Dinner",
            "amount": "4500",
            "category": "Food",
            "date": "2026-10-09",
        },
    )

    assert response.status_code == 302

    with app.app_context():
        expense = db.session.get(Expense, expense_id)

        assert expense.description == "Dinner"
        assert expense.amount == 4500
        assert expense.category == "Food"

        # Editing should not create a second record.
        assert db.session.execute(
            db.select(db.func.count()).select_from(Expense)
        ).scalar_one() == 1


def test_edit_rejects_invalid_amount(client, app):
    expense_id = create_expense(app)

    response = client.post(
        f"/edit/{expense_id}",
        data={
            "description": "Dinner",
            "amount": "-10",
            "category": "Food",
            "date": "2026-10-09",
        },
    )

    assert response.status_code == 200
    assert b"amount greater than zero" in response.data

    with app.app_context():
        expense = db.session.get(Expense, expense_id)
        assert expense.description == "Lunch"
        assert expense.amount == 3000


def test_edit_unknown_expense_returns_404(client):
    response = client.get("/edit/999999")

    assert response.status_code == 404