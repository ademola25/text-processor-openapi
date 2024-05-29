# Text PRocessing App

## Description
How to run the application and this also provide more details about the app.

## Insert the openai secret key 
Insert openai secret key for OPEN_API_KEY in env file


## How to Run the App

### With Docker

docker build -t ml-openai-app .
docker run -p 8000:8000 ml-openai-app

### With Dvirtual environment
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
pip install -r requirements.txt
streamlit run app.py

### Drop down on web UI
For the drop down on the Ui to change from one function to another.


###  Exception Handling
Exception Log
Exceptions are logged into a log file to facilitate detailed inspections when needed.

### Error Decorator
Using a decorator simplifies the management of try-except blocks across multiple functions, reducing code repetition and enhancing maintainability.


### If error faced: 
If you encounter following error: 

TomlDecodeError: Key group not on a line by itself
streamlit cache clear
It will output: 
Nothing to clear at /{some addresss}/cache.
Go to that address: 
cd {address}
remove the file : config.toml
In ubuntu : type the following command to remove the file. 
sudo rm config.toml 



### STREAMLIT FOR FRONT END:
Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. 

I wanted to use react but i conclude react will be an overkill when the streamlit already acheive the purpose seamlessly.

### Contributing
IF i were to use transformer (hugging face) which i didnt use because chatgpt 3.5 is not accessible to transformer. Below is the transfer model trending that i would use'
 

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)
pipeline("Hey how are you doing today?")



<!-- API log -->
### API sample log
For write_properly function
Sample text: "Meta AI have been focusing on things that use withmuch existing platforms and move into new frontiers like the metaverse."

Result from the model: "Meta AI has been focused on utilizing existing platforms and expanding into new frontiers such as the metaverse."

for write_the_same_grammar_fixed function

Sample text: "It can answered your many question, summarized search result and even helps you plans activities within chats"
Result: "It can answer many of your questions, summarize search results, and even help you plan activities within chats."

for summarize function.
Sample text: "We’re beta launching SynthID, a tool for watermarking and identifying AI-generated content. With this tool, users can embed a digital watermark directly into AI-generated images or audio they create. This watermark is imperceptible to humans, but detectable for identification.
Being able to identify AI-generated content is critical to promoting trust in information. While not a silver bullet for addressing the problem of misinformation, SynthID is an early and promising technical solution to this pressing AI safety issue.
This technology was developed by Google DeepMind and refined in partnership with Google Research. SynthID could be further expanded for use across other AI models and we plan to integrate it into more products in the near future, empowering people and organizations to responsibly work with AI-generated content"

Result: "SynthID, a tool developed by Google DeepMind and Google Research, is being beta launched for watermarking and identifying AI-generated content. Users can embed imperceptible digital watermarks into AI-generated images or audio for identification. This technology aims to promote trust in information and address the issue of misinformation, offering a promising solution to AI safety concerns. Future plans include expanding SynthID for use across other AI models and integrating it into more products to empower responsible work with AI-generated content."

# text-processor-openapi
