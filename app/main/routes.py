from flask import render_template, url_for, g, redirect, \
            request, current_app
from app import db
from app.main.forms import Start, SearchForm
from app.models import Car
from app.main import bp

@bp.before_request
def before_request():
    g.search_form = SearchForm()

@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = Start()
    if form.validate_on_submit():
        print("hello")
        return redirect(url_for("main.form"))
    return render_template("index.html", form=form)

@bp.route('/forms', methods=['GET', 'POST'])
def forms():
    search = SearchForm()
    if search.validate_on_submit():
        print("ghellfdsafdsa")
        return redirect(url_for("main.search"))
    return render_template("forms.html")

@bp.route('/search')
def search():
    if not g.search_form.validate():
        print("not validated")
    page = request.args.get('page', 1, type=int)
    posts, total = Car.search(g.search_form.q.data, page,
                               20)
    next_url = url_for("search", q=g.search_form.q.data, page=page+1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title='Search', posts=posts,
                           next_url=next_url, prev_url=prev_url)

# @bp.routes('/explore')
# def explore():
#     page = request.args.get('page', 1, type=int)
#     posts = Car.query.order_by(id).paginate(
#         page, current_app.config['POSTS_PER_PAGE'], False)
#     next_url = url('main.explore')

@bp.route('/comparison')
def comparison():
    return render_template("compare.html")
