from flask import *
from booths import booths_multiply
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('main.html', product = None)

@app.route('/booths', methods=['POST'])
def mult():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    return render_template('main.html', product = booths_multiply(number1, number2))		


if __name__ == '__main__':
   #app.run()
   app.run(host = '0.0.0.0', wdebug = True)