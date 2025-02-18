from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# tabla para la relacion muchos a muchos
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
)

# Modelo User
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)

    # relacion para el uno a uno
    profile = db.relationship("Profile", backref="user", uselist=False) # [<Profile 1>] => <Profile 1>
    
    # relacion para el uno a muchos
    tasks = db.relationship("Task", back_populates="user")

    # relacion para el muchos a muchos
    followeds = db.relationship("User", 
                    secondary=followers, 
                    primaryjoin="followers.c.follower_id == User.id", 
                    secondaryjoin="followers.c.followed_id == User.id",
                    backref="followers"
                )

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "profile": self.profile.serialize(),
            "total_tasks": len(self.tasks),
            "tasks": self.get_tasks(),
            "seguidos": self.get_followeds(),
            "seguidores": self.get_followers()
        }

    def get_followeds(self):
        return [
            {"id": f.id, "username": f.username } for f in self.followeds
        ]
    
    def get_followers(self):
        return [
            {"id": f.id, "username": f.username } for f in self.followers
        ]
    
    def get_tasks(self):
        return [task.serialize() for task in self.tasks]
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    biography = db.Column(db.String, default="")
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            #"id": self.id,
            "biography": self.biography,
            #"users_id": self.users_id,
            #"username": self.user.username
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, default=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship("User", back_populates="tasks")

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done,
            "users_id": self.users_id,
            "username": self.user.username
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()