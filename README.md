# Student Management System

A full-stack Student Management System built with Flask backend and vanilla HTML/CSS/JavaScript frontend.

## 🌟 Features

- **Add Students**: Add new students with name, marks, and attendance
- **Edit Students**: Update existing student information
- **Delete Students**: Remove students from the system
- **View Students**: Display all students in a clean, card-based layout
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Real-time Updates**: Immediate feedback for all operations

## 🏗️ Architecture

### Frontend

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **Vanilla JavaScript**: No frameworks, pure ES6+
- **Fetch API**: RESTful communication with backend
- **Responsive Design**: Mobile-first approach

### Backend

- **Flask**: Python web framework
- **SQLite**: Lightweight database
- **Flask-CORS**: Cross-origin resource sharing
- **RESTful APIs**: Full CRUD operations

## 🚀 Live Demo

- **Frontend**: [GitHub Pages](https://your-username.github.io/student-management-system/)
- **Backend API**: [Railway](https://student-management-system-backend-production.up.railway.app)

## 📁 Project Structure

```
student-management-system/
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── style.css           # Styling
│   └── script.js           # JavaScript functionality
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── Procfile           # Railway deployment config
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## 🛠️ API Endpoints

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/students`      | Get all students |
| POST   | `/students`      | Add new student  |
| PUT    | `/students/{id}` | Update student   |
| DELETE | `/students/{id}` | Delete student   |

### Request/Response Format

**Add/Update Student:**

```json
{
  "name": "John Doe",
  "marks": 85,
  "attendance": 92
}
```

**Get Students Response:**

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "marks": 85,
    "attendance": 92
  }
]
```

## 🚀 Deployment

### Frontend (GitHub Pages)

1. Push code to GitHub repository
2. Go to Settings > Pages
3. Select source branch (usually `main`)
4. Your site will be available at `https://username.github.io/repo-name/`

### Backend (Railway)

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Flask app
3. Deploy and get your live API URL
4. Update the `API_URL` in `frontend/script.js`

## 🛠️ Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
# Open index.html in your browser
# Or use a local server:
python -m http.server 8000
```

## 🔧 Configuration

### Update API URL

In `frontend/script.js`, update the `API_URL` constant with your Railway deployment URL:

```javascript
const API_URL = "https://your-railway-app.up.railway.app";
```

## 📱 Features

- **Responsive Design**: Works on all screen sizes
- **Form Validation**: Client-side validation for marks and attendance
- **Error Handling**: Graceful error messages
- **Loading States**: Visual feedback during operations
- **Confirmation Dialogs**: Safe delete operations
- **Smooth Animations**: Enhanced user experience

## 🎨 UI/UX Highlights

- **Modern Gradient Background**: Eye-catching design
- **Card-based Layout**: Clean student information display
- **Hover Effects**: Interactive elements
- **Color-coded Actions**: Edit (yellow) and Delete (red) buttons
- **Success/Error Messages**: User feedback
- **Mobile Responsive**: Touch-friendly interface

## 🔒 Security Features

- **Input Validation**: Prevents invalid data
- **CORS Enabled**: Secure cross-origin requests
- **SQL Injection Protection**: Parameterized queries
- **Error Handling**: No sensitive information exposure

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Flask for the backend framework
- Railway for hosting
- GitHub Pages for frontend hosting
- Modern CSS for beautiful styling
