from db import init_db
from first_data_insertio import insert_initial_data
from bank_workflow_prefect import bank_workflow

def main():
    print("starting....")
    init_db()

    print("Insert data...")
    insert_initial_data()

    print("workflow on...")
    bank_workflow()


    print(" Done with no issues✅")

if __name__ == "__main__":
    main()
