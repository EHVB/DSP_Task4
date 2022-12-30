from flask import Flask, render_template, request
from PIL import Image
from flask import send_file
app = Flask(__name__)

@app.route('/')
def home():
    return (render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)
