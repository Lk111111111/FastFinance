import datetime

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="FastFinance", page_icon="💰")

st.title("💰 FastFinance")
st.subheader("📥 Neue Transaktion erfassen")


with st.form("eintrag_formular"):
    betrag = st.number_input("💶 Betrag (€)", min_value=0.00, step=0.01, format="%.2f")
    typ = st.selectbox("📂 Typ der Transaktion", ["einnahme", "ausgabe"])
    kategorie = st.text_input("🏷️ Kategorie", placeholder="z. B. Lebensmittel, Miete...")
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


st.subheader("📊 Alle Ein- und Ausgaben anzeigen")

if st.button("🔍 Abrufen"):
    try:
        response = requests.get("http://127.0.0.1:8000/entries")
        if response.status_code == 200:
            eintraege = response.json()
            if eintraege:
                df = pd.DataFrame(eintraege)
                df = df.sort_values(by="datum", ascending=False)
                df["datum"] = pd.to_datetime(df["datum"]).dt.date
                st.dataframe(df)
            else:
                st.info("ℹ️ Noch keine Einträge vorhanden.")
        else:
            st.error(f"❌ Fehler beim Abrufen: {response.status_code}")
    except Exception as e:
        st.error(f"🚫 Verbindungsfehler: {e}")
