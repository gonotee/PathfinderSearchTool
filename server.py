from flask import Flask, render_template, request
from forms import SignUpForm, SpellSearchForm
from databaseHandler import spellSearchHandler
from jinja2 import Environment
from jinja2_ansible_filters import AnsibleCoreFiltersExtension
env = Environment(extensions=[AnsibleCoreFiltersExtension])


import urllib.parse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.jinja_env.add_extension('jinja2_ansible_filters.AnsibleCoreFiltersExtension')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

@app.route('/spellSearch', methods=['GET', 'POST'])
def spellSearch():
    form = SpellSearchForm()
    if form.is_submitted():
        formResult = request.form
        handler = spellSearchHandler()
        handler.attachForm(formResult)
        handler.cleanseForm()
        databaseResult = handler.executePreparedStatement()
        return render_template('databaseResults.html', formResult=formResult, databaseResult=databaseResult)
    return render_template('spellSearchForm.html', form=form)

@app.route('/spellResult/<spell_name>')
def spellResult(spell_name):
    # decodes the url into a regular string, currently seems unneeded
    # spell_name = urllib.parse.unquote(spell_name)
    handler = spellSearchHandler()
    databaseResult = handler.executePreparedSpellFind(str(spell_name))
    return render_template('spellPage.html', databaseResult=databaseResult)

if __name__ == '__main__':
    app.run(host='0.0.0.0')