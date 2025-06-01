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
        team_size = int(request.form['team_size'])
        members = []
        for i in range(team_size):
            members.append({
                'first_name': request.form.get(f'first_name_{i}', ''),
                'last_name': request.form.get(f'last_name_{i}', ''),
                'state': request.form.get(f'state_{i}', ''),
                'email': request.form.get(f'email_{i}', ''),
                'institute': request.form.get(f'institute_{i}', ''),
                'branch': request.form.get(f'branch_{i}', ''),
                'year': request.form.get(f'year_{i}', ''),
            })
        registration = {
            'team_name': request.form['team_name'],
            'team_size': team_size,
            'members': members,
            'problem': request.form['problem'],
        }
    return render_template('register.html', problems=PROBLEM_STATEMENTS, registration=registration)

if __name__ == '__main__':
    app.run(debug=True)
