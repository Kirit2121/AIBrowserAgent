# 🕵️‍♂️ AI Browser Agent 🚀

## **Overview**
AI-powered browser automation agent that executes natural language instructions using DeepSeek & Ollama, automates web navigation, performs real-time bug detection, and generates test reports.

### **Tech Stack**
- **Python** (Main Language)
- **Ollama + DeepSeek-R1 (7B)** (AI Model)
- **Playwright** (Browser Automation)
- **FastAPI** (Backend API)
- **Gradio** (Web UI)
- **Docker** (For Deployment)

---

## **🔧 Installation**
### **1️⃣ Prerequisites**
- Install [Ollama](https://ollama.com) & download DeepSeek-R1 model:
  ```bash
  ollama pull deepseek/deepseek-coder:7b
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Install Playwright:
  ```bash
  playwright install
  ```

---

## **🚀 Running the Project**
### **1️⃣ Start AI Model Locally**
Run Ollama:
```bash
ollama serve
```

### **2️⃣ Run Backend API**
```bash
uvicorn app.main:app --reload
```

### **3️⃣ Run Web UI**
```bash
python frontend/web_ui.py
```

---

## **📌 Example Usage**
#### **Using API**
```bash
curl -X POST "http://localhost:8000/execute" -H "Content-Type: application/json" -d '{"text": "go to google.com and type OpenAI click search and give me the first url"}'
```

#### **Using Web UI**
- Open **`http://localhost:7860`** in the browser.
- Enter a command like:
  ```
  Go to google.com, search "OpenAI", and return the first link.
  ```
- Watch AI take control of the browser! 🎭

---

## **📊 Features**
✅ **AI-powered Browser Navigation**  
✅ **Real-time Bug Detection** (Broken links, missing elements)  
✅ **AI-Generated Test Reports** (Logs + Screenshots)  
✅ **FastAPI Backend + Gradio UI**  
✅ **Dockerized for Deployment**  

---

## **🐛 Deployment (Docker)**
```bash
docker build -t ai-browser-agent .
docker run -p 8000:8000 ai-browser-agent
```

---

## **💂️ Folder Structure**
```
💁 ai_browser_agent
🌂 app
🌂 automation          
🌂 models              
🌂 api                 
🌂 main.py                
🌂 frontend
🌂 reports
🌂 tests
🌂 docker
🌂 requirements.txt
🌂 README.md
🌂 .gitignore
🌂 start.sh
🌂 config.yaml
```

---

## **🛠️ TODO**
- [ ] Multi-browser support (Firefox, Edge)
- [ ] CI/CD pipeline for auto-deployment
- [ ] AI-generated test cases

---

## **👨‍💻 Contributors**
- **Your Name** (@yourgithub)
- Feel free to contribute! Open a PR. 💡

---

## **🐟 License**
MIT License

