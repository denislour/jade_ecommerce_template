from flask import Flask, render_template
from data import data

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.context_processor
def inject_page():
    return dict(
        page="ahihi",
        promo=data.promo,
        advantages=data.advantages,
        navbarMenu=data.navbarMenu,
        shopInfo=data.shopInfo,
        toolbarMenu=data.toolbarMenu,
        socials=data.socials,
        footerMenuLeft=data.footerMenuLeft,
        footerMenuRight=data.footerMenuRight,
        categories=data.categories,
        products=data.products,
        brands=data.brands,
        articles=data.articles,
        news=data.news
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.jade'), 404

@app.route('/')
def index():
    return render_template('pages/index.jade')


if __name__ == '__main__':
    app.run(debug=True)