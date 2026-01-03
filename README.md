# Software Testing Assignment

## 📌 Project Overview
This repository is created as part of a **Software Testing assignment**.  
The objective of this project is to demonstrate:
- Proper project structure
- Manual test case design
- Automated unit testing
- Basic understanding of testing concepts

---

## 🔧 Selected Functionality
**Login System**

The login functionality validates user credentials and returns success or failure based on input.

---

## 📁 Project Structure

software-testing-assignment/
│
├── src/
│ └── login.py # Main login functionality
│
├── tests/
│ ├── unit/
│ │ └── test_login.py # Automated unit test cases
│ └── integration/ # Integration tests (future use)
│
├── docs/
│ └── test_cases.md # Manual test cases
│
└── README.md

---

## 🧪 Test Cases

### Manual Test Cases
- Written in: `docs/test_cases.md`
- Total test cases: **6**
  - ✅ 4 Positive test cases
  - ❌ 2 Negative test cases

### Automated Unit Tests
- Written in: `tests/unit/test_login.py`
- Tool used: **Pytest**
- Covers:
  - Valid login
  - Invalid credentials
  - Empty username/password
  - Edge cases

---

## ▶️ How to Run Automated Tests

1. Install pytest (if not installed):
   ```bash
   pip install pytest
for runing 
pytest
🛠️ Technologies Used

Python

Pytest

Git & GitHub
👤 Author

Ahmad Gul
📄 Notes

This project is created for academic purposes.

The login system uses dummy credentials for testing.

