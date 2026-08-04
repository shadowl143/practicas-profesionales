from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, DateField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileAllowed
from wtforms import SubmitField

class ReporteForm(FlaskForm):
    nombre_reporte = StringField("Nombre", validators=[DataRequired()])
    fecha_alta = DataRequired("Fecha")
    solicitado_por = StringField("solicitado", validators=[DataRequired()])
    dirigido_por = StringField("dirigido", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])
    submit = SubmitField("Enviar")