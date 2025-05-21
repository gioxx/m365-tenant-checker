# 🧠 Microsoft 365 Tenant Checker

This file is [also available in italian](README-IT.md).

> Quickly and easily verify whether a domain is associated with a Microsoft 365 tenant (Exchange Online, Teams, etc.).

![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)
![Render](https://img.shields.io/badge/Hosted%20on-Render.com-blueviolet?logo=render)
![MIT License](https://img.shields.io/github/license/gioxx/m365-tenant-checker)

---

## 🚀 Live Demo

Try it now:

👉 **[https://m365-tenant-checker.onrender.com](https://m365-tenant-checker.onrender.com)**

---

## ⚙️ Features

- 🔎 Check if a domain is registered with Microsoft 365
- 📤 Exposes a simple API endpoint (`/check?domain=...`)
- 🌐 Integrated static HTML interface
- 🐳 Public Docker container available
- ☁️ Deployable on Render.com (free tier)

---

## 🧪 API Usage

### Endpoint

```
GET /check?domain=example.com
```

### Example response

```json
{
  "domain": "example.com",
  "status": 200,
  "found": true,
  "message": "Domain is associated with Microsoft 365. Redirect URL: https://outlook.office365.com/autodiscover/autodiscover.xml"
}
```

---

## 📦 Docker

### Pull the image

```bash
docker pull ghcr.io/gioxx/m365-tenant-checker:latest
```

### Run locally

```bash
docker run -p 5000:5000 ghcr.io/gioxx/m365-tenant-checker:latest
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🧰 Alternative Deployment: Render.com

1. Create an account at [https://render.com](https://render.com)
2. Click **New → Web Service**
3. Connect this GitHub repo
4. Set:

   | Field            | Value                            |
   |------------------|----------------------------------|
   | Build Command     | *(leave empty)*                |
   | Start Command     | `gunicorn backend.app:app`      |
   | Runtime           | Python 3                        |
   | Instance Type     | Free                            |

5. Click **Deploy**

---

## 📁 Project Structure

```
m365-tenant-checker/
├── backend/
│   ├── app.py              ← Flask app (API + serves HTML)
│   └── requirements.txt
├── frontend/
│   └── index.html          ← Web interface
├── Dockerfile              ← For Docker packaging
├── Procfile                ← For Render deployment
```

---

## 📝 License

Distributed under the MIT License — see `LICENSE`.

---

## 👤 Author

- 👨‍💻 [Giovanni "Gioxx" Solone](https://github.com/gioxx)
- 📫 Visit [gioxx.org](https://gioxx.org) or GitHub
