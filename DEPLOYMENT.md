# Deployment Guide

## 🚀 Quick Deployment Steps

### 1. GitHub Repository Setup ✅

- Repository: https://github.com/reddy672/student-management-system
- Code is already pushed and ready for deployment

### 2. Frontend Deployment (GitHub Pages)

1. Go to your GitHub repository: https://github.com/reddy672/student-management-system
2. Click on **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** branch and **/(root)** folder
6. Click **Save**
7. Wait a few minutes for deployment
8. Your site will be available at: https://reddy672.github.io/student-management-system/

### 3. Backend Deployment (Railway)

1. Go to [Railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click **New Project**
4. Select **Deploy from GitHub repo**
5. Choose your repository: `reddy672/student-management-system`
6. Railway will automatically detect the Flask app in the `backend/` folder
7. Deploy the project
8. Get your live API URL (e.g., `https://your-app-name.up.railway.app`)

### 4. Update Frontend API URL

After getting your Railway URL:

1. Go to your GitHub repository
2. Navigate to `frontend/script.js`
3. Edit the file and update line 2:
   ```javascript
   const API_URL = "https://your-railway-app-name.up.railway.app";
   ```
4. Commit and push the changes
5. GitHub Pages will automatically redeploy

### 5. Test Your Application

1. Visit your GitHub Pages URL
2. Try adding a student
3. Test edit and delete functionality
4. Verify everything works correctly

## 🔧 Troubleshooting

### Frontend Issues

- **CORS Errors**: Make sure your Railway backend has CORS enabled
- **API Connection**: Verify the API_URL in script.js is correct
- **GitHub Pages not updating**: Check if the deployment is complete

### Backend Issues

- **Railway deployment fails**: Check if requirements.txt is in the backend folder
- **Database issues**: Railway will create a new SQLite database
- **Port issues**: Railway handles port configuration automatically

## 📝 Important Notes

- The frontend is already configured to work with a Railway backend
- Update the API_URL in `frontend/script.js` after deploying to Railway
- GitHub Pages will automatically redeploy when you push changes
- Railway provides HTTPS by default
- The database will be created automatically on first run

## 🎯 Final URLs

After deployment, you should have:

- **Frontend**: https://reddy672.github.io/student-management-system/
- **Backend**: https://your-railway-app-name.up.railway.app
