def print_expenses_table(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    print("\nID  | DATE       | CATEGORY    | AMOUNT   | NOTE")

    for e in expenses:
        id_str = str(e["id"]).ljust(3)
        date_str = e["date"].ljust(10)
        cat_str = e["category"].ljust(11)      
        amt_str = f"{e['amount']:.2f}".rjust(8)
        note_str = e["note"][:25]

        print(f"{id_str} | {date_str} | {cat_str} | {amt_str} | {note_str}")
