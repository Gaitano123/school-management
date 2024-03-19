# from server.__init__ import app
from flask_migrate import Migrate
from flask_restx import Api, fields, Namespace, Resource
# from server.models import db,app

from models import *

app.config['SECRET_KEY'] = 'bb8f7de46cd4426ebf5ca7df06d43665'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

ns =Namespace("api")

role_model = api.model("Role", {
    "id": fields.integer,
    "role": fields.string
})

role_input_model = api.model("Role", {
    "role": fields.string
})

memeber_model = api.model("Member", {
    "first_name": fields.string,
    "middle_name": fields.string,
    "last_name": fields.string,
    "photo": fields.string,
    "date_of_birth": fields.datetime,
    "age": fields.integer,
    "gender": fields.string,
    "nationality": fields.string,
    "ethnicity": fields.string,
    "religion": fields.string,
    "home_address": fields.string,
    "phone_no": fields.string,
    "role_id": fields.integer,
    "role": fields.string(attribute=lambda x: Role.query.get(x.role_id).role),
})

memeber_input_model = api.model("Member", {
    "first_name": fields.string,
    "middle_name": fields.string,
    "last_name": fields.string,
    "photo": fields.string,
    "date_of_birth": fields.datetime,
    "age": fields.integer,
    "gender": fields.string,
    "nationality": fields.string,
    "ethnicity": fields.string,
    "religion": fields.string,
    "home_address": fields.string,
    "phone_no": fields.string,
    "role_id": fields.integer
})

teacher_model = api.model("Teacher", {
    "id": fields.integer,
    "id_no": fields.integer,
    "kcse": fields.string,
    "degree": fields.string,
    "license_by_tsc": fields.string,
    "experience": fields.string
})

Teacher_input_model = api.model("Teacher", {

    "id_no" : fields.integer,
    "kcse": fields.string,
    "degree": fields.string,
    "license_by_tsc": fields.string,
    "experience": fields.string
})

medic_model = api.model("Medic", {
    "id": fields.Integer,
    "id_no":fields.Integer,
    "license":fields.String,
    "degree":fields.String,
    "experience":fields.String
})

medic_input_model = api.model("Medic", {
    "id_no":fields.Integer,
    "license":fields.String,
    "degree":fields.String,
    "experience":fields.String
    
})

parent_model = api.model("Parent", {
     "id": fields.Integer,
    "id_no": fields.Integer,
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "phone_no": fields.String,
    "gender": fields.String
})

parent_input_model = api.model("Parent", {
    "id_no": fields.Integer,
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "phone_no": fields.String,
    "gender": fields.String
})

student_model = api.model("Student", {
    "admin_no": fields.Integer,
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "photo": fields.String,
    "date_of_birth": fields.DateTime,
    "age": fields.Integer,
    "gender": fields.String,
    "nationality": fields.String,
    "ethnicity": fields.String,
    "religion": fields.String,
    "home_address": fields.String,
    "phone_no": fields.String,
    "prev_school_name": fields.String,
    "prev_school_address": fields.String,
    "kcpe": fields.Integer,
    "blood_group": fields.String,
    "immunization_records": fields.String,
    "allergies": fields.String,
    "emergency_contact": fields.String,
    "birth_no": fields.Integer,
    "leaving_cert": fields.String,
    "special_needs": fields.String,
    "admission_date": fields.DateTime
})

student_input_model = api.model("Student", {
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "photo": fields.String,
    "date_of_birth": fields.String,
    "gender": fields.String,
    "nationality": fields.String,
    "ethnicity": fields.String,
    "religion": fields.String,
    "home_address": fields.String,
    "phone_no": fields.String,
    "prev_school_name": fields.String,
    "prev_school_address": fields.String,
    "kcpe": fields.Integer,
    "blood_group": fields.String,
    "immunization_records": fields.String,
    "allergies": fields.String,
    "emergency_contact": fields.String,
    "birth_no": fields.Integer,
    "leaving_cert": fields.String,
    "special_needs": fields.String
})

parent_student_model = api.model("Parent_Student",{
    "id": fields.Integer,
    "parent_id": fields.Integer,
    "student_id": fields.Integer
})

parent_student_input_model = api.model("Parent_Student",{
    "parent_id": fields.Integer,
    "student_id": fields.Integer
})

finance_model = api.model("Finance", {
    "id": fields.Integer,
    "year": fields.Integer,
    "tearm": fields.String,
    "form": fields.Integer
})

student_finance_model = api.model("Student_Finance",{
    "id": fields.Integer,
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "paid": fields.Integer,
    "balance": fields.Integer,
    "date": fields.DateTime
})

student_finance_input_model = api.model("Student_Finance",{
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "paid": fields.Integer,
    "balance": fields.Integer
})

replacement_model = api.model("Replacemnt", {
    "id": fields.Integer,
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "item": fields.String,
    "quantitiy": fields.Integer,
    "amount": fields.Integer,
    "date": fields.DateTime
})

replacement_input_model = api.model("Replacemnt", {
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "item": fields.String,
    "quantitiy": fields.Integer,
    "amount": fields.Integer
})

department_model = api.model("Department", {
    "id": fields.Integer,
    "name": fields.String
})

department_input_model = api.model("Department", {
    "name": fields.String
})

academic_department_model = api.model("Academic_Department", {
    "id": fields.Integer,
    "subject": fields.String,
    "department_id": fields.Integer,
    "head_id": fields.Integer,
    "block": fields.String
})

academic_department_input_model = api.model("Academic_Department", {
    "subject": fields.String,
    "department_id": fields.Integer,
    "head_id": fields.Integer,
    "block": fields.String
})

teacher_department_model = api.model("Teacher_Department", {
    "id": fields.Integer,
    "subject_id": fields.String,
    "teacher_id": fields.Integer
})

teacher_department_input_model = api.model("Teacher_Department", {
    "subject_id": fields.String,
    "teacher_id": fields.Integer
})

class_model = api.model("Class", {
    "id": fields.Integer,
    "form": fields.Integer,
    "stream": fields.String,
    "teacher_id": fields.Integer,
    "captain_id": fields.Integer
})

class_input_model = api.model("Class", {
    "form": fields.Integer,
    "stream": fields.String,
    "teacher_id": fields.Integer,
    "captain_id": fields.Integer
})

student_class_model = api.model("Student_Class", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "student_id": fields.Integer
})

student_class_input_model = api.model("Student_Class", {
    "class_id": fields.Integer,
    "student_id": fields.Integer
})

teacher_class_models = api.model("Teacher_Class", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "teacher_id": fields.Integer,
    "subject_id": fields.String
})

teacher_class_input_models = api.model("Teacher_Class", {
    "class_id": fields.Integer,
    "teacher_id": fields.Integer,
    "subject_id": fields.String
})

class_rep_model = api.model("Class_Rep", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "rep_id": fields.Integer
})

class_rep_input_model = api.model("Class_Rep", {
    "class_id": fields.Integer,
    "rep_id": fields.Integer
})

health_model = api.model("Health", {
    "id": fields.Integer,
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

health_input_model = api.model("Health", {
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

medical_record_model = api.model("Medical_Record", {
    "id": fields.Integer,
    "medic_id": fields.Integer,
    "admin_no": fields.Integer,
    "symptoms": fields.String,
    "sickness": fields.String,
    "sick_leave": fields.String,
    "date": fields.DateTime
})

medical_record_input_model = api.model("Medical_Record", {
    "medic_id": fields.Integer,
    "admin_no": fields.Integer,
    "symptoms": fields.String,
    "sickness": fields.String,
    "sick_leave": fields.String,
    "date": fields.DateTime
})

drug_model = api.model("Drug", {
    "id": fields.Integer,
    "medical_id": fields.Integer,
    "drug": fields.String,
    "dose": fields.String,
    "days": fields.Integer,
    "complete": fields.Boolean
})

drug_input_model = api.model("Drug", {
    "medical_id": fields.Integer,
    "drug": fields.String,
    "dose": fields.String,
    "days": fields.Integer,
    "complete": fields.Boolean
})

dosage_day_mode =api.model("Dosage_Day",{
    "id": fields.Integer,
    "drug_id": fields.Integer,
    "morning": fields.Boolean,
    "afternoon": fields.Boolean,
    "evening": fields.Boolean,
    "date": fields.DateTime
})

dosage_day_input_mode =api.model("Dosage_Day",{
    "drug_id": fields.Integer,
    "morning": fields.Boolean,
    "afternoon": fields.Boolean,
    "evening": fields.Boolean,
    "date": fields.DateTime
})

book_exchange_model = api.models("Book_Exchange", {
    "id": fields.Integer,
    "admin_no": fields.Integer,
    "size": fields.String,
    "type": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

book_exchange_input_model = api.models("Book_Exchange", {
    "admin_no": fields.Integer,
    "size": fields.String,
    "type": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

teacher_exchange_model = api.models("Teacher_Exchange", {
    "id": fields.Integer,
    "teacher_id": fields.Integer,
    "admin_no": fields.Integer,
    "item": fields.String,
    "colour": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

teacher_exchange_input_model = api.models("Teacher_Exchange", {
    "teacher_id": fields.Integer,
    "admin_no": fields.Integer,
    "item": fields.String,
    "colour": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

staff_exchange_model = api.models("Staff_Exchange", {
    "id": fields.Integer,
    "member_id": fields.Integer,
    "item": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

staff_exchange_input_model = api.models("Staff_Exchange", {
    "member_id": fields.Integer,
    "item": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

sport_model = api.models("Sport", {
    "id": fields.Integer,
    "sport": fields.String,
    "captain_id": fields.Integer,
    "shod": fields.String
})

sport_input_model = api.models("Sport", {
    "sport": fields.String,
    "captain_id": fields.Integer,
    "shod": fields.String
})

sport_detail_model = api.model("Sport_Detail", {
    "id": fields.Integer,
    "sport_id": fields.Integer,
    "coach_id": fields.Integer,
    "captain_id": fields.Integer
})

sport_detail_input_model = api.model("Sport_Detail", {
    "sport_id": fields.Integer,
    "coach_id": fields.Integer,
    "captain_id": fields.Integer
})

sport_member_model = api.model("Sport_Member", {
    "id": fields.Integer,
    "sport_id": fields.Integer,
    "admin_id": fields.Integer
})

sport_member_input_model = api.model("Sport_Member", {
    "sport_id": fields.Integer,
    "admin_id": fields.Integer
})

sport_model = api.models("Sport", {
    "id": fields.Integer,
    "sport": fields.String,
    "captain_id": fields.Integer,
    "shod": fields.String
})

club_input_model = api.models("Club", {
    "club": fields.String,
    "captain_id": fields.Integer,
    "shod_id": fields.String
})

club_detail_model = api.model("Club_Detail", {
    "id": fields.Integer,
    "club_id": fields.Integer,
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

club_detail_input_model = api.model("Club_Detail", {
    "club_id": fields.Integer,
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

club_member_model = api.model("Club_Member", {
    "id": fields.Integer,
    "club_id": fields.Integer,
    "admin_no": fields.Integer
})

club_member_input_model = api.model("Club_Member", {
    "club_id": fields.Integer,
    "admin_no": fields.Integer
})

block_model = api.models("Block", {
     "id": fields.Integer,
    "block": fields.String,
    "master_id": fields.Integer
})

block_input_model = api.models("Block", {
    "block": fields.String,
    "master_id": fields.Integer
})

dorms_model = api.models("Dorms", {
    "id": fields.Integer,
    "block_id": fields.Integer,
    "house": fields.String,
    "captain_id": fields.Integer,
    "master_id": fields.Integer
})

dorms_input_model = api.models("Dorms", {
    "block_id": fields.Integer,
    "house": fields.String,
    "captain_id": fields.Integer,
    "master_id": fields.Integer
})

student_dorms_model = api.models("StudentDorms", {
    "id": fields.Integer,
    "dorm_id": fields.Integer,
    "cube": fields.Integer,
    "admin_no": fields.Integer
})

student_dorms_input_model = api.models("StudentDorms", {
    "dorm_id": fields.Integer,
    "cube": fields.Integer,
    "admin_no": fields.Integer
})



api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
