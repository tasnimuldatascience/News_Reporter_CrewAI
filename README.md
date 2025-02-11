# 📰 News Reporter CrewAI 🚀

This project is an AI-powered **news blog generator** using **CrewAI** and **Google Gemini API**. It researches tech topics and generates **detailed blog posts** in Markdown format.

## 📌 Features
- 🧠 **AI Research Agent**: Uncovers the latest trends in tech.
- ✍ **AI Writing Agent**: Creates structured blog posts.
- 📄 **Markdown Blog Output**: Saves content in `new-blog-post.md`.
- 🌐 **Streamlit UI**: Interactive interface for generating blogs.

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tasnimuldatascience/News_Reporter_CrewAI.git
cd News_Reporter_CrewAI
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your **Google API Key**:
```
GOOGLE_API_KEY=your_actual_google_api_key
```

## 🚀 Running the App
### 1️⃣ Start the Streamlit Web App
```bash
streamlit run app.py
```
- Open the browser link (`http://localhost:8501`).
- Enter a **topic** and click **"Generate Blog"**.

### 2️⃣ Run the CLI Version (Optional)
```bash
python crew.py
```

## 📂 Project Structure
```
📁 News_Reporter_CrewAI
 ├── .env                 # API keys
 ├── .gitignore           # Ignore unnecessary files
 ├── agents.py            # Defines AI agents
 ├── app.py               # Streamlit UI
 ├── crew.py              # CrewAI logic
 ├── new-blog-post.md     # Generated blog post
 ├── requirements.txt     # Python dependencies
 ├── tasks.py             # AI task definitions
 ├── tools.py             # Additional utilities
 └── README.md            # Project documentation
```

## 🔧 Dependencies
- `CrewAI`
- `langchain_google_genai`
- `streamlit`
- `python-dotenv`
- `google-generative-ai`
