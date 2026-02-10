import storage
import menu

def main():
    storage.start_db() #initialize db

    expenses,next_id=storage.load_expenses() #load existing data in db
    expenses,next_id=menu.run(
        expense_list=expenses,
        next_id=next_id
    )

    print("end")

if __name__ == "__main__":
    main()
