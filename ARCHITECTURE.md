# 🏗️ Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Interface                       │
│                    (Streamlit Frontend)                      │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Image Upload                            │
│                    (PIL Image Processing)                    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   Computer Vision Layer                      │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │   BLIP Model (Salesforce)                          │    │
│  │   - Image Captioning                               │    │
│  │   - Visual Question Answering                      │    │
│  │   - Ingredient Detection                           │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   NLP Processing Layer                       │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │   Text Analysis                                    │    │
│  │   - Keyword Extraction                             │    │
│  │   - Ingredient Matching                            │    │
│  │   - Context Understanding                          │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Carbon Footprint Database                   │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │   40+ Ingredients with CO2e values                 │    │
│  │   - Meat, Poultry, Fish                            │    │
│  │   - Dairy & Eggs                                   │    │
│  │   - Grains & Legumes                               │    │
│  │   - Vegetables & Fruits                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Calculation Engine                          │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │   Carbon Footprint Calculation                     │    │
│  │   - Ingredient × Portion × CO2e/kg                 │    │
│  │   - Total emissions aggregation                    │    │
│  │   - Impact breakdown                               │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Recommendation Engine                       │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │   Smart Suggestions                                │    │
│  │   - Ingredient substitutions                       │    │
│  │   - Portion recommendations                        │    │
│  │   - Impact comparisons                             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Results Display                         │
│                                                              │
│  • Carbon footprint metric                                  │
│  • Ingredient breakdown table                               │
│  • Visual comparisons                                       │
│  • Actionable suggestions                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Input**: User uploads dish image
2. **Vision**: BLIP model analyzes image → generates description
3. **NLP**: Extract ingredient keywords from description
4. **Matching**: Match keywords to carbon database
5. **Calculation**: Compute CO2e based on portions
6. **Output**: Display results + suggestions

## Key Components

### 1. Image Processing
- **Library**: PIL (Python Imaging Library)
- **Format Support**: JPG, PNG, JPEG
- **Max Size**: Configurable via Streamlit

### 2. AI Model
- **Model**: Salesforce BLIP (Bootstrapping Language-Image Pre-training)
- **Size**: ~500MB
- **Capabilities**: 
  - Image captioning
  - Visual question answering
  - Zero-shot image classification
- **Cache**: Model loaded once and cached

### 3. Carbon Database
- **Format**: Python dictionary
- **Ingredients**: 40+ common food items
- **Unit**: kg CO2e per kg of ingredient
- **Source**: Environmental impact studies

### 4. Frontend
- **Framework**: Streamlit
- **Features**:
  - Drag & drop image upload
  - Real-time processing
  - Interactive ingredient selection
  - Responsive design

## Technology Stack Details

```python
Core Technologies:
├── Python 3.8+
├── Streamlit (Web Framework)
├── PyTorch (Deep Learning)
├── Transformers (Hugging Face)
├── Pillow (Image Processing)
└── Pandas (Data Analysis)
```

## Performance Considerations

- **Model Caching**: `@st.cache_resource` prevents reloading
- **Memory**: ~2GB RAM recommended
- **First Load**: 30-60 seconds (model download)
- **Subsequent**: <5 seconds per image

## Scalability

### Current MVP
- Single user
- Local computation
- In-memory database

### Future Enhancements
- Multi-user support
- Cloud-based model serving
- PostgreSQL database
- API endpoints
- Batch processing

## Security

- File type validation
- Size limits
- No data persistence (privacy)
- HTTPS ready for deployment

## API Potential

Future API structure:
```
POST /api/analyze
{
  "image": "base64_encoded_image"
}

Response:
{
  "ingredients": [...],
  "carbon_footprint": 4.2,
  "suggestions": [...]
}
```

---

This architecture provides a solid foundation for the MVP while allowing for future enhancements and scaling.
