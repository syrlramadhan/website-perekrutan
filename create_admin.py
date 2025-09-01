# One-off script to create missing tables and a default admin user
from app import app, db
from app.models import Admin

with app.app_context():
    # Create any missing tables
    db.create_all()
    # Check if admin exists
    if Admin.query.filter_by(username='hacklab').first():
        print('Admin already exists')
    else:
        a = Admin(username='hacklab')
        a.set_password('C0c0nut2008!')
        db.session.add(a)
        db.session.commit()
        print('Created hacklab/C0c0nut2008!')
