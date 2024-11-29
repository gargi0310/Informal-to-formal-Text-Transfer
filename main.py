import streamlit as st
from transformers import pipeline

pipe = pipeline("text2text-generation", model="rajistics/informal_formal_style_transfer")

st.title("Informal to Formal Text Style Transfer")

st.markdown("""
This app converts informal text to formal language using a pre-trained model. 
Enter your text in the box below, and see the magic happen!
""")

text = st.text_area("Enter informal text", placeholder="Type something informal...")

# Generate button
if st.button("Transform Text"):
    if text.strip():
        with st.spinner("Transforming..."):
            prompt = f"transfer informal to formal: {text}"
            
            try:
                output = pipe(prompt)
                formal_text = output[0]['generated_text']
                
                st.success("Here is the formal text:")
                st.write(formal_text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text!")
