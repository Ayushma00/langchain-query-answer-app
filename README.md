# README

## Ask Me Anything

This Streamlit app, titled "Ask Me Anything", serves as your answer buddy, capable of providing answers to your queries using web links you provide. The app utilizes various technologies and libraries, including Langchain, Streamlit, OpenAI, and FAISS.

### How to Use

1. **Input Web Links**: On the sidebar, provide up to three website URLs where the app will search for answers to your queries.

2. **Submit URLs**: After entering the URLs, click the "Submit" button on the sidebar to proceed.

3. **Query Input**: Once the URLs are submitted, a text input field will appear below. Enter your query in this field.

4. **Get Answers**: After entering your query, the app will process the information from the provided URLs and attempt to answer your query. The answer will be displayed on the main panel.

### Technologies Used

- **Streamlit**: The app's user interface is created using Streamlit, allowing for easy interaction and visualization of results.
  
- **Langchain**: Langchain is utilized for processing text data, including text splitting, embedding generation, and document retrieval. It integrates with OpenAI for language models and FAISS for efficient similarity search.

- **OpenAI**: OpenAI's language model is used for generating answers to user queries. The model is fine-tuned for question answering tasks.

- **FAISS**: FAISS is employed for efficient similarity search of embeddings generated from the provided web content. It helps in retrieving relevant information for answering user queries.

### Development

The code for this app is written in Python and is available in the provided script. To run the app locally, ensure you have the necessary dependencies installed. You can install dependencies using pip and the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

Once dependencies are installed, run the script `app.py` to launch the Streamlit app locally. The app will be accessible through your web browser.

### Disclaimer

This app relies on information available on the provided web links for generating answers. The accuracy and relevance of the answers may vary based on the quality and content of the linked web pages. Additionally, the app may have limitations in understanding context and nuances, so results should be interpreted with caution.
