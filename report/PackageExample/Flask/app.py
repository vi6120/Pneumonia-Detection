# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
# and assign it to the variable 'app'
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    # Return the string 'Hello, World!'
    # as the response
    return 'Hello, World!'

# Run the Flask application
# if this file is executed directly
if __name__ == '__main__':
    # Start the development server
    app.run()
