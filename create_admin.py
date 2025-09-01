# One-off script to create missing tables and a default admin user
from app import app, db
from app.models import Admin

with app.app_context():
    # Create any missing tables
    db.create_all()
    # Check if admin exists
    if Admin.query.filter_by(username='admin').first():
        print('Admin already exists')
    else:
        a = Admin(username='admin')
        a.set_password('admin')
        db.session.add(a)
        db.session.commit()
        print('Created admin/admin')
