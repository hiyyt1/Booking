from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    href = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    short_text = db.Column(db.String(500), nullable=False)
    full_text = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.String(20), nullable=False)
    pub_time = db.Column(db.String(10), nullable=False)
    tag = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<News {self.title}>"
