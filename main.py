import streamlit as st

# Streamlit app title
st.title('GPU Memory Requirement Calculator')

# User inputs
#P = st.number_input('Enter the amount of parameters in the model (in billions):', min_value=0.0, value=7.0, step=0.1)
P = st.number_input('Enter the amount of parameters in the model (in billions):', min_value=0.0, value=100.0, step=1)
Q = st.selectbox('Select the amount of bits used for loading the model:', options=[1, 2, 3, 4, 5, 6, 7 8, 16, 32], index=1)

# Calculate GPU memory (M)
# Convert P from billions to actual number of parameters
P = P * 1e9  # Convert billions to actual number
#M = (((32 / Q) * (P * 4)) / 32) * 1.2
M = ((P * 4)/(32 / Q)) * 1.2

# Display the result
st.write(f'GPU memory required: {M / 1e9:.2f} GB')
