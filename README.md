# Smart Expense Manager

A Streamlit-based web application to help users track, categorize, and analyze personal expenses efficiently. Built for the Moneyspecs hackathon, this project demonstrates practical use of data science, machine learning, and web development for real-world financial management.

## Features
- **Intelligent Expense Tracking:** Add expenses with auto-categorization (keyword + ML-based) or manual selection.
- **Comprehensive Management:** View, filter, and manage all expenses. Real-time total calculations.
- **Data Visualization:** Interactive pie charts and monthly trend lines for spending insights.
- **Budget Management & Alerts:** Set monthly budgets and receive automatic warnings at 90% and 100% usage.
- **Bill Splitting Utility:** Easily split group expenses.
- **AI-Powered Insights:** Weekly spending comparisons and top category identification.
- **Data Export:** Export filtered expenses to CSV.

## Technologies Used
- Python, Streamlit, SQLite, Pandas, Matplotlib, Seaborn
- Scikit-learn (Naive Bayes classifier), TF-IDF Vectorization

## Project Structure
- `main.py` - Streamlit UI and app entry point
- `database.py` - SQLite database operations
- `categorization.py` - Expense categorization logic (keyword & ML)
- `visualization.py` - Chart and graph generation
- `utils.py` - Helper functions (alerts, bill split, AI insights, etc.)

## Getting Started
1. **Install dependencies:**
   ```sh
   pip install streamlit pandas matplotlib seaborn scikit-learn
   ```
2. **Run the app:**
   ```sh
   streamlit run "smart expence calculator/main.py"
   ```
3. **Open the local URL** provided by Streamlit in your browser.
4. **Add sample data** using the sidebar button for demo/testing.

## Usage
- Use the sidebar to navigate between features: Add Expense, View Expenses, Visualizations, Budget & Alerts, Bill Splitter, AI Insights, Export.
- Add expenses with date, amount, description, and category. Use "auto" for automatic categorization.
- Set budgets and receive alerts as you approach/exceed limits.
- View AI-powered insights for weekly spending trends and top categories.
- Export your data for backup or further analysis.

## Future Enhancements
- Advanced ML models for prediction
- Multi-currency and recurring expense support
- Mobile app and cloud sync
- Bank integration for automatic imports

## License
This project is for educational and demonstration purposes.
