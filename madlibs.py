"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]




@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """routes user to game"""

    user_input = request.args.get("yesno")
    if user_input == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")



@app.route('/madlib')
def show_madlib():
    """Displays madlib end result."""

    person_input = request.args.get("person")
    color_input = request.args.get("color")
    adj_input = request.args.get("adj")
    noun_input = request.args.get("noun")

    friends_list = request.args.getlist("friends")
    friends_input = ", ".join(friends_list[0:len(friends_list)-1])
    last_friend = friends_list[-1]


    return render_template("madlibs.html", person=person_input,
                            color=color_input, adj=adj_input,
                            noun=noun_input, friends=friends_input,
                            last_friend=last_friend)





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
