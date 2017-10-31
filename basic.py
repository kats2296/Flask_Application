from flask import Flask

app = Flask(__name__)   

#homepage
@app.route('/')  
def index():
    return 'This is the home page'

#another page named tuna
@app.route('/tuna')
def tuna(): 
    return "Hey there!"

#another page named profile accepting a parameter named username
#use of string variable
@app.route('/profile/<username>') 
def abc(username):
    return "Hey there %s" % username

#use of integer variable
#similar use of variable of any other data type except string
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2> POST ID : %d <h2>" % post_id


if __name__ == "__main__":
    app.run(debug=True) 
