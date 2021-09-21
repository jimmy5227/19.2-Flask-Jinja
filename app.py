from flask import Flask, request, render_template
import stories
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HelloWorld'
# debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    prompts = stories.story.prompts
    return render_template('index.html', prompts=prompts)


@app.route('/story')
def story():

    text = stories.story.generate(request.args)

    # place = request.args['place']
    # noun = request.args['noun']
    # verb = request.args['verb']
    # adjective = request.args['adjective']
    # plural_noun = request.args['plural_noun']
    return render_template('story.html', text=text)
