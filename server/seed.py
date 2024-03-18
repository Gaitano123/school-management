from faker import Faker
import random
from datetime import datetime

from models import *

with app.app_context():
    
    #deleting all the previous records
    
    print('🦸‍♀️ Deleting previous records...')
    
    fake = Faker()
    
    Role.query.delete()
    Member.query.delete()
    Teacher.query.delete()
    Medic.query.delete()
    Parent.query.delete()
    Student.query.delete()
    Parent_Student.query.delete()
    Finance.query.delete()
    Student_Finance.query.delete()
    Replacement.query.delete()
    Department.query.delete()
    Academic_Department.query.delete()
    Teacher_Department.query.delete()
    Class.query.delete()
    Student_Class.query.delete()
    Teacher_Class.query.delete()
    Class_Rep.query.delete()
    Health.query.delete()
    Medical_Record.query.delete()
    Drug.query.delete()
    Dosage_Day.query.delete()
    Book_Exchange.query.delete()
    Teacher_Exchange.query.delete()
    Staff_Exchange.query.delete()
    Sport.query.delete()
    sport_Detail.query.delete()
    Sport_Member.query.delete()
    Club.query.delete()
    Club_Detail.query.delete()
    Club_Member.query.delete()
    Block.query.delete()
    Dorms.query.delete()
    StudentDorms.query.delete()
    
    print('🦸‍♀️ seeding roles...')
    
    roles_data =[
        {"role": "Teacher"},
        {"role": "Medic"},
        {"role": "Coach"},
        {"role": "Cook"},
        {"role": "Cleaner"},
        {"role": "HR"},
        {"role": "Administrator"},
        {"role": "Librarian"},
        {"role": "Lab-technician"},
        {"role": "ICT-Technician"},
        {"role": "Board"},
        {"role" : "Chaplain"},
        {"role" : "Watchman"},
        {"role" : "Drivers"}
    ]
    
    roles = [Role(**role_info) for role_info in roles_data]
    
    db.session.add_all(roles)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Members...')
    
    members = []
    
    for _ in range(1, 300):
        member = Member(
            first_name= fake.first_name(),
            middle_name= fake.first_name(),
            last_name=fake.last_name(),
            photo = f'https://dummyimage.com/200x200/{random.randint(10, 100000)}',
            date_of_birth= fake.date_of_birth().strftime('%d/%m/%Y'),
            gender= fake.random_element(["Male", "Female"]),
            nationality= fake.random_element(["Kenyan", "Uganadan", "Tanzanian"]),
            ethnicity=fake.random_element(["African", "Mixed", "European"]),
            religion= fake.random_element(["Christian", "Muslim", "Hindu"]),
            home_address= fake.address(),
            phone_no=fake.phone_number(),
            role_id=random.randint(1, 11)
        )
        members.append(member)
        
    db.session.add_all(members)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Teachers...')
    
    teachers = []
    teachers_id = Member.query.filter_by(role_id = 1).all()
    
    for _ in range(1, 100):
        random_teacher = random.choice(teachers_id)
        teacher =Teacher(
            id_no=random_teacher.id,
            kcse= random.randint(300, 450),
            degree= "first_class",
            license_by_tsc= "64564",
            experience= fake.random_element(["3 years", "10 years", "20 years", "30 years"])
        )
        teachers.append(teacher)
        
    db.session.add_all(teachers)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Medic...')
    
    medics =[]
    medics_id = Member.query.filter_by(role_id = 2).all()
    
    for _ in range(0, 4):
        random_medic = random.choice(medics_id)
        medic = Medic(
            id_no= random_medic.id,
            license= "doctor",
            degree= "first_class",
            experience= fake.random_element(["3 years", "10 years", "20 years", "30 years"])
        )
        medics.append(medic)
        
    db.session.add_all(medics)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Parent...')
    
    parents=[]
    
    for _ in range(1, 600):
        parent = Parent(
            id_no= random.randint(20000000, 30000000),
            first_name= fake.first_name(),
            middle_name= fake.first_name(),
            last_name=fake.last_name(),
            phone_no=fake.phone_number(),
            gender= fake.random_element(["Male", "Female"]),
        )
        parents.append(parent)
        
    db.session.add_all(parents)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Student...')
    
    students =[]
    
    for _ in range(1, 300):
        student = Student(
            first_name= fake.first_name(),
            middle_name=fake.first_name(),
            last_name=fake.last_name(),
            photo = f'https://dummyimage.com/200x200/{random.randint(10, 100000)}',
            date_of_birth = fake.date_of_birth().strftime('%d/%m/%Y'),
            gender= fake.random_element(["Male", "Female"]),
            nationality= fake.random_element(["Kenyan", "Uganadan", "Tanzanian"]),
            ethnicity=fake.random_element(["African", "Mixed", "European"]),
            religion= fake.random_element(["Christian", "Muslim", "Hindu"]),
            home_address= fake.address(),
            phone_no= fake.phone_number(),
            prev_school_name= fake.street_name(),
            prev_school_address=fake.address(),
            kcpe= random.randint(300, 450),
            blood_group=fake.random_element(["A", "AB", "B", "O"]),
            immunization_records="None",
            allergies="None",
            emergency_contact= fake.phone_number(),
            birth_no=random.randint(20000000, 30000000),
            leaving_cert="Good",
            special_needs="None"
        )
        students.append(student)
        
    db.session.add_all(students)
    db.session.commit()
    
    print('🦸‍♀️ Seeding parent_student...')
    
    parent_students=[]
    
    for _ in range(1, 600):
        parent_student = Parent_Student(
            parent_id= random.randint(1, 600),
            student_id=random.randint(1, 300)
        )
        parent_students.append(parent_student)
        
    db.session.add_all(parent_students)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Finance...')
    
    finances = []
    
    for _ in range(1, 90):
        finace = Finance(
            year= random.randint(1996, 2024),
            tearm= random.randint(1, 3),
            form= random.randint(1, 4)
        )
        finances.append(finace)
        
    db.session.add_all(finances)
    db.session.commit()
    
    print('🦸‍♀️ Seeding student_finances...')
    
    student_fanances =[]
    
    for _ in range(0, 9000):
        student_finance = Student_Finance(
            finance_id= random.randint(1, 30),
            admin_no=random.randint(1, 300),
            paid= random.randint(100000, 150000),
            balance= random.randint(10000, 1000000),
        )
        student_fanances.append(student_finance)
        
    db.session.add_all(student_fanances)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Replacements...')
    
    replacements=[]
    
    for _ in range(0, 200):
        replacement = Replacement(
            finance_id= random.randint(1, 20),
            admin_no= random.randint(1, 300),
            item=fake.random_element(['Burrette', 'Pippette', 'conical falsk']),
            quantitiy= random.randint(1, 6),
            amount= random.randint(300, 10000)
        )
        replacements.append(replacement)
        
    db.session.add_all(replacements)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Departments...')
    
    departments_data= [
        {"name": "Maths"},
        {"name": "Languages"},
        {"name": "sciences"},
        {"name": "Humanities"},
        {"name": "Technical"}
    ]
    
    departments = [Department(**department_info) for department_info in departments_data]
    
    db.session.add_all(departments)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Academic_Departments...')
    
    academic_departments =[]
    
    for _ in range(0, 16):
        random_head = random.choice(teachers_id)
        academic_department1 = Academic_Department(
            subject= fake.random_element(["Maths", "English", "Kiswahili", "Physics", "Chemistry", "Biology"]),
            department_id=random.randint(1, 5),
            head_id= random_head.id,
            block=fake.random_element(["Admission", "A", "B", "O"]),
        )
        academic_departments.append(academic_department1)
        
    db.session.add_all(academic_departments)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Teacher_Departments...')
    
    teacher_departments=[]
    
    for _ in range(0, 100):
        random_teacher = random.choice(teachers_id)
        teacher_department = Teacher_Department(
            subject_id= random.randint(0, 16),
            teacher_id= random_teacher.id
        )
        teacher_departments.append(teacher_department)
    
    db.session.add_all(teacher_departments)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Class...')
    
    classes=[]
    
    for _ in range (0, 32):
        random_teacher = random.choice(teachers_id)
        class1 = Class(
            form= random.randint(1, 4),
            stream= fake.random_element(["M", "N", "P", "Q"]),
            teacher_id=random_teacher.id,
            captain_id=random.randint(1, 300)
        )
        classes.append(class1)
        
    db.session.add_all(classes)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Student_Class...')
    
    student_classes = []
    
    for _ in range(0, 9200):
        student_class = Student_Class(
            class_id= random.randint(0, 32),
            student_id=random.randint(1, 300)
        )
        student_classes.append(student_class)
        
    db.session.add_all(student_classes)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Teacher_Class...')
    
    teacher_classes = []
    
    for _ in range(0, 150):
        random_teacher = random.choice(teachers_id)
        teacher_class = Teacher_Class(
            class_id= random.randint(0, 32),
            teacher_id= random_teacher.id,
            subject_id= random.randint(0, 16)
        )
        teacher_classes.append(teacher_class)
        
    db.session.add_all(teacher_classes)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Class_reps...')
    
    class_reps = []
    
    for _ in range(0, 64):
        class_rep = Class_Rep(
            class_id= random.randint(0, 32),
            rep_id = random.randint(1, 600)
        )
        class_reps.append(class_rep)
        
    db.session.add_all(class_reps)
    db.session.commit()
    
    print('🦸‍♀️ Seeding health...')
    
    random_medic = random.choice(medics_id)
    health = Health(
        head_id=random_medic.id,
        captain_id= random.randint(1, 300)
    )    
    db.session.add(health)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Medical_records...')
    
    medical_records = []
    
    for _ in range (200):
        random_medic = random.choice(medics_id)
        medical_record = Medical_Record(
            medic_id= random_medic.id,
            admin_no=random.randint(1, 300),
            symptoms= "Headache",
            sickness= "Sickness",
            sick_leave=fake.random_element([True, None])
        )
        medical_records.append(medical_record)
        
    db.session.add_all(medical_records)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Drug...')
    
    drugs=[]
    
    for _ in range(0, 380):
        drug = Drug(
            medical_id=random.randint(1, 200),
            drug= "panadol",
            dose= "2*3",
            days= 6,
            complete=fake.random_element([True, None])
        )
        drugs.append(drug)
        
    db.session.add_all(drugs)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Dosage_Day...')
    
    dosage_days = []
    
    for _ in range(0, 180):
        drug_day = Dosage_Day(
            drug_id=random.randint(1, 380),
            morning=fake.random_element([True, None]),
            afternoon=fake.random_element([True, None]),
            evening=fake.random_element([True, None]),
            date=datetime.strptime(fake.date(), '%Y-%m-%d')
        )
        dosage_days.append(drug_day)
        
    db.session.add_all(dosage_days)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Book_Exchange...')
    
    books_exhange = []
    
    for _ in range(0, 100):
        book_exhange = Book_Exchange(
            admin_no= random.randint(1, 300),
            size="A4",
            type= fake.random_element(["rulled", "squared"]),
            quantity= random.randint(1, 4),
            date=datetime.strptime(fake.date(), '%Y-%m-%d')
        )
        books_exhange.append(book_exhange)
        
    db.session.add_all(books_exhange)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Teacher_exhange...')
    
    teachers_exchange = []
    
    for _ in range(0, 100):
        random_teacher = random.choice(teachers_id)
        teacher_exchange = Teacher_Exchange(
            teacher_id=random_teacher.id,
            admin_no=random.randint(1, 300),
            item=fake.random_element(['Burrette', 'Pippette', 'conical falsk']),
            colour=fake.color(),
            quantity= random.randint(1, 5),
            date=datetime.strptime(fake.date(), '%Y-%m-%d')
        )
        teachers_exchange.append(teacher_exchange)
        
    db.session.add_all(teachers_exchange)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Staff_echange...')
    
    staffs_exchange = []
    
    for _ in range(0, 100):
        staff_exchange = Staff_Exchange(
            members_id=random.randint(1, 150),
            item=fake.random_element(['Burrette', 'Pippette', 'conical falsk']),
            quantity= random.randint(1, 6),
            date=datetime.strptime(fake.date(), '%Y-%m-%d')
        )
        staffs_exchange.append(staff_exchange)
        
    db.session.commit()
    
    print('🦸‍♀️ Seeding Sports...')
    
    sports= []
    
    for _ in range(0, 30):
        random_teacher = random.choice(teachers_id)
        sport = Sport(
            sport = fake.random_element(["Football", "Bascket_ball", "Hockey", "Swimming", "Rugby"]),
            captain_id=random.randint(1, 300),
            shod=random_teacher.id
        )
        sports.append(sport)
        
    db.session.add_all(sports)
    db.session.commit()
    
    print('🦸‍♀️ Seeding sport details...')
    
    sport_details = []
    coaches_id = Member.query.filter_by(role_id = 3).all()
    for _ in range(0, 30):
        random_coach = random.choice(coaches_id) 
        sport_detail= sport_Detail(
            sport_id=random.randint(0, 30),
            coach_id=random_coach.id,
            captain_id= random.randint(0, 300)
        )
        sport_details.append(sport_detail)
        
    db.session.add_all(sport_details)
    db.session.commit()
    
    print('🦸‍♀️ Seeding sport Members...')
    
    sport_members = []
    
    for _ in range(0, 300):
        sport_member = Sport_Member(
            sport_id=random.randint(0, 30),
            admin_id=random.randint(0, 300)
        )
        sport_members.append(sport_member)
        
    db.session.add_all(sport_members)
    db.session.commit()
        
    print('🦸‍♀️ Seeding clubs...')
    
    clubs= []
    
    for _ in range(0, 30):
        random_teacher = random.choice(teachers_id)
        club = Club(
            club= fake.random_element(["PA", "Aviation", "ICT","Debate" , "Farming"]),
            captain_id= random.randint(1, 300),
            shod_id= random_teacher.id
        )
        clubs.append(club)
        
    db.session.add_all(clubs)
    db.session.commit()
    
    print('🦸‍♀️ Seeding club details...')
    
    club_details = []
    
    for _ in range(0, 30):
        random_teacher = random.choice(teachers_id)
        club_detail= Club_Detail(
            club_id= random.randint(0, 30),
            head_id= random_teacher.id,
            captain_id=random.randint(1, 300)
        )
        club_details.append(club_detail)
        
    db.session.add_all(club_details)
    db.session.commit()
    
    print('🦸‍♀️ Seeding club Members...')
    
    club_members = []
    
    for _ in range(0, 300):
        club_member = Club_Member(
            club_id=  random.randint(0, 30),
            admin_no= random.randint(1, 300)
        )
        club_members.append(club_member)
        
    db.session.add_all(club_members)
    db.session.commit()
    
    print('🦸‍♀️ Seeding blocks...')
    
    blocks =[]
    
    for _ in range(0, 5):
        random_teacher = random.choice(teachers_id)
        block = Block(
            block=fake.random_element(["A", "B", "C", "D", "E"]),
            master_id=random_teacher.id,
        )
        blocks.append(block)
        
    db.session.add_all(blocks)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Dorms...')
    
    dorms = []
    
    for _ in range(0, 20):
        random_teacher = random.choice(teachers_id)
        dorm = Dorms(
            block_id= random.randint(0, 5),
            house=fake.random_element(["Longonot", "Elgon", "Kilimanjaro", "Marsabit", "Usambara"]),
            captain_id=random.randint(1, 300),
            master_id=random_teacher.id
        )
        dorms.append(dorm)
        
    db.session.add_all(dorms)
    db.session.commit()
    
    print('🦸‍♀️ Seeding Student Dorms...')
    
    student_dorms = []
    
    for _ in range(0, 300):
        student_dorm = StudentDorms(
            dorm_id= random.randint(0, 20),
            cube= random.randint(1, 10),
            admin_no=random.randint(1, 300)
        )
        student_dorms.append(student_dorm)
        
    db.session.add_all(student_dorms)
    db.session.commit()
    
    print('🦸‍♀️ Done Seeding...')
                