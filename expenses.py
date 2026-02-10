def add_expense(expense_list, next_id, date, category, amount, note):
    expense={
        "id":next_id,
        "date":date,
        "category":category,
        "amount":amount,
        "note":note
    }
    
    expense_list.append(expense)
    return expense, next_id +1 



def filter_by_category(expense_list, category):
    result=[]
    for e in expense_list:
        if e["category"].lower() == category.lower():
            result.append(e)
    
    return result




def filter_by_month(expense_list, year, month):
    pattern = f"{year}-{month:02d}"
    result=[]
    for e in expense_list:
        if e["date"].startswith(pattern):
            result.append(e)
    
    return result
