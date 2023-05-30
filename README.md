# Flask Cafe Database

This is a Flask web application that allows you to maintain a database of cafes. You can add new cafes with their corresponding details such as opening and closing times, coffee rating, wifi rating, and power outlet rating.

## Features

- Display a list of all cafes in the database.
- Add new cafes to the database through a web form.

## Setup and Running the App

1. **Clone the repository**

   ```
   git clone https://github.com/yourusername/flask-cafe-database.git
   cd flask-cafe-database
   ```

2. **Setup a virtual environment (optional but recommended)**

   On MacOS/Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   On Windows:
   ```
   py -3 -m venv venv
   venv\Scripts\activate
   ```

3. **Install the requirements**

   ```
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```
   python app.py
   ```

   Then, open your web browser and go to `http://127.0.0.1:5000/` to see the application in action.

## Technologies Used

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - A lightweight WSGI web application framework.
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - Simple integration of Flask and WTForms.
- [Flask-Bootstrap](https://flask-bootstrap.readthedocs.io/en/latest/) - Ready-to-use Bootstrap for Flask.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please replace "yourusername" with your actual GitHub username in the clone command if you want to use this readme as a template for your GitHub project.
