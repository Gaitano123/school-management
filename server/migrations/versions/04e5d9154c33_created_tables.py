"""created tables

Revision ID: 04e5d9154c33
Revises: 
Create Date: 2024-03-13 10:42:56.751979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04e5d9154c33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('finances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('tearm', sa.String(), nullable=True),
    sa.Column('form', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_no', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_no', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('admin_no', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('ethnicity', sa.String(), nullable=True),
    sa.Column('religion', sa.String(), nullable=True),
    sa.Column('home_address', sa.String(), nullable=True),
    sa.Column('phone_no', sa.String(), nullable=True),
    sa.Column('prev_school_name', sa.String(), nullable=True),
    sa.Column('prev_school_address', sa.String(), nullable=True),
    sa.Column('kcpe', sa.Integer(), nullable=True),
    sa.Column('blood_group', sa.String(), nullable=True),
    sa.Column('immunization_records', sa.String(), nullable=True),
    sa.Column('allergies', sa.String(), nullable=True),
    sa.Column('emergency_contact', sa.String(), nullable=True),
    sa.Column('birth_no', sa.Integer(), nullable=True),
    sa.Column('leaving_cert', sa.String(), nullable=True),
    sa.Column('special_needs', sa.String(), nullable=True),
    sa.Column('admission_date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('admin_no')
    )
    op.create_table('exercise_book_exchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('size', sa.String(length=3), nullable=True),
    sa.Column('type', sa.String(length=2), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('ethnicity', sa.String(), nullable=True),
    sa.Column('religion', sa.String(), nullable=True),
    sa.Column('home_address', sa.String(), nullable=True),
    sa.Column('phone_no', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent_students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parents.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.admin_no'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('replacements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('finance_id', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('quantitiy', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['finance_id'], ['finances.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_finances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('finance_id', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('paid', sa.Integer(), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['finance_id'], ['finances.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_no', sa.Integer(), nullable=True),
    sa.Column('license', sa.String(), nullable=True),
    sa.Column('degree', sa.String(), nullable=True),
    sa.Column('experience', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_no'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff_excahnge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_no', sa.Integer(), nullable=True),
    sa.Column('kcse', sa.String(), nullable=True),
    sa.Column('degree', sa.String(), nullable=True),
    sa.Column('license_by_tsc', sa.String(), nullable=True),
    sa.Column('experience', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_no'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('academic_departments',
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('head_id', sa.Integer(), nullable=True),
    sa.Column('block', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['head_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('subject')
    )
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block', sa.String(), nullable=True),
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['master_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form', sa.Integer(), nullable=True),
    sa.Column('stream', sa.String(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.Column('class_reps', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clubs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('club', sa.String(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.Column('shod_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['shod_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('head_id', sa.Integer(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['head_id'], ['medics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medical_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medic_id', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('symptoms', sa.String(), nullable=True),
    sa.Column('sickness', sa.String(), nullable=True),
    sa.Column('sick_leave', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['medic_id'], ['medics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport', sa.String(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.Column('shod', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['shod'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers_exchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('colour', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class_reps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('rep_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['rep_id'], ['parents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('club_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('club_id', sa.Integer(), nullable=True),
    sa.Column('head_id', sa.Integer(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], ),
    sa.ForeignKeyConstraint(['head_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('club_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('club_id', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dorms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=True),
    sa.Column('house', sa.String(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], ),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['master_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drugs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medical_id', sa.Integer(), nullable=True),
    sa.Column('drug', sa.String(), nullable=True),
    sa.Column('dose', sa.String(), nullable=True),
    sa.Column('days', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['medical_id'], ['medical_records.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport_id', sa.Integer(), nullable=True),
    sa.Column('coach_id', sa.Integer(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['coach_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['sport_id'], ['sports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['sport_id'], ['sports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.admin_no'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['subject'], ['academic_departments.subject'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher_departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subject'], ['academic_departments.subject'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dosage_days',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.Column('morning', sa.Boolean(), nullable=True),
    sa.Column('afternoon', sa.Boolean(), nullable=True),
    sa.Column('evening', sa.Boolean(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_dorms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dorm_id', sa.Integer(), nullable=True),
    sa.Column('cube', sa.Integer(), nullable=True),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_no'], ['students.admin_no'], ),
    sa.ForeignKeyConstraint(['dorm_id'], ['dorms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_dorms')
    op.drop_table('dosage_days')
    op.drop_table('teacher_departments')
    op.drop_table('teacher_classes')
    op.drop_table('student_classes')
    op.drop_table('sport_members')
    op.drop_table('sport_details')
    op.drop_table('drugs')
    op.drop_table('dorms')
    op.drop_table('club_members')
    op.drop_table('club_details')
    op.drop_table('class_reps')
    op.drop_table('teachers_exchange')
    op.drop_table('sports')
    op.drop_table('medical_records')
    op.drop_table('health')
    op.drop_table('clubs')
    op.drop_table('classes')
    op.drop_table('blocks')
    op.drop_table('academic_departments')
    op.drop_table('teachers')
    op.drop_table('staff_excahnge')
    op.drop_table('medics')
    op.drop_table('student_finances')
    op.drop_table('replacements')
    op.drop_table('parent_students')
    op.drop_table('members')
    op.drop_table('exercise_book_exchange')
    op.drop_table('students')
    op.drop_table('roles')
    op.drop_table('parents')
    op.drop_table('finances')
    op.drop_table('departments')
    # ### end Alembic commands ###