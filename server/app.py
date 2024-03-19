from flask_migrate import Migrate
from flask_restx import Api, fields, Namespace, Resource

from models import *
from api_models import *

app.config['SECRET_KEY'] = 'bb8f7de46cd4426ebf5ca7df06d43665'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

ns =Namespace("api")

#-------------------------Role-------------------------

@ns.route("/roles")
class Roles(Resource):
    
    @ns.marshal_list_with(role_model)
    def get(self):
        return Role.query.all()
    
    @ns.expect(role_input_model)
    @ns.marshal_with(role_model)
    def post(self):
        role = Role(
            role = ns.payload["role"]
        )
        db.session.add(role)
        db.session.commit()
        return role, 201
    
@ns.route("/role/<int:id>")
class Role_By_ID(Resource):
    
    @ns.marshal_with(role_model)
    def get(self, id):
        role = Role.query.get(id)
        return role


#-------------------------Member-------------------------

@ns.route("/members")
class Members(Resource):
    
    @ns.marshal_list_with(member_model)
    def get(self):
        return Member.query.all()
    
    @ns.expect(member_input_model)
    @ns.marshal_with(member_model)
    def post(self):
        member = Member(
            first_name= ns.payload["first_name"],
            middle_name= ns.payload["middle_name"],
            last_name= ns.payload["last_name"],
            photo= ns.payload["photo"],
            date_of_birth= ns.payload["date_of_birth"],
            gender= ns.payload["gender"],
            nationality= ns.payload["nationality"],
            ethnicity= ns.payload["ethnicity"],
            religion= ns.payload["religion"],
            home_address= ns.payload["home_address"],
            phone_no= ns.payload["phone_no"],
            role_id= ns.payload["role_id"]
        )
        db.session.add(member)
        db.session.commit()
        return member, 201
    
    
@ns.route("/member/<int:id>")
class Members_By_Id(Resource):
    
    @ns.marshal_with(member_model)
    def get(self, id):
        member = Member.query.get(id)
        return member


#-------------------------Teacher-------------------------

@ns.route('/teachers')
class Teachers(Resource):
    
    @ns.marshal_list_with(teacher_model)
    def get(self):
        return Teacher.query.all()
    
    @ns.expect(Teacher_input_model)
    @ns.marshal_with(teacher_model)
    def post(self):
        teacher = Teacher(
            id_no= ns.payload['id_no'],
            kcse= ns.payload['kcse'],
            degree= ns.payload['degree'],
            license_by_tsc= ns.payload['license_by_tsc'],
            experience= ns.payload['experience']
        )
        db.session.add(teacher)
        db.session.commit()
        return teacher, 201
    
    
@ns.route('/teacher/<int:id>')
class Teacher_By_Id(Resource):
    
    @ns.marshal_with(teacher_model)
    def get(self, id):
        teacher = Teacher.query.get(id)
        return teacher


#-------------------------Medic-------------------------

@ns.route("/medics")
class Medics(Resource):
    
    @ns.marshal_list_with(medic_model)
    def get(self):
        return Medic.query.all()
    
    @ns.expect(medic_input_model)
    @ns.marshal_with(medic_model)
    def post(self):
        medic = Medic(
            id_no= ns.payload['id_no'],
            license= ns.payload['license'],
            degree= ns.payload['degree'],
            experience= ns.payload['experience'],
        )
        db.session.add(medic)
        db.session.commit()
        return medic, 201
  
@ns.route("/medic/<int:id>")
class Medic_By_Id(Resource):
    
    @ns.marshal_with(medic_model)
    def get(self, id):
        medic = Medic.query.get(id)
        return medic
    
    
#-------------------------Parent-------------------------

@ns.route('/parents')
class Parents(Resource):
    
    @ns.marshal_list_with(parent_model)
    def get(self):
        return Parent.query.all()
    
    @ns.expect(parent_input_model)
    @ns.marshal_with(parent_model)
    def post(self):
        parent = Parent(
            id_no= ns.payload['id_no'],
            first_name= ns.payload["first_name"],
            middle_name= ns.payload["middle_name"],
            last_name= ns.payload["last_name"],
            phone_no= ns.payload["phone_no"],
            gender= ns.payload["gender"],
        )
        db.session.add(parent)
        db.session.commit()
        return parent, 201
  
@ns.route('/parent/<int:id>')
class Parents_By_Id(Resource):
    
    @ns.marshal_with(parent_model)
    def get(self, id):
        parent = Parent.query.get(id)
        return parent


#-------------------------Student-------------------------


@ns.route('/students')
class Students(Resource):
    
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
        
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(
            first_name= ns.payload["first_name"],
            middle_name= ns.payload["middle_name"],
            last_name= ns.payload["last_name"],
            photo= ns.payload["photo"],
            date_of_birth= ns.payload["date_of_birth"],
            gender= ns.payload["gender"],
            nationality= ns.payload["nationality"],
            ethnicity= ns.payload["ethnicity"],
            religion= ns.payload["religion"],
            home_address= ns.payload["home_address"],
            phone_no= ns.payload["phone_no"],
            prev_school_name= ns.payload['prev_school_name'],
            prev_school_address= ns.payload['prev_school_address'],
            kcpe= ns.payload['kcpe'],
            blood_group= ns.payload['blood_group'],
            immunization_records= ns.payload['immmunization_records'],
            allergies= ns.payload['allergies'],
            emergency_contact= ns.payload['emergency_contact'],
            birth_no= ns.payload['birth_no'],
            leaving_cert= ns.payload['leaving_cert'],
            special_needs= ns.payload['special_needs'],
        )
        db.session.add(student)
        db.session.commit()
        return student, 201
  
@ns.route('/student/<int:id>')
class Student_By_Id(Resource):
    
    @ns.marshal_with(student_model)
    def get(self, id):
        student = Student.query.get(id)
        return student


#-------------------------Parent Student-------------------------

@ns.route('/parent_student')
class Parent_Students(Resource):
    
    @ns.marshal_list_with(parent_student_model)
    def get(self):
        return Parent_Student.query.all()
        
    @ns.expect(parent_input_model)
    @ns.marshal_with(parent_model)
    def post(self):
        parent_student = Parent_Student(
            parent_id= ns.payload['parent_id'],
            student_id= ns.payload['student_id']
        )
        db.session.add(parent_student)
        db.session.commit()
        return parent_student
  
@ns.route('/parent_student/<int:id>')
class Parent_Student_By_Id(Resource):
    
    @ns.marshal_with(parent_student_model)
    def get(self, id):
        parent_student= Parent_Student.query.get(id)
        return parent_student
    

#-------------------------Finance-------------------------

@ns.route('/finances')
class Finances(Resource):
    
    @ns.marshal_list_with(finance_model)
    def get(self):
        return Finance.query.all()
        
    @ns.expect(finance_model)
    @ns.marshal_with(finance_input_model)
    def post(self):
        finance = Finance(
            year= ns.payload['year'],
            tearm= ns.payload['tearm'],
            form= ns.payload['form'],
        )
        db.session.add(finance)
        db.session.commit()
        return finance, 201
  
@ns.route('/finance/<int:id>')
class FInance_By_Id(Resource):
    
    @ns.marshal_with(finance_model)
    def get(self, id):
        finance = Finance.query.get(id)
        return finance
    

#-------------------------Student Finance-------------------------

@ns.route('/students_finance')
class Student_finances(Resource):
    
    @ns.marshal_list_with(student_finance_model)
    def get(self):
        return Student_Finance.query.all()
        
    @ns.expect(student_finance_input_model)
    @ns.marshal_with(student_finance_model)
    def post(self):
        student_finance = Student_Finance(
            finance_id= ns.payload['finance_id'],
            admin_no= ns.payload['admin_no'],
            paid= ns.payload['paid'],
            balance= ns.payload['balance']
        )
        db.session.add(student_finance)
        db.session.commit()
        return student_finance, 201
  
@ns.route('/student_finance/<int:id>')
class Student_Finance_By_Id(Resource):
    
    @ns.marshal_with(student_finance_model)
    def get(self, id):
        student_finance = Student_Finance.query.get(id)
        return student_finance
    
    
#-------------------------Replacement-------------------------

@ns.route('/replacements')
class Replacements(Resource):
    
    @ns.marshal_list_with(replacement_model)
    def get(self):
        return Replacement.query.all()
        
    @ns.expect(replacement_input_model)
    @ns.marshal_with(replacement_model)
    def post(self):
        replacement = Replacement(
            finance_id= ns.payload['finance_id'],
            admin_no= ns.payload['admin_no'],
            item= ns.payload['item'],
            quantitiy= ns.payload['quantitiy'],
            amount= ns.payload['amount']
        )
        db.session.add(replacement)
        db.session.commit()
        return replacement, 201
  
@ns.route('/replacement/<int:id>')
class Replacement_By_Id(Resource):
    
    @ns.marshal_with(replacement_model)
    def get(self, id):
        replacement = Replacement.query.get(id)
        return replacement
    
#-------------------------Department-------------------------


@ns.route('/departments')
class Departments(Resource):
    
    @ns.marshal_list_with(department_model)
    def get(self):
        return Department.query.all()
        
    @ns.expect(department_input_model)
    @ns.marshal_with(department_input_model)
    def post(self):
        department = Department(
            name= ns.payload['name']
        )
        db.session.add(department)
        db.session.commit()
        return department, 201
  
    
@ns.route('/department/<int:id>')
class Department_By_Id(Resource):
    
    @ns.marshal_with(department_model)
    def get(self, id):
        department = Department.query.get(id)
        return department


#-------------------------Academic Department-------------------------

@ns.route('/academic_departments')
class Academic_Departments(Resource):
    
    @ns.marshal_list_with(academic_department_model)
    def get(self):
        return Academic_Department.query.all()
    
        
    @ns.expect(academic_department_input_model)
    @ns.marshal_with(academic_department_model)
    def post(self):
        academic_department = Academic_Department(
            subject= ns.payload['subject'],
            department_id= ns.payload['department_id'],
            head_id= ns.payload['head_id'],
            block= ns.payload['block'],
        )
        db.session.add(academic_department)
        db.session.commit()
        return academic_department, 201
 
  
@ns.route('/academic_department/<int:id>')
class Academic_Department_By_Id(Resource):
    
    @ns.marshal_with(academic_department_model)
    def get(self, id):
        academic_department = Academic_Department.query.get(id)
        return academic_department



#-------------------------Teacher Department-------------------------

@ns.route('/teacher_departments')
class Teachers_Departments(Resource):
    
    @ns.marshal_list_with(teacher_department_model)
    def get(self):
        return Teacher_Department.query.all()
        
    @ns.expect(teacher_department_input_model)
    @ns.marshal_with(teacher_department_model)
    def post(self):
        teacher_department = Teacher_Department(
            subject_id= ns.payload['subject_id'],
            teacher_id= ns.payload['teacher_id']
        )
        db.session.add(teacher_department)
        db.session.commit()
        return teacher_department, 201
  
    
@ns.route('/teacher_department/<int:id>')
class Teacher_Department_By_Id(Resource):
    
    @ns.marshal_with(teacher_department_model)
    def get(self, id):
        teacher_department = Teacher_Department.query.get(id)
        return teacher_department



#-------------------------Class-------------------------

@ns.route('/classes')
class Classes(Resource):
    
    @ns.marshal_list_with(class_model)
    def get(self):
        return Class.query.all()
    
        
    @ns.expect(class_input_model)
    @ns.marshal_with(class_model)
    def post(self):
        class1 = Class(
            form= ns.payload['form'],
            stream= ns.payload['stream'],
            teacher_id= ns.payload['teacher_id'],
            captain_id= ns.payload['captain_id']
        )
        db.session.add(class1)
        db.session.commit()
        return class1, 201
  
@ns.route('/class/<int:id>')
class Class_By_Id(Resource):
    
    @ns.marshal_with(class_model)
    def get(self, id):
        class1 = Class.query.get(id)
        return class1



#-------------------------Student Class-------------------------

@ns.route('/students_classes')
class Students_Classes(Resource):
    
    @ns.marshal_list_with(student_class_model)
    def get(self):
        return Student_Class.query.all()
        
    @ns.expect(student_class_input_model)
    @ns.marshal_with(student_class_model)
    def post(self):
        student_class = Student_Class(
            class_id= ns.payload['class_id'],
            student_id= ns.payload['student_id']
        )
        db.session.add(student_class)
        db.session.commit()
        return student_class, 201
  
    
@ns.route('/student_class/<int:id>')
class Student_Class_By_Id(Resource):
    
    @ns.marshal_with(student_class_model)
    def get(self, id):
        student_class = Student_Class.query.get(id)
        return student_class


#-------------------------Teacher Class-------------------------

@ns.route('/teachers_classes')
class Teachers_Classes(Resource):
    
    @ns.marshal_list_with(teacher_class_models)
    def get(self):
        return Teacher_Class.query.all()
        
    @ns.expect(teacher_class_input_models)
    @ns.marshal_with(teacher_class_models)
    def post(self):
        teacher_class = Teacher_Class(
            class_id= ns.payload['class_id'],
            teacher_id= ns.payload['teacher_id'],
            subject_id= ns.payload['subject_id'],
        )
        db.session.add(teacher_class)
        db.session.commit()
        return teacher_class, 201
  
    
@ns.route('/teacher_class/<int:id>')
class Teacher_Class_By_Id(Resource):
    
    @ns.marshal_with(teacher_class_models)
    def get(self, id):
        teacher_class = Teacher_Class.query.get(id)
        return teacher_class


#-------------------------Class Reps-------------------------

@ns.route('/classes_reps')
class Classes_Reps(Resource):
    
    @ns.marshal_list_with(class_rep_model)
    def get(self):
        return Class_Rep.query.all()
        
    @ns.expect(class_rep_input_model)
    @ns.marshal_with(class_rep_model)
    def post(self):
        class_rep = Class_Rep(
            class_id=ns.payload['class_id'],
            rep_id = ns.payload['rep_id']
        )
        db.session.add(class_rep)
        db.session.commit()
  
    
@ns.route('/class_rep/<int:id>')
class Class_rep_By_Id(Resource):
    
    @ns.marshal_with(class_rep_model)
    def get(self, id):
        rep = Class_Rep.query.get(id)
        return rep


#-------------------------Health-------------------------

@ns.route('/health')
class Health_api(Resource):
    
    @ns.marshal_list_with(health_model)
    def get(self):
        return Health.query.all()
        
    @ns.expect(health_input_model)
    @ns.marshal_with(health_model)
    def post(self):
        health = Health(
            head_id= ns.payload['head_id'],
            captain_id= ns.payload['captain_id']
        )
        db.session.add(health)
        db.session.commit()
        return health, 201
  
    
@ns.route('/health/<int:id>')
class Health_By_Id(Resource):
    
    @ns.marshal_with(health_model)
    def get(self, id):
        health = Health.query.get(id)
        return health


#-------------------------Medical Record-------------------------

@ns.route('/medical_records')
class Medical_Records(Resource):
    
    @ns.marshal_list_with(medical_record_model)
    def get(self):
        return Medical_Record.query.all()
        
    @ns.expect(medical_record_input_model)
    @ns.marshal_with(medical_record_model)
    def post(self):
        record = Medical_Record(
            medic_id= ns.payload['medic_id'],
            admin_no= ns.payload['admin_no'],
            symptoms= ns.payload['symptoms'],
            sickness= ns.payload['sickness'],
            sick_leave= ns.payload['sick_leave']
        )
        db.session.add(record)
        db.session.commit()
        return record, 201
  
    
@ns.route('/medical_record/<int:id>')
class Medical_record_By_Id(Resource):
    
    @ns.marshal_with(medical_record_model)
    def get(self, id):
        Medical_Record = Medical_Record.query.get(id)
        return Medical_Record


#-------------------------Drug-------------------------

@ns.route('/drugs')
class Drugs(Resource):
    
    @ns.marshal_list_with(drug_model)
    def get(self):
        return Drug.query.all()
        
    @ns.expect(drug_input_model)
    @ns.marshal_with(drug_model)
    def post(self):
        drug = Drug(
            medical_id= ns.payload['medical_id'],
            drug= ns.payload['drug'],
            dose= ns.payload['dose'],
            days= ns.payload['days'],
            complete= ns.payload['complete'],
        )
        db.session.add(drug)
        db.session.commit()
        return drug, 201
  
    
@ns.route('/drug/<int:id>')
class Drug_By_Id(Resource):
    
    @ns.marshal_with(drug_model)
    def get(self, id):
        drug = Drug.query.get(id)
        return drug


#-------------------------Dosage Day-------------------------

@ns.route('/dosage_days')
class Dosage_Days(Resource):
    
    @ns.marshal_list_with(dosage_day_model)
    def get(self):
        return Dosage_Day.query.all()
        
    @ns.expect(dosage_day_input_model)
    @ns.marshal_with(dosage_day_model)
    def post(self):
        dosage = Dosage_Day(
            drug_id= ns.payload['drug_id'],
            morning= ns.payload['morning'],
            afternoon= ns.payload['afternoon'],
            evening= ns.payload['evening'],
        )
        db.session.add(dosage)
        db.session.commit()
        return dosage, 201
  
    
@ns.route('/dosage_day/<int:id>')
class Dosage_Day_By_Id(Resource):
    
    @ns.marshal_with(dosage_day_model)
    def get(self, id):
        dose = Dosage_Day.query.get(id)
        return dose


#-------------------------Book Exchange-------------------------

@ns.route('/books_exchange')
class Books_Exchange(Resource):
    
    @ns.marshal_list_with(book_exchange_model)
    def get(self):
        return Book_Exchange.query.all()
        
    @ns.expect(book_exchange_input_model)
    @ns.marshal_with(book_exchange_model)
    def post(self):
        book = Book_Exchange(
            admin_no= ns.payload['admin_no'],
            size= ns.payload['size'],
            type= ns.payload['type'],
            quantity= ns.payload['quantity'],
        )
        db.session.add(book)
        db.session.commit()
        return book, 201
  
    
@ns.route('/book_exchange/<int:id>')
class Book_Exchange_By_Id(Resource):
    
    @ns.marshal_with(book_exchange_model)
    def get(self, id):
        book = Book_Exchange.query.get(id)
        return book


#-------------------------Teacher Exchange-------------------------
@ns.route('/teachers_exchange')
class Teachers_Exchange(Resource):
    
    @ns.marshal_list_with(teacher_exchange_model)
    def get(self):
        return Teacher_Exchange.query.all()
        
    @ns.expect(teacher_exchange_input_model)
    @ns.marshal_with(teacher_exchange_model)
    def post(self):
        teacher_exchange = Teacher_Exchange(
            teacher_id= ns.payload['teacher_id'],
            admin_no= ns.payload['admin_no'],
            item= ns.payload['item'],
            colour= ns.payload['colour'],
            quantity= ns.payload['quantity']
        )
        db.session.add(teacher_exchange)
        db.session.commit()
        return teacher_exchange, 201
  
    
@ns.route('/teacher_exchange/<int:id>')
class Teacher_Exchange_By_Id(Resource):
    
    @ns.marshal_with(teacher_exchange_model)
    def get(self, id):
        teacher_exchange = Teacher_Exchange.query.get(id)
        return teacher_exchange



#-------------------------Staff Exchange-------------------------

@ns.route('/staffs_exchange')
class Staffs_Exchange(Resource):
    
    @ns.marshal_list_with(staff_exchange_model)
    def get(self):
        return Staff_Exchange.query.all()
        
    @ns.expect(staff_exchange_input_model)
    @ns.marshal_with(staff_exchange_model)
    def post(self):
        stuff = Staff_Exchange(
            members_id= ns.payload['members_id'],
            item= ns.payload['item'],
            quantity= ns.payload['quantity'],
        )
        db.session.add(stuff)
        db.session.commit()
        return stuff, 201
  
    
@ns.route('/staff_exchange/<int:id>')
class Staff_Exchange_By_Id(Resource):
    
    @ns.marshal_with(staff_exchange_model)
    def get(self, id):
        stuff = Staff_Exchange.query.get(id)
        return stuff


#-------------------------Sport-------------------------

@ns.route('/sports')
class Sports(Resource):
    
    @ns.marshal_list_with(sport_model)
    def get(self):
        return Sport.query.all()
        
    @ns.expect(sport_input_model)
    @ns.marshal_with(sport_model)
    def post(self):
        sport = Sport(
            sport= ns.payload['sport'],
            captain_id= ns.payload['captain_id'],
            shod= ns.payload['shod'],
        )
        db.session.add(sport)
        db.session.commit()
        return sport, 201
  
    
@ns.route('/sport/<int:id>')
class Sport_By_Id(Resource):
    
    @ns.marshal_with(sport_model)
    def get(self, id):
        sport = Sport.query.get(id)
        return sport


#-------------------------Sport Detail-------------------------

@ns.route('/sports_details')
class Sports_Details(Resource):
    
    @ns.marshal_list_with(sport_detail_model)
    def get(self):
        return sport_Detail.query.all()
        
    @ns.expect(sport_detail_input_model)
    @ns.marshal_with(sport_detail_model)
    def post(self):
        detail = sport_Detail(
            sport_id= ns.payload['sport_id'],
            coach_id= ns.payload['coach_id'],
            captain_id= ns.payload['captain_id'],
        )
        db.session.add(detail)
        db.session.commit()
        return detail, 201
  
    
@ns.route('/sport_detail/<int:id>')
class Sport_Detail_By_Id(Resource):
    
    @ns.marshal_with(department_model)
    def get(self, id):
        detail = sport_Detail.query.get(id)
        return detail


#-------------------------sport Member-------------------------

@ns.route('/sports_members')
class Sports_Members(Resource):
    
    @ns.marshal_list_with(sport_member_model)
    def get(self):
        return Sport_Member.query.all()
        
    @ns.expect(sport_member_input_model)
    @ns.marshal_with(sport_member_model)
    def post(self):
        member = Sport_Member(
            sport_id= ns.payload['sport_id'],
            admin_id= ns.payload['admin_id'],
        )
        db.session.add(member)
        db.session.commit()
        return member, 201
  
    
@ns.route('/sport_member/<int:id>')
class Sport_Member_By_Id(Resource):
    
    @ns.marshal_with(sport_member_model)
    def get(self, id):
        member = Sport_Member.query.get(id)
        return member


#-------------------------club-------------------------

@ns.route('/clubs')
class Clubs(Resource):
    
    @ns.marshal_list_with(club_model)
    def get(self):
        return Club.query.all()
        
    @ns.expect(club_input_model)
    @ns.marshal_with(club_model)
    def post(self):
        club = Club(
            club= ns.payload['club'],
            captain_id= ns.payload['captain_id'],
            shod_id= ns.payload['shod_id'],
        )
        db.session.add(club)
        db.session.commit()
        return club, 201
  
    
@ns.route('/club/<int:id>')
class Club_By_Id(Resource):
    
    @ns.marshal_with(club_model)
    def get(self, id):
        club = Club.query.get(id)
        return club


#-------------------------Club Detail-------------------------

@ns.route('/clubs_details')
class Clubs_Details(Resource):
    
    @ns.marshal_list_with(club_detail_model)
    def get(self):
        return Club_Detail.query.all()
        
    @ns.expect(club_detail_input_model)
    @ns.marshal_with(club_detail_model)
    def post(self):
        detail = Club_Detail(
            club_id= ns.payload['club_id'],
            head_id= ns.payload['head_id'],
            captain_id= ns.payload['captain_id'],
        )
        db.session.add(detail)
        db.session.commit()
        return detail, 201
  
    
@ns.route('/club_detail/<int:id>')
class Club_Detail_By_Id(Resource):
    
    @ns.marshal_with(club_detail_model)
    def get(self, id):
        detail = Club_Detail.query.get(id)
        return detail


#-------------------------Club Member-------------------------

@ns.route('/clubs_members')
class Clubs_Members(Resource):
    
    @ns.marshal_list_with(club_member_model)
    def get(self):
        return Club_Member.query.all()
        
    @ns.expect(club_member_input_model)
    @ns.marshal_with(club_member_model)
    def post(self):
        member = Club_Member(
            club_id= ns.payload['club_id'],
            admin_id= ns.payload['admin_id'],
        )
        db.session.add(member)
        db.session.commit()
        return member
  
    
@ns.route('/club_member/<int:id>')
class Club_Member_By_Id(Resource):
    
    @ns.marshal_with(club_member_model)
    def get(self, id):
        member = Club_Member.query.get(id)
        return member


#-------------------------Block-------------------------

@ns.route('/blocks')
class Blocks(Resource):
    
    @ns.marshal_list_with(block_model)
    def get(self):
        return Block.query.all()
        
    @ns.expect(block_input_model)
    @ns.marshal_with(block_model)
    def post(self):
        block = Block(
            block= ns.payload['block'],
            master_id= ns.payload['master_id']
        )
        db.session.add(block)
        db.session.commit()
        return block, 201
  
    
@ns.route('/block/<int:id>')
class Block_By_Id(Resource):
    
    @ns.marshal_with(block_model)
    def get(self, id):
        block = Block.query.get(id)
        return block


#-------------------------Dorm-------------------------

@ns.route('/dorms')
class Dorms_Api(Resource):
    
    @ns.marshal_list_with(dorms_model)
    def get(self):
        return Dorms.query.all()
        
    @ns.expect(dorms_input_model)
    @ns.marshal_with(dorms_model)
    def post(self):
        dorm = Dorms(
            block_id= ns.payload['block_id'],
            house= ns.payload['house'],
            captain_id= ns.payload['captain_id'],
            master_id= ns.payload['master_id']
        )
        db.session.add(dorm)
        db.session.commit()
        return dorm, 201
  
    
@ns.route('/dorm/<int:id>')
class Dorm_By_Id(Resource):
    
    @ns.marshal_with(dorms_model)
    def get(self, id):
        dorm = Dorms.query.get(id)
        return dorm


#-------------------------Student Dorm-------------------------

@ns.route('/students_dorms')
class Students_Dorms(Resource):
    
    @ns.marshal_list_with(student_dorms_model)
    def get(self):
        return StudentDorms.query.all()
        
    @ns.expect(student_dorms_input_model)
    @ns.marshal_with(student_dorms_model)
    def post(self):
        student = StudentDorms(
            dorm_id= ns.payload['dorm_id'],
            cube= ns.payload['cube'],
            admin_no= ns.payload['admin_no']
        )
        db.session.add(student)
        db.session.commit()
        return student, 201
  
    
@ns.route('/student_dorm/<int:id>')
class Student_Dorm_By_Id(Resource):
    
    @ns.marshal_with(student_dorms_model)
    def get(self, id):
        student_dorm = StudentDorms.query.get(id)
        return student_dorm


api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
