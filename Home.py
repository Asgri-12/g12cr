# import module
import streamlit as st
from PIL import Image


img = Image.open("Banner.png")

# Title
st.title("Cancer Possibilites")

st.image(img)

st.header('What is Cancer?')
st.write("""Cancer is a disease in which some of the body’s cells grow uncontrollably and spread to other parts of the body. 

Cancer can start almost anywhere in the human body, which is made up of trillions of cells. Normally, human cells grow and multiply (through a process called cell division) to form new cells as the body needs them. When cells grow old or become damaged, they die, and new cells take their place.

Sometimes this orderly process breaks down, and abnormal or damaged cells grow and multiply when they shouldn’t. These cells may form tumors, which are lumps of tissue. Tumors can be cancerous or not cancerous (benign). 

Cancerous tumors spread into, or invade, nearby tissues and can travel to distant places in the body to form new tumors (a process called metastasis). Cancerous tumors may also be called malignant tumors. Many cancers form solid tumors, but cancers of the blood, such as leukemias, generally do not.

Benign tumors do not spread into, or invade, nearby tissues. When removed, benign tumors usually don’t grow back, whereas cancerous tumors sometimes do. Benign tumors can sometimes be quite large, however. Some can cause serious symptoms or be life threatening, such as benign tumors in the brain.""")

