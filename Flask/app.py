/* 
Description of Flask App
=============================================================================
This is a simple Flask web application with multiple routes:
/ (home route)
Displays a welcome message introducing yourself.
"Welcome to my World. I'm a recent Graduate Engineer. I live in USA"
================================================================================
/success/<int:score>
Shows a success message if a person has graduated, embedding HTML with <h1>.
/fail/<int:score>
Shows a fail message with the score included in the string.
(Currently has a small typo: "gradute" → should be "graduate").
----------------------------------------------------------------------------------
/results/<int:marks>
Decides whether a user passes or fails:
If marks < 50 → redirect to /fail/<marks>
Else → redirect to /success/<marks>
This is basically a student result simulation app where marks determine success/failure.
======================================================================================
*/
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my World. I'm a recent Graduate Engineer.I live in USA"
    
@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Person is graduated successfully</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed to gradute in just"+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result =""
    if marks<50:
        result = 'fail'
    else:
        result ='success'
    return redirect(url_for(result,score=marks)) 
        

if __name__=='__main__':

    app.run(debug=True)

