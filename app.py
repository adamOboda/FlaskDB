from flask import Flask, make_response, request, render_template, redirect, url_for
from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardsecretkey'

# Strona główna i podstrony


@app.route('/')
def Index():
    #name= 'Adam'
    context = {
        'text': 'Wartość klucza text',
        'name': 'Wartość klucza name'
    }
    return render_template('index.html', data=context)


@app.route('/contact')
def Contact():
    return render_template('contact.html')


@app.route('/about')
def About():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect (url_for('Index'))

    return render_template('login.html', title='Login', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == "__main__":
    app.run(debug=True)
