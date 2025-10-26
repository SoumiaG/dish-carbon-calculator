# Deployment Guide

This guide covers deploying the Dish Carbon Calculator to various platforms.

## 🚀 Streamlit Cloud (Recommended - Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and branch
6. Set main file path: `app.py`
7. Click "Deploy"

**That's it!** Your app will be live in minutes.

## 🐳 Docker Deployment

### Build Docker Image

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t dish-carbon-calculator .
docker run -p 8501:8501 dish-carbon-calculator
```

## ☁️ AWS EC2 Deployment

1. Launch an EC2 instance (t2.medium recommended)
2. SSH into your instance
3. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip
```

4. Clone and setup:
```bash
git clone https://github.com/yourusername/dish-carbon-calculator.git
cd dish-carbon-calculator
pip3 install -r requirements.txt
```

5. Run with nohup:
```bash
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

6. Configure security group to allow port 8501

## 🔷 Google Cloud Run

1. Create `Dockerfile` (see above)
2. Build and push:
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/dish-carbon-calculator
```

3. Deploy:
```bash
gcloud run deploy dish-carbon-calculator \
  --image gcr.io/PROJECT_ID/dish-carbon-calculator \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 🟦 Azure App Service

1. Create an Azure App Service with Python runtime
2. Configure deployment from GitHub
3. Set startup command: `streamlit run app.py --server.port=$PORT`
4. Deploy

## 📱 Heroku Deployment

1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## 🔒 Environment Variables

For production, consider adding:
- `STREAMLIT_SERVER_MAX_UPLOAD_SIZE`: Control max file size
- `STREAMLIT_THEME_*`: Custom theme settings

## 📊 Performance Tips

1. **Model Caching**: Already implemented with `@st.cache_resource`
2. **CDN**: Use CDN for static assets
3. **Compression**: Enable gzip compression
4. **Monitoring**: Set up logging and monitoring

## 🐛 Troubleshooting

### Out of Memory
- Use a larger instance type
- Implement model quantization
- Use CPU-only PyTorch build

### Slow Loading
- Pre-download models
- Use lighter model variants
- Implement lazy loading

## 📈 Scaling

For high traffic:
1. Use load balancer
2. Deploy multiple instances
3. Implement Redis caching
4. Use a dedicated model serving infrastructure

## 🔐 Security Considerations

1. Add rate limiting
2. Implement user authentication if needed
3. Sanitize file uploads
4. Use HTTPS
5. Keep dependencies updated

---

Need help? Check the [Streamlit documentation](https://docs.streamlit.io) or open an issue on GitHub.
