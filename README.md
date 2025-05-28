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

## 📁 Projektstruktur

```bash
.
├── alembic/               # Databas-migreringsfiler
├── data/                  # CSV-filer med transaktioner
├── notebooks/             # Jupyter Notebooks för analys och rapport
├── src/
│   ├── database.py        # DB-anslutning
│   ├── models.py          # SQLAlchemy-modeller
│   ├── import_transactions.py # Import av validerad data
│   └── workflow.py        # Prefect-arbetsflöde
├── tests/                 # pytest-tester
├── requirements.txt       # Projektberoenden
└── README.md              # Projektbeskrivning



## 💼 Automatiserat Dataflöde för Svenska Banktransaktioner
Ett samarbetsprojekt från Yrkeshögskolan där vi simulerar ett verkligt banksystem. Systemet hanterar cirka 1 miljon transaktioner per dag, med automatiserade arbetsflöden för datavalidering och hög datakvalitet genom strukturerade pipelines och felsäkringsmekanismer.

## 📚 Projektöversikt
Fallstudie:
En svensk bank tar dagligen emot stora mängder transaktionsdata i CSV-format, inklusive både inhemska och internationella överföringar. Dessa kan innehålla potentiella fel eller tecken på bedrägeri.

## Projektets mål:

✅ Automatiskt läsa in och validera CSV-filer
✅ Rensa, transformera och lagra data i en PostgreSQL-databas
✅ Hantera transaktioner med stöd för rollback
✅ Bygga ett automatiserat och återanvändbart arbetsflöde
✅ Spåra och rapportera datakvalitetsproblem

## 🛠 Teknikstack
Python – databehandling och automatisering

PostgreSQL – relationsdatabas för säker datalagring

Jupyter Notebooks – dokumentation och kodanalys

Git / GitHub – versionshantering och samarbete

Trello (SCRUM) – projektstyrning och sprintplanering

Prefect / Airflow / Cron – arbetsflödesautomation

Alembic / Flask-Migrate – databas-migreringar

pytest – automatiserade tester

## 🚀 Kom igång
1. Sätt upp projektmiljön

git clone https://github.com/WeeHorse/python-bank.git
cd python-bank
git checkout projekt_start

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
Starta PostgreSQL (antingen lokalt eller med Docker) och se till att din DATABASE_URL är korrekt inställd i .env eller i alembic.ini.

## 📌 Syfte
Läsa in stora transaktionsvolymer (CSV-format)

Validera och filtrera ogiltig data

Spara korrekt data i en PostgreSQL-databas

Automatisera hela processen med Prefect

Säkerställa datakvalitet och generera rapporter

Korrekt data laddas till databasen

Rapportering sker automatiskt i slutet av varje körning

## 👥 Projektteam
Detta projekt genomfördes av studenter vid TUC Yrkeshögskola i kursen Datakvalitet och Databashantering, som en del av Data Manager-programmet.
