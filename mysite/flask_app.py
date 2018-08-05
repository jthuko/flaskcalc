from flask import Flask, render_template, request
from sympy import *
from numpy import *


app = Flask(__name__,template_folder="templates")


@app.route("/", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        expression = request.form.get('expression')
        result = simplify(expression)
        result1 = simplify(expression)
    else:
        result1 = None

    return render_template('index.html', result1=result1)

@app.route("/MathForum")
def mathforum():

    return render_template('MathForum.html')



if __name__ == "__main__":
 app.run()