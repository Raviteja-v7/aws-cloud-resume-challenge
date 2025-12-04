# 🌩️ AWS Cloud Resume Challenge

This repository contains my implementation of the **Cloud Resume Challenge** — a full-stack cloud project designed to showcase AWS, DevOps, and Web development skills.

---

## ✨ Features

✔ Cloud-hosted resume website  
✔ **Live visitor counter** displayed on the page  
✔ Visitor count stored in DynamoDB  
✔ Serverless backend using AWS Lambda  
✔ API Gateway endpoint consumed from frontend  
✔ Infrastructure managed using AWS SAM

---

## 🛠️ Tech Stack

### Frontend
- HTML (CSS/JS coming soon)

### Backend (Serverless)
- AWS Lambda (Python)
- AWS API Gateway
- AWS DynamoDB
- AWS SAM (Serverless Application Model)

---

## 📂 Project Structure
AWS Cloud Resume Challenge/
├── Index.html                     # Frontend Resume Website
└── cloud-resume-backend/
├── template.yaml              # SAM Infrastructure Template
├── visitor_function/          # Lambda code for Visitor Counter
│   └── app.py
├── hello_world/               # Sample Lambda (optional)
├── events/

---

## 🚀 How it Works

1️⃣ Resume page loads  
2️⃣ JavaScript triggers an API request to API Gateway  
3️⃣ Lambda function runs and increments the count  
4️⃣ Count stored + retrieved from DynamoDB  
5️⃣ Frontend updates with new count dynamically

---

## 🔜 Upcoming Enhancements

- Modern UI styling with CSS
- Deployment of frontend to **Amazon S3 + CloudFront**
- Automated CI/CD pipelines
- Custom domain + HTTPS using Route 53 & ACM
- Add badges, screenshots & architecture diagram

---

## 📌 Challenge Reference

This project follows the popular **Cloud Resume Challenge** by Forrest Brazeal.

---

### 👀 Stay tuned — more cloud magic coming soon! ⚡
