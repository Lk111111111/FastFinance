import datetime
from urllib import request

import pandas as pd
import requests
import streamlit as st
from sqlalchemy import false

st.set_page_config(page_title="FastFinance", page_icon="💰")

st.title("FastFinance")
st.subheader("Neue Transaktion erfassen")


with st.form("eintrag_formular"):
    betrag = st.number_input("💶 Betrag (€)", min_value=0.00, step=0.01, format="%.2f")
    typ = st.selectbox("📂 Typ der Transaktion", ["einnahme", "ausgabe"])
    kategorie = st.selectbox(
        "🏷️ Kategorie",
        [
            "Lebensmittel",
            "Transport",
            "Fast Food",
            "Gehalt",
            "Freizeit",
            "Monatliche Fixkosten",
        ],
    )
    beschreibung = st.text_input(
        "📝 Beschreibung", placeholder="Optional: z. B. Pizza bei XY"
    )
    datum = st.date_input("📅 Datum", value=datetime.date.today())

    submitted = st.form_submit_button("💾 Eintrag speichern")
    if submitted:
        payload = {
            "betrag": betrag,
            "typ": typ,
            "kategorie": kategorie,
            "beschreibung": beschreibung,
            "datum": str(datum),
        }

        try:
            response = requests.post("http://127.0.0.1:8000/entries", json=payload)
            if response.status_code == 200:
                st.success("✅ Eintrag erfolgreich gespeichert!")
            else:
                st.error(f"❌ Fehler: {response.status_code} – {response.text}")
        except Exception as e:
            st.error(f"🚫 Verbindungsfehler: {e}")


st.markdown("---")


st.subheader("Alle Ein- und Ausgaben anzeigen")

# 🔍 Einträge abrufen
if st.button("🔍 Einträge anzeigen"):
    try:
        response = requests.get("http://127.0.0.1:8000/entries")
        if response.status_code == 200:
            eintraege = response.json()
            if eintraege:
                df = pd.DataFrame(eintraege)
                df["datum"] = pd.to_datetime(df["datum"]).dt.date
                df = df.set_index("id")
                df = df.sort_index(ascending=True)
                st.dataframe(df)
            else:
                st.info("ℹ️ Noch keine Einträge vorhanden.")
        else:
            st.error(f"❌ Fehler beim Abrufen: {response.status_code}")
    except Exception as e:
        st.error(f"🚫 Verbindungsfehler: {e}")

# 🗑️ Eintrag löschen
st.markdown("---")
st.subheader("Eintrag löschen")

id_to_delete = st.number_input("ID zum Löschen eingeben:", min_value=1, step=1)


if st.button("Löschen"):
    try:
        response = requests.get("http://127.0.0.1:8000/entries")
        if not response.json():
            st.error("❌ Keine Einträge mehr in der Tabelle.")
        else:
            response = requests.delete(f"http://127.0.0.1:8000/entries/{id_to_delete}")
            if response.status_code == 200:
                st.success(f"✅ Eintrag {id_to_delete} wurde gelöscht.")
            else:
                st.error(f"❌ Fehler beim Löschen: {response.status_code}")
    except Exception as e:
        st.error(f"🚫 Verbindungsfehler beim Löschen: {e}")

st.markdown("---")
st.subheader("Einzelnen Eintrag finden")

id_to_find = st.number_input(
    "ID zum Finden eines Eintrags eingeben", min_value=1, step=1
)

if st.button("Eintrag anzeigen"):
    try:
        response = requests.get(f"http://127.0.0.1:8000/entries/{id_to_find}")
        if response.status_code == 200:
            eintrag = response.json()
            st.dataframe(pd.DataFrame([eintrag]))
        elif response.status_code == 404:
            st.warning("❗ Kein Eintrag mit dieser ID gefunden.")
        else:
            st.error(f"Fehler: {response.status_code}")
    except Exception as e:
        st.error(f"Verbindungsfehler: {e}")

st.subheader("🔄 Einzelnen Eintrag aktualisieren")


id_to_find = st.number_input("ID des Eintrags", min_value=1, step=1)


if "eintrag_laden" not in st.session_state:
    st.session_state.eintrag_laden = False

# Button-Handler
if st.button("Eintrag laden"):
    try:
        response = requests.get(f"http://127.0.0.1:8000/entries/{id_to_find}")
        if response.status_code == 200:
            st.session_state.eintrag = response.json()
            st.session_state.eintrag_laden = True  # Trigger zum Rendern
        elif response.status_code == 404:
            st.warning("Eintrag nicht gefunden.")
        else:
            st.error(f"Fehler: {response.status_code}")
    except Exception as e:
        st.error(f"Verbindungsfehler: {e}")


if st.session_state.get("eintrag_laden"):
    eintrag = st.session_state.eintrag

    new_betrag = st.number_input("Neuer Betrag", value=eintrag["betrag"], step=0.01)
    new_typ = st.selectbox(
        "Neuer Typ",
        ["einnahme", "ausgabe"],
        index=["einnahme", "ausgabe"].index(eintrag["typ"]),
    )
    new_kategorie = st.text_input("Neue Kategorie", value=eintrag["kategorie"])
    new_beschreibung = st.text_input("Neue Beschreibung", value=eintrag["beschreibung"])
    new_datum = st.date_input(
        "Neues Datum", value=datetime.date.fromisoformat(eintrag["datum"])
    )

    if st.button("Eintrag aktualisieren"):
        payload = {
            "betrag": new_betrag,
            "typ": new_typ,
            "kategorie": new_kategorie,
            "beschreibung": new_beschreibung,
            "datum": str(new_datum),
        }
        try:
            update_response = requests.put(
                f"http://127.0.0.1:8000/entries/{id_to_find}",
                json=payload,
            )
            if update_response.status_code == 200:
                st.success("✅ Eintrag aktualisiert.")
                del st.session_state.eintrag
            else:
                st.error(f"Fehler: {update_response.status_code}")
        except Exception as e:
            st.error(f"Verbindungsfehler: {e}")
