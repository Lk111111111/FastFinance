# FastFinance – Dein persönlicher Einnahmen- und Ausgaben-Tracker

FastFinance ist ein minimalistisches Tool zur Verwaltung und Analyse deiner persönlichen Finanzen.  
Du kannst Einnahmen und Ausgaben manuell eintragen, nach Kategorien filtern, und dir einfache Auswertungen anzeigen lassen – alles über eine moderne Oberfläche (Streamlit) und ein API-Backend (FastAPI).

---

## 🚀 Features

- ✅ Einfache Eingabemaske für Einnahmen & Ausgaben
- ✅ Kategorien wie "Lebensmittel", "Miete", "Fast-Food" etc.
- ✅ Speicherung in SQLite-Datenbank
- ✅ Übersicht über vergangene Einträge
- ✅ Summen und Filterfunktionen (z. B. nach Monat oder Typ)
- ✅ Moderne Backend-API mit FastAPI
- ✅ Frontend mit Streamlit

---

## Frontend Aktuell

<video controls src="streamlit-app-2025-07-25-21-07-41.webm" title="A small demonstration video"</video>

---

## 🧱 Tech Stack

| Komponente    | Beschreibung                   |
| ------------- | ------------------------------ |
| 🐍 Python     | Hauptsprache                   |
| 📦 FastAPI    | REST-API Backend               |
| 📊 Streamlit  | Benutzeroberfläche (Frontend)  |
| 🛢️ SQLite     | Lokale Datenbank               |
| 🧠 SQLAlchemy | ORM zur DB-Anbindung           |
| 🔌 Requests   | Kommunikation Frontend <-> API |

---

## ⚙️ Projektstruktur

```plaintext
fastfinance/
├── backend/
│   ├── main.py            # FastAPI App
│   ├── models.py          # SQLAlchemy DB-Modell
│   ├── crud.py            # Create, Read, Update, Delete Funktionen
│   └── database.py        # DB-Verbindung & Initialisierung
│
├── frontend/
│   └── app.py             # Streamlit Interface
│
├─
```
