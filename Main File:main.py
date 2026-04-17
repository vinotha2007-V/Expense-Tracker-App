from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import monthly_expense
from src.model import train_model
from src.visualization import plot_expense

df = load_data("data/raw/expenses.csv")
df = preprocess(df)

trend = monthly_expense(df)
plot_expense(trend)

model = train_model(df)
print("Model trained successfully")
