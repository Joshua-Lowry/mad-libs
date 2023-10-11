from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story2
import random
app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'secret'
debug = DebugToolbarExtension(app)

stories = [story, story2]
madlibs = random.choice(stories)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/questions')
def question_page():
    prompts = madlibs.prompts
    return render_template("question.html", prompts=prompts)

@app.route('/results')
def results_page():
    text = madlibs.generate(request.args)
    return render_template("results.html", text=text)


