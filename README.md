# Medical Chatbot

An AI-powered medical chatbot built with Flask, LangChain, and Pinecone that provides medical information using retrieval-augmented generation (RAG).

## Features

- **RAG-based Q&A System**: Leverages retrieval-augmented generation for accurate medical information
- **Vector Database**: Uses Pinecone for efficient semantic search of medical documents
- **Web Interface**: Clean, responsive chat interface built with Flask
- **PDF Processing**: Extracts and processes medical information from PDF documents
- **Semantic Search**: Uses Hugging Face embeddings for intelligent document retrieval

## Tech Stack

- **Backend**: Flask
- **LLM Framework**: LangChain
- **Vector Database**: Pinecone
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **LLM**: Google Gemini 2.0 Flash
- **Frontend**: HTML/CSS with chat interface

## Project Structure

```
Medical-Chatbot/
├── app.py                 # Main Flask application
├── store_index.py         # Script to build and populate vector database
├── data/                  # Medical PDF documents
│   └── Medical_book.pdf
├── src/
│   ├── helper.py          # Helper functions for PDF processing and embeddings
│   └── prompt.py          # System prompts for the chatbot
├── templates/
│   └── chat.html          # Chat interface template
├── static/
│   └── style.css          # Styling for the chat interface
└── requirements.txt       # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Medical-Chatbot.git
cd Medical-Chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```env
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key  # If using OpenAI
GOOGLE_API_KEY=your_google_api_key  # If using Gemini
```

4. Build the vector database:
```bash
python store_index.py
```
This will:
- Load PDF documents from the `data/` folder
- Split text into chunks
- Generate embeddings
- Store vectors in Pinecone index

5. Run the application:
```bash
python app.py

## How It Works

1. **Document Processing**: PDFs are loaded and split into manageable chunks
2. **Embedding Generation**: Text chunks are converted to vector embeddings using Sentence Transformers
3. **Vector Storage**: Embeddings are stored in Pinecone for fast retrieval
4. **Query Processing**: User questions are embedded and similar chunks are retrieved
5. **Answer Generation**: Retrieved context is passed to the LLM to generate accurate responses

## API Endpoints

- `GET /`: Serves the chat interface
- `POST /get`: Handles chat messages and returns AI responses

## Configuration

- **Chunk Size**: 500 characters (configurable in `src/helper.py`)
- **Retrieval Count**: Top 3 most relevant chunks (configurable in `app.py`)
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Dimension**: 384 (based on embedding model)

## Development

To run in development mode with auto-reload:
```bash
python app.py  # Debug mode is enabled by default
```

## Author

Surya Potnuru - GenAI Developer at Bobble AI

## License

This project is licensed under the MIT License - see the LICENSE file for details.