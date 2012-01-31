## Flask imports
from flask import Flask, abort, Markup
from flask import render_template as render_flask_template
## Third party imports
import markdown
import yaml
## Standard library imports
import os
##
from collections import defaultdict
from glob import glob

# Configuration
app = Flask(__name__, static_url_path="/media")
app.config["DEBUG"] = True
md = markdown.Markdown(extensions=['codehilite'])

def render_template(*args, **kwargs):
  kwargs["site"] = {"name": "Smerity.com"}
  return render_flask_template(*args, **kwargs)

def get_articles(base_directory="content/articles/"):
  d = base_directory
  years = [(x, os.path.join(d, x)) for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)) and x.isdigit()]
  articles = []
  for year, year_fn in years:
    slugs = [x.replace(".yaml", "") for x in os.listdir(year_fn) if x.endswith(".yaml")]
    pages = []
    for slug in slugs:
      page = get_page(int(year), slug, get_dict=True)
      page["year"] = year
      page["slug"] = slug
      pages.append(page)
    pages.sort(key=lambda x: x["date"], reverse=True)
    articles.append((year, pages))
  return sorted(articles, reverse=True)

def load_page(fn):
  if not os.path.exists(fn):
    return None
  page = yaml.load(open(fn))
  page["content"] = md.convert(page["content"])
  return page

@app.route("/articles/<int:year>/<slug>.html")
def get_page(year, slug, get_dict=False):
  fn = os.path.join("content", "articles/%d/%s.yaml" % (year, slug))
  page = load_page(fn)
  if not page: abort(404)
  if get_dict: return page
  return render_template("page.html", page=page)

@app.route("/articles/articles.html")
def articles():
  articles = get_articles()
  return render_template("listing.html", page={"title": "Articles"}, articles=get_articles())

@app.route("/")
def index():
  return render_template("page.html",
      page = {
        "title":Markup("&uarr; Look! Up there! &uarr;"),
        "content":Markup("<div align='center'><img class='smooth' src='media/images/mouse.jpg' /></div>")
      }
    )

### Redirects
@app.route("/noogler2010.html")
def noogler():
  return render_template("redirect.html", redirect_url="/articles/2010/noogler2010.html")

@app.route("/interviews.html")
def noogler():
  return render_template("redirect.html", redirect_url="/articles/2009/interviews.html")

### General pages

@app.route("/abme.html")
def about():
  return render_template("page.html", page=load_page("content/abme.yaml"))

@app.route("/define.html")
def define():
  return render_template("page.html", page=load_page("content/define.yaml"))

@app.route("/404.html")
def get_404():
  # Weird Zen like programming realisation:
  ## If a user is lost on your site, they hit the 404 Not Found page.
  ## If, however, they are looking for the 404 Not Found page, and find it, then they found the page they were looking for.
  ## Hence, 404 should return the HTTP status code 404 Not Found unless they're looking for the 404 page, in which case the HTTP status code should be 200 Ok.
  page = {
    "title": "404",
    "content": """<h2>Page not found</h2>
    <p><em>Programmer Zen:</em> This page returns a 200 OK if viewed at <a href='/404.html'>404.html</a> and a 404 Not Found otherwise.</p>"""
  }
  return render_template("page.html", page=page)

@app.errorhandler(404)
def page_not_found(e):
  return get_404(), 404

if __name__ == "__main__":
  app.run()
