from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class Form(Form):
    date = StringField('Fecha', validators=[DataRequired()])
    type = SelectField(u'Tipo', choices=[('1', 'Caja'), ('2', 'Bandeja'), ('3', 'Racimo')])
    zona = SelectField(u'Zona', coerce=str)
    hacienda = SelectField(u'Hacienda', choices=[('001-01', 'Caja'), ('002-01', 'Bandeja'), ('001-02', 'Racimo')])
    empacadora = SelectField(u'Empacadora', choices=[('001-01', 'Caja'), ('002-01', 'Bandeja'), ('001-02', 'Racimo')])
    group_by = SelectField(u'Agrupar por', choices=[('zona', 'Zona'), ('hacienda', 'Hacienda'), ('empacadora', 'Empacadora'),
                                                 ('lote', 'Lote'), ('producto', 'Producto'), ('empleado', 'Empleado')])