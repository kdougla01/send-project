from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField
from wtforms.validators import DataRequired

class addStudentForm(FlaskForm):
	stuId = StringField('Id', validators=[DataRequired()])
	stuFirstName = StringField('First Name', validators=[DataRequired()])
	stuLastName = StringField('Last Name', validators=[DataRequired()])
	stuGender = StringField('Gender', validators=[DataRequired()])
	stuYearGroup = IntegerField('Year Group', validators=[DataRequired()])
	stuFormClass = StringField('Form Class', validators=[DataRequired()])
	stuSenStatus = StringField('Sen Status', validators=[DataRequired()])
	stuBarrier = StringField('Barrier', validators=[DataRequired()])
	stuReadingAge = StringField('Reading Age', validators=[DataRequired()])
	stuFullDescription = TextField('Full Description', validators=[DataRequired()])


class searchStudentForm(FlaskForm):
	stuFirstName = StringField('stuFirstName')