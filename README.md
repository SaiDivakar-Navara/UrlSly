# 🔗 UrlSly – Serverless URL Shortener

UrlSly is a **fully serverless URL shortener** built using **AWS services** and a **free GitHub Pages frontend**.  
It converts long URLs into short URLs and redirects users efficiently using a scalable, cost-effective architecture.

---

## 🌐 Live Demo (Example)

- **Frontend (Create Short URL):**
[Live Demo](https://SaiDivakar-Navara.github.io/UrlSly/)

---

## 🛠️ Tech Stack

### Backend (AWS – Serverless)
- AWS Lambda (Python 3.14)
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

### Frontend
- GitHub Pages
- HTML, CSS, JavaScript

---

## 🧱 Architecture Diagram

![Home Page](https://raw.githubusercontent.com/SaiDivakar-Navara/UrlSly/refs/heads/main/assests/architecture.jpeg)
---

## 🔄 Application Workflow

### 1️⃣ Create Short URL
1. User opens the frontend hosted on GitHub Pages.
2. Enters a long URL.
3. Frontend sends a `POST /shorten` request to API Gateway.
4. `CreateShortUrl` Lambda:
   - Generates a unique short code.
   - Stores the mapping in DynamoDB.
   - Returns a GitHub Pages short URL.

---

### 2️⃣ Redirect Using Short URL
1. User opens the generated short URL.
2. GitHub Pages serves `404.html` for dynamic routes.
3. `404.html` extracts the short code and redirects to API Gateway.
4. `RedirectUrl` Lambda:
   - Fetches the original URL from DynamoDB.
   - Returns an HTTP `302` redirect.
5. Browser redirects to the original long URL.

---

## 💡 Key Design Decisions

- **Serverless Architecture:** No servers to manage, auto-scaling.
- **HTTP API:** Faster and cheaper than REST API.
- **GitHub Pages:** Completely free frontend hosting.
- **404.html Routing:** Standard SPA technique to handle dynamic routes on static hosting.
