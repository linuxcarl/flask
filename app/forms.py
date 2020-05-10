from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# agregamos otra clase para agregar las tareas
class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear tarea')

#Clase de formulario para eliminar tareas
class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

#Clase de formulario para poner como terminadas las tareas tareas
class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')
