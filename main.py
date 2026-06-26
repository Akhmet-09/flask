from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return '<h1>Welcome to my simple Flask website!</h1><p>It works perfectly.</p>'

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    print('The website is working successfully')