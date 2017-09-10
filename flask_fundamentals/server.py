from flask import Flask, render_template, request, redirect,session
app=Flask(__name__)
app.secret_key='ThisisSecret'
@app.route('/')
def index():
    return render_template('index.html', phrase="hello",times=5)
@app.route('/users',methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name']=request.form['name']
    session['email']=request.form['email']
    print request.form
    return redirect('/show')
    '''
    return render_template('index.html')
    '''
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html')

@app.route('/show')
def show_user():
    # return render_template('user.html',name=session['name'],email=session['email']) 
    # we can write it in render_template or we can also write session in html. check user.html
    # I am concern that what a session. A project? A dictionary? A list? How does it store data? For now we are creating a page for user to read to know their own information, but session is also for creator to check their customer's record. If we use Python OOP to create a class and use it under session, is it a good way to store for creator?
    return render_template('user.html')
app.run(debug=True)
'''
how to print request.form and make it show up?
why isn't there any /users page?
How can I see those print?
'''