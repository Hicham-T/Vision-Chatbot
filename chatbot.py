import streamlit as st
from langchain_community.llms import Ollama
import base64
from io import BytesIO
from PIL import Image


def convert_to_base64(image_file_path):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    pil_image = Image.open(image_file_path)

    buffered = BytesIO()
    pil_image.save(buffered, format="png")  
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def convert_to_html(img_base64):
    """
    Disply base64 encoded string as image

    :param img_base64:  Base64 string
    """
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" style="max-width: 100%;"/>'
    return image_html




st.set_page_config(layout="wide")

st.title("Local image chatbot")
def upload_image():
    images = st.file_uploader("Upload an image to chat about", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    # assert max number of images, e.g. 7
    assert len(images) <= 7, (st.error("Please upload at most 7 images"), st.stop())

    if images:
        # convert images to base64
        images_b64 = []
        for image in images:
            image_b64 = convert_to_base64(image)
            images_b64.append(image_b64)

        # display images in multiple columns
        cols = st.columns(len(images_b64))
        for i, col in enumerate(cols):
            col.markdown(f"**Image {i+1}**")
            col.markdown(convert_to_html(images_b64[i]), unsafe_allow_html=True)
        st.markdown("---")
        return images_b64
    st.stop()


@st.cache_data(show_spinner=False)
def ask_vllm(question, image_b64, model):
    llm = Ollama(model=st.session_state.model)
    llm_with_image_context = llm.bind(images=image_b64)
    res = llm_with_image_context.invoke(question)
    return res


def app():
    st.session_state["model"] = st.selectbox("Choose a model", ["minicpm-v:latest", "llava", "minicpm-v:8b-2.6-q2_K"])
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c2:
        image_b64 = upload_image()
    with c1:
        question = st.chat_input("Ask a question about the image(s)")
    if not question: st.stop()
    with c1:
        with st.chat_message("question"):
            st.markdown(question, unsafe_allow_html=True)
        with st.spinner("Thinking..."):
            res = ask_vllm(question, image_b64, model=st.session_state["model"])
            with st.chat_message("response"):
                st.write(res)



if __name__ == "__main__":
    app()