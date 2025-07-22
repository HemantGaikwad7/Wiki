# Wiki
# 📖 Knowledge Base Wiki

A modern, responsive web application for creating and managing a knowledge base with articles organized by categories. Built with Flask backend and Alpine.js frontend with Markdown support.

## ✨ Features

- **📝 Markdown Support**: Write articles using Markdown syntax with live preview
- **🔍 Real-time Search**: Search articles by title with instant filtering
- **📂 Category Management**: Organize articles by categories with filtering
- **✏️ Inline Editing**: Edit articles directly in the interface with preview
- **🎨 Modern UI**: Beautiful gradient design with glassmorphism effects
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **⚡ Real-time Updates**: Instant updates without page refresh
- **🗃️ Database Storage**: Persistent storage with SQLite (easily configurable for SQL Server)

## 🛠️ Tech Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Development database (configurable for SQL Server)
- **Flask-CORS**: Cross-origin resource sharing support

### Frontend
- **Alpine.js**: Lightweight reactive framework
- **Marked.js**: Markdown parser and renderer
- **HTML5 & CSS3**: Modern web standards
- **Vanilla JavaScript**: No heavy framework dependencies

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd Wiki

# Or download and extract the project files
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py (Open terminal and run this command then Open with live Server "index.html" file)
```

The application will start on `http://127.0.0.1:5000`

### 4. Access the Application
Open your web browser and navigate to:
- Main interface: `http://127.0.0.1:5000`
- Alternative view: `http://127.0.0.1:5000/wiki`
- Open with Live Server "index.html" file

## 📁 Project Structure

```
Wiki/
├── app.py              # Flask backend application
├── index.html          # Main frontend interface
├── wiki.html           # Alternative frontend view
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── instance/
    └── wiki.db        # SQLite database (auto-created)
```

## 🎯 Usage

### Adding Articles
1. Fill in the "Article Title" field
2. Specify a category for organization
3. Write your content using Markdown syntax
4. Click "Add Article" to save

### Searching Articles
- Use the search bar to find articles by title
- Filter by category using the dropdown menu
- Combine search and category filters for precise results

### Editing Articles
1. Click the "Edit" button on any article
2. Modify the content in the editor
3. See live preview of your changes
4. Click "Save" to update or "Cancel" to discard changes

### Deleting Articles
- Click the "Delete" button on any article
- Confirm the deletion in the popup dialog

## 🔧 Configuration

### Database Configuration

#### SQLite (Default - Development)
The application uses SQLite by default for easy setup:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wiki.db'
```

#### SQL Server (Production)
To use SQL Server, uncomment and modify the connection string in `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server'
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/articles` | Retrieve all articles |
| GET | `/api/articles/<id>` | Retrieve specific article |
| POST | `/api/articles` | Create new article |
| PUT | `/api/articles/<id>` | Update existing article |
| DELETE | `/api/articles/<id>` | Delete article |

### Article Data Structure
```json
{
  "id": 1,
  "title": "Article Title",
  "category": "Category Name",
  "content": "Markdown content here..."
}
```

## 🎨 Markdown Support

The application supports standard Markdown syntax:

- **Headers**: `# H1`, `## H2`, `### H3`
- **Bold**: `**bold text**`
- **Italic**: `*italic text*`
- **Links**: `[link text](URL)`
- **Lists**: `- item` or `1. item`
- **Code**: `` `inline code` `` or ``` for code blocks
- **Blockquotes**: `> quote text`

## 🔍 API Usage Examples

### Create Article
```bash
curl -X POST http://127.0.0.1:5000/api/articles \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Article",
    "category": "Documentation",
    "content": "# Hello World\nThis is **markdown** content."
  }'
```

### Get All Articles
```bash
curl http://127.0.0.1:5000/api/articles
```

### Update Article
```bash
curl -X PUT http://127.0.0.1:5000/api/articles/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content"
  }'
```

## 🚨 Troubleshooting

### Common Issues

1. **Server not starting**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version: `python --version`

2. **Database errors**
   - Delete `instance/wiki.db` to reset the database
   - Check file permissions in the project directory

3. **Frontend not loading**
   - Verify the Flask server is running on port 5000
   - Check browser console for JavaScript errors

4. **CORS errors**
   - Ensure Flask-CORS is installed and configured
   - Check that the API base URL matches your server address

## 🔒 Security Considerations

- This is a development setup - implement authentication for production use
- Sanitize user inputs for production deployment
- Use environment variables for sensitive configuration
- Implement rate limiting for API endpoints

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure a reverse proxy (Nginx, Apache)
4. Use a production database (PostgreSQL, SQL Server)
5. Implement proper security measures

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Support

For support or questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review the API documentation

---

**Built with ❤️ for knowledge sharing and documentation**
