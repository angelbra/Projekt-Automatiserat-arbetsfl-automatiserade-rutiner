
# 📊 Automatiserat Arbetsflöde för Datakvalitet i Banktransaktioner
Ett samarbetsprojekt där vi simulerar ett automatiserat datakvalitetsflöde i en svensk bankmiljö. Projektet fokuserar på datavalidering, flödesautomation, felsökning och rapportering.

---

## 📁 Projektbeskrivning
I detta projekt simulerar vi en verklighetstrogen arbetsmiljö där en bank hanterar över en miljon transaktioner per dag. Målet är att automatisera hela flödet från inläsning av CSV-filer till validering, databaslagring och generering av rapporter kring datakvalitet.

---

## ✅ Funktioner

- Automatisk inläsning av transaktionsdata (CSV)

- Validering av fält (negativa belopp, saknade värden m.m.)

- Transaktionshantering med rollback

- Databaslagring med PostgreSQL

- Automatiserat arbetsflöde med Prefect

- Rapporter kring datakvalitet

- Kodtestning med pytest

- Versionering och samarbeten via Git/GitHub

---

## 🧠 Lärandemål

- Förståelse för ETL-processer (Extract, Transform, Load)

- Praktisk tillämpning av datakvalitetsprinciper

- Arbete i grupp med SCRUM-metodik (Trello)

- Automatisering av dataprocesser med moderna verktyg

- Användning av branching och versionkontroll i Git

## 🛠 Teknikstack
 
 * Verktyg / Teknik	Syfte
 * Python	Databehandling, validering, skript
 * PostgreSQL	Databaslagring
 * Prefect	Automatisering av arbetsflöden
 * SQLAlchemy	Objekt-Relationell Mapping (ORM)
 * Alembic / Flask-Migrate	Databasmigrationer
 * Jupyter Notebook	Prototypning och testning
 * Git / GitHub	Versionshantering och samarbete
 * pytest	Automatisk testning
 * Trello	SCRUM och grupporganisation

## 🚀 Kom igång
1. Klona repot och skapa virtual environment:
   
git clone

---
https://github.com/angelbra/Projekt-Automatiserat-arbetsfl-automatiserade-rutiner.git

---

cd Projekt-Automatiserat-arbetsfl-automatiserade-rutiner

---

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

---

2. Starta databasen (PostgreSQL)
Via Docker eller lokalt – se alembic.ini för DB-inställningar.

---

4. Kör main.py

---

## 🧪 Testning
Kör testerna med:
pytest

---

## 📘 Dokumentation
Se mappen notebooks/ för Jupyter Notebooks där vi:

- Validerar data

- Visar statistik på datakvalitet

- Testar olika scenarier

---

## 👥 Gruppmedlemmar

Alaa Al-Moayed : https://github.com/alaa-najib/automated-bank-data-workflow

Marziyeh Akbari : https://github.com/Marcidata/Grupp-Arbete

Angelica Bracamonte : https://github.com/angelbra

Saher Raja : https://github.com/Sahraj12/Gruppuppgift

---

🧾 Licens
Projektet är en del av undervisningen på [TUC Yrkeshögskola – Data Manager].
