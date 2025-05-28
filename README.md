# 💼 Automatiserat arbetsflöde för datakvalitet i en svensk bank

Detta projekt simulerar ett verkligt bankscenario där cirka **1 miljon transaktioner per dag** behandlas. Syftet är att utveckla ett **automatiserat arbetsflöde** som säkerställer **hög datakvalitet** genom validering, migrering och rapportering. Projektet är en del av Data Manager-utbildningen vid TUC Yrkeshögskola.

## 🧠 Syfte

Att skapa ett arbetsflöde som:
- Läser och validerar stora mängder transaktionsdata (CSV)
- Rensar och laddar data till en databas (PostgreSQL)
- Automatiserar processen via ett workflow-verktyg (Prefect)
- Säkerställer spårbarhet och rollback vid fel
- Genererar rapporter om datakvalitet

## 🛠️ Teknisk översikt

- **Python** – Databehandling och validering
- **PostgreSQL** – Lagring av transaktionsdata
- **SQLAlchemy + Alembic** – Databasmodellering och migrering
- **Prefect** – Workflow-automatisering
- **Jupyter Notebooks** – Dokumentation och analys
- **pytest** – Testning
- **GitHub / Git** – Versionshantering
- **SCRUM / Trello** – Projektstyrning

## 🚀 Kom igång
1. Sätt upp projektmiljön

git clone https://github.com/WeeHorse/python-bank.git
cd python-bank
git checkout projekt_start

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
Starta PostgreSQL (antingen lokalt eller med Docker) och se till att din DATABASE_URL är korrekt inställd i .env eller i alembic.ini.

## 👥 Projektteam
Detta projekt genomfördes av studenter vid TUC Yrkeshögskola i kursen Datakvalitet och Databashantering, som en del av Data Manager-programmet.

📄 Licens
MIT License. Endast för utbildningssyfte.

