from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Tutorial works!"

if __name__ == '__main__':
    app.run(host='::', port=8000)
