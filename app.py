from flask import Flask,render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/home')
def homepage():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)

@app.route('/status')
def status_update():
    return render_template('status.html')
