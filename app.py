from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello from flask</h1>';


@app.route('/<name>')
def name(name):
	return "Hello {}!".format(name)


if __name__ == '__main__':
	app.run(debug=True)
