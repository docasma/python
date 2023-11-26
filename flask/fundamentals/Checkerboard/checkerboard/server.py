from flask import Flask, render_template
app = Flask (__name__)


@app.route ('/')
def index ():
    return render_template("index.html", row=8 ,col=8 , color1='red' , color2='black')

@app.route ('/<int:x>')
def index_x (x):
    return render_template("index.html", row=x ,col=4 , color1='red' , color2='black')


@app.route ('/<int:x>/<int:y>')
def index_x_y (x,y):
    return render_template("index.html", row=x ,col=y , color1='red' , color2='black')


@app.route ('/<int:x>/<int:y>/<string:color_one>')
def index_x_y_color_one (x,y,color_one):
    return render_template("index.html", row=x ,col=y , color1=color_one , color2='black')



@app.route ('/<int:x>/<int:y>/<color_one>/<color_two>')
def index_x_y_colors (x,y,color_one, color_two):
    return render_template("index.html", row=x ,col=y , color1=color_one , color2=color_two)




if (__name__)==("__main__"):
    app.run(debug=True)
