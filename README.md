# Python Todo List App

This is a simple Todo List application built with Flask. It allows users to create, read, update, and delete todo items.

## Project Structure

```
python-todo-list
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── styles.css
├── requirements.txt
├── app.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python-todo-list.git
   cd python-todo-list
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the Todo List app.

## Features

- Add new todo items
- View existing todo items
- Update todo items
- Delete todo items

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.