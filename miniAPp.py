from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, PasswordField, validators, SelectField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a1111'
 


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])
    gender = SelectField('Gender:',choices=[('1','M'),('2','F')])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    #print form.errors
    if request.method == 'POST':
        name=request.form['name']
        surname=request.form['surname']
        gender=request.form['gender']
        #print name
    
    if form.validate():
    # Save the comment here.
        if gender == '1':
            g = 'M'
        else:
            g = 'F'
        flash('Hello ' + name + ' '+ surname + ' 1เพศ ' + g)
    else:
        flash('All the form fields are required. ')
    
    return render_template('miniForm.html', form=form)
    
if __name__ == "__main__":
    app.run()