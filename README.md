# 💰 Personal Finance & Budgeting System

> A modular Python application for tracking personal finances, managing budgets, analyzing spending patterns, and generating actionable financial insights.


\

---

## 📌 Overview

**Personal Finance & Budgeting System** is a personal finance management application built with Python.

It provides a structured way to record income and expenses, organize transactions into categories, define spending limits, monitor budgets, and understand overall financial health.

The project is being developed incrementally, starting with a lightweight **CLI + JSON architecture** and evolving toward a more complete financial platform with database persistence, analytics, visualization, dashboards, and AI-powered insights.

### Why this project?

Many people track their finances using spreadsheets or scattered notes. This project explores how a software system can turn raw transaction data into useful financial information.

The system focuses on:

* 📥 Reliable transaction management
* 💰 Income and expense tracking
* 🎯 Category-based budgeting
* 📊 Financial analytics
* 📅 Monthly reporting
* 🔎 Transaction search and filtering
* 📈 Spending pattern analysis
* 🤖 Future AI-powered financial insights

---

## ✨ Features

### 💵 Income & Expense Tracking

Record financial transactions with:

* Transaction ID
* Transaction type
* Amount
* Category
* Description
* Date

Example:

```text
┌────┬─────────┬──────────┬──────────────┬──────────────────┐
│ ID │ Type    │ Amount   │ Category     │ Description      │
├────┼─────────┼──────────┼──────────────┼──────────────────┤
│ 01 │ Income  │ ₹30,000  │ Salary       │ September Salary │
│ 02 │ Expense │ ₹500     │ Food         │ Dinner           │
│ 03 │ Expense │ ₹100     │ Transport    │ Bus              │
└────┴─────────┴──────────┴──────────────┴──────────────────┘
```

---

### 🎯 Budget Management

Create category-specific monthly budgets and monitor spending.

```text
Food

Budget     : ₹5,000
Spent      : ₹4,200
Remaining  : ₹800
Utilization: 84%
Status     : Within Budget
```

The system can identify categories where spending exceeds the defined budget.

---

### 📊 Financial Summary

Get a high-level view of your financial position:

```text
╔════════════════════════════════════╗
║        FINANCIAL SUMMARY           ║
╠════════════════════════════════════╣
║ Total Income       ₹30,000         ║
║ Total Expenses      ₹9,500         ║
║ Savings            ₹20,500         ║
║ Savings Rate          68.33%       ║
╚════════════════════════════════════╝
```

---

### 🔎 Transaction Search

Search and filter transactions using different attributes:

* Category
* Transaction type
* Date
* Amount
* Description

---

### 📅 Monthly Analysis

Analyze financial activity for a specific month.

The system can provide:

* Total income
* Total expenses
* Savings
* Savings rate
* Category-wise spending
* Highest spending category
* Transaction count

---

## 🏗️ Architecture

The application follows a modular architecture to keep business logic separated from user interaction and data storage.

```text
                       ┌──────────────┐
                       │     USER     │
                       └──────┬───────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │      main.py     │
                    │   CLI Interface  │
                    └────────┬─────────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
      ┌────────────┐  ┌────────────┐  ┌────────────┐
      │Transaction │  │   Budget   │  │   Report   │
      │   Module   │  │   Module   │  │   Module   │
      └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
            │               │                │
            └───────────────┼────────────────┘
                            ▼
                   ┌─────────────────┐
                   │   Data Layer    │
                   │                 │
                   │   JSON / SQLite │
                   └─────────────────┘
```

### Design Principles

The project aims to follow:

* **Separation of concerns**
* **Modular design**
* **Single responsibility**
* **Reusable functions**
* **Input validation**
* **Error handling**
* **Persistent data storage**

---

## 📂 Project Structure

```text
personal-finance/
│
├── main.py
│
├── transaction.py
├── budget.py
├── report.py
├── utils.py
│
├── data/
│   └── finance.json
│
├── tests/
│   └── ...
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### Module Responsibilities

| Module           | Responsibility                  |
| ---------------- | ------------------------------- |
| `main.py`        | Application entry point and CLI |
| `transaction.py` | Income and expense operations   |
| `budget.py`      | Budget creation and monitoring  |
| `report.py`      | Financial analysis and reports  |
| `utils.py`       | Shared utilities and validation |
| `data/`          | Persistent application data     |
| `tests/`         | Automated tests                 |

---

## 🛠️ Tech Stack

### Current

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python 3   | Core application              |
| JSON       | Local data persistence        |
| `datetime` | Date handling                 |
| `os`       | File and directory management |

### Planned

| Technology | Purpose                 |
| ---------- | ----------------------- |
| SQLite     | Relational data storage |
| Pandas     | Financial data analysis |
| Matplotlib | Data visualization      |
| Streamlit  | Interactive dashboard   |
| LLM API    | AI financial assistant  |

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

* Python 3.10+
* Git

Verify your Python installation:

```bash
python --version
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<username>/personal-finance.git
```

### 2. Navigate to the project

```bash
cd personal-finance
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

---

# 🖥️ Usage

After launching the application, the CLI provides the following options:

```text
╔════════════════════════════════════════╗
║       PERSONAL FINANCE MANAGER         ║
╠════════════════════════════════════════╣
║  1. Add Income                         ║
║  2. Add Expense                        ║
║  3. View Transactions                  ║
║  4. Set Monthly Budget                 ║
║  5. View Budget Status                 ║
║  6. Financial Summary                  ║
║  7. Search Transactions                ║
║  8. Generate Monthly Report            ║
║  9. Exit                               ║
╚════════════════════════════════════════╝
```

---

# 🗃️ Data Model

A transaction is represented as:

```json
{
  "id": 1,
  "type": "expense",
  "amount": 500,
  "category": "Food",
  "description": "Dinner",
  "date": "2026-09-07"
}
```

### Transaction Fields

| Field         | Type    | Description                   |
| ------------- | ------- | ----------------------------- |
| `id`          | Integer | Unique transaction identifier |
| `type`        | String  | `income` or `expense`         |
| `amount`      | Number  | Transaction amount            |
| `category`    | String  | Financial category            |
| `description` | String  | Transaction description       |
| `date`        | String  | Transaction date              |

---

# 🧮 Financial Calculations

### Balance

```text
Balance = Total Income − Total Expenses
```

### Savings

```text
Savings = Total Income − Total Expenses
```

### Savings Rate

```text
Savings Rate = (Savings / Total Income) × 100
```

### Budget Utilization

```text
Budget Utilization = (Category Spending / Category Budget) × 100
```

These calculations form the foundation of the financial analytics layer.

---

# 🧪 Testing

The project will use automated tests to verify core functionality.

Example:

```bash
python -m pytest
```

Testing goals include:

* Transaction creation
* Input validation
* Financial calculations
* Budget calculations
* Search functionality
* Data persistence
* Error handling

---

# 🔐 Data & Privacy

The initial version stores financial data locally.

```text
data/
└── finance.json
```

No financial information is sent to an external service in the basic version.

> **Important:** This project is educational software and does not provide professional financial advice.

---

# 🗺️ Roadmap

The project is being developed in multiple phases.

### Phase 1 — Core CLI

* [x] Project structure
* [ ] Add income
* [ ] Add expenses
* [ ] View transactions
* [ ] Search transactions
* [ ] Calculate balance
* [ ] JSON persistence

### Phase 2 — Budgeting & Analytics

* [ ] Category management
* [ ] Monthly budgets
* [ ] Budget utilization
* [ ] Budget alerts
* [ ] Monthly reports
* [ ] Savings analysis

### Phase 3 — Database

* [ ] SQLite integration
* [ ] Database schema
* [ ] CRUD operations
* [ ] Database migrations
* [ ] Improved data integrity

### Phase 4 — Data Visualization

* [ ] Expense distribution
* [ ] Income vs expenses
* [ ] Monthly spending trends
* [ ] Budget utilization charts
* [ ] Financial dashboards

### Phase 5 — Web Dashboard

* [ ] Interactive dashboard
* [ ] Transaction management UI
* [ ] Filters and search
* [ ] Financial charts
* [ ] Monthly/yearly views

### Phase 6 — AI Financial Assistant

* [ ] Natural-language financial queries
* [ ] Spending pattern analysis
* [ ] Personalized budgeting suggestions
* [ ] Expense anomaly detection
* [ ] AI-generated monthly reports

---

# 🤖 Future AI Capabilities

The long-term goal is to allow users to interact with their financial data using natural language.

For example:

```text
User:
Where did most of my money go this month?

Assistant:
Food was your largest expense category,
accounting for 42% of your total spending.

Your Food expenses increased by 18%
compared with the previous month.
```

Another example:

```text
User:
Am I overspending on entertainment?

Assistant:
Yes.

Entertainment Budget : ₹2,000
Current Spending     : ₹2,700
Budget Utilization   : 135%

You have exceeded your budget by ₹700.
```

The AI layer will operate on the user's existing financial data rather than replacing the underlying transaction and budgeting system.

---

# 🎯 Learning Objectives

This project is designed to develop practical skills in:

### Python

* Functions
* Modules
* Lists & dictionaries
* Exception handling
* File handling
* JSON
* Object-oriented programming

### Software Engineering

* Modular architecture
* Separation of concerns
* Data modeling
* Input validation
* Error handling
* Testing
* Version control

### Data

* Data aggregation
* Filtering
* Financial calculations
* Data analysis
* Visualization

### Backend / Database

* SQL
* SQLite
* CRUD operations
* Database design

### AI/ML

* Data-driven insights
* Natural-language interfaces
* LLM integration
* Financial pattern analysis

---

# 🤝 Contributing

Contributions are welcome.

### Development workflow

```bash
git checkout -b feature/your-feature
```

Make your changes, test them, and commit:

```bash
git add .
git commit -m "Add budget tracking"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

For larger changes, open an issue first to discuss the proposed approach.

---

# 📜 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

# 👨‍💻 Author

**Prabhat Jha**

Computer Science & Engineering Student
Interested in Software Engineering, AI/ML, and Cloud Computing.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

---

> **Built with Python. Designed to turn everyday financial data into meaningful insights.**
