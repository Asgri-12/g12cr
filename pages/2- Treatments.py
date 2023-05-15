# import module
import streamlit as st
from PIL import Image
img = Image.open("img2.jpg")

# Title
st.title("Treatment")
st.image(img)
st.write("Cancer treatment is based on the stage of the cancer. Sometimes, treatment is meant to cure the cancer. Other times, the goal is to stop the cancer from spreading further.")

st.subheader("Common Types of Cancer Treatment")
st.write("""Surgery: An operation where doctors cut out tissue with cancer cells.""")
st.write("""Chemotherapy: Special medicines that shrink or kill cancer cells.""")
st.write("""Radiation therapy: Using high-energy rays (similar to X-rays) to kill cancer cells.""")
st.write("""Hormone therapy: Blocks cancer cells from getting the hormones they need to grow.""")
st.write("""Immunotherapy: A treatment that works with your body’s immune system to help it fight cancer cells or to control side effects from other cancer treatments.""")
st.write("""Stem cell transplant (bone marrow transplant): Replace bone marrow cells lost due to very high doses of chemotherapy or radiation therapy. Most commonly used to treat blood cancers and cancers in lymph nodes.""")
