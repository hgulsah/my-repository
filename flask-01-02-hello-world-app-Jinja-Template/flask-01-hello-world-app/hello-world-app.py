from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello world</h1>"

@app.route('/second')
def second():
    return "<h2>this is the second page</h2>"

@app.route('/third/subthird')
def third():
    return "<h2>this is the sub page of the third page</h2>"

@app.route('/forth/<string:id>')
def forth(id):
    return f"This is page id{id}"

if __name__ == '__main__':
    app.run(debug=False)

