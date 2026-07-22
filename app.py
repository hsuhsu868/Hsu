from flask import Flask, render_template #import flask and render_template function
app=Flask(__name__) #treate this file as flask app 

@app.route("/content") #route decorator route ta ku a phyit run chin
def index():
    return render_template("content.html") #render_template function ka template folder hma html file ko render chin