'''
Description of Flask App
This app demonstrates key Flask features:
Home (/)
Renders index.html (a homepage with probably a form for entering marks).
Success (/success/<int:score>)
Shows result message depending on score (>=50 → success, <50 → fail).
Uses Jinja2 templates and passes data as a dictionary ({'score':..., 'res':...}) into result.html.
Fail (/fail/<int:score>)
Simple text message (not templated yet).
==============================================================================================                     
Results (/results/<int:marks>)
Logic-based redirect:
If marks < 50 → redirect to /fail/<marks>
Else → redirect to /success/<marks>
Submit (/submit) [GET & POST]
Handles form submission from index.html.
Expects form fields: science, maths, c, datascience.
Calculates the average of 4 subjects → redirects to /success/<score>.
Templates (index.html, result.html)
Uses Jinja2 to dynamically render messages.
##It’s a Student Result Web App built with Flask + HTML + Jinja2 templates.'''
=============================================================================================
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):  
    res=""
    if score>=50:
        res="YOU MADE IT BUDDY"
    else:
        res="BETTER LUCK NEXT TIME"           
    exp={'score':score,'res':res}    
    return render_template('result.html',result=exp)
                    

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
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))
if __name__=='__main__':

    app.run(debug=True)
