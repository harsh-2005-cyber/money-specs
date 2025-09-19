import pandas as pd
from datetime import datetime, timedelta
from database import get_total_spent, get_budget, get_expenses
from categorization import CATEGORY_KEYWORDS

def check_budget_alerts():
    """Check if any category is nearing or exceeding budget."""
    alerts = []
    current_month = datetime.now().month
    current_year = datetime.now().year
    for category in CATEGORY_KEYWORDS.keys():
        spent = get_total_spent(category=category, month=current_month, year=current_year)
        budget = get_budget(category)
        if budget > 0:
            percentage = (spent / budget) * 100
            if percentage >= 90:
                alerts.append(f"Warning: {category} spending is at {percentage:.1f}% of budget (${spent:.2f}/${budget:.2f})")
            elif percentage >= 100:
                alerts.append(f"Alert: {category} budget exceeded! Spent ${spent:.2f} of ${budget:.2f}")
    return alerts

def split_bill(total_amount, num_people, payer_name="You"):
    """Split a bill among friends."""
    split_amount = total_amount / num_people
    return {f"Person {i+1}": split_amount for i in range(num_people)}

def generate_ai_insights():
    """Generate simple AI insights based on spending patterns."""
    insights = []
 
    today = datetime.now()
    this_week_start = today - timedelta(days=today.weekday())
    last_week_start = this_week_start - timedelta(days=7)
    last_week_end = this_week_start - timedelta(days=1)

    this_week_expenses = get_expenses(start_date=this_week_start.strftime('%Y-%m-%d'), end_date=today.strftime('%Y-%m-%d'))
    last_week_expenses = get_expenses(start_date=last_week_start.strftime('%Y-%m-%d'), end_date=last_week_end.strftime('%Y-%m-%d'))


    if this_week_expenses is None or last_week_expenses is None:
        return ["No expense data available for insights."]

    for df in [this_week_expenses, last_week_expenses]:
        if 'date' in df.columns:
            try:
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            except Exception:
                pass


    if 'amount' not in this_week_expenses.columns or 'amount' not in last_week_expenses.columns:
        return ["Expense data missing 'amount' column. Cannot generate insights."]

    this_week_total = this_week_expenses['amount'].sum() if not this_week_expenses.empty else 0
    last_week_total = last_week_expenses['amount'].sum() if not last_week_expenses.empty else 0

    if last_week_total > 0:
        change = ((this_week_total - last_week_total) / last_week_total) * 100
        if change > 0:
            insights.append(f"You spent {change:.1f}% more this week (${this_week_total:.2f}) compared to last week (${last_week_total:.2f}).")
        else:
            insights.append(f"You spent {abs(change):.1f}% less this week (${this_week_total:.2f}) compared to last week (${last_week_total:.2f}).")
    elif this_week_total > 0:
        insights.append(f"You spent ${this_week_total:.2f} this week. No data for last week to compare.")
    else:
        insights.append("No expenses recorded for this week or last week.")


    if 'category' in this_week_expenses.columns and not this_week_expenses.empty:
        category_totals = this_week_expenses.groupby('category')['amount'].sum()
        if not category_totals.empty:
            top_category = category_totals.idxmax()
            top_amount = category_totals.max()
            insights.append(f"Your top spending category this week is {top_category} with ${top_amount:.2f}.")
    else:
        insights.append("No category data available for this week's expenses.")

    return insights

def filter_expenses(expenses_df, category=None, start_date=None, end_date=None, min_amount=None, max_amount=None):
    """Filter expenses based on criteria."""
    filtered = expenses_df.copy()
    if category:
        filtered = filtered[filtered['category'] == category]
    if start_date:
        filtered = filtered[filtered['date'] >= start_date]
    if end_date:
        filtered = filtered[filtered['date'] <= end_date]
    if min_amount is not None:
        filtered = filtered[filtered['amount'] >= min_amount]
    if max_amount is not None:
        filtered = filtered[filtered['amount'] <= max_amount]
    return filtered

def export_to_csv(expenses_df, filename):
    """Export filtered expenses to CSV."""
    expenses_df.to_csv(filename, index=False)
    return filename

