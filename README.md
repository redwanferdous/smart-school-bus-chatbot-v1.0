# smart-school-bus-chatbot-v1.0
Chatbot for supporting Smart School Bus system, Chattogram (https://smartschoolbus.gov.bd)

This project is designed to run entirely on **Google Colab**, making it easy to use without any local setup.  
It provides step-by-step execution of code blocks, ensuring that even beginners can follow along and reproduce the results.  

You can explore, modify, and run the code in your own Colab environment without needing to install additional software.  
The main goal of this repository is to provide a simple, reproducible workflow for your project. 

---
## Extended Description

This project is a **RAG (Retrieval-Augmented Generation)** powered chatbot built for FronTech’s Smart School Bus Solution 🚍🤖.

Unlike standard chatbots that only rely on their pre-trained knowledge, this RAG chatbot combines vector embeddings + GPT to:

-Retrieve relevant information from a given PDF document.
-Generate accurate, context-aware answers.
-Provide evidence-based responses instead of relying only on memory.

**Tech Stack**

-Python → Core logic & processing.
-Sentence-Transformers + NumPy → Vector embeddings & similarity search.
-OpenAI API (GPT-4) → Answer generation.
-Streamlit → User-friendly interface.
-pypdf → Extracting text from PDF.

**Key Features**

-Upload a PDF (e.g., project documentation or manuals).
-Ask natural language questions.
-Get precise answers based on context from the PDF.

**Challenges**

During development, one challenge was that similarity scores often came low (0.65 or ~0.6) 😅, but the model still successfully extracted correct information.

**Future Plan**

The next step is to integrate this chatbot directly into the Smart School Bus live system so that:
-Parents can ask questions like “Where is my child’s bus now?” 📍
-Get real-time updates about departure and arrival.
-Build a more human-centric experience for guardians 👨‍👩‍👧‍👦.

---

## Setup
1. Open the Google Colab link provided in this repository.  
2. Make sure you are signed in to your Google account.  
3. Click **"Copy to Drive"** to create your own editable copy.  

---

## Configuration
- No installation is required — everything runs directly in Colab.  
- If external credentials (such as API keys, dataset paths, etc.) are needed, you must enter them manually in the notebook.  
- Replace placeholders like `YOUR_API_KEY` with your actual values when prompted in the notebook.  

---

## Usage
1. Open the notebook in Google Colab.  
2. Run each cell sequentially from top to bottom.  
3. Provide any required inputs when prompted (such as credentials or dataset links).  
4. Review the outputs and modify parameters as needed.  

---

## Example
```python
# Example: running a function in the notebook
result = my_function(input_data)
print(result)
````

---

## Contributing

Contributions are welcome!
If you’d like to suggest improvements or fix issues:

1. Fork this repository.
2. Make your changes.
3. Submit a pull request.

---

## License

This project is licensed under the APACHE License2.0 — see the [LICENSE](LICENSE) file for details.

```
```

