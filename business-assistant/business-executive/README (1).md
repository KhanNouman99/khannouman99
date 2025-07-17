# Business Executive AI Assistant 💼🤖

This is a lightweight AI assistant powered by FastAPI and GPT4All. It helps CEOs and small business owners generate business templates like experience letters, termination letters, job posts, email replies, notifications, and more — via an easy chatbot interface.

## 🔧 Features

- ✉️ Experience / Termination letters
- 📋 Job posts
- 🧾 Payslip help
- 🏛️ Company policy generator
- 📢 HR notifications
- 📩 Email replies
- 📈 Project updates
- 💬 Chatbot-style frontend (HTML UI)

---

## 🚀 How to Run

### 1. Install Python libraries

```bash
pip install -r requirements.txt
```

### 2. Download GPT4All Model

Manually download the model (e.g., `llama3-8b-instruct.Q4_0.gguf`) from GPT4All and place it in:

```
C:/Users/YOUR_USERNAME/AppData/Local/nomic.ai/GPT4All/
```

Update the `model_name` and `model_path` in `main.py` if needed.

### 3. Run the API

```bash
uvicorn main:app --no-reload
```

Then open in browser:

```
http://127.0.0.1:8000/chat
```

---

## 🌐 Deployment

- Use services like **Render**, **Railway**, or **Deta Space** (free) to host online.
- FastAPI is compatible with n8n via HTTP Webhooks.

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT License