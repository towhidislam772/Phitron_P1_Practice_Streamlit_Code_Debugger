# 🐞 Code Debugger and Solution Provider

An AI-powered **Streamlit** web app that reads a screenshot of your code error and helps you fix it — choose between getting **guided hints** (no direct answer) or the **full corrected code**, powered by **Google Gemini**.

Upload a photo of your error, pick a mode, and let AI guide you (or solve it for you)! 🚀

---

## ✨ Features

- 📷 **Image Upload** — Upload a single screenshot/photo of your code error (`jpg`, `jpeg`, `png`)
- 💡 **Hints Mode** — Gemini analyzes the error and gives you progressive hints with examples, **without** revealing the fix — great for learning
- ✅ **Solution Mode** — Gemini gives you the fully corrected code plus explanatory hints
- 🛡️ **Robust Error Handling** — Gracefully handles invalid images, API rate limits (daily quota), and server overload instead of crashing
- 🎛️ **Clean UI** — Sidebar controls, image preview, loading spinners, and neatly bordered result sections

---

## 🖥️ Demo Workflow

1. Upload a photo of your code error from the sidebar
2. Select what you want: **Hints** or **Solution with code**
3. Click **"Enter to Debug"**
4. Get:
   - 💡 A set of guided hints (Hints mode), **or**
   - 📄 The fully corrected code with explanation (Solution mode)

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io/) |
| AI Model | [Google Gemini](https://ai.google.dev/) (`gemini-3.1-flash-lite`) via `google-genai` SDK |
| Image Handling | Pillow (PIL) |
| Environment Config | python-dotenv / Streamlit Secrets |

---

## 📂 Project Structure

```
Code-Debugger-and-Solution-Provider/
│
├── app.py              # Streamlit UI — upload, controls, and result display
├── api_calling.py      # Gemini API calls for hints/solution generation + error handling
├── requirements.txt    # Project dependencies
├── .env                # API key for local dev (not committed)
├── .streamlit/
│   └── secrets.toml    # API key for local parity with deployment (not committed)
└── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1. Clone the repository

```bash
git clone https://github.com/towhidislam772/Phitron_P1_Streamlit_Gemini_Note_Genarator.git
cd Phitron_P1_Streamlit_Gemini_Note_Genarator
```

### 2. Create & activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit google-genai gTTS pillow python-dotenv
```

### 4. Set up your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploying to Streamlit Community Cloud

This app is built to work seamlessly both locally (`.env`) and when deployed (`st.secrets`) — no code changes needed.

1. Push your code to GitHub (make sure `.env` and `.streamlit/secrets.toml` are in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a **New app**
3. Connect your GitHub repo and select `app.py` as the main file
4. In your app's **Settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
5. Save and deploy — the app automatically picks up the key via `st.secrets`

---

## 🧠 How It Works

1. **`app.py`** lets the user upload one error screenshot, converts it to a PIL `Image`, and handles all UI logic and error display.
2. **`api_calling.py`** loads the Gemini API key from `st.secrets` (deployment) or `.env` (local), whichever is available.
3. **`hints_generator()`** sends the image with a prompt instructing Gemini to give hints and examples **without** revealing the fixed code.
4. **`solution_generator()`** sends the image with a prompt instructing Gemini to return the **fully corrected code** with explanation.
5. Both functions wrap the Gemini API call in `try/except`, catching:
   - `ClientError` (e.g. `429` daily quota exceeded)
   - `ServerError` (e.g. `503` server overloaded)
   - Any other unexpected exception

   and return a friendly `⚠️` message string instead of crashing. `app.py` detects the `⚠️` prefix and renders it via `st.warning()` instead of plain markdown.

---

## 📌 Notes & Limitations

- Only **1 image** per request (single error screenshot at a time)
- Requires an active internet connection (Gemini API)
- Keep your `.env` / `secrets.toml` private — never commit your API key
- Hints mode is designed for learning — it intentionally withholds the direct fix

---

## 🚀 Future Improvements

- [ ] Support multiple error screenshots in one request
- [ ] Language/framework detection for more targeted hints
- [ ] Downloadable solution as a `.py` / `.txt` file
- [ ] Step-by-step hint reveal (progressive disclosure) in the UI

---

## 👨‍💻 Author

**Md. Towhidul Islam**

- GitHub: [@towhidislam772](https://github.com/towhidislam772)

---

## 📄 License

This project was built as part of the **Phitron** curriculum. Feel free to fork, learn from, and build upon it!
---

⭐ If you found this project helpful, consider giving it a star!
