from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1=10, number2=20)


@app.route('/number1/<string:num1>')
def num1(num1):
    return render_template('index.html', number1=num1, number2=100)

if __name__ == '__main__':
    app.run(debug=True)
