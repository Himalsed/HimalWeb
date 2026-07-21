from flask import Flask, render_template, request, redirect, url_for, flash
from flask_compress import Compress

Compress(app)
import os
app = Flask(__name__)
app.secret_key = "portfolio-dev-key"



PROFILE = {
    "name": "Himal Sedhai",
    "role": "Full-Stack Developer",
    "tagline": "I am a Bachelor of Information Management (BIM) student from Nepal with a strong interest in Full Stack Development and Artificial Intelligence."
"Currently, I'm building practical web applications while learning Machine Learning, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG)."
    ,
    "location": "Based in Nepal",
    "email": "himalsedhai10@example.com",
    "github": "https://github.com/Himalsed",
    "linkedin": "https://linkedin.com/in/HimalSedhai",
}

ABOUT = {
    "summary": (
      " I'm a Computer Science student who enjoys turning ideas into practical software. I like building projects that solve real-world problems while continuously exploring new technologies."
"My main interests are Python,AI, and full-stack development. I've worked on projects ranging from web applications to AI-powered systems, including a Retrieval-Augmented Generation (RAG) knowledge hub, a Book Management System, personal portfolio websites, and productivity-focused applications. I enjoy taking a project from idea to deployment, learning something new at every step."
"I believe the best way to improve as a developer is by building. Whether it's designing clean user interfaces, creating backend logic, integrating APIs, or deploying applications, I enjoy the complete development process. I'm always looking for opportunities to expand my skills and contribute to meaningful projects."
"Currently, I'm focused on improving my software engineering skills, exploring artificial intelligence, and building applications that make everyday tasks simpler and more efficient."
    ),
    "education": [
        {
            "period": "2024 — present",
            "title": "Bachelor in Information Management",
            "place": "Tribhvan University",
            "detail": "Coursework in data structures, databases, and web development,Python,AI.",
        },
        {
            "period": "2021 — 2023",
            "title": "Higher Secondary Education",
            "place": "New Capital Secondary School",
            "detail": "Focused on physics, mathematics, and computer science.",
        },
    ],
}
TECH_STACKS = [
    {
        "category": "Languages",
        "skills": [
            {"name": "Python", "icon": "devicon-python-plain colored"},
            {"name": "JavaScript", "icon": "devicon-javascript-plain colored"},
            {"name": "HTML5", "icon": "devicon-html5-plain colored"},
            {"name": "CSS3", "icon": "devicon-css3-plain colored"},
            {"name": "SQL", "icon": "devicon-azuresqldatabase-plain colored"},
            {"name":"PHP","icon":"devicon-php-colored"}
            
        ],
    },
    {
        "category": "Frameworks",
        "skills": [
            {"name": "Flask", "icon": "devicon-flask-original colored"},
            {"name": "React", "icon": "devicon-react-original colored"},
            {"name": "Node.js", "icon": "devicon-nodejs-plain colored"},
            {"name": "Bootstrap", "icon": "devicon-bootstrap-plain colored"}
        ],
    },
    {
        "category": "Tools",
        "skills": [
            {"name": "Git", "icon": "devicon-git-plain colored"},
            {"name": "GitHub", "icon": "devicon-github-original colored"},
            {"name": "VS Code", "icon": "devicon-vscode-plain colored"},
            {"name": "Figma", "icon": "devicon-figma-plain colored"},
  
        ],
    },
    {
        "category": "Databases",
        "skills": [
            {"name": "MySQL", "icon": "devicon-mysql-plain colored"},
            {"name": "SQLite", "icon": "devicon-sqlite-plain colored"},
            {"name": "MongoDB", "icon": "devicon-mongodb-plain colored"}
        ],
    },
]

PROJECTS = [
    {
        "id": 1,
        "title": "DevMemory AI - powered CLI based Weapon",
        "description": (
    "A local AI assistant that helps developers remember and search their own codebase. "
    "Developers work on multiple projects and often forget where they wrote a specific function, "
    "how a feature was implemented, or where certain logic exists. "
    "DevMemory AI solves this by creating a searchable memory of your code using embeddings, "
    "vector search, and a local LLM. "
    "The project runs locally, meaning your code stays on your machine."
        ),
        "stack": "Flask · RAG · ChromaDB ·Typer. LLM :Olama ",
        "link": "https://github.com/Himalsed/DevMemory-AI",
    },



    
    {
        "id": 2,
        "title": "Hotel-Hub" "Ai-powered using RAG for Hotels" ,
        "description": (
          "Hotel Knowledge Hub is an AI-powered chatbot that answers hotel-related questions using Retrieval-Augmented Generation (RAG)."
          "  Instead of relying only on an LLM, it retrieves relevant information from hotel knowledge documents and generates accurate,"
              "context-aware responses."
        ),
        "stack": "Flask · RAG · ChromaDB . LLM :Lama ",
        "link": "https://github.com/Himalsed/Hotel-Hub",
    },
    {
        "id": 3,
        "title": "Book Sys MGMT",
        "description": (
           " A full-stack web application designed to manage a library or personal book collection. "
            "This project allows users to perform core CRUD operations (Create, Read, Update, Delete) on books, track inventory, and manage authors."
        ),

        
        
        "stack": "HTML5 · CSS· JAVASCRIPT·EXPRESS ·MongoDB·",
        "link": "https://github.com/Himalsed/Book-Mgmt-Sys",
    }
    
]

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        about=ABOUT,
        tech_stacks=TECH_STACKS,
        projects=PROJECTS,
    )

@app.after_request
def security_headers(response):

    response.headers["X-Frame-Options"] = "SAMEORIGIN"

    response.headers["X-Content-Type-Options"] = "nosniff"

    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

    return response


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in every field before sending.", "error")
    else:
       
        flash("Thanks — your message has been sent.", "success")

    return redirect(url_for("home") + "#contact")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
