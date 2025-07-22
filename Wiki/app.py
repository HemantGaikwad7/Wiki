from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Database configuration - SQLite for development (easy setup)
# Replace with your actual SQL Server connection string when ready
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wiki.db'
# Uncomment the line below for SQL Server (and comment out SQLite line above)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://Welcome:@DESKTOP-EIM87GG/Wiki?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Article model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'content': self.content
        }

# Initialize DB
with app.app_context():
    db.create_all()

# API Routes
@app.route('/api/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return jsonify([a.to_dict() for a in articles])

@app.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify(article.to_dict())

@app.route('/api/articles', methods=['POST'])
def create_article():
    data = request.json
    new_article = Article(
        title=data['title'],
        category=data['category'],
        content=data['content']
    )
    db.session.add(new_article)
    db.session.commit()
    return jsonify(new_article.to_dict()), 201

@app.route('/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    data = request.json
    article.title = data.get('title', article.title)
    article.category = data.get('category', article.category)
    article.content = data.get('content', article.content)
    db.session.commit()
    return jsonify(article.to_dict())

@app.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({'message': 'Article deleted'})

# Serve frontend files
@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/wiki')
def wiki():
    with open('wiki.html', 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True)
