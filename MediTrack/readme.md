# MediTrack – Health & Medicine Management System

## 1. Introduction

MediTrack is a simple Python and MySQL based Health & Medicine Management System.

The project helps users manage their medicines and basic health information through a command-line interface.

## 2. Objectives

- Store user registration and login details.
- Store medicines for individual users.
- View and search medicines.
- Update and delete medicine records.
- Mark medicines as taken.
- Calculate BMI.
- Provide general health tips.
- Generate a basic health and medicine report.

## 3. Technologies Used

- Python 3
- MySQL
- MySQL Connector/Python
- Visual Studio Code

## 4. Main Features

### User Registration & Login
Users can create an account and securely access their own MediTrack data.

### Medicine Management
Users can add, view, search, update and delete their medicines.

### Medicine Status
Users can mark medicines as taken and check their current medicine status.

### BMI Calculator
The system calculates BMI using the user's height and weight.

### Health Tips
The system provides basic general health and wellness information.

### Reports
The system generates a summary of the user's medicines and their status.

## 5. Database

MediTrack uses MySQL for storing data.

Main tables:

- `users`
- `medicines`
- `bmi_records`

The `medicines` table is linked to a username so that users can access their own medicine records.

## 6. Project Files

```text
MediTrack/
│
├── main.py
├── database.py
├── database.sql
├── login.py
├── medicine.py
├── bmi.py
├── health.py
├── reports.py
├── requirements.txt
└── README.md
