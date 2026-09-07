# Mallika56.github.io

Source for [mallika56.github.io](https://mallika56.github.io) — a static portfolio site for data
analytics and data engineering work: SQL, Python, Power BI, Tableau, and AWS/data pipeline
projects.

## Pages

| Page | Content |
|---|---|
| `index.html` | Landing page, skill overview |
| `about.html` | About / bio |
| `projects.html` | All projects, with links to source repos |
| `sql.html` | SQL-focused work |
| `python.html` | Python/pandas EDA work |
| `powerbi.html` | Power BI dashboards |
| `tableau.html` | Tableau visualizations |
| `aws.html` | AWS & data engineering pipelines |

## Quick start

The site is plain HTML/CSS with no build step.

```bash
git clone https://github.com/Mallika56/Mallika56.github.io.git
cd Mallika56.github.io
python3 -m http.server 8000
```

Then open http://localhost:8000 in a browser.

## Tests

A small pytest suite (`tests/test_site.py`) checks that every page has a title and viewport
meta tag, links its stylesheet, includes the site nav, and that every internal link resolves to
a real file. It runs in CI on every push and pull request.

```bash
pip install -r requirements.txt
python -m pytest -q
```
