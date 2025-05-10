from . import db
from datetime import date

# Teacher model
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    guardian_name = db.Column(db.String(100), nullable=False)
    guardian_email = db.Column(db.String(100), nullable=False)
    guardian_phone = db.Column(db.String(20), nullable=False)

    # Relationship: one student has many attendance records
    attendances = db.relationship('Attendance', backref='student', lazy=True)

# Attendance model
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(10), nullable=False)  # 'Present' or 'Absent'
    student = db.relationship('Student', backref='attendance_records')
