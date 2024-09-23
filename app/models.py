from app import db, login
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    password_hash = Column(String(128))
    def __repr__(self):
        return f'<Admin {self.username}'
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class calgot(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_lengkap = Column(String(64))
    nama_panggilan = Column(String(64))
    jenis_kelamin = Column(String(10))
    nomor_wa = Column(String(15))
    email = Column(String(64))
    alamat = Column(String(128))
    kampus = Column(String(64))
    jurusan = Column(String(20))
    foto = Column(String(64), default="tidak_ada.jpg")
    alasan = Column(String(120))
    timestamp = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<Calgot {self.nama_panggilan}"

