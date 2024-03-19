from flask_restx import Api,fields
from models import *
# from app import api
api = Api(app)




#-------------------------Role-------------------------

role_model = api.model("Role", {
    "id": fields.Integer,
    "role": fields.String
})

role_input_model = api.model("Role", {
    "role": fields.String
})

#-------------------------Member-------------------------

member_model = api.model("Member", {
    "id": fields.Integer,
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "full_name": fields.String,
    "photo": fields.String,
    "date_of_birth": fields.DateTime,
    "age": fields.Integer,
    "gender": fields.String,
    "nationality": fields.String,
    "ethnicity": fields.String,
    "religion": fields.String,
    "home_address": fields.String,
    "phone_no": fields.String,
    "role_id": fields.Integer,
    "role": fields.String(attribute=lambda x: Role.query.get(x.role_id).role),
    "admission_date": fields.DateTime
})

member_input_model = api.model("Member", {
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
    "role_id": fields.Integer
})

#-------------------------Teacher-------------------------

teacher_model = api.model("Teacher", {
    "id": fields.Integer,
    "id_no": fields.Integer,
    "full_name": fields.String(attribute =lambda x: Member.query.get(x.id_no).full_name),
    "kcse": fields.String,
    "degree": fields.String,
    "license_by_tsc": fields.String,
    "experience": fields.String
})

Teacher_input_model = api.model("Teacher", {
    "id_no" : fields.Integer,
    "kcse": fields.String,
    "degree": fields.String,
    "license_by_tsc": fields.String,
    "experience": fields.String
})

#-------------------------Medic-------------------------

medic_model = api.model("Medic", {
    "id": fields.Integer,
    "id_no":fields.Integer,
    "full_name": fields.String(attribute =lambda x: Member.query.get(x.id_no).full_name),
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

#-------------------------Parent-------------------------

parent_model = api.model("Parent", {
    "id": fields.Integer,
    "id_no": fields.Integer,
    "first_name": fields.String,
    "full_name": fields.String,
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

#-------------------------Student-------------------------

student_model = api.model("Student", {
    "admin_no": fields.Integer,
    "first_name": fields.String,
    "middle_name": fields.String,
    "last_name": fields.String,
    "full_name": fields.String,
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

#-------------------------Parent Student-------------------------

parent_student_model = api.model("Parent_Student",{
    "id": fields.Integer,
    "parent_id": fields.Integer,
    "parent_name": fields.String(attribute = lambda x: Parent.query.get(x.parent_id).full_name),
    "student_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.student_id).full_name)
})

parent_student_input_model = api.model("Parent_Student",{
    "parent_id": fields.Integer,
    "student_id": fields.Integer
})

#-------------------------Finance-------------------------

finance_model = api.model("Finance", {
    "id": fields.Integer,
    "year": fields.Integer,
    "tearm": fields.String,
    "form": fields.Integer
})

#-------------------------Student Finance-------------------------

student_finance_model = api.model("Student_Finance",{
    "id": fields.Integer,
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
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

#-------------------------Replacement-------------------------

replacement_model = api.model("Replacemnt", {
    "id": fields.Integer,
    "finance_id": fields.Integer,
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
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

#-------------------------Department-------------------------

department_model = api.model("Department", {
    "id": fields.Integer,
    "name": fields.String
})

department_input_model = api.model("Department", {
    "name": fields.String
})

#-------------------------Academic Department-------------------------

academic_department_model = api.model("Academic_Department", {
    "id": fields.Integer,
    "subject": fields.String,
    "department_id": fields.Integer,
    "head_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.head_id).full_name),
    "block": fields.String
})

academic_department_input_model = api.model("Academic_Department", {
    "subject": fields.String,
    "department_id": fields.Integer,
    "head_id": fields.Integer,
    "block": fields.String
})

#-------------------------Teacher Department-------------------------

teacher_department_model = api.model("Teacher_Department", {
    "id": fields.Integer,
    "subject_id": fields.String,
    "teacher_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.teacher_id).full_name),
})

teacher_department_input_model = api.model("Teacher_Department", {
    "subject_id": fields.String,
    "teacher_id": fields.Integer
})

#-------------------------Class-------------------------

class_model = api.model("Class", {
    "id": fields.Integer,
    "form": fields.Integer,
    "stream": fields.String,
    "teacher_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.teacher_id).full_name),
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
})

class_input_model = api.model("Class", {
    "form": fields.Integer,
    "stream": fields.String,
    "teacher_id": fields.Integer,
    "captain_id": fields.Integer
})

#-------------------------Student Class-------------------------

student_class_model = api.model("Student_Class", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "student_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.student_id).full_name),
})

student_class_input_model = api.model("Student_Class", {
    "class_id": fields.Integer,
    "student_id": fields.Integer
})

#-------------------------Teacher Class-------------------------

teacher_class_models = api.model("Teacher_Class", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "teacher_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.teacher_id).full_name),
    "subject_id": fields.String,
})

teacher_class_input_models = api.model("Teacher_Class", {
    "class_id": fields.Integer,
    "teacher_id": fields.Integer,
    "subject_id": fields.String
})

#-------------------------Class Reps-------------------------

class_rep_model = api.model("Class_Rep", {
    "id": fields.Integer,
    "class_id": fields.Integer,
    "rep_id": fields.Integer
})

class_rep_input_model = api.model("Class_Rep", {
    "class_id": fields.Integer,
    "rep_id": fields.Integer
})

#-------------------------Health-------------------------

health_model = api.model("Health", {
    "id": fields.Integer,
    "head_id": fields.Integer,
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name)
})

health_input_model = api.model("Health", {
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

#-------------------------Medical Record-------------------------

medical_record_model = api.model("Medical_Record", {
    "id": fields.Integer,
    "medic_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.medic_id).full_name),
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
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

#-------------------------Drug-------------------------

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

#-------------------------Dosage Day-------------------------

dosage_day_model =api.model("Dosage_Day",{
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

#-------------------------Book Exchange-------------------------

book_exchange_model = api.model("Book_Exchange", {
    "id": fields.Integer,
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
    "size": fields.String,
    "type": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

book_exchange_input_model = api.model("Book_Exchange", {
    "admin_no": fields.Integer,
    "size": fields.String,
    "type": fields.String,
    "quantity": fields.Integer,
})

#-------------------------Teacher Exchange-------------------------

teacher_exchange_model = api.model("Teacher_Exchange", {
    "id": fields.Integer,
    "teacher_id": fields.Integer,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.teacher_id).full_name),
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
    "item": fields.String,
    "colour": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

teacher_exchange_input_model = api.model("Teacher_Exchange", {
    "teacher_id": fields.Integer,
    "admin_no": fields.Integer,
    "item": fields.String,
    "colour": fields.String,
    "quantity": fields.Integer,
})

#-------------------------Staff Exchange-------------------------

staff_exchange_model = api.model("Staff_Exchange", {
    "id": fields.Integer,
    "member_id": fields.Integer,
    "member_name": fields.String(attribute =lambda x: Member.query.get(x.member_id).full_name),
    "item": fields.String,
    "quantity": fields.Integer,
    "date": fields.DateTime
})

staff_exchange_input_model = api.model("Staff_Exchange", {
    "member_id": fields.Integer,
    "item": fields.String,
    "quantity": fields.Integer,
})

#-------------------------Sport-------------------------

sport_model = api.model("Sport", {
    "id": fields.Integer,
    "sport": fields.String,
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
    "shod": fields.String,
    "Teacher_name": fields.String(attribute =lambda x: Member.query.get(x.shod).full_name),
})

sport_input_model = api.model("Sport", {
    "sport": fields.String,
    "captain_id": fields.Integer,
    "shod": fields.String
})

#-------------------------Sport Detail-------------------------

sport_detail_model = api.model("Sport_Detail", {
    "id": fields.Integer,
    "sport_id": fields.Integer,
    "coach_id": fields.Integer,
    "coach_name": fields.String(attribute =lambda x: Member.query.get(x.coach_id).full_name),
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
})

sport_detail_input_model = api.model("Sport_Detail", {
    "sport_id": fields.Integer,
    "coach_id": fields.Integer,
    "captain_id": fields.Integer
})

#-------------------------sport Member-------------------------

sport_member_model = api.model("Sport_Member", {
    "id": fields.Integer,
    "sport_id": fields.Integer,
    "admin_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
})

sport_member_input_model = api.model("Sport_Member", {
    "sport_id": fields.Integer,
    "admin_id": fields.Integer
})

#-------------------------club-------------------------

club_model = api.model("Club", {
    "id": fields.Integer,
    "sport": fields.String,
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
    "shod": fields.String,
    "shod_name": fields.String(attribute =lambda x: Member.query.get(x.shod_id).full_name),
})

club_input_model = api.model("Club", {
    "club": fields.String,
    "captain_id": fields.Integer,
    "shod_id": fields.String
})

#-------------------------Club Detail-------------------------

club_detail_model = api.model("Club_Detail", {
    "id": fields.Integer,
    "club_id": fields.Integer,
    "head_id": fields.Integer,
    "head_name": fields.String(attribute =lambda x: Member.query.get(x.head_id).full_name),
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
})

club_detail_input_model = api.model("Club_Detail", {
    "club_id": fields.Integer,
    "head_id": fields.Integer,
    "captain_id": fields.Integer
})

#-------------------------Club Member-------------------------

club_member_model = api.model("Club_Member", {
    "id": fields.Integer,
    "club_id": fields.Integer,
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.admin_no).full_name),
})

club_member_input_model = api.model("Club_Member", {
    "club_id": fields.Integer,
    "admin_no": fields.Integer
})

#-------------------------Block-------------------------

block_model = api.model("Block", {
    "id": fields.Integer,
    "block": fields.String,
    "master_id": fields.Integer,
    "master_name": fields.String(attribute =lambda x: Member.query.get(x.master_id).full_name),
})

block_input_model = api.model("Block", {
    "block": fields.String,
    "master_id": fields.Integer
})

#-------------------------Dorm-------------------------

dorms_model = api.model("Dorms", {
    "id": fields.Integer,
    "block_id": fields.Integer,
    "house": fields.String,
    "captain_id": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
    "master_id": fields.Integer,
    "master_name": fields.String(attribute =lambda x: Member.query.get(x.master_id).full_name),
})

dorms_input_model = api.model("Dorms", {
    "block_id": fields.Integer,
    "house": fields.String,
    "captain_id": fields.Integer,
    "master_id": fields.Integer
})

#-------------------------Student Dorm-------------------------

student_dorms_model = api.model("StudentDorms", {
    "id": fields.Integer,
    "dorm_id": fields.Integer,
    "cube": fields.Integer,
    "admin_no": fields.Integer,
    "student_name": fields.String(attribute = lambda x: Student.query.get(x.captain_id).full_name),
})

student_dorms_input_model = api.model("StudentDorms", {
    "dorm_id": fields.Integer,
    "cube": fields.Integer,
    "admin_no": fields.Integer
})

