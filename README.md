
# ⚖️ Legal Chatbot

An AI-powered chatbot that answers legal questions using Retrieval-Augmented Generation (RAG).
Built with Python, it combines large language models and embeddings to deliver contextual responses based on legal documents.

---

## ✨ Features

* Ask legal questions and get instant AI-powered answers
* Retrieval-Augmented Generation (RAG) for better accuracy
* Handles large legal documents
* Modular and clean Python codebase
* Environment variables managed securely via `.env`

---

## 📂 Project Structure

```
legal_chatbot/
├── app.py              # Chatbot logic and response handling and entry point (e.g. Streamlit UI)
├── rag_engine.py       # RAG logic (embeddings, retrieval)
├── data/
│    └── sample_legal_docs/  # Legal documents for testing
├── .env.example        # Example env file (no secrets)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/iamudayshaharwle/legal-chatbot.git
cd legal-chatbot
```

(Optional) Create a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in your project root with the following:

```
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

> **Important:** Never commit your real `.env` to GitHub.
> Use `.env.example` to show others how to configure the project.

---

## 🚀 Running the App

If using Streamlit:

```bash
streamlit run app.py
```

---

## 📝 Example Usage

> **User:** What is a legal contract?
> **Bot:** A legal contract is a legally enforceable agreement between two or more parties...

---

## 🛡 Security Notes

* Keep API keys private in `.env`.
* Add `.env` to `.gitignore` to avoid leaking secrets.

---

## 📄 License

This project is open-source under the MIT License.

---

## 🤝 Contributing

Pull requests and issues are welcome! Help improve this chatbot.

---

## 👤 Author

* [Uday Shaharwale](https://github.com/iamudayshaharwle)

---
