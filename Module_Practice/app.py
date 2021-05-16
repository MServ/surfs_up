# Import dependencies
from flask import Flask

# Create a flask instance
app = Flask(__name__)

# Create the root route
@app.route('/')

def hello_world():
    return 'Hello world'

@app.route('/simple')
def simple():
    return 'Here is some temperature and preciptation analysis'