from flask import render_template
from app import app
from app.forms import Start

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Start()
    if form.validate_on_submit():
        print("hello")
        return redirect('/forms')
    return render_template("index.html", form=form)

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    return render_template("compare.html")
