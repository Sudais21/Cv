from flask import Flask, render_template

app = Flask(__name__)

# Route to render the home page
@app.route('/')
def home():
    return render_template('Cv.html')

if __name__ == '__main__':
    app.run()
