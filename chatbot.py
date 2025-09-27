import pandas as pd
import re
from database import get_expenses

def get_expense_summary():
    expenses_df = get_expenses()
    if expenses_df.empty:
        return "No expenses recorded yet."

    total_expenses = expenses_df['amount'].sum()
    category_totals = expenses_df.groupby('category')['amount'].sum().to_dict()
    recent_expenses = expenses_df.sort_values('date', ascending=False).head(5).to_string(index=False)

    summary = f"""
    Total Expenses: ₹{total_expenses:.2f}
    Expenses by Category: {category_totals}
    Recent Expenses:
    {recent_expenses}
    """
    return summary, total_expenses, category_totals

def chat_with_ai(user_message, api_key=None):
    summary, total_expenses, category_totals = get_expense_summary()
    
    user_lower = user_message.lower()
    
    if "total" in user_lower or "spending" in user_lower or "expenses" in user_lower:
        return f"Based on your data: {summary}. Keep tracking to stay on budget!"
    
    elif "category" in user_lower or "breakdown" in user_lower:
        cat_str = ", ".join([f"{cat}: ₹{amt:.2f}" for cat, amt in category_totals.items()])
        return f"Your spending by category: {cat_str}. Consider reviewing the highest category for savings."
    
    elif "advice" in user_lower or "tip" in user_lower:
        if total_expenses > 500:
            return "Your total spending is high. Tip: Set a monthly budget and prioritize essentials like groceries and bills."
        else:
            return "Great job keeping expenses low! Continue monitoring categories like entertainment for potential savings."
    
    elif "recent" in user_lower or "last" in user_lower:
        recent = "\n".join(recent_expenses.split('\n')[:5])
        return f"Your recent expenses:\n{recent}"
    
    elif "save" in user_lower or "reduce" in user_lower:
        top_cat = max(category_totals, key=category_totals.get)
        return f"To save money, focus on reducing spending in your top category: {top_cat} (₹{category_totals[top_cat]:.2f}). Track daily habits!"
    
    else:
        return f"Hi! I can help with your expenses summary, categories, recent spends, or saving tips. Your total is ₹{total_expenses:.2f}. Ask something like 'What's my total spending?'"

