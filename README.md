# 🌱 Dish Carbon Footprint Calculator

An AI-powered web application that analyzes dish images to identify ingredients and calculate their carbon footprint, helping users make more sustainable food choices.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Features

- **Image Recognition**: Upload photos of dishes for automatic ingredient detection
- **Carbon Footprint Analysis**: Calculate CO₂ emissions based on identified ingredients
- **Smart Suggestions**: Get personalized recommendations to reduce environmental impact
- **Visual Breakdown**: See detailed emission data per ingredient
- **Real-world Context**: Understand impact through relatable comparisons

## 🚀 Demo

1. Upload an image of any dish
2. AI identifies the ingredients using Computer Vision
3. Instantly see the carbon footprint calculation
4. Receive actionable suggestions to reduce emissions

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Computer Vision**: BLIP (Salesforce) - Image Captioning Model
- **Deep Learning**: PyTorch, Transformers (Hugging Face)
- **Data Processing**: Pandas, Pillow
- **Carbon Data**: Based on environmental impact studies

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dish-carbon-calculator.git
cd dish-carbon-calculator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser to `http://localhost:8501`

3. Upload a dish image and click "Analyze Dish"

4. Review the carbon footprint results and suggestions

## 📊 Carbon Footprint Data

The application uses scientifically-backed carbon emission data (kg CO₂e per kg of ingredient) from environmental studies:

- **High Impact**: Beef (27.0), Lamb (39.2), Shrimp (26.9)
- **Medium Impact**: Chicken (6.9), Fish (6.1), Cheese (13.5)
- **Low Impact**: Lentils (0.9), Potatoes (0.5), Carrots (0.4)

## 🧪 Example Use Cases

- **Meal Planning**: Compare carbon footprints of different meal options
- **Restaurant Analysis**: Evaluate menu items for sustainability
- **Education**: Learn about food's environmental impact
- **Personal Tracking**: Monitor your dietary carbon footprint

## 🔮 Future Enhancements

- [ ] Integration with Recipe1M+ dataset for more accurate recognition
- [ ] NLP-based recipe parsing from text input
- [ ] Database to track historical carbon footprint
- [ ] Mobile app version
- [ ] User accounts and meal history
- [ ] Water footprint calculation
- [ ] Seasonal and local food recommendations
- [ ] Restaurant integration API

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌍 Impact

Food production accounts for approximately 26% of global greenhouse gas emissions. By making informed choices about what we eat, we can significantly reduce our environmental impact.

## 👤 Author

**Soumia Ghalim**

- LinkedIn: [@soumia-ghalim](https://www.linkedin.com/in/soumia-ghalim/)
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- BLIP model by Salesforce Research
- Carbon footprint data from environmental impact studies
- Inspired by Data for Good initiatives

## 📧 Contact

For questions or feedback, please reach out through LinkedIn or open an issue on GitHub.

---

**Made with ❤️ for a sustainable future**
