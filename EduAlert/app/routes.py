from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Teacher
from . import db
from flask import render_template, request, redirect, url_for, session, flash
from .models import Student, Attendance
from datetime import date
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        teacher = Teacher.query.filter_by(username=username, password=password).first()
        if teacher:
            session['teacher_id'] = teacher.id
            session['teacher_name'] = teacher.username
            return redirect(url_for('main.dashboard'))
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

@main.route('/dashboard')
def dashboard():
    if 'teacher_id' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html', teacher=session['teacher_name'])

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))
@main.route('/attendance')
def attendance():
    return render_template('attendance.html')


# Route to display and mark attendance
@main.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if 'teacher_id' not in session:
        return redirect(url_for('login'))

    students = Student.query.all()

    if request.method == 'POST':
        for student in students:
            status = request.form.get(f'status_{student.id}')
            if status:
                attendance_record = Attendance(
                    student_id=student.id,
                    date=date.today(),
                    status=status
                )
                db.session.add(attendance_record)
        db.session.commit()
        flash('✅ Attendance submitted successfully!')
        return redirect(url_for('dashboard'))

    return render_template('attendance.html', students=students)


