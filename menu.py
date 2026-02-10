import expenses
import reports
import formatting
import validation

def run(expense_list,next_id):
    while True:
        print("\n     EXPENSE TRACKER     ")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Search by category")
        print("4. Monthly summary")
        print("5. Analytics summary")
        print("6. Exit and save")

        choice=input("enter choice (1-6): ").strip()

        if choice == "1":
            next_id = add_expense_option(expense_list, next_id)
        elif choice == "2":
            formatting.print_expenses_table(expense_list)
        elif choice == "3":
            category_option(expense_list)
        elif choice == "4":
            summary_option(expense_list)
        elif choice == "5":
            analytics_option(expense_list)
        elif choice == "6":
            return expense_list, next_id
        else:
            print("invalid input.try again")

def add_expense_option(expense_list,next_id):
    print("\n    ADD EXPENSE    ")
    date=validation.get_valid_date("Enter date (YYYY-MM-DD): ")
    category=input("Enter category: ").strip()
    amount=validation.get_valid_amount("Enter amount: ")
    note=input("Enter note: ").strip()

    new_expense, next_id=expenses.add_expense(
        expense_list, next_id, date, category, amount, note
    )
    import storage
    storage.save_expense(new_expense)
    
    print("Added with ID:",new_expense["id"])
    return next_id

def category_option(expense_list):
    print("\n    SEARCH BY CATEGORY    ")
    category=input("Enter category: ").strip()
    filtered=expenses.filter_by_category(expense_list, category)
    if filtered:
        formatting.print_expenses_table(filtered)
    else:
        print("No expenses found for category:",category)

def summary_option(expense_list):
    print("\n    MONTHLY SUMMARY    ")

    year=validation.get_valid_year("Enter year: ")
    month=validation.get_valid_month("Enter month: ")
    monthly=expenses.filter_by_month(expense_list, year, month)

    if not monthly:
        print("No data for that month.")
        return
    
    total=reports.total_spent(monthly)
    print(f"Total spent in {year}-{month:02d}: {total:.2f}")
    print("\n By category:")

    cat_summary=reports.category_summary(monthly)
    reports.print_category_summary(cat_summary)

    top_cat=reports.highest_category(cat_summary)
    if top_cat is not None:
        print("Highest spending category:", top_cat)

def analytics_option(expense_list):
    print("\n    ANALYTICAL SUMMARY    ")
    if not expense_list:
        print("No data available.")
        return
    
    total=reports.total_spent(expense_list)
    print(f"Total spent: {total:.2f}")

    print("\n By category:")
    cat_summary=reports.category_summary(expense_list)
    reports.print_category_summary(cat_summary)

    top_cat=reports.highest_category(cat_summary)
    if top_cat is not None:
        print("Highest category:",top_cat)
 