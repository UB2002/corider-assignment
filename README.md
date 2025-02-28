# User Management API

A simple RESTful API for user management built with Docker.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your system

### Clone the Application
   ```bash
   git clone https://github.com/UB2002/corider-assignment.git
   ```

### Running the Application

1. **Build and Start**:
   ```powershell
   docker-compose up --build
   ```
   * Application runs on http://localhost:5000

2. **View Logs**:
   ```powershell
   docker-compose logs app
   ```

3. **Stop**:
   ```powershell
   docker-compose down
   ```

## API Endpoints

1. **GET /users**:
   * URL: http://localhost:5000/users
   * Method: GET

2. **POST /users**:
   * URL: http://localhost:5000/users
   * Method: POST
   * Body (JSON):
   ```json
   {"name": "John Doe", "email": "john@example.com", "password": "secure123"}
   ```

3. **GET /users/<id>**:
   * URL: http://localhost:5000/users/<id-from-post>
   * Method: GET

4. **PUT /users/<id>**:
   * URL: http://localhost:5000/users/<id>
   * Method: PUT
   * Body (JSON):
   ```json
   {"name": "Jane Doe", "email": "jane@example.com", "password": "newpass456"}
   ```

5. **DELETE /users/<id>**:
   * URL: http://localhost:5000/users/<id>
   * Method: DELETE