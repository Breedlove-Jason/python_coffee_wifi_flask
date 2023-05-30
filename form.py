from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=[('0', 'x'), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'),
                                         ('☕☕☕☕☕', '☕☕☕☕☕')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating',
                              choices=[('0', 'x'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                                       ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=[('0', 'x'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                                        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')
