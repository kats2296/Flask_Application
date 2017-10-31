from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "METHOD USED %s" % request.method


# by default bacon web page can only handle get method
#so we need to throw a list to be able to use POST method as well

@app.route("/bacon", methods=['GET' , 'POST'])
def bacon():
    if request.method == 'POST' :
        return "YOU ARE USING POST"

    else :
        return "you are probably using GET"


if __name__ == '__main__':
    app.run(port=8080, use_reloader=True)
