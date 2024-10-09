# Junior Software Developer Hurdle Task - Contact Us Form & FastAPI

This project includes two parts:
1. A **Contact Us Form** built with **HTML**, **CSS**, and **JavaScript**.
2. A **RESTful API** built with **FastAPI** that manages a list of courses with basic CRUD operations.

## 1. Contact Us Form

The **Contact Us Form** is a front-end feature that allows users to submit their name, email, and message.

### Features
- **Form Validation**: Ensures all fields are filled and the email is in the correct format.
- **Success Message**: Displays a success message upon valid submission.
- **Console Logging**: Logs form data (name, email, and message) to the browser console.

### Technologies Used
- **HTML5**: For creating the structure of the form.
- **CSS3**: For styling the form and making it responsive.
- **JavaScript**: For form validation and handling form submission.

### How to Run the Contact Us Form
1. Clone this repository:
   ```bash
   git clone https://github.com/ashilmathew/Ashil-Mathew_JSD_NagaED.git



# Course Management API

This is a simple API built using FastAPI for managing a list of courses. It provides basic CRUD (Create, Read, Update, Delete) operations on course data. The API uses JSON format to send and receive data.

## Features

- **Create** a new course
- **Retrieve** all courses or a specific course by ID
- **Update** a course by ID
- **Delete** a course by ID
- Automatically generated interactive API documentation using Swagger and ReDoc

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/course-management-api.git
    cd course-management-api
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install fastapi uvicorn
    ```

## Running the API

To run the FastAPI application:

1. **Run the server**:

    ```bash
    python main.py
    ```

2. The API will be available at: `http://127.0.0.1:8000/`

3. You can interact with the API using:

    - **Swagger UI**: `http://127.0.0.1:8000/docs`
    - **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Create a Course (POST `/courses/`)

- **Description**: Create a new course.
- **Payload Example**:

    ```json
    {
      "id": 1,
      "title": "Python for Beginners",
      "description": "Learn Python programming from scratch.",
      "duration": "4 weeks"
    }
    ```

### Retrieve All Courses (GET `/courses/`)

- **Description**: Get the list of all available courses.

### Retrieve Course by ID (GET `/courses/{course_id}`)

- **Description**: Retrieve details of a specific course by its ID.

### Update a Course by ID (PUT `/courses/{course_id}`)

- **Description**: Update the information of an existing course.
- **Payload Example**:

    ```json
    {
      "id": 1,
      "title": "Advanced Python",
      "description": "Deep dive into Python advanced concepts.",
      "duration": "6 weeks"
    }
    ```

### Delete a Course by ID (DELETE `/courses/{course_id}`)

- **Description**: Delete a course by its ID.

## Example Usage

To interact with the API, you can use [Postman](https://www.postman.com/) or [curl](https://curl.se/), or simply visit the Swagger UI at `http://127.0.0.1:8000/docs` and try out the available endpoints interactively.

### Example: Creating a Course with `curl`

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/courses/' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "title": "Python for Beginners",
  "description": "Learn Python programming from scratch.",
  "duration": "4 weeks"
}'
