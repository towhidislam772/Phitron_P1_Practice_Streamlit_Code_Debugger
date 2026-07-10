#pip install streamlit google-genai gTTS pillow python-dotenv

import streamlit as st

from api_calling import hints_generator, solution_generator
from PIL import Image, UnidentifiedImageError

#to run this
#streamlit run app.py

#title
st.title(" Code Debugger and Solution Provider", anchor=False)
st.subheader("Upload your error image to find the error and get solution of it")
st.divider()

pil_image = None

with st.sidebar:
    st.header("Controls")

    #image
    image = st.file_uploader("Upload Your photo of your code error",
                     type=["jpg", "jpeg", "png"],
                     accept_multiple_files=False)

    if image is not None:
        try:
            pil_image = Image.open(image)
            st.subheader("Your uploaded Image:")
            st.image(image, width=300)
        except UnidentifiedImageError:
            st.error("⚠️ Couldn't read this file as an image. Please upload a valid jpg/jpeg/png.")
            pil_image = None
        except Exception as e:
            st.error(f"⚠️ Error loading image: {e}")
            pil_image = None

    #difficulty
    selected = st.selectbox("Enter what you want me to do: ",
             ("Hints", "Solution with code"),
             index=None,
             accept_new_options=True)

    pressed = st.button("Enter to Debug", type="primary")

if pressed:
    if not image:
        st.error("Upload image first")
    elif pil_image is None:
        st.error("Please upload a valid image before continuing")
    elif not selected:
        st.error("You must select an option")
    else:
        if selected == "Hints":
            with st.container(border=True):
                st.subheader("Your Hints")

                with st.spinner("Ai is writing hints for you......."):
                    generated_hints = hints_generator(pil_image)

                    if generated_hints.startswith("⚠️"):
                        st.warning(generated_hints)
                    else:
                        st.markdown(generated_hints)

        if selected == "Solution with code":
            with st.container(border=True):
                st.subheader("Your Solution")

                with st.spinner("Ai is writing solution for you......."):
                    generated_solution = solution_generator(pil_image)

                    if generated_solution.startswith("⚠️"):
                        st.warning(generated_solution)
                    else:
                        st.markdown(generated_solution)