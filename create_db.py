from flaskblog import create_app, db
from flaskblog.models import User, Post

user1 = User(username="admin", firstname='admin', lastname='admin', email="admin@gmail.com", password="admin")
print(user1)
app = create_app(())
with app.app_context():
    db.create_all()
    db.session.add(user1)
    db.session.commit()