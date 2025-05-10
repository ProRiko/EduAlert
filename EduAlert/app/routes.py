# Import additional modules
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import Teacher, Student, Attendance
from . import db
from datetime import date

main = Blueprint('main', __name__)

# Home redirects to login
@main.route('/')
def home():
    return redirect(url_for('main.login'))

# Login route
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

# Dashboard view
@main.route('/dashboard')
def dashboard():
    if 'teacher_id' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html', teacher=session['teacher_name'])

# Logout route
@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))

# Attendance marking route
@main.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if 'teacher_id' not in session:
        return redirect(url_for('main.login'))

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
        return redirect(url_for('main.dashboard'))

    return render_template('attendance.html', students=students)

# View attendance records route
@main.route('/view_attendance', methods=['GET', 'POST'])
def view_attendance():
    if 'teacher_id' not in session:
        return redirect(url_for('main.login'))

    attendance_records = []
    students = Student.query.all()
    filters = {}

    if request.method == 'POST':
        # Get filters from the form
        date_filter = request.form.get('date')
        student_id_filter = request.form.get('student_id')

        # Build the query dynamically based on filters
        query = Attendance.query
        if date_filter:
            query = query.filter_by(date=date_filter)
            filters['date'] = date_filter
        if student_id_filter:
            query = query.filter_by(student_id=student_id_filter)
            filters['student_id'] = student_id_filter

        attendance_records = query.all()

    return render_template('view_attendance.html', 
                           students=students, 
                           attendance_records=attendance_records, 
                           filters=filters)
