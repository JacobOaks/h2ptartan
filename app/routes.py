from flask import render_template, url_for, g
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

@app.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POST_PER_PAGE'])
    next_url = url_for("search", q=g.search_form.q.data, page=page+1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)
