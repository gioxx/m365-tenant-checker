# 🤖 Microsoft 365 Tenant Checker

This file is [also available in italian](README-IT.md).

> Quickly and easily verify whether a domain is associated with a Microsoft 365 tenant (Exchange Online, Teams, etc.).

[![](https://img.shields.io/badge/Hosted%20on-Render.com-blueviolet?logo=render)](https://m365-tenant-checker.onrender.com/)
[![](https://img.shields.io/github/issues/gioxx/m365-tenant-checker.svg)](https://github.com/gioxx/m365-tenant-checker/issues)
[![](https://img.shields.io/github/issues-pr-raw/gioxx/m365-tenant-checker.svg)](https://github.com/gioxx/m365-tenant-checker/pulls)
[![MIT License](https://img.shields.io/github/license/gioxx/m365-tenant-checker)](https://github.com/gioxx/m365-tenant-checker/blob/main/LICENSE)
[![](https://img.shields.io/badge/GHCR-available-blue?logo=docker)](https://github.com/users/gioxx/packages/container/package/m365-tenant-checker)
[![](https://img.shields.io/docker/pulls/gfsolone/m365-tenant-checker.svg)](https://hub.docker.com/r/gfsolone/m365-tenant-checker)
[![](https://img.shields.io/docker/image-size/gfsolone/m365-tenant-checker/latest.svg)](https://hub.docker.com/r/gfsolone/m365-tenant-checker)

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
The [emoji graphics](https://github.com/twitter/twemoji/blob/master/assets/svg/1f9e0.svg), used as a favicon in the webpage, are from the open source project [Twemoji](https://twemoji.twitter.com/). The graphics are copyright 2020 Twitter, Inc and other contributors. The graphics are licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
