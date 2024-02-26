from flask import (render_template, url_for,
                    request, redirect)
from models import db, Project, app
import datetime


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/new', methods=('GET', 'POST'))
def add_project():
    if request.form:
        dateconv = request.form['date'].replace('-', '')
        date_obj = datetime.datetime.strptime(dateconv, "%Y%m")
        new_project = Project(name=request.form['title'], project_finished=date_obj,
                            description=request.form['desc'],skills_practiced=request.form['skills'],
                            url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
