from flask import Flask, render_template, session, redirect

app=Flask(__name__)

app.secret_key='abcdef'

@app.route('/')
def root_route():
    if 'count' not in session:
        session['count']=0
    else: session['count']+=1
    return render_template("index.html",number=session['count'])

@app.route('/reset')
def reset():
    session.clear()
    return render_template("index.html")



if __name__ =="__main__":
    app.run(debug=True)