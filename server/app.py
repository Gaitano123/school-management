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
    "id": fields.Integer,
    "role": fields.String
})

role_input_model = api.model("Role", {
    "role": fields.String
})

memeber_model = api.model("Member", {
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "photo": fields.String,
    "date_of_birth": fields.datetime,
    "age": fields.Integer,
    "gender": fields.String,
    "nationality": fields.String,
    "ethnicity": fields.String,
    "religion": fields.String,
    "home_address": fields.String,
    "phone_no": fields.String,
    "role_id": fields.Integer,
    "role": fields.String(attribute=lambda x: Role.query.get(x.role_id).role),
})

memeber_input_model = api.model("Member", {
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "photo": fields.String,
    "date_of_birth": fields.datetime,
    "age": fields.Integer,
    "gender": fields.String,
    "nationality": fields.String,
    "ethnicity": fields.String,
    "religion": fields.String,
    "home_address": fields.String,
    "phone_no": fields.String,
    "role_id": fields.Integer
})

teacher_model = api.model("Teacher", {
    "id": fields.Integer,
    "id_no": fields.Integer,
    "kcse": fields.String,
    "degree": fields.String,
    "license_by_tsc": fields.String,
    "experience": fields.String
})

Teacher_input_model = api.model("Teacher", {
    
})

medic_model = api.model("Medic", {
    
})

medic_input_model = api.model("Medic", {
    
})

parent_model = api.model("Parent", {
    
})

parent_input_model = api.model("Parent", {
    
})

student_model = api.model("Student", {
    
})

student_input_model = api.model("Student", {
    
})

parent_student_model = api.model("Parent_Student",{
    
})

parent_student_input_model = api.model("Parent_Student",{
    
})

finance_model = api.model("Finance", {
    
})

student_finance_model = api.model("Student_Finance",{
    
})

student_finance_input_model = api.model("Student_Finance",{
    
})

replacement_model = api.model("Replacemnt", {
    
})

replacement_input_model = api.model("Replacemnt", {
    
})

department_model = api.model("Department", {
    
})

department_input_model = api.model("Department", {
    
})

academic_department_model = api.model("Academic_Department", {
    
})

academic_department_input_model = api.model("Academic_Department", {
    
})

teacher_department_model = api.model("Teacher_Department", {
    
})

teacher_department_input_model = api.model("Teacher_Department", {
    
})

class_model = api.model("Class", {
    
})

class_input_model = api.model("Class", {
    
})

student_class_model = api.model("Student_Class", {
    
})

student_class_input_model = api.model("Student_Class", {
    
})

teacher_class_models = api.model("Teacher_Class", {
    
})

teacher_class_input_models = api.model("Teacher_Class", {
    
})

class_rep_model = api.model("Class_Rep", {
    
})

class_rep_input_model = api.model("Class_Rep", {
    
})

health_model = api.model("Health", {
    
})

health_input_model = api.model("Health", {
    
})

medical_record_model = api.model("Medical_Record", {
    
})

medical_record_input_model = api.model("Medical_Record", {
    
})

drug_model = api.model("Drug", {
    
})

drug_input_model = api.model("Drug", {
    
})

dosage_day_mode =api.model("Dosage_Day",{
    
})

dosage_day_input_mode =api.model("Dosage_Day",{
    
})

book_exchange_model = api.models("Book_Exchange", {
    
})

book_exchange_input_model = api.models("Book_Exchange", {
    
})

teacher_exchange_model = api.models("Teacher_Exchange", {
    
})

teacher_exchange_input_model = api.models("Teacher_Exchange", {
    
})

staff_exchange_model = api.models("Staff_Exchange", {
    
})

staff_exchange_input_model = api.models("Staff_Exchange", {
    
})

sport_model = api.models("Sport", {
    
})

sport_input_model = api.models("Sport", {
    
})

sport_detail_model = api.model("Sport_Detail", {
    
})

sport_detail_input_model = api.model("Sport_Detail", {
    
})

sport_member_model = api.model("Sport_Member", {
    
})

sport_member_input_model = api.model("Sport_Member", {
    
})

sport_model = api.models("Sport", {
    
})

club_input_model = api.models("Club", {
    
})

club_detail_model = api.model("Club_Detail", {
    
})

club_detail_input_model = api.model("Club_Detail", {
    
})

club_member_model = api.model("Club_Member", {
    
})

club_member_input_model = api.model("Club_Member", {
    
})

block_model = api.models("Block", {
    
})

block_input_model = api.models("Block", {
    
})

dorms_model = api.models("Dorms", {
    
})

dorms_input_model = api.models("Dorms", {
    
})

student_dorms_model = api.models("StudentDorms", {
    
})

student_dorms_input_model = api.models("StudentDorms", {
    
})



api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
