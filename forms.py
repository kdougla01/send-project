from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired

class addStudentForm(FlaskForm):
	stuId = StringField('Id', validators=[DataRequired()])
	stuFirstName = StringField('First Name', validators=[DataRequired()])
	stuLastName = StringField('Last Name', validators=[DataRequired()])
	stuGender = StringField('Gender', validators=[DataRequired()])
	stuYearGroup = IntegerField('Year Group', validators=[DataRequired()])
	stuFormClass = StringField('Form Class', validators=[DataRequired()])
	stuSenStatus = StringField('Sen Status', validators=[DataRequired()])
	#stuBarrier = StringField('Barrier', validators=[DataRequired()])
	stuBarrier = SelectField(u'Barrier', choices=[('asd', 'Autistic Spectrum Disorder'), ('cp', 'Child Protection'), ('med', 'Medical')])
	stuReadingAge = StringField('Reading Age', validators=[DataRequired()])
	stuFullDescription = TextField('Full Description', validators=[DataRequired()])
	submit = SubmitField('Submit')


class addBarrierForm(FlaskForm):
	barId = StringField('Id', validators=[DataRequired()])
	barName = StringField('Barrier Name', validators=[DataRequired()])
	barAcro = StringField('Barrier Acronym', validators=[DataRequired()])
	barInfo = StringField('Barrier Info', validators=[DataRequired()])
	submit = SubmitField('Submit')

class editStudentForm(FlaskForm):
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
	submit = SubmitField('Submit')



class searchStudentForm(FlaskForm):
	stuFirstName = StringField('stuFirstName')