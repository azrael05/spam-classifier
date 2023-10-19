import flask
from flask import Flask, request, render_template
from inference import classify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict")
def inference():
    text = str(request.args.get('text'))
    print(text)
    return classify(text)

if __name__ == "__main__":
    app.run(debug=True)