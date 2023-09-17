"""Server for portfolio site"""

from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# app route to homepage


@app.route("/")
def view_homepage():
    """Load the homepage."""
# renders homepage.html template
    return render_template('main-page.html')


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
