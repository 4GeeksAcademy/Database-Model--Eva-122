from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), unique=True, nullable=False)
    firstname=db.Column(db.String(120))
    lastname=db.Column(db.String(120))
    email= db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"

        
class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)

    def __repr__(self):
        return f"<Post {self.id}>"

class Media(db.Model):
    __tablename__ = "media"
    id = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.Enum("image", "video", name="media_type"))
    URL= db.Column(db.String(120))
    post_id= db.Column(db.Integer,db.ForeignKey("post.id"), nullable= False)

    def __repr__(self):
        return f"<Media {self.id}>"
    
class Comment(db.Model): 
    __tablename__ = "comment"  
    id = db.Column(db.Integer, primary_key=True)
    comment_text= db.Column(db.String(500), nullable= False)
    author_id= db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)
    post_id= db.Column(db.Integer, db.ForeignKey("post.id"), nullable= False)

    def __repr__(self):
        return f"<Comment {self.id}>" 
    
class Follower(db.Model): 
    __tablename__ = "follower"   
    user_from_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False, primary_key=True)
    user_to_id= db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False, primary_key=True)
    

    def __repr__(self):
        return f"<Follower {self.user_from_id} -> {self.user_to_id}>"