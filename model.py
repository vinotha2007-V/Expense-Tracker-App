from sklearn.linear_model import LinearRegression

def train_model(df):
    df['Month'] = df['Date'].dt.month
    X = df[['Month']]
    y = df['Amount']

    model = LinearRegression()
    model.fit(X, y)
    return model
