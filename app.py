import streamlit as st

from project import write_properly, write_the_same_grammar_fixed, summarize


def main():
    st.title("Intelli Text Processing Application")
    st.caption("A Python-based application leveraging the OpenAI API and Transformers \
    library to create an agent that assists non-native English speakers in improving their written English. \
    The application does not involve model training or fine-tuning but focuses on effective prompt engineering using the \
    Retrieval-Augmented Generation (RAG) approach when needed. The agent will provide three primary functionalities below:")
    st.write('1. Write Properly: Enhances both the grammar and style of the input message.')
    st.write('2. Correct Grammar: Correct only the grammatical errors in the input message.')
    st.write('3. Summarize : Provide a concise summary of the input message"')
    ## creating a side bar to select an option for three services properly from drop down
    function_choice = st.sidebar.selectbox("Select a function from this drop down", ("Write Properly", "Fix Grammar", "Summarize"))
    ## text box for user input message 
    input_message = st.text_area("Enter your message")
    ## creating button to initiate the process
    if st.button("Process"):
        if function_choice == "Write Properly":
            result = write_properly(input_message)
        elif function_choice == "Fix Grammar":
            result = write_the_same_grammar_fixed(input_message)
        elif function_choice == "Summarize":
            result = summarize(input_message)

        st.write("Result:")
        ## model output
        st.write(result)

if __name__ == "__main__":
    main()

