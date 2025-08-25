# Streamlit Demos

This repository contains a collection of demos created while learning Streamlit.
Streamlit makes it easy to build interactive web applications using Python, without needing to write HTML, CSS, or JavaScript.

## 🚀 Quick Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Krish-Naidu/Streamlit.git
   cd Streamlit
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/Scripts/activate  # On Windows
   # Or
   source myenv/bin/activate      # On Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your API keys if needed.

### Running a Demo
```bash
streamlit run <demo_file.py>
```
For example:
```bash
streamlit run 9_vector_store_demo.py
```

## 📋 Demo List
- `1_form_demo.py`: Form handling and user input
- `2_chat_demo.py`: Chat interface implementation
- `3_pydanticai_demo.py`: Pydantic AI integration
- `4_chatGPT_clone.py`: ChatGPT-like interface using Gemini
- `5_read_pdf_demo.py`: PDF reading and processing
- `6_file_upload_demo.py`: File upload functionality
- `7_multi_file_upload.py`: Multiple file upload handling
- `8_embedding_demo.py`: Text embeddings demonstration
- `9_vector_store_demo.py`: ChromaDB Vector Store with persistent database

## 🔑 Environment Variables
Some demos require API keys (e.g., Google Generative AI). Add them to your `.env` file:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## 📦 Requirements
See `requirements.txt` for all dependencies. Core packages include:
- streamlit
- chromadb
- pandas
- numpy
- pillow
- PyPDF2
- pydantic-ai
- google-generativeai
- python-dotenv

## 🧪 Testing
To verify your environment and configuration, run:
```bash
python test_env_config.py
```

## 📚 Documentation
- [INSTALLATION.md](INSTALLATION.md): Detailed setup instructions
- [CHROMADB_README.md](CHROMADB_README.md): ChromaDB usage and features

## 🤝 Contributing
Feel free to fork the repo and submit pull requests with improvements or new demos!

## 📝 License
This project is for educational purposes.
