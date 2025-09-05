# Website Perekrutan COCONUT Computer Club

Website resmi untuk pendaftaran anggota COCONUT Computer Club Chapter Bandung. Website ini dibangun menggunakan Flask dengan database SQLite dan Bootstrap untuk UI.

## 🚀 Fitur

- ✅ Formulir pendaftaran online dengan validasi
- ✅ Upload foto profil
- ✅ Dashboard admin untuk melihat data pendaftar
- ✅ Export data ke Excel dan PDF
- ✅ Responsive design
- ✅ Sistem autentikasi admin
- ✅ Halaman About dengan informasi lengkap
- ✅ Section berita dan acara terbaru

## 🛠️ Tech Stack

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy dengan SQLite
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Icons**: Bootstrap Icons
- **Charts**: (jika diperlukan)
- **Export**: OpenPyXL (Excel), ReportLab (PDF)

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## 🔧 Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/your-username/website-perekrutan.git
   cd website-perekrutan
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup database**
   ```bash
   # Inisialisasi database
   flask db init
   flask db migrate
   flask db upgrade

   # Atau jalankan script setup
   python create_admin.py
   ```

5. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

   Aplikasi akan berjalan di `http://localhost:5000`

## ⚙️ Configuration

### Environment Variables

Buat file `.env` di root directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=production
```

### Default Admin Account

Username: `admin`
Password: `admin123` (ubah setelah login pertama)

## 📁 Project Structure

```
website-perekrutan/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # Route definitions
│   ├── forms.py             # WTForms definitions
│   └── templates/           # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── about.html
│       ├── daftar2.html
│       ├── login.html
│       └── pendaftar.html
├── static/                  # Static files (CSS, JS, images)
├── migrations/              # Database migrations
├── requirements.txt         # Python dependencies
├── config.py               # Configuration settings
├── app.py                  # Main application file
└── README.md
```

## 🔐 Admin Features

- **Login**: `/login`
- **Dashboard**: `/pendaftar`
- **Export Data**:
  - Excel: `/pendaftar/export/xlsx`
  - PDF: `/pendaftar/export/pdf`

## 🌐 Production Deployment

### Menggunakan Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Environment Variables untuk Production

```env
SECRET_KEY=your-production-secret-key
DATABASE_URL=sqlite:///app.db
FLASK_ENV=production
```

### Database Production

Untuk production, gunakan database yang lebih robust:

```python
# config.py
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/dbname'
```

## 📝 API Endpoints

- `GET /api/getData` - Mendapatkan data pendaftar
- `POST /api/postData` - Menambah data pendaftar baru

## 🤝 Contributing

1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

- **Email**: hello@coconut.or.id
- **LinkedIn**: [COCONUT Computer Club](https://www.linkedin.com/company/coconut-computer-club)
- **Instagram**: [@coconutdotorg](https://www.instagram.com/coconutdotorg/)
- **WhatsApp**: +62 856-5737-6820

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [COCONUT Computer Club](https://coconut.or.id/)

---

**COCONUT Computer Club** - Chapter Bandung
*Every Entity Best Seed*
