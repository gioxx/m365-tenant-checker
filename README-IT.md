# 🤖 Microsoft 365 Tenant Checker

Questo file è [disponibile anche in inglese](README.md).

> Verifica in modo semplice e automatico se un dominio è associato a un tenant Microsoft 365 (Exchange Online, Teams, ecc).

![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)
![Render](https://img.shields.io/badge/Hosted%20on-Render.com-blueviolet?logo=render)
![MIT License](https://img.shields.io/github/license/gioxx/m365-tenant-checker)

---

## 🚀 Demo pubblica

Puoi provare subito la versione online all’indirizzo:

👉 **[https://m365-tenant-checker.onrender.com](https://m365-tenant-checker.onrender.com)**

---

## ⚙️ Funzionalità

- 🔎 Verifica se un dominio è registrato su Microsoft 365
- 📤 Espone un endpoint API semplice (`/check?domain=...`)
- 🌐 Interfaccia web minimale (HTML statico) integrata
- 🐳 Distribuito come container Docker pubblico
- ☁️ Eseguibile anche su Render.com (free tier)

---

## 🧪 API Usage

### Endpoint

```
GET /check?domain=example.com
```

### Esempio di risposta

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

### Pull dell'immagine

```bash
docker pull ghcr.io/gioxx/m365-tenant-checker:latest
```

### Avvio locale

```bash
docker run -p 5000:5000 ghcr.io/gioxx/m365-tenant-checker:latest
```

Apri il browser su: [http://localhost:5000](http://localhost:5000)

---

## 🧰 Deployment alternativo: Render.com

1. Crea un account su [https://render.com](https://render.com)
2. Clicca su **New → Web Service**
3. Collega questo repo
4. Imposta:

   | Campo            | Valore                            |
   |------------------|------------------------------------|
   | Build Command     | *(lascia vuoto)*                  |
   | Start Command     | `gunicorn backend.app:app`        |
   | Runtime           | Python 3                          |
   | Instance Type     | Free                              |

5. Click su **Deploy**

---

## 📁 Struttura del progetto

```
m365-tenant-checker/
├── backend/
│   ├── app.py              ← App Flask (API + serve HTML)
│   └── requirements.txt
├── frontend/
│   └── index.html          ← Interfaccia web
├── Dockerfile              ← Per containerizzare
├── Procfile                ← Per Render.com
```

---

## 📝 Licenza

Distribuito sotto licenza MIT — vedi `LICENSE`.  
Le [emoji grafiche](https://github.com/twitter/twemoji/blob/master/assets/svg/1f9e0.svg), utilizzate come favicon nella pagina web, provengono dal progetto open source [Twemoji](https://twemoji.twitter.com/). La grafica è coperta da copyright 2020 di Twitter, Inc. e di altri collaboratori. La grafica è rilasciata sotto licenza [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
