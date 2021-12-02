from typing import ValuesView
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet Name", validators = [InputRequired(message = "Please enter a pet name")])
    species = SelectField("Pet Species", choices = [('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField("Pet Image URL", validators = [Optional(), URL(message = "Please enter a valid URL")])
    age = IntegerField("Age of Pet", validators = [Optional(), NumberRange(min = 0, max = 30, message = "Age must be between 0 and 30")])
    notes = StringField("Notes", validators = [Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)],)

    available = BooleanField("Available?")