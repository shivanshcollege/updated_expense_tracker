def total_spent(expense_list):
    total=0
    for e in expense_list:
        total=total+e["amount"]
    return total

def category_summary(expense_list):
    summary={}
    for e in expense_list:
        cat=e["category"]
        amt=e["amount"]

        if cat in summary:
            summary[cat]=summary[cat]+amt
        else:
            summary[cat]=amt

    return summary

def highest_category(summary):
    if summary == {}:
        return None
    
    max_cat=None
    max_val=0

    for cat, amt in summary.items():
        if amt>max_val:
            max_val=amt
            max_cat=cat

    return max_cat

def print_category_summary(summary):
    if summary == {}:
        print("no category data.")
        return
    
    for cat, amt in summary.items():
        print("-",cat,":",format(amt,".2f")) 