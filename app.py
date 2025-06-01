from flask import Flask, render_template, request

app = Flask(__name__)

PROBLEM_STATEMENTS = [
    'AI for Healthcare',
    'Smart City Solutions',
    'Green Energy Innovations',
    'FinTech for All',
    'Education Technology',
]

@app.route('/', methods=['GET', 'POST'])
def register():
    registration = None
    if request.method == 'POST' and 'submit' in request.form:
        registration = {
            'name': request.form['name'],
            'email': request.form['email'],
            'institute': request.form['institute'],
            'branch': request.form['branch'],
            'year': request.form['year'],
            'problem': request.form['problem'],
        }
    return render_template('register.html', problems=PROBLEM_STATEMENTS, registration=registration)

if __name__ == '__main__':
    app.run(debug=True)
