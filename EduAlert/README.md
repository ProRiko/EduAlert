# EduAlert Project

EduAlert is a web application designed to manage attendance and provide a dashboard for users. This application is built using Flask, a lightweight WSGI web application framework in Python.

## Project Structure

```
EduAlert
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── attendance.html
│   └── static
│       ├── css
│       └── js
├── instance
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd EduAlert
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

- Update the `instance/config.py` file with your configuration settings, such as database connection details and secret keys.

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will start on `http://127.0.0.1:5000/`.

## Usage

- Navigate to the login page to authenticate.
- Once logged in, you will be directed to the dashboard where you can view your information and manage attendance records.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.