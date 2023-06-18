"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
MEANNESS = [
    'annoying', 'stinky', 'loud']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
    <a href='/hello'> Hi! This is the home page.</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <!-- <form action="/greet">
          What's your name? <input type="text" name="person">
          <select type="select" name="compliment"
            <option value="awesome" > {AWESOMENESS[0]}</option>
            <option value="terrific" > {AWESOMENESS[1]}</option>
            <option value="fantastic" > {AWESOMENESS[2]}</option>
            <option value="neato" > {AWESOMENESS[3]}</option>
            <option value="fantabulous" > {AWESOMENESS[4]}</option>
            <option value="wowza" > {AWESOMENESS[5]}</option>
            <option value="oh-so-not-meh" > {AWESOMENESS[6]}</option>
            <option value="brilliant" > {AWESOMENESS[7]}</option>
            <option value="ducky" > {AWESOMENESS[8]}</option>
            <option value="coolio" > {AWESOMENESS[9]}</option>
            <option value="incredible" > {AWESOMENESS[10]}</option>
            <option value="wonderful" > {AWESOMENESS[11]}</option>
            <option value="smashing" > {AWESOMENESS[12]}</option>
            <option value="lovely" > {AWESOMENESS[13]}</option>
          </select>
          <input type="submit" value="Submit">
        </form> -->
        
        <form action="/diss">
          What's your name? <input type="text" name="person">
          
          <input type="checkbox" name="disses" value={MEANNESS[0]} id="annoying">
          <label for="annoying">Annoying</label>
          
          <input type="checkbox" name="disses" value={MEANNESS[1]} id="stinky">
          <label for="stinky">Stinky</label>
          
          <input type="checkbox" name="disses" value={MEANNESS[2]} id="loud">
          <label for="loud">Loud</label>
          <input type="submit" value="Submit">
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def unfriendly_greeting():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("disses")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
