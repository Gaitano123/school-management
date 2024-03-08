from __init__ import *
from datetime import datetime

class Role(db.Model):
    
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)

class Member(db.Model):
    
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    photo = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    nationality = db.Column(db.String)
    ethnicity = db.Column(db.String)
    religion = db.Column(db.String)
    home_address = db.Column(db.String)
    phone_no = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class Teacher(db.Model):
    
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    kcse = db.Column(db.String)
    degree = db.Column(db.String)
    license_by_tsc = db.Column(db.String)
    experience = db.Column(db.String)
    
class Medic(db.Model):
    
    __tablename__ = 'medics'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    license = db.Column(db.String)
    degree = db.Column(db.String)
    experience = db.Column(db.String)


class Parent(db.Model):
    
    __tablename__ = 'parents'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_no = db.Column(db.Integer)
    gender = db.Column(db.String)

class Student(db.Model):
    
    __tablename__ = 'students'
    
    admin_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    photo = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    nationality = db.Column(db.String)
    ethnicity = db.Column(db.String)
    religion = db.Column(db.String)
    home_address = db.Column(db.String)
    phone_no = db.Column(db.String)
    prev_school_name = db.Column(db.String)
    prev_school_address = db.Column(db.String)
    kcpe = db.Column(db.Integer)
    blood_group = db.Column(db.String)
    immunization_records = db.Column(db.String)
    allergies = db.Column(db.String)
    emergency_contact = db.Column(db.String)
    birth_no = db.Column(db.Integer)
    leaving_cert = db.Column(db.String)
    special_needs = db.Column(db.String)
    admission_date = db.Column(db.DateTime, server_default=db.func.now())
    
class Parent_Student(db.Model):
    
    __tablename__ = 'parent_students'
    
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    
# class Finance(db.Model):
#     pass

# class Student_Finance(db.Model):
#     pass

# class Replacement(db.Model):
#     pass

# class Department(db.Model):
#     pass

# class Academic_Department(db.Model):
#     pass

# class Teacher_Department(db.Model):
#     pass

# class Class(db.Model):
#     pass

# class Student_Class(db.Model):
#     pass

# class Teacher_Class(db.Model):
#     pass

# class Health(db.Model):
#     pass

# class Medical_Record(db.Model):
#     pass

# class Drug(db.Model):
#     pass

# class Dosage_Day(db.Model):
#     pass

# class Book_Exchange(db.Model):
#     pass

# class Teacher_Exchange(db.Model):
#     pass

# class Staff_Exchange(db.Model):
#     pass

# class Sport(db.Model):
#     pass

# class sport_Detail(db.Model):
#     pass

# class Sport_Member(db.Model):
#     pass

# class Club(db.Model):
#     pass

# class Club_Detail(db.Model):
#     pass

# class Club_Member(db.Model):
#     pass

# class Block(db.Model):
#     pass

# class Dorms(db.Model):
#     pass

# class Student_Dorm(db.Model):
#     pass
