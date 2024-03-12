
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
    
    role_member = db.relationship('Role', backref='members')

class Teacher(db.Model):
    
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    kcse = db.Column(db.String)
    degree = db.Column(db.String)
    license_by_tsc = db.Column(db.String)
    experience = db.Column(db.String)
    
    member = db.relationship('Member', backref='teachers')
    
class Medic(db.Model):
    
    __tablename__ = 'medics'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    license = db.Column(db.String)
    degree = db.Column(db.String)
    experience = db.Column(db.String)
    
    member_medic = db.relationship('Member', backref='medics')


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
    
    parent_student = db.relationship('Parent', backref='parent_students')
    student_parent = db.relationship('Student', backref= 'parent_students')
    
class Finance(db.Model):
    
    __tablename__ = 'finances'
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    tearm = db.Column(db.String)
    form = db.Column(db.Integer)
    

class Student_Finance(db.Model):
    
    __tablename__ = 'student_finances'
    
    id = db.Column(db.Integer, primary_key=True)
    finance_id = db.Column(db.Integer, db.ForeignKey('finances.id'))
    admin_no = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    paid = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())
    
    finances = db.relationship('finances', backref='student_finances')
    student_finances = db.relationship('Student', backref='student_finances')

class Replacement(db.Model):
    
    __tablename__ = 'replacements'
    
    id = db.Column(db.Integer, primary_key=True)
    finance_id = db.Column(db.Integer, db.ForeignKey('finances.id'))
    admin_no = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    item = db.Column(db.String)
    quantitiy = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())
    
    relacements = db.relationship('finances', backref='student_finances')
    student = db.relationship('Student', backref='student_finances')
        
class Department(db.Model):
    
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Academic_Department(db.Model):
    
    __tablename__ = 'academic_departments'
    
    subject = db.Column(db.String, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    head_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    block = db.Column(db.String)
    
    department = db.relationship('Department', backref='academic_departments')
    head = db.relationship('Teacher', backref='academic_departments')

class Teacher_Department(db.Model):
    
    __tablename__ = 'teacher_departments'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, db.ForeignKey('academic_departments.subject'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    
    subject_department = db.relationship('Academic_Department', backref='teacher_departments')
    teacher = db.relationship('Teacher', backref='teacher_departments' )

class Class(db.Model):
    
    __tablename__ = 'classes'
    
    id = db.Column(db.Integer, primary_key=True)
    form = db.Column(db.Integer)
    stream = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    captain_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    class_reps = db.Column(db.String)
    
    teacher = db.relationship('Teacher', backref='classes')
    student = db.relationship('Student', backref='classes')

class Student_Class(db.Model):
    
    __tablename__ = 'student_classes'
    
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='student_classes')
    class_student = db.relationship('Class', backref ='student_classes')    

class Teacher_Class(db.Model):
    
    __tablename__ = 'teacher_classes'
    
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    subject = db.Column(db.String, db.ForeignKey('academic_departments.subject'))
    
    student = db.relationship('Student', backref='teacher_classes')
    teacher = db.relationship('Teacher', backref='teacher_classes')
    subject_department = db.relationship('Academic_Department', backref='teacher_classes')
    
class Health(db.Model):
    
    __tablename__ = 'health'
    
    id = db.Column(db.Integer, primary_key=True)
    head_id = db.Column(db.Integer, db.ForeignKey('medics.id'))
    captain_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='health')
    medic = db.relationship('Medic', backref='health')    

class Medical_Record(db.Model):
    
    __tablename__ = 'medical_records'
    
    id = db.Column(db.Integer, primary_key=True)
    head_id = db.Column(db.Integer, db.ForeignKey('medics.id'))
    admin_no = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    symptoms = db.Column(db.String)
    sickness = db.Column(db.String)
    sick_leave = db.Column(db.String)
    date = db.Column(db.DateTime, server_default=db.func.now()) 
    
    student = db.relationship('Student', backref='medical_records')
    medic = db.relationship('Medic', backref='medical_records')         
    
class Drug(db.Model):
    
    __tablename__ = 'drugs'
    
    id = db.Column(db.Integer, primary_key=True)
    medical_id = db.Column(db.Integer, db.ForeignKey('medical_records.id'))
    drug = db.Column(db.String)
    dose = db.Column(db.String)
    days = db.Column(db.Integer)
    complete = db.Column(db.Boolean)
    
    medic = db.relationship('Medic', backref='medical_records')         
    
class Dosage_Day(db.Model):
    
    __tablename__ = 'dosage_days'
    
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'))
    morning = db.Column(db.Boolean)
    afternoon = db.Column(db.Boolean)
    evening = db.Column(db.Boolean)
    date = db.Column(db.DateTime)
    
    drugs = db.relationship('Drug', backref='dosage_days')     


class Book_Exchange(db.Model):
    __tablename__ = 'exercise_book_exchange'


    id = db.Column(db.Integer , primary_key=True)
    admin_no = db.Column(db.Integer , db.ForeignKey('students.admin_no'))
    size = db.Column(db.String(3))
    type = db.Column(db.String(2))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    student = db.relationship('Student', backref='medical_records')

    def __init__(self, admin_no, size, type, quantity, date):
        self.admin_no = admin_no
        self.size = size
        self.type = type
        self.quantity = quantity
        self.date = date

class Teacher_Exchange(db.Model):
    __tablename__ = 'teachers_exchange'


    id = db.Column(db.Integer , primary_key=True)
    teacher_id = db.Column (db.Integer , db.ForeignKey('teachers.id'))
    admin_no = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    item = db.Column (db.String)
    colour = db.Column (db.String)
    quantity = db.Column (db.Integer)
    date = db.Column(db.DateTime)

    student = db.relationship('Student', backref='teachers_exchange')
    teacher = db.relationship('Teacher', backref='teachers_exchange')

    def __init__(self, teacher_id, admin_no, item, colour, quantity, date):
        self.teacher_id = teacher_id
        self.admin_no = admin_no
        self.item = item
        self.colour = colour
        self.quantity = quantity
        self.date = date

class Staff_Exchange(db.Model):
    __tablename__ = 'staff_excahnge'


    id = db.Column (db.Integer , primary_key=True)
    member_id = db.Column (db.Integer , db.ForeignKey('members.id'))
    item = db.Column (db.String)
    quantity = db.Column (db.Integer)
    date = db.Column(db.DateTime)
    
    member = db.relationship('Member', backref='staff_excahnge')

    def __init__(self , members_id , item , quantity , date):
        self.member_id = members_id
        self.item = item
        self.quantity = quantity
        self.date = date
   

class Sport(db.Model):
    __tablename__ = 'sports'


    id = db.Column (db.Integer , primary_key=True)
    sport = db.Column(db.String)
    captain_id = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    shod = db.Column (db.String , db.ForeignKey('teachers.id'))
    
    student = db.relationship('Student', backref='sports')
    teacher = db.relationship('Teacher', backref='sports')  

    def __init__(self , sport , captain_id , shod):
        self.sport = sport 
        self.captain_id = captain_id
        self.shod = shod
          

class sport_Detail(db.Model):
    __tablename__ = 'sport_details'


    id = db.Column (db.Integer , primary_key=True)
    sport_id = db.Column (db.Integer , db.ForeignKey('sports.id'))
    coach_id = db.Column (db.Integer , db.ForeignKey('members.id'))
    captain_id = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='sport_details')
    member = db.relationship('Member', backref='sport_details')
    sport = db.relationship('Sport', backref = 'sport_details') 

    def __init__(self , sport_id , coach_id , captain_id):
        self.sport_id = sport_id
        self.coach_id = coach_id
        self.captain_id = captain_id   
    

class Sport_Member(db.Model):
    __tablename__ = 'sport_members'


    id = db.Column (db.Integer , primary_key=True)
    sport_id = db.Column (db.Integer , db.ForeignKey('sports.id'))
    admin_id = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='sport_members')
    sport = db.relationship('Sport', backref = 'sport_members')    

    def __init__ (self , sport_id , admin_id):
        self.sport_id = sport_id
        self.admin_id = admin_id

class Club(db.Model):
    __tablename__ = 'clubs'


    id = db.Column (db.Integer , primary_key=True)
    club = db.Column (db.String)
    captain_id = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    shod_id = db.Column (db.String , db.ForeignKey('teachers.id'))

    student = db.relationship('Student', backref='clubs')
    teacher = db.relationship('Teacher', backref='clubs') 

    def __init__ (self ,club , captain_id , shod_id ):
        self.club = club
        self.captain_id = captain_id
        self.shod_id = shod_id

class Club_Detail(db.Model):
    __tablename__ = 'club_details'


    id = db.Column (db.Integer , primary_key=True)
    club_id = db.Column (db.Integer , db.ForeignKey('clubs.id'))
    head_id = db.Column (db.Integer , db.ForeignKey('members.id'))
    captain_id = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='club_details')
    teacher = db.relationship('Teacher', backref='club_details')     
    club = db.relationship('Club', backref='club_details')

    def __init__(self , club_id , head_id , captain_id):
        self.club_id = club_id
        self.head_id = head_id
        self.captain_id = captain_id


class Club_Member(db.Model):
    __tablename__ = 'club_members'


    id = db.Column (db.Integer , primary_key=True)
    club_id = db.Column (db.Integer , db.ForeignKey('clubs.id'))
    admin_no = db.Column (db.Integer , db.ForeignKey('students.admin_no'))
    
    club = db.relationship('Club', backref='club_members')
    student = db.relationship('Student', backref='club_members')

    def __init__(self , club_id , admin_no):
        self.club_id = club_id
        self.admin_no = admin_no


class Block(db.Model):
    __tablename__ = 'blocks'


    id = db.Column (db.Integer , primary_key=True)
    block = db.Column (db.String)
    master_id = db.Column (db.Integer , db.ForeignKey('teachers.id'))
    
    teacher = db.relationship('Teacher', backref='blocks') 

    def __init__ (self , block , master_id):
        self.block = block
        self.master_id = master_id    

class Dorms(db.Model):
    __tablename__ = 'dorms'
    
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.Integer, db.ForeignKey('blocks.id'))
    house = db.Column(db.String)
    captain_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    master_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  
    
    teacher = db.relationship('Teacher', backref='dorms')     
    student = db.relationship('Student', backref='dorms')

    def __init__ (self , block_id,house,captain_id,master_id):
        self.block_id = block_id
        self.house = house
        self.captain_id = captain_id
        self.master_id = master_id

class StudentDorms(db.Model):
    __tablename__ = 'student_dorms'
    
    id = db.Column(db.Integer, primary_key=True)
    dorm_id = db.Column(db.Integer, db.ForeignKey('dorms.id'))
    cube = db.Column(db.Integer)
    admin_no = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    
    dorm = db.relationship('Dorm', backref='student_dorms')
    student = db.relationship('Student', backref='student_dorms')

    def __init__(self, dorm_id , cube , admin_no):
        self.dorm_id = dorm_id
        self.cube = cube 
        self.admin_no = admin_no
