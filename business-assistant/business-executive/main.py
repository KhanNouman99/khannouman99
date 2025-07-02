from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from gpt4all import GPT4All

app = FastAPI(
    title="Business Executive",
    description="Your personal AI assistant for business letters, policies, and more.",
    version="1.1.0"
)

# Enable CORS for browser to send/receive
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load GPT4All model
model = GPT4All(
    model_name="Llama-3.2-1B-Instruct-Q4_0.gguf",
    model_path="C:/Users/PC/AppData/Local/nomic.ai/GPT4All",
    allow_download=False
)

# ✅ General chatbot endpoint
@app.get("/ask")
def ask(prompt: str = Query(..., description="Type any business-related question")):
    response = model.generate(prompt)
    return JSONResponse(content={"response": response})

@app.get("/")
def read_root():
    return {"message": "Business Executive is ready with GPT4All connected."}

@app.get("/experience-letter")
def experience_letter(name: str, role: str, years: int):
    prompt = f"Write a formal experience letter for {name}, who worked as a {role} for {years} years."
    return {"letter": model.generate(prompt)}

@app.get("/termination-letter")
def termination_letter(name: str, reason: str):
    prompt = f"Write a professional termination letter for {name} due to {reason}. Keep the tone respectful."
    return {"letter": model.generate(prompt)}

@app.get("/job-post")
def job_post(title: str, skills: str, location: str):
    prompt = f"Write a job post for a {title} with skills like {skills} in {location}."
    return {"post": model.generate(prompt)}

@app.get("/company-policy")
def company_policy(topic: str):
    prompt = f"Write a professional company policy on: {topic}"
    return {"policy": model.generate(prompt)}

@app.get("/payslip-help")
def payslip_help(employee_name: str, month: str, amount: str):
    prompt = f"Generate a polite explanation message about the payslip for {employee_name} for the month of {month}, with total salary {amount}."
    return {"message": model.generate(prompt)}

@app.get("/notification")
def notification(subject: str, details: str):
    prompt = f"Write a formal notification for: {subject}. Include these details: {details}"
    return {"notification": model.generate(prompt)}

@app.get("/email-reply")
def email_reply(context: str):
    prompt = f"Write a professional email reply based on this context: {context}"
    return {"email": model.generate(prompt)}

@app.get("/project-update")
def project_update(project_name: str, status: str, next_steps: str):
    prompt = (
        f"Write a project update for {project_name}. Current status: {status}. "
        f"Next steps: {next_steps}. Format it as an internal update for the team."
    )
    return {"update": model.generate(prompt)}

# ✅ Serve chatbot interface
@app.get("/chat")
def serve_chat_ui():
    return FileResponse("chat.html")

