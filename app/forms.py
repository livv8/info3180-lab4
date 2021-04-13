from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from wtforms import SubmitField

class MyForm(UploadForm):
    file = FileField('file', validators=[DataRequired()])
    submit= SubmitField ('Submit', validators= [DataRequired()])
    
    