# 🚀 Quick Start Guide

Get the Dish Carbon Calculator running in 5 minutes!

## ⚡ Fastest Way to Run

### Option 1: Local Setup (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/dish-carbon-calculator.git
cd dish-carbon-calculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

Open your browser to `http://localhost:8501` 🎉

### Option 2: Try the Test Script First

Want to see how it works without the UI?

```bash
python test_example.py
```

This will run examples and show you carbon calculations for different meals.

## 📝 What You Get

✅ **Functional MVP** - Upload dish images and get instant carbon footprint analysis  
✅ **AI-Powered** - Uses Salesforce BLIP model for image recognition  
✅ **40+ Ingredients** - Pre-loaded carbon footprint database  
✅ **Smart Suggestions** - Get personalized tips to reduce emissions  
✅ **Production Ready** - Includes deployment guides for multiple platforms  

## 🎨 File Structure

```
dish-carbon-calculator/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── test_example.py        # Testing and examples
├── README.md              # Project documentation
├── DEPLOYMENT.md          # Deployment guides
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## 🧪 Test It Out

Try these sample dishes:
1. **Beef steak with potatoes** → High carbon footprint
2. **Chicken pasta with vegetables** → Medium footprint
3. **Lentil curry with rice** → Low footprint
4. **Salmon sushi** → Medium footprint

## 🐛 Common Issues

**Issue**: Model download takes time  
**Solution**: First run downloads the AI model (~500MB). Be patient!

**Issue**: Out of memory  
**Solution**: Close other applications or use a machine with more RAM

**Issue**: Import errors  
**Solution**: Make sure you're using Python 3.8+

## 📦 Next Steps

1. **Customize**: Add more ingredients to the database
2. **Deploy**: Use Streamlit Cloud for free hosting
3. **Enhance**: Integrate Recipe1M+ dataset for better accuracy
4. **Share**: Contribute improvements via Pull Request

## 💡 Pro Tips

- The AI model is cached after first run (much faster!)
- You can manually select/deselect ingredients if detection is off
- Try different angles and lighting for better recognition
- Compare meals to see which choices are most sustainable

## 🤝 Contributing

Found a bug? Have an idea? Open an issue or submit a PR!

## 📧 Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for hosting options
- Open an issue on GitHub

---

**Happy Coding! 🌱**
