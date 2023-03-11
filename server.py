from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Speak friend and enter'

@app.route('/')
def index():
    # Clear session to account for checkbox logic persisting in session
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['post'])
def result_post():
    print(request.form)
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['name'] = request.form['name']
    session['comment'] = request.form['comment']
    session['radio'] = request.form['radio']
    if 'goober' in request.form:
        session['goober'] = request.form['goober']
    if 'ready' in request.form:
        session['ready'] = request.form['ready']

    # session['goober'] = request.form['goober']
    # session['ready'] = request.form['ready']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)