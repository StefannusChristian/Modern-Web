from package import app, db
from flask import render_template, redirect, request, url_for, session
from package.models import User

@app.route('/')
def index():
    if not session.get('username'):
        return redirect(url_for('login'))
    else:
        # Username and role must exist already in session data
        # Therefore, they have logged in
        # Redirect them to their respective role page
        return redirect(url_for(session['role']))
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    # if session.get("username"):
    #     return redirect(url_for('index'))

    title = 'Login'

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # If username or password is empty
        if not (username and password):
            return render_template('login.html')
        
        # If username and password is not empty (proceed)
        user_is_found = User.query.filter_by(username=username).first()

        # If user exists in database
        if user_is_found:
            pass_is_valid = user_is_found.check_password(password)

            if pass_is_valid:
                session['username'] = username
                session['role'] = user_is_found.role

                return redirect(url_for(session['role']))

    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session["username"] = None
    return redirect(url_for('login'))

