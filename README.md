# Algobulls-Internship-Task
# To-do List Application

This is a web-based To-do List application built with Django.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Description

The To-do List application is designed to help users manage their tasks efficiently. It provides features to create, read, update, and delete todo items. Each todo item consists of a title, description, due date, tags, and status. The application is built using Django and Django REST Framework for the backend.

## Features

- Create a new todo item with a title, description, due date, tags, and status.
- Read a single todo item by its ID.
- Read all todo items.
- Update a todo item with new information.
- Delete a todo item.
- Schema Structure contains two main folders , the todo_app folder contains all the Django mains and the todo_app_main folder contains all the implementation of the backend with files like models.py , views.py , serializers.py.
![image](https://github.com/amit429/Algobulls-Task/assets/68067897/ea15f287-01aa-4435-920f-7633c099c344)


## Requirements

- Python (version 3.8)
- Django
- Django REST Framework
- Other dependencies...

## Installation

1. Clone the repository:
    git clone [https://github.com/amit429/Algobulls-Task](https://github.com/amit429/Algobulls-Task.git)


2. Change to the project directory:
    cd Algobulls-Task


3. Create and activate a virtual environment (optional but recommended):
    python -m venv env
    source env/bin/activate # for macOS/Linux
    .\env\Scripts\activate # for Windows


4. Install the required dependencies:
    pip install -r requirements.txt


5. Configure the database settings in the `settings.py` file.

6. Apply the database migrations:
    python manage.py migrate

## Usage

1. Start the development server:
    python manage.py runserver


2. Access the application in your web browser at `http://localhost:8000`.

3. Use the provided REST APIs to interact with the application. Refer to the [API Documentation](#api-documentation) for details on the available endpoints.

## API Documentation

The API documentation provides detailed information on the available endpoints and their usage. It can be found at [API Documentation](/api-docs).

Test the APIs using Postman

1. Create a new Postman Collection and add the following requests:
2. Create a todo item: POST request to /todoList/ with the necessary data.
3. Read one todo item: GET request to /todoList/<id>/.
4. Read all todo items: GET request to /todoList/.
5. Update a todo item: PUT request to /todoList/<id>/ with the updated data.
6. Delete a todo item: DELETE request to /todoList/<id>/.
Test each request and ensure they work as expected.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.




