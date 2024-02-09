import streamlit as st

# Streamlit app title
st.title('LLM - GPU Memory Calculator')

# User inputs
P = 0

P = st.number_input('Enter the amount of parameters in the LLM (in billions):', min_value=1.0, value=7.0, step=1.0)
st.caption('*** Enter 30 for 30 Billion parameter LLM')
Q = st.number_input('Select the amount of bits used for loading the model:', min_value=2.0, value=32.0, step=1.0)
st.caption('*** Most of the models are full 32 bits. If you are using quantized version enter the bits (Enter 5 for 5 bit Q)')


# Calculate GPU memory (M)
# Convert P from billions to actual number of parameters
P = P * 1e9  # Convert billions to actual number

# Corrected formula
M = ((P * 4) / (32 / Q)) * 1.2

# Display the result
#st.header(f'GPU memory required : {M / 1e9:.2f} GB')
st.markdown(f"""
    <style>
        .result {{
            font-size: 24px;
            font-weight: bold;
            color: #FF4B4B;
        }}
    </style>
    <div class="result">GPU memory required: {M / 1e9:.2f} GB</div>
    """, unsafe_allow_html=True)
