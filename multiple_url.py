from flask import Flask ,render_template

app = Flask(__name__)

# homepage
@app.route("/")

#user page
@app.route("/<user>") 
# since we have this user variable here , whenever we load the home page it still needs this var ; so assign it to NONE
# by default set the variable to None

def index(user=None):
    return render_template("user.html" , user=user)


if __name__ == "__main__" :
    app.run(port=8080 , use_reloader=True)

