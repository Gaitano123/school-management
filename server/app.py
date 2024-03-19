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
    
    
@ns.route('/student_dorm/<int:id>')
class Student_Dorm_By_Id(Resource):
    
    @ns.marshal_with(student_dorms_model)
    def get(self, id):
        student_dorm = StudentDorms.query.get(id)
        return student_dorm





















api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
