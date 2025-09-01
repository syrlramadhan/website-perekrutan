from flask import render_template, url_for, jsonify, request, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


from app import app, db
from app.models import calgot, Admin
from app.forms import CalgotForm

import os


class LoginForm(FlaskForm):
	username = StringField('Username')
	password = StringField('Password')
	submit = SubmitField('Login')


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('pendaftar'))
	if form.validate_on_submit():
		user = Admin.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash("Username atau Password Salah!!")
			return redirect(url_for('login'))
		flash("Berhasil Login")
		login_user(user)
		return redirect(url_for('pendaftar'))
	return render_template('login.html', form=form)
	
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/newDaftar', methods=['GET','POST'])
def newDaftar():
	form = CalgotForm()
	return render_template('daftar2.html', form=form)


@app.route('/pendaftar')
@login_required
def pendaftar():
	return render_template('pendaftar.html')

@app.route('/daftar')
def daftar():
	return render_template('daftar2.html')



@app.route('/news')
def news():
	return render_template('news.html')



@app.route('/api/getData', methods=['GET'])
def getData():
	try:
		print("DEBUG: getData route called")
		daftar_calgot = calgot.query.all()
		print(f"DEBUG: Found {len(daftar_calgot)} records")
		
		data_jsom = []
		for baris in daftar_calgot:
			print(f"DEBUG: Processing record {baris.id}: {baris.nama_lengkap}")
			# Handle foto path safely
			foto_path = baris.foto
			if foto_path and len(foto_path) > 11:
				foto_path = foto_path[11:]  # Remove 'app/static/' prefix
			elif foto_path:
				foto_path = foto_path
			else:
				foto_path = "tidak_ada.jpg"
			
			data_jsom.append({
				'id': baris.id,
				'nama_lengkap': baris.nama_lengkap,
				'nama_panggilan': baris.nama_panggilan,
				'jenis_kelamin': baris.jenis_kelamin,
				'nomor_wa': baris.nomor_wa,
				'email': baris.email,
				'username_telegram': baris.username_telegram or '',
				'alamat': baris.alamat,
				'pilihan_tinggal': baris.pilihan_tinggal or '',
				'kampus': baris.kampus,
				'jurusan': baris.jurusan,
				'foto': foto_path,
				'tanggal': baris.timestamp.strftime('%d-%m-%Y %H:%M') if baris.timestamp else '',
				'alasan': baris.alasan
			})
		
		print(f"DEBUG: Returning {len(data_jsom)} records")
		return jsonify(data_jsom)
	except Exception as e:
		print(f"ERROR in getData: {e}")
		import traceback
		traceback.print_exc()
		return jsonify({'error': str(e)}), 500


@app.route('/api/postData', methods=['GET','POST'])
def postData():
	try:
		print("DEBUG: postData route called")
		print("DEBUG: Form data:", request.form)
		print("DEBUG: Files:", request.files)
		
		# Get form data
		nama_lengkap = request.form.get('nama_lengkap')
		nama_panggilan = request.form.get('nama_panggilan')
		jenis_kelamin = request.form.get('jenis_kelamin')
		email = request.form.get('email')
		nomor_wa = request.form.get('nomor_wa')
		username_telegram = request.form.get('username_telegram')
		alamat = request.form.get('alamat')
		pilihan_tinggal = request.form.get('pilihan_tinggal')
		kampus = request.form.get('kampus')
		jurusan = request.form.get('jurusan')
		alasan = request.form.get('alasan')
		
		print(f"DEBUG: Received data - nama: {nama_lengkap}, email: {email}")
		print(f"DEBUG: New fields - telegram: {username_telegram}, pilihan_tinggal: {pilihan_tinggal}")
		
		# Handle photo
		photo_path = "tidak_ada.jpg"  # default
		if 'photo' in request.files:
			photo = request.files['photo']
			if photo.filename != '':
				# Clean filename
				clean_name = nama_lengkap.replace(' ','_').replace(',','').replace('.','')
				photo_path = os.path.join("app/static/foto_calgot", clean_name + '.jpg')
				photo.save(photo_path)
				print(f"DEBUG: Photo saved to {photo_path}")
		
		# Create calgot object
		add_calgot = calgot(
			nama_lengkap=nama_lengkap,
			nama_panggilan=nama_panggilan,
			jenis_kelamin=jenis_kelamin,
			email=email,
			nomor_wa=nomor_wa,
			username_telegram=username_telegram,
			alamat=alamat,
			pilihan_tinggal=pilihan_tinggal,
			kampus=kampus,
			jurusan=jurusan,
			foto=photo_path,
			alasan=alasan
		)
		
		print(f"DEBUG: Creating calgot object: {add_calgot}")
		
		# Save to database
		db.session.add(add_calgot)
		db.session.commit()
		
		print(f"DEBUG: Calgot {nama_lengkap} berhasil didaftarkan")
		return jsonify({'status': 'success', 'message': 'Pendaftaran berhasil!'})
		
	except Exception as e:
		print(f"ERROR in postData: {e}")
		import traceback
		traceback.print_exc()
		db.session.rollback()
		return jsonify({'status': 'error', 'message': str(e)}), 500
