
# 🔐 Secure AI Chatbot (Flask + JWT + NLP)

A secure, context-aware chatbot built using:

- Python
- Flask
- JWT Authentication
- Scikit-learn (Intent Classification)
- In-memory Conversation Context

This project demonstrates backend API design, authentication, machine learning integration, and clean architecture principles.

---

## 🚀 Features

- 🔐 JWT-based authentication
- 👥 Role-based access (admin / user)
- 🧠 Intent classification using trained ML model
- 💬 Context-aware conversation handling
- 🌐 REST API architecture
- 📦 Deployment-ready structure

---

## 📁 Project Structure

```
chatbot-project/
│
├── backend/
│   ├── app.py              # Main Flask application
│   ├── chatbot.py          # ML prediction + context logic
│   ├── auth.py             # Login & register logic
│   ├── memory.py           # In-memory context storage
│   ├── train.py            # Model training script
│   ├── intents.json        # Training dataset
│   ├── model.pkl           # Generated after training
│   └── vectorizer.pkl      # Generated after training
│
├── requirements.txt
└── README.md
```

---

# 🧠 How to Train the Model

The chatbot uses intent classification trained from `intents.json`.

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the model

```bash
python backend/train.py
```

This will generate:

- `model.pkl`
- `vectorizer.pkl`

These files are required for chatbot responses.

---

# ▶️ How to Run the Application

### Step 1: (Optional) Set JWT Secret Key

On Windows:

```bash
set JWT_SECRET_KEY=super-secret-key
```

On Mac/Linux:

```bash
export JWT_SECRET_KEY=super-secret-key
```

---

### Step 2: Run the Flask app

```bash
python backend/app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

# 🔑 API Endpoints

## 🔹 Register

```
POST /register
```

Body:
```json
{
  "username": "user1",
  "password": "1234"
}
```

---

## 🔹 Login

```
POST /login
```

Body:
```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:
```json
{
  "access_token": "<JWT_TOKEN>"
}
```

---

## 🔹 Chat (Protected Endpoint)

```
POST /chat
```

Headers:
```
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

Body:
```json
{
  "message": "What is SQL injection?"
}
```

---

# 🧠 Context Handling

The chatbot stores the last 5 user messages per user session.

Example:

User: What is cybersecurity?  
User: And SQL injection?  

The chatbot interprets follow-up questions using conversation history.

---

# 🛠 Technologies Used

- Python
- Flask
- Flask-JWT-Extended
- Scikit-learn
- NLTK
- REST API Architecture

---

# 📦 Deployment

The application can be deployed using platforms such as:

- Render
- Railway
- Heroku

Required Environment Variable:

```
JWT_SECRET_KEY
```

---

# 🎯 Interview Highlights

- Implemented secure REST API with JWT authentication
- Built intent classification model using scikit-learn
- Designed modular backend structure
- Integrated context-aware conversation logic
- Followed Git best practices by excluding ML artifacts

---

## 👨‍💻 Author

Girish Gowda
