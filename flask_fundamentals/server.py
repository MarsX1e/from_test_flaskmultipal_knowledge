from flask import Flask, render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', phrase="hello",times=5)
@app.route('/users',methods=['POST'])
def create_user():
    print "Got Post Info"
    name=request.form['name']
    email=request.form['email']
    print request.form
    return redirect('/')
    '''
    return render_template('index.html')
    '''
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html')

@app.route('/show')
def show_user():
    return render_template('user.html',name='Jay',email='kpatel@codingdojo.com')
app.run(debug=True)
'''
how to print request.form and make it show up?
why isn't there any /users page?
How can I see those print?
'''