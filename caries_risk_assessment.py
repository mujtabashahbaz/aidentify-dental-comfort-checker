import streamlit as st

# Function to calculate caries risk
def calculate_caries_risk(inputs):
    score = 0
    # Age factor
    if inputs['age'] < 6:
        score += 2
    elif 6 <= inputs['age'] <= 15:
        score += 1
    else:
        score += 0
    
    # Oral hygiene
    if inputs['brushing_frequency'] == 'Less than once a day':
        score += 2
    elif inputs['brushing_frequency'] == 'Once a day':
        score += 1
    else:
        score += 0
    
    if inputs['flossing'] == 'Never':
        score += 2
    elif inputs['flossing'] == 'Sometimes':
        score += 1
    else:
        score += 0
    
    # Dietary habits
    if inputs['sugar_intake'] == 'High':
        score += 2
    elif inputs['sugar_intake'] == 'Moderate':
        score += 1
    else:
        score += 0
    
    if inputs['snacking_frequency'] == 'More than 5 times a day':
        score += 2
    elif inputs['snacking_frequency'] == '3-5 times a day':
        score += 1
    else:
        score += 0
    
    # Fluoride exposure
    if inputs['fluoride_toothpaste'] == 'No':
        score += 2
    elif inputs['fluoride_toothpaste'] == 'Yes, regular use':
        score += 0
    else:
        score += 1
    
    if inputs['fluoride_treatment'] == 'No':
        score += 1
    elif inputs['fluoride_treatment'] == 'Yes':
        score += 0
    
    # Medical history
    if inputs['previous_caries'] == 'Yes':
        score += 2
    else:
        score += 0
    
    if inputs['dry_mouth'] == 'Yes':
        score += 2
    else:
        score += 0
    
    if inputs['medications'] == 'Yes':
        score += 1
    else:
        score += 0
    
    # Lifestyle factors
    if inputs['smoking'] == 'Yes':
        score += 1
    else:
        score += 0
    
    if inputs['alcohol'] == 'Yes':
        score += 1
    else:
        score += 0
    
    return score

# Function to determine risk level
def determine_risk_level(score):
    if score >= 10:
        return 'High Risk'
    elif 5 <= score < 10:
        return 'Moderate Risk'
    else:
        return 'Low Risk'

# Function to provide recommendations
def get_recommendations(risk_level):
    recommendations = {
        'High Risk': [
            'Increase frequency of dental visits.',
            'Consider fluoride treatments.',
            'Implement a strict oral hygiene regimen.',
            'Reduce sugar intake and snacking frequency.',
            'Address dry mouth conditions.'
        ],
        'Moderate Risk': [
            'Maintain regular dental check-ups.',
            'Use fluoride toothpaste consistently.',
            'Improve oral hygiene practices.',
            'Moderate sugar consumption.'
        ],
        'Low Risk': [
            'Continue good oral hygiene practices.',
            'Maintain a balanced diet.',
            'Regular dental check-ups every 6 months.'
        ]
    }
    return recommendations[risk_level]

def main():
    st.title("🦷 Comprehensive Caries Risk Assessment Tool")
    st.write("Evaluate the risk of dental caries based on various factors.")

    # Sidebar for inputs
    st.sidebar.header("Patient Information")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=25)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])

    st.sidebar.header("Oral Hygiene Habits")
    brushing_frequency = st.sidebar.selectbox(
        "How often do you brush your teeth?",
        ["Less than once a day", "Once a day", "More than once a day"]
    )
    flossing = st.sidebar.selectbox(
        "Do you floss regularly?",
        ["Never", "Sometimes", "Yes, daily"]
    )

    st.sidebar.header("Dietary Habits")
    sugar_intake = st.sidebar.selectbox(
        "How would you rate your sugar intake?",
        ["Low", "Moderate", "High"]
    )
    snacking_frequency = st.sidebar.selectbox(
        "How often do you snack between meals?",
        ["Less than 3 times a day", "3-5 times a day", "More than 5 times a day"]
    )

    st.sidebar.header("Fluoride Exposure")
    fluoride_toothpaste = st.sidebar.selectbox(
        "Do you use fluoride toothpaste?",
        ["No", "Yes, occasionally", "Yes, regular use"]
    )
    fluoride_treatment = st.sidebar.selectbox(
        "Have you received professional fluoride treatments?",
        ["No", "Yes"]
    )

    st.sidebar.header("Medical History")
    previous_caries = st.sidebar.selectbox(
        "Do you have a history of dental caries?",
        ["No", "Yes"]
    )
    dry_mouth = st.sidebar.selectbox(
        "Do you experience dry mouth?",
        ["No", "Yes"]
    )
    medications = st.sidebar.selectbox(
        "Are you currently taking medications that reduce saliva flow?",
        ["No", "Yes"]
    )

    st.sidebar.header("Lifestyle Factors")
    smoking = st.sidebar.selectbox(
        "Do you smoke?",
        ["No", "Yes"]
    )
    alcohol = st.sidebar.selectbox(
        "Do you consume alcohol regularly?",
        ["No", "Yes"]
    )

    # Compile inputs
    inputs = {
        'age': age,
        'gender': gender,
        'brushing_frequency': brushing_frequency,
        'flossing': flossing,
        'sugar_intake': sugar_intake,
        'snacking_frequency': snacking_frequency,
        'fluoride_toothpaste': fluoride_toothpaste,
        'fluoride_treatment': fluoride_treatment,
        'previous_caries': previous_caries,
        'dry_mouth': dry_mouth,
        'medications': medications,
        'smoking': smoking,
        'alcohol': alcohol
    }

    # Calculate risk score
    score = calculate_caries_risk(inputs)
    risk_level = determine_risk_level(score)
    recommendations = get_recommendations(risk_level)

    # Display results
    st.header("Assessment Results")
    st.write(f"**Total Risk Score:** {score}")
    st.write(f"**Caries Risk Level:** {risk_level}")

    st.subheader("Recommendations:")
    for idx, rec in enumerate(recommendations, 1):
        st.write(f"{idx}. {rec}")

    # Optional: Display detailed inputs (for debugging)
    # st.subheader("Input Data")
    # st.write(inputs)

if __name__ == "__main__":
    main()
