from flask import Flask, request, jsonify, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Dummy user credentials (replace this with your actual authentication logic)
valid_credentials = {'username': 'jaloladdin', 'password': 'jalol2007'}
valid_credentials = {'username': 'user', 'password': 'user1234'}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == valid_credentials['username'] and password == valid_credentials['password']:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render_template('error.html', error_message=error_message)
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
