from flask import Flask
from markupsafe import escape
#from flask import escape
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    mylist = ["apel", "mangga", "jeruk"]
    return render_template('index.html', nama="Andi", umur = 20, list=mylist)

@app.route('/about')
def about():
    return '<h1>About Us </h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

@app.route('/profile',defaults={'route':"home",'nilai':0})
@app.route('/profile/<int:nilai>',defaults={'route':"profile"})
def profile_name(nilai, route):
    if route=="home":
        return '<h1>ProfileHome</h1>'
    elif route=='profile':
        nilai = nilai+100
        return '<h1>Hello %s!</h1>' % nilai
@app.route("/htmlescape/<code>")
def htmlescape(code):
    mystring="~@@@@@@@@%&"
    return escape(mystring)

@app.route('/routetanpaslah')
def routetanpaslah():
    return '<h1>Route Tanpa Slah</h1>'

@app.route('/routedenganslah/')
def routedenganslah():
    return '<h1>Route dengan Slah</h1>'

@app.route("/cobarequest")
def cobarequest():
    if request.method=="GET":
        return request.args.get("nama") + request.args.get("alamat")
    elif request.method=="POST":
        return request.form["nama"]

app.run(debug=True)