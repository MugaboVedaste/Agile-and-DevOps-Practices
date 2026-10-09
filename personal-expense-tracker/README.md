# Personal Expense Tracker

## 1. Project Overview

The Personal Expense Tracker is a web application developed using Python and Flask to help users record, manage, and monitor their personal expenses. The application uses SQLite to store expense records and provides a simple web interface for managing spending.

This project was developed as part of the **Agile and DevOps in Practice** assessment. Development followed an incremental Agile approach, with requirements organized into a product backlog and delivered across Sprint 0, Sprint 1, and Sprint 2.

## 2. Project Objectives

The main objectives are to:

- Provide a simple way to record and manage personal expenses.
- Allow users to view, edit, and delete expense records.
- Support category-based filtering and calculation of total spending.
- Apply automated testing to improve software quality.
- Use continuous integration to automatically verify code changes.
- Implement application logging and a health-check endpoint.
- Document the development process and provide clear setup instructions.

## 3. Features

- **Add expenses:** Record a description, amount, category, and date.
- **View expenses:** Display recorded expenses.
- **Edit expenses:** Update existing expense information.
- **Delete expenses:** Remove unwanted expense records.
- **Filter by category:** Display expenses belonging to a selected category.
- **Calculate total spending:** Display the total amount spent.
- **Application status:** Check application database connectivity.
- **Application logging:** Record important application events.
- **Automated testing:** Verify functionality using pytest.
- **Continuous integration:** Automatically run tests using GitHub Actions.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web framework |
| Flask-SQLAlchemy | Database integration and ORM |
| SQLite | Database storage |
| HTML | Page structure |
| CSS | User interface styling |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | Continuous integration |
| Python logging | Application event logging |

## 5. Project Structure

```text
Agile-and-DevOps-Practices/
├── .github/
│   └── workflows/
│       └── tests.yml
└── personal-expense-tracker/
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   ├── add_expense.html
    │   │   └── edit_expense.html
    │   └── static/
    │       └── css/
    │           └── style.css
    ├── tests/
    │   ├── conftest.py
    │   ├── test_expenses.py
    │   ├── test_edit_expense.py
    │   ├── test_delete_expense.py
    │   ├── test_total_expenses.py
    │   ├── test_category_filter.py
    │   └── test_status.py
    ├── instance/
    ├── logs/
    ├── run.py
    ├── requirements.txt
    └── README.md
```

The `app` directory contains the application code, templates, static files, and database model. The `tests` directory contains automated tests. The `instance` directory is used for the SQLite database, while the `logs` directory stores application logs when file logging is configured.

The `.github/workflows/tests.yml` file is located at the repository root and defines the automated test workflow.

*Note: The structure above describes the intended project layout. Confirm that all listed files and directories exist in your repository.*

## 6. Installation and Setup

### Prerequisites

- Python 3.12 or another version compatible with the project's dependencies.
- Git, if cloning the repository.

### Step 1: Clone the repository

```bash
git clone https://github.com/MugaboVedaste/Agile-and-DevOps-Practices.git
cd Agile-and-DevOps-Practices/personal-expense-tracker
```

### Step 2: Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 7. Running the Application

From the `personal-expense-tracker` directory, run:

```bash
python run.py
```

Open the application in your browser:

http://127.0.0.1:5000/

The application initializes the required database tables when the Flask application is created.

## 8. Using the Application

1. Open the homepage to view existing expenses and total spending.
2. Add a new expense by entering its description, amount, category, and date.
3. Edit an existing expense when its details need to change.
4. Delete an expense that is no longer required.
5. Select a category to filter the displayed expenses.
6. Review the total spending shown on the homepage.

## 9. Application Status and Logging

### Health-check endpoint

Visit:

http://127.0.0.1:5000/status

When the application and database are functioning correctly, the endpoint should return HTTP `200` with a response similar to:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

If the database health check fails, the endpoint should return an unhealthy response with HTTP `503`.

### Application logging

When configured, application events are written to `logs/app.log`. These may include:

- Application initialization.
- Successful expense creation.
- Successful expense updates.
- Expense deletion requests.
- Database health-check failures.

The configured rotating file handler limits the active log file to approximately 1 MB and retains up to three backup files.

Logs help with troubleshooting and understanding application behavior.

## 10. Automated Testing

The project uses pytest to test application behavior, including expense management, validation, category filtering, total spending, and the status endpoint.

Run the full test suite from the project directory:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest tests/test_status.py -v
```

Automated tests help identify defects and verify that new features do not break existing functionality.

## 11. Continuous Integration with GitHub Actions

GitHub Actions automatically runs the test suite when changes are pushed to the repository or a pull request is opened.

The workflow is located at:

```text
.github/workflows/tests.yml
```

The workflow performs the following steps:

1. Checks out the repository.
2. Sets up the Python environment.
3. Installs project dependencies.
4. Runs the automated tests from the `personal-expense-tracker` directory.

View workflow runs:

https://github.com/MugaboVedaste/Agile-and-DevOps-Practices/actions

Continuous integration helps identify errors early and provides repeatable feedback on code changes.

## 12. Agile Development Process

The project followed an incremental Agile development approach. Work was organized into sprints, with each sprint focused on a defined goal and a manageable set of backlog items.

### Sprint 0: Planning and Setup

**Sprint goal:** Define the project scope, organize the work, and establish the development foundation.

Activities:

- Defined the problem and project objectives.
- Identified the initial application requirements.
- Created and prioritized the product backlog.
- Set up the Git repository and project structure.
- Planned the initial implementation and testing approach.

**Expected outcome:** A clear project scope, an initial backlog, and a foundation for development.

### Sprint 1: Core Application Development

**Sprint goal:** Deliver a working application with core expense-management functionality and automated testing.

Main backlog items:

- Set up the Flask application and database.
- Create the expense data model.
- Implement adding and viewing expenses.
- Implement editing existing expenses.
- Create automated tests for application functionality.
- Configure GitHub Actions to run the tests automatically.

**Outcome:** The application gained its core expense-management functionality, automated tests, and an initial CI workflow.

### Sprint 1 Review

The application and completed features were checked against the sprint goal. Automated tests were used to verify functionality, and GitHub Actions provided a way to run tests after code changes.

### Sprint 1 Retrospective

**What went well:**

- Development was broken into manageable tasks.
- Git helped track changes.
- Automated tests supported verification.
- GitHub Actions introduced automated quality checks.

**Challenges encountered:**

- The test suite initially encountered a missing test-client fixture.
- Implementation and testing errors required debugging.

**Actions for improvement:**

- Verify test fixtures and environment setup early.
- Run tests before pushing changes.
- Include relevant tests when implementing new features.

### Sprint 2: Feature Improvements and Monitoring

**Sprint goal:** Extend expense-management capabilities, improve operational visibility, and document the application.

Main backlog items:

- **Delete Expense:** Allow users to delete expense records.
- **Filter by Category:** Filter displayed expenses by category.
- **Calculate Total Spending:** Display total spending.
- **Logging and Status Page:** Record application events and check database health.
- **Documentation:** Document setup, usage, testing, monitoring, and the Agile development process.

Features were implemented incrementally and verified with relevant automated tests.

### Sprint 2 Review

The review should demonstrate the implemented functionality:

- Adding, viewing, editing, and deleting expenses.
- Filtering expenses by category.
- Calculating total spending.
- Checking the `/status` endpoint.
- Inspecting application logs.
- Running the automated tests.
- Reviewing the GitHub Actions workflow.

**Outcome:** The application was extended with additional expense-management features, monitoring, logging, and documentation.

### Sprint 2 Retrospective

**What went well:**

- Additional features were developed incrementally.
- Automated tests helped verify functionality.
- CI provided repeatable test execution.
- Logging and a status endpoint improved operational visibility.

**Challenges encountered:**

- Missing imports, test setup issues, and integration problems required troubleshooting.
- Additional features increased the importance of regression testing.

**Actions for improvement:**

- Identify integration dependencies earlier.
- Update automated tests whenever functionality changes.
- Keep documentation consistent with the implementation.
- Continue improving error handling and deployment readiness.

*Before submission, update this retrospective to reflect your actual Sprint 2 review and results.*

## 13. Product Backlog Summary

| Backlog item | Sprint |
|---|---|
| Project scope and initial planning | Sprint 0 |
| Repository and project setup | Sprint 0 |
| Flask application and database foundation | Sprint 1 |
| Add and view expenses | Sprint 1 |
| Edit expenses | Sprint 1 |
| Automated tests | Sprint 1 |
| GitHub Actions CI workflow | Sprint 1 |
| Delete expenses | Sprint 2 |
| Filter expenses by category | Sprint 2 |
| Calculate total spending | Sprint 2 |
| Application logging and status page | Sprint 2 |
| Project documentation | Sprint 2 |

## 14. Agile Practices Applied

The project applied the following Agile practices:

- **Product backlog:** Requirements were organized into work items.
- **Sprint planning:** Work was grouped into sprints with defined goals.
- **Incremental delivery:** Features were delivered in manageable stages.
- **Sprint reviews:** Completed functionality was checked against sprint goals.
- **Retrospectives:** Challenges and successes were reviewed to identify improvements.
- **Continuous feedback:** Test results and debugging informed further work.
- **Definition of Done:** Features were expected to meet their requirements, pass relevant tests, and be integrated into the project.

### Definition of Done

A backlog item is considered complete when:

1. The feature meets its stated requirement.
2. Relevant automated tests pass.
3. The change is integrated into the project.
4. Documentation is updated where necessary.
5. The CI workflow passes for the submitted changes.

## 15. Troubleshooting

- **Dependencies are missing:** Activate the virtual environment and run `python -m pip install -r requirements.txt`.
- **The application does not start:** Check the terminal output and confirm the required dependencies are installed.
- **Tests fail:** Run `python -m pytest -v` and inspect the failure messages.
- **The status endpoint reports an unhealthy database:** Check the database configuration and application logs.
- **Changes are not reflected on GitHub:** Confirm that the correct branch was committed and pushed.

## 16. Future Improvements

Possible future enhancements include:

- Monthly and yearly spending reports.
- Budget limits and alerts.
- Expense charts and visualizations.
- User authentication and individual expense accounts.
- Deployment to a production hosting service.

## 17. Author

**Vedaste MUGABO**

Developed as part of the Agile and DevOps in Practice assessment.

GitHub repository: https://github.com/MugaboVedaste/Agile-and-DevOps-Practices