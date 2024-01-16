from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

SKILLS = [
    {
        'id': 1,
        'name': 'Python',
        'description': 'Python Description',
        'icon': 'python.jpg'
    },
    {
        'id': 2,
        'name': 'Flask',
        'description': 'Flask Description',
        'icon': 'flask.png'
    },
    {
        'id': 3,
        'name': 'HTML',
        'description': 'HyperText Markup Language',
        'icon': 'html_5.png'
    },
    {
        'id': 4,
        'name': 'CSS',
        'description': 'Cascading Style Sheets',
        'icon': 'css_img.png'
    },
    {
        'id': 5,
        'name': 'Bootstrap',
        'description': 'Bootstrap description',
        'icon': 'bootstrap_5.jpg'
    },
]


@app.route('/')
def homepage():
  return render_template("home.html", skills=SKILLS)


@app.route("/api/skills")
def list_skills():
  return jsonify(SKILLS)


@app.route('/about')
def about():
  return "<h2>This is about page<h2>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
