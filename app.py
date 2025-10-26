"""
Dish Carbon Footprint Calculator
Upload a photo of a dish to identify ingredients and calculate carbon footprint
"""

import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import json
import re

# Carbon footprint data (kg CO2e per kg of ingredient)
CARBON_FOOTPRINT_DATA = {
    'beef': 27.0,
    'lamb': 39.2,
    'pork': 12.1,
    'chicken': 6.9,
    'turkey': 10.9,
    'fish': 6.1,
    'salmon': 11.9,
    'tuna': 6.1,
    'shrimp': 26.9,
    'cheese': 13.5,
    'milk': 3.2,
    'eggs': 4.8,
    'butter': 12.0,
    'rice': 2.7,
    'wheat': 1.4,
    'bread': 1.6,
    'pasta': 2.0,
    'potatoes': 0.5,
    'tomatoes': 2.1,
    'onions': 0.5,
    'carrots': 0.4,
    'lettuce': 1.3,
    'broccoli': 2.0,
    'beans': 2.0,
    'lentils': 0.9,
    'tofu': 2.0,
    'nuts': 2.3,
    'olive oil': 5.4,
    'sugar': 3.2,
    'chocolate': 18.7,
    'coffee': 16.9,
    'avocado': 2.5,
    'banana': 0.9,
    'apple': 0.4,
    'orange': 0.4,
}

# Standard portion sizes (kg)
STANDARD_PORTIONS = {
    'beef': 0.15,
    'chicken': 0.15,
    'fish': 0.15,
    'rice': 0.075,
    'pasta': 0.075,
    'vegetables': 0.15,
    'cheese': 0.03,
    'eggs': 0.05,
}

@st.cache_resource
def load_model():
    """Load the BLIP model for image captioning"""
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def analyze_image(image, processor, model):
    """Generate description from image using BLIP"""
    inputs = processor(image, return_tensors="pt")
    
    # Generate caption
    out = model.generate(**inputs, max_length=50)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    # Generate more detailed description with question
    prompt = "Question: What ingredients are in this dish? Answer:"
    inputs = processor(image, text=prompt, return_tensors="pt")
    out = model.generate(**inputs, max_length=100)
    detailed_description = processor.decode(out[0], skip_special_tokens=True)
    
    return caption, detailed_description

def extract_ingredients(description):
    """Extract potential ingredients from description"""
    description_lower = description.lower()
    found_ingredients = []
    
    for ingredient in CARBON_FOOTPRINT_DATA.keys():
        if ingredient in description_lower:
            found_ingredients.append(ingredient)
    
    return found_ingredients

def calculate_carbon_footprint(ingredients, portions=None):
    """Calculate total carbon footprint"""
    if portions is None:
        portions = {}
    
    total_footprint = 0
    breakdown = []
    
    for ingredient in ingredients:
        if ingredient in CARBON_FOOTPRINT_DATA:
            # Use provided portion or standard portion
            portion = portions.get(ingredient, STANDARD_PORTIONS.get(ingredient, 0.1))
            footprint = CARBON_FOOTPRINT_DATA[ingredient] * portion
            total_footprint += footprint
            breakdown.append({
                'ingredient': ingredient,
                'portion_kg': portion,
                'co2_per_kg': CARBON_FOOTPRINT_DATA[ingredient],
                'total_co2': footprint
            })
    
    return total_footprint, breakdown

def get_suggestions(total_footprint, ingredients):
    """Provide suggestions to reduce carbon footprint"""
    suggestions = []
    
    # Check for high-impact ingredients
    high_impact = ['beef', 'lamb', 'shrimp', 'cheese', 'chocolate']
    has_high_impact = any(ing in ingredients for ing in high_impact)
    
    if has_high_impact:
        suggestions.append("🔄 Replace red meat with chicken, fish, or plant-based proteins to reduce emissions by up to 70%")
    
    if 'beef' in ingredients or 'lamb' in ingredients:
        suggestions.append("🌱 Try plant-based alternatives like lentils, beans, or tofu")
    
    if 'cheese' in ingredients:
        suggestions.append("🧀 Reduce cheese portions or try plant-based cheese alternatives")
    
    if total_footprint > 5:
        suggestions.append("📊 Your meal has a high carbon footprint. Consider smaller portions or ingredient substitutions")
    elif total_footprint < 2:
        suggestions.append("✅ Great choice! This is a low-carbon meal")
    
    if 'rice' in ingredients:
        suggestions.append("🌾 Consider local, sustainably grown rice or alternatives like quinoa")
    
    return suggestions

# Streamlit UI
st.set_page_config(page_title="Dish Carbon Calculator", page_icon="🌱", layout="wide")

st.title("🌱 Dish Carbon Footprint Calculator")
st.markdown("Upload a photo of your dish to identify ingredients and calculate its carbon footprint")

# Sidebar
with st.sidebar:
    st.header("About")
    st.info("""
    This tool uses Computer Vision to analyze dish images and estimate carbon footprint 
    based on identified ingredients.
    
    **How it works:**
    1. Upload a dish image
    2. AI identifies potential ingredients
    3. Calculate CO₂ emissions
    4. Get reduction suggestions
    """)
    
    st.header("Carbon Impact Scale")
    st.metric("Low Impact", "< 2 kg CO₂e", delta="Good")
    st.metric("Medium Impact", "2-5 kg CO₂e", delta="Moderate")
    st.metric("High Impact", "> 5 kg CO₂e", delta="High")

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Upload Dish Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("🔍 Analyze Dish", type="primary"):
            with st.spinner("Analyzing image..."):
                # Load model
                processor, model = load_model()
                
                # Analyze image
                caption, detailed = analyze_image(image, processor, model)
                
                # Store results in session state
                st.session_state['caption'] = caption
                st.session_state['detailed'] = detailed
                st.session_state['analyzed'] = True

with col2:
    st.header("📊 Results")
    
    if 'analyzed' in st.session_state and st.session_state['analyzed']:
        # Display AI analysis
        st.subheader("🤖 AI Analysis")
        st.write(f"**Dish Description:** {st.session_state['caption']}")
        st.write(f"**Details:** {st.session_state['detailed']}")
        
        # Extract ingredients
        combined_text = f"{st.session_state['caption']} {st.session_state['detailed']}"
        detected_ingredients = extract_ingredients(combined_text)
        
        st.subheader("🥗 Detected Ingredients")
        
        # Allow user to select/modify ingredients
        selected_ingredients = st.multiselect(
            "Confirm or add ingredients:",
            options=list(CARBON_FOOTPRINT_DATA.keys()),
            default=detected_ingredients
        )
        
        if selected_ingredients:
            # Calculate footprint
            total_footprint, breakdown = calculate_carbon_footprint(selected_ingredients)
            
            # Display total
            st.metric(
                "Total Carbon Footprint", 
                f"{total_footprint:.2f} kg CO₂e",
                help="Total greenhouse gas emissions for this meal"
            )
            
            # Breakdown table
            st.subheader("📋 Ingredient Breakdown")
            import pandas as pd
            df = pd.DataFrame(breakdown)
            df.columns = ['Ingredient', 'Portion (kg)', 'CO₂/kg', 'Total CO₂ (kg)']
            st.dataframe(df, use_container_width=True)
            
            # Suggestions
            st.subheader("💡 Reduction Suggestions")
            suggestions = get_suggestions(total_footprint, selected_ingredients)
            for suggestion in suggestions:
                st.success(suggestion)
            
            # Comparison
            st.subheader("🌍 Context")
            st.info(f"""
            Your meal's footprint is equivalent to:
            - 🚗 Driving {total_footprint * 4.5:.1f} km in an average car
            - 💡 {total_footprint * 120:.0f} hours of LED light bulb usage
            - 📱 Charging a smartphone {total_footprint * 120:.0f} times
            """)
    else:
        st.info("👆 Upload an image and click 'Analyze Dish' to get started")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ for sustainability | Data source: Environmental impact studies</p>
</div>
""", unsafe_allow_html=True)
