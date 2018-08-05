
from flask import Flask, render_template, request
from sympy import *
from numpy import *

# create app
app = Flask(__name__,template_folder="templates")


@app.route("/", methods=['GET', 'POST'])# Pull user's input
def new():
    if request.method == 'POST':
        expression = request.form.get('expression')
        result = simplify(expression)# Calculate the user input using sympy
        result1 = simplify(expression)
    else:
        result1 = None

    return render_template('index.html', result1=result1)#render results to the user

#run app
if __name__ == "__main__":
 app.run()