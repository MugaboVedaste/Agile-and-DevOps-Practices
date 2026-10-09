
from datetime import date

from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Expense

main = Blueprint("main", __name__)


@main.route("/")
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template("index.html", expenses=expenses)


@main.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        description = request.form.get("description", "").strip()
        amount_text = request.form.get("amount", "").strip()
        category = request.form.get("category", "").strip()
        expense_date = request.form.get("date", "").strip()

        if not description or not amount_text or not category or not expense_date:
            return render_template(
                "add_expense.html",
                error="Please fill in all fields.",
                today=date.today().isoformat(),
            )

        try:
            amount = float(amount_text)
            parsed_date = date.fromisoformat(expense_date)

            if amount <= 0:
                raise ValueError
        except ValueError:
            return render_template(
                "add_expense.html",
                error="Enter a valid date and an amount greater than zero.",
                today=date.today().isoformat(),
            )

        expense = Expense(
            description=description,
            amount=amount,
            category=category,
            date=parsed_date,
        )

        db.session.add(expense)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template(
        "add_expense.html",
        today=date.today().isoformat(),
    )
