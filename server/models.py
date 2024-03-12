from __init__ import *
from datetime import datetime

current_date = datetime.now()

class Role(db.Model):
    
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    
    def __init__(self, role):
        self.role = role

class Member(db.Model):
    
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    photo = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime)
    age = db.Column(db.Integer, name="age")
    gender = db.Column(db.String)
    nationality = db.Column(db.String)
    ethnicity = db.Column(db.String)
    religion = db.Column(db.String)
    home_address = db.Column(db.String)
    phone_no = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    role_member = db.relationship('Role', backref='members')
    
    def __init__(self, first_name, middle_name, last_name, photo, date_of_birth, gender, nationality, ethnicity, religion, home_address, phone_no, role_id):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.photo = photo
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
        self.age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        self.gender = gender
        self.nationality = nationality
        self.ethnicity =ethnicity
        self.religion = religion
        self.home_address = home_address
        self.phone_no = phone_no
        self.role_id = role_id

class Teacher(db.Model):
    
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    kcse = db.Column(db.String)
    degree = db.Column(db.String)
    license_by_tsc = db.Column(db.String)
    experience = db.Column(db.String)
    
    member = db.relationship('Member', backref='teachers')
    
    def __init__(self, id_no, kcse, degree, license_by_tsc, experience):
        self.id_no = id_no
        self.kcse = kcse
        self.degree = degree
        self.license_by_tsc = license_by_tsc
        self.experience = experience
    
class Medic(db.Model):
    
    __tablename__ = 'medics'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer, db.ForeignKey('members.id'))
    license = db.Column(db.String)
    degree = db.Column(db.String)
    experience = db.Column(db.String)
    
    member_medic = db.relationship('Member', backref='medics')
    
    def __init__(self, id_no, license, degree, experience):
        self.id_no = id_no
        self.license = license
        self.degree = degree
        self.experience = experience

class Parent(db.Model):
    
    __tablename__ = 'parents'
    
    id = db.Column(db.Integer, primary_key=True)
    id_no = db.Column(db.Integer)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_no = db.Column(db.Integer)
    gender = db.Column(db.String)
    
    def __init__(self, id_no, first_name, middle_name, last_name, phone_no, gender):
        self.id_no = id_no
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.gender = gender

class Student(db.Model):
    
    __tablename__ = 'students'
    
    admin_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    photo = db.Column(db.String)
    date_of_birth = db.Column(db.DateTime)
    age = db.Column(db.Integer, name ='age')
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
    
    def __init__(self, first_name, middle_name, last_name, photo, date_of_birth, gender, 
        nationality, ethnicity, religion, home_address, phone_no, prev_school_name, prev_school_address, 
        kcpe, blood_group, immunization_records, allergies, emergency_contact, birth_no, leaving_cert, special_needs):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.photo = photo
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
        self.age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        self.gender = gender
        self.nationality = nationality
        self.ethnicity = ethnicity
        self.religion = religion
        self.home_address = home_address
        self.phone_no = phone_no
        self.prev_school_name = prev_school_name
        self.prev_school_address = prev_school_address
        self.kcpe = kcpe
        self.blood_group = blood_group
        self.immunization_records = immunization_records
        self.allergies = allergies
        self.emergency_contact = emergency_contact
        self.birth_no = birth_no
        self.leaving_cert = leaving_cert
        self.special_needs = special_needs
    
class Parent_Student(db.Model):
    
    __tablename__ = 'parent_students'
    
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    
    parent_student = db.relationship('Parent', backref='parent_students')
    student_parent = db.relationship('Student', backref= 'parent_students')
    
    def __init__(self, parent_id, student_id):
        self.parent_id = parent_id
        self.student_id = student_id
    
class Finance(db.Model):
    
    __tablename__ = 'finances'
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    tearm = db.Column(db.String)
    form = db.Column(db.Integer)
    
    def __init__(self, year, tearm, form):
        self.year = year
        self.tearm = tearm
        self.form = form

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
    
    def __init__(self, finance_id, admin_no, paid, balance):
        self.finance_id = finance_id
        self.admin_no = admin_no
        self.paid = paid
        self.balance = balance

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
    
    def __init__(self, finance_id, admin_no, item, quantitiy, amount):
        self.finance_id = finance_id
        self.admin_no = admin_no
        self.item = item
        self.quantitiy = quantitiy
        self.amount = amount
        
class Department(db.Model):
    
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    def __init__(self, name):
        self.name = name

class Academic_Department(db.Model):
    
    __tablename__ = 'academic_departments'
    
    subject = db.Column(db.String, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    head_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    block = db.Column(db.String)
    
    department = db.relationship('Department', backref='academic_departments')
    head = db.relationship('Teacher', backref='academic_departments')
    
    def __init__(self, subject, department, head_id, block):
        self.subject = subject
        self.department = department
        self.head_id = head_id
        self.block = block

class Teacher_Department(db.Model):
    
    __tablename__ = 'teacher_departments'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, db.ForeignKey('academic_departments.subject'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    
    subject_department = db.relationship('Academic_Department', backref='teacher_departments')
    teacher = db.relationship('Teacher', backref='teacher_departments' )
    
    def __init__(self, subject, teacher_id):
        self.subject = subject
        self.teacher = teacher_id

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
    
    def __init__(self, form, stream, teacher_id, captain_id, class_reps):
        self.form = form
        self.stream = stream
        self.teacher_id = teacher_id
        self.captain_id = captain_id
        self.class_reps = class_reps

class Student_Class(db.Model):
    
    __tablename__ = 'student_classes'
    
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='student_classes')
    class_student = db.relationship('Class', backref ='student_classes')  
    
    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id

class Teacher_Class(db.Model):
    
    __tablename__ = 'teacher_classes'
    
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    subject = db.Column(db.String, db.ForeignKey('academic_departments.subject'))
    
    student = db.relationship('Student', backref='teacher_classes')
    teacher = db.relationship('Teacher', backref='teacher_classes')
    subject_department = db.relationship('Academic_Department', backref='teacher_classes')
    
    def __init__(self, class_id, teacher_id, subject):
        self.class_id = class_id
        self.teacher_id = teacher_id
        self.subject = subject
        
class Class_Reps(db.Model):
    
    __tablename__ = 'class_reps'
    
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    rep_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    
    class_relationship = db.relationship('Class', backref='class_reps')
    parent_relationship = db.relationship('Parent', backref ='class_reps')
    
class Health(db.Model):
    
    __tablename__ = 'health'
    
    id = db.Column(db.Integer, primary_key=True)
    head_id = db.Column(db.Integer, db.ForeignKey('medics.id'))
    captain_id = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    
    student = db.relationship('Student', backref='health')
    medic = db.relationship('Medic', backref='health')  
    
    def __init__(self, head_id, captain_id):
        self.head_id = head_id
        self.captain_id = captain_id

class Medical_Record(db.Model):
    
    __tablename__ = 'medical_records'
    
    id = db.Column(db.Integer, primary_key=True)
    medic_id = db.Column(db.Integer, db.ForeignKey('medics.id'))
    admin_no = db.Column(db.Integer, db.ForeignKey('students.admin_no'))
    symptoms = db.Column(db.String)
    sickness = db.Column(db.String)
    sick_leave = db.Column(db.String)
    date = db.Column(db.DateTime, server_default=db.func.now()) 
    
    student = db.relationship('Student', backref='medical_records')
    medic = db.relationship('Medic', backref='medical_records')   
    
    def __init__(self, medic_id, admin_no, symptoms, sickness, sick_leave):
        self.medic_id = medic_id
        self.admin_no = admin_no
        self.symptoms = symptoms
        self.sickness = sickness
        self.sick_leave = sick_leave     
    
class Drug(db.Model):
    
    __tablename__ = 'drugs'
    
    id = db.Column(db.Integer, primary_key=True)
    medical_id = db.Column(db.Integer, db.ForeignKey('medical_records.id'))
    drug = db.Column(db.String)
    dose = db.Column(db.String)
    days = db.Column(db.Integer)
    complete = db.Column(db.Boolean)
    
    medic = db.relationship('Medic', backref='medical_records') 
    
    def __init__(self, medical_id, drug, dose, days, complete):
        self.medical_id = medical_id
        self.drug = drug
        self.dose = dose
        self.days = days
        self.complete = complete        
    
class Dosage_Day(db.Model):
    
    __tablename__ = 'dosage_days'
    
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'))
    morning = db.Column(db.Boolean)
    afternoon = db.Column(db.Boolean)
    evening = db.Column(db.Boolean)
    date = db.Column(db.DateTime)
    
    drugs = db.relationship('Drug', backref='dosage_days')     
    
    def __init__(self, drug_id, morning, afternoon, evening):
        self.drug_id = drug_id
        self.morning = morning
        self.afternoon = afternoon
        self.evening = evening

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
