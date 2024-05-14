import streamlit as st

# Title of the app
st.title('Aung Khine Moe widget testing')

# Text input
name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')

# Slider
age = st.slider('Select your age:', 0, 100, 25)
st.write(f'You selected: {age}')

# Checkbox
if st.checkbox('Show/Hide'):
    st.write('Checkbox is checked!')

# Radio button
status = st.radio('Select your status:', ('Active', 'Inactive'))
st.write(f'Status: {status}')

# Button
if st.button('Click me'):
    st.write('Button clicked!')
