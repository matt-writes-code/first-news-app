from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    #Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
    
# Note: “What the heck is if __name__ == '__main__'?” The short answer: It’s just one of the weird things in Python you have to memorize. But it’s worth the brain space because it allows you to run any Python script as a program. Anything indented inside that particular if clause is executed when the script is called from the command line. In this case, that means booting up your web site using Flask’s built-in app.run function.