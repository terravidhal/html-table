from flask import Flask ,render_template , redirect # added redirect!
app = Flask(__name__)    

@app.route('/')
def checkerboard_home():
    return redirect("/users")


@app.route('/users')
def users_infos():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", usersInfos = users)


@app.errorhandler(404) # we specify in parameter here the type of error, here it is 404
def page_not_found(error): # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__=="__main__":   
    app.run(debug=True)    