### README

# Contact Management System

## Overview
This Python application is an object-oriented system for managing an address book. It uses classes to represent contact information, including names and phone numbers, and provides functionality for adding, deleting, and editing contact details.

## Features
- **Class-Based Structure**: Utilizes OOP principles for efficient data management.
- **Core Classes**:
  - `Field`: Base class for all record fields, implementing general field logic.
  - `Name`: Stores contact names. It's a mandatory field in a record.
  - `Phone`: Handles phone number storage with format validation (10 digits).
  - `Record`: Manages contact information, including names and a list of phone numbers.
  - `AddressBook`: Inherits from `UserDict` to store and manage `Record` objects.
- **Functionality**:
  - **AddressBook**:
    - Add records.
    - Find records by name.
    - Delete records by name.
  - **Record**:
    - Add, delete, and edit phone numbers.
    - Search for phone numbers.
- **Data Validation**: Includes validation for phone numbers ensuring correct format.

## Installation
Clone the repository and ensure Python is installed on your system. The application does not require external dependencies.
