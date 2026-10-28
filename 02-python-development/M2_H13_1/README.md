

# Enhanced REST API with Email Verification and Rate Limiting

## Overview
This project enhances the existing REST API by introducing email verification for registered users, limiting the rate of API requests, enabling Cross-Origin Resource Sharing (CORS), and allowing users to update their avatars using Cloudinary. It maintains the security and integrity of the application by storing sensitive data in environment variables and using Docker Compose for deployment.

## Features
- **Email Verification**:
  - Verification process for user email addresses upon registration.
- **Rate Limiting**:
  - Limits on the number of API requests, especially for contact creation.
- **CORS Support**:
  - Enables CORS to allow resource sharing across different origins.
- **Avatar Updates with Cloudinary**:
  - Integration with Cloudinary for user avatar management.
- **Environment Variables**:
  - Sensitive data and configurations stored in `.env` files.
- **Docker Compose**:
  - Simplified deployment and management of services and databases.

## Technical Details
- **Email Verification Mechanism**:
  - Sends verification emails to users and validates them upon response.
- **Request Rate Limiting**:
  - Implements rate limiting on API endpoints to prevent abuse.
- **Cloudinary Integration**:
  - Configures Cloudinary for storing and managing user avatars.
- **CORS Configuration**:
  - Set up CORS in FastAPI to handle requests from different origins.

## Usage
- **User Registration and Verification**:
  - New users receive an email to verify their account.
- **Making API Requests**:
  - Requests to contact endpoints are rate-limited.
- **Updating Avatar**:
  - Users can update their profile picture, which is stored in Cloudinary.
- **Running the Application**:
  - Use Docker Compose to start the application and its services.

## Installation and Dependencies
- Clone the repository.
- Requires Python, FastAPI, SQLAlchemy, PostgreSQL, Pydantic, JWT library, Cloudinary, and Docker Compose.
- Set up environment variables in a `.env` file (API keys, database credentials, etc.).
