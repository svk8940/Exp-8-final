from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8083, debug=True)
