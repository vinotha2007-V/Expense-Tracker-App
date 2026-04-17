def monthly_expense(df):
    return df.groupby(df['Date'].dt.month)['Amount'].sum()
