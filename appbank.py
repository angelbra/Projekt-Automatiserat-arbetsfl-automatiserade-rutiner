import streamlit as st
import pandas as pd
import sqlite3
import os

st.title("Bankdata Rapport")

# Hitta sökvägen till den aktuella mappen där appen körs
BASE_DIR = os.path.dirname(__file__)

# Skapa sökvägar till CSV och databasfiler
CUSTOMERS_CSV = os.path.join(BASE_DIR, "sebank_customers_with_accounts.csv")
TRANSACTIONS_CSV = os.path.join(BASE_DIR, "transactions.csv")
DATABASE = os.path.join(BASE_DIR, "bank_data.db")

# Visa kunder från CSV
st.header("Kunddata")
try:
    df_customers = pd.read_csv(CUSTOMERS_CSV)
    st.dataframe(df_customers.head(10))
except Exception as e:
    st.error(f"Kunde inte läsa kunddata: {e}")

# Visa transaktioner från CSV
st.header("Transaktionsdata")
try:
    df_transactions = pd.read_csv(TRANSACTIONS_CSV)
    st.dataframe(df_transactions.head(10))
except Exception as e:
    st.error(f"Kunde inte läsa transaktionsdata: {e}")

# Visa summering från SQLite-databasen
st.header("Sammanfattning från databasen")
try:
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Antal kunder
    c.execute("SELECT COUNT(*) FROM customers")
    antal_kunder = c.fetchone()[0]

    # Antal transaktioner
    c.execute("SELECT COUNT(*) FROM transactions")
    antal_transaktioner = c.fetchone()[0]

    st.write(f"🧍 Totalt antal kunder i databasen: **{antal_kunder}**")
    st.write(f"💳 Totalt antal transaktioner i databasen: **{antal_transaktioner}**")

    conn.close()
except Exception as e:
    st.error(f"Kunde inte ansluta till databasen: {e}")
