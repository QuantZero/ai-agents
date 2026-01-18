def calculate_total_expenses(data):
    income = data['income']
    fixed_expenses = sum(data['fixed_expenses'].values())
    variable_expenses = sum(data['variable_expenses'].values())
    total_expenses = fixed_expenses + variable_expenses
    return {"total_expenses": total_expenses}


def generate_advice(data):
    total_expenses = data['total_expenses']
    savings_goal = data['savings_goal']
    income = data['income']
    remaining_budget = income - total_expenses - savings_goal
    advice = ""
    if remaining_budget < 0:
        advice = "Reduce variable expenses to meet your savings goal."
    else:
        advice = "You are on track to meet your savings goal. Consider increasing your savings."
    return {
        "remaining_budget": remaining_budget,
        "advice": advice
    }
