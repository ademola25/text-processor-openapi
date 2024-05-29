import streamlit as st

from project import write_properly, write_the_same_grammar_fixed, summarize


### Main function
def main():
    ## adding page title
    st.title("Intelli Text Processing Application")
    ## creating a side bar to select an option for three services properly from drop down
    function_choice = st.sidebar.selectbox("Select a function", ("Write Properly", "Fix Grammar", "Summarize"))
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

