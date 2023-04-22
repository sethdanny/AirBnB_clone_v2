#!/usr/bin/python3
""" create a flask application """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnh():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ display C followed by a text given in a text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display 'n is a number" if only n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=True)
def numbersandtemplate(n):
    """ display number using template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           m=even_or_odd)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''lists available states'''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''lists available states'''
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """teardown the app , closes current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
