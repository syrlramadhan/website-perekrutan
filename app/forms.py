from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email

class CalgotForm(FlaskForm):
    nama_lengkap = StringField('Nama Lengkap', validators=[DataRequired('Isi Nama Lengkap')])
    nama_panggilan = StringField('Nama Panggilan', validators=[DataRequired()])
    jenis_kelamin = SelectField('Jenis Kelamin', choices=[('Pria', 'Pria'), ('Wanita', 'Wanita')],
                                validators=[DataRequired()])
    nomor_wa = StringField('Nomor Whatsapp', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    alamat = StringField('Alamat', validators=[DataRequired()])
    kampus = StringField('Asal Kampus', validators=[DataRequired()])
    jurusan = StringField('Jurusan', validators=[DataRequired()])
    foto = StringField('Nama File Foto', default="tidak_ada.jpg")
    alasan = TextAreaField('Alasan Mengikuti COCONUT', validators=[DataRequired()])
