import streamlit as st 
from src.helper import voice_input, text_to_speech, llm_model_object


def main():
    st.title("Multilingual AI Assistant")
    st.header('Look :coffee: My first Appplication AI based :beer:', divider='rainbow')
    st.header('Vikram Singh :eyes: is :blue[cool] :sunglasses:')
    col1, col2 = st.columns(2)
    #row1 = st.columns(3)
    with col1:
        st.header("Listen What I'm Saying")
        st.image("https://static.streamlit.io/examples/dog.jpg",width=160)
    with col2:
        if st.button("Ask me question!"):
             with st.spinner("Listening..."):
                text = voice_input()
                response = llm_model_object(text)
                text_to_speech(response)


            # Display audio player and download link
                audio_file = open("speech.mp3", 'rb')
                audio_bytes = audio_file.read()
                #tile = col3.container(height=120)
                #tile.title(":balloon:")
                st.text_area(label="Response:", value=response, height=350)
                st.audio(audio_bytes, format='audio/mp3')
                st.download_button(label="Download Speech",
                                    data=audio_bytes,
                                    file_name="speech.mp3",
                                    mime="audio/mp3")
            
if __name__ == "__main__":
    main()   
