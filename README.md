# Online Finance Managment
> An online Finance Managment web aplication using DRF 
# Description
The Finance Management project is a comprehensive financial management API system designed to help users manage their finances efficiently. The application provides tools for budgeting, expense tracking, and financial reporting.

## 🚀 Features

- **transactions**: Create, edit, and delete transactions (income and expense)
- **budgets**: Create, edit, and delete budgets
- **authentication**: User authentication using jwt and secure access
- **Signup and Login users**: Users can easily signup and login using API endpoints.

## Installation:
**1.Clone the Repo**
```sh
git clone https://github.com/SMojtabaE/CortexSys_Finance_Management.git
cd CortexSys_Finance_Management
```
**2.Setup venv & Install Requirements**
```sh
python -m venv .venv        # Create new venv
.venv\Scripts\Activate.ps1  # Activate venv in windows
pip install -r requirements.txt
```

**3.Migrate Database**
```sh
python manage.py makemigrations
python manage.py migrate
```
**4.Start Server**
```sh
python manage.py runserver
```
# Contributors
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.<br/>

Please star the repo and feel free to make pull requests.