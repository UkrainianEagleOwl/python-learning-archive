# CLI Assistant Bot

## Overview
This Python script is a command-line interface (CLI) assistant bot designed to interact with users through typed commands. It can manage a simple contact book and respond to specific commands, including adding, changing, and displaying contact information.

## Features
- **Command Parsing**: Recognizes and processes user-typed commands.
- **Contact Management**: Stores, modifies, and retrieves contact information.
- **Supported Commands**:
  - `"hello"`: Responds with "How can I help you?"
  - `"add [name] [phone number]"`: Adds a new contact.
  - `"change [name] [new phone number]"`: Updates an existing contact's phone number.
  - `"phone [name]"`: Displays the phone number of a specified contact.
  - `"show all"`: Lists all stored contacts and their phone numbers.
  - `"good bye", "close", "exit"`: Terminates the program with "Good bye!" message.
- **Error Handling**: Utilizes an `input_error` decorator to manage exceptions and provide user-friendly error messages.
- **Case Insensitivity**: Handles commands irrespective of their case (upper/lower).

## Usage
1. Run the script in a Python environment.
2. Type commands following the syntax described in Features.
3. Interact with the bot to manage and retrieve contact information.
4. Use `good bye`, `close`, or `exit` to terminate the session.

## Main Function
- Houses the primary user interaction logic.
- All `print` and `input` operations are performed here.
- Manages the command-response loop.

## Command Handlers
- Separate functions for each command (`add`, `change`, `phone`, `show all`).
- Accept strings as input and return response strings.

## Error Handling
- The `input_error` decorator captures and handles `KeyError`, `ValueError`, and `IndexError`.
- Provides appropriate feedback to the user for erroneous inputs.

## Installation
Clone the repository and ensure Python is installed on your system. No external libraries are required to run the script.
