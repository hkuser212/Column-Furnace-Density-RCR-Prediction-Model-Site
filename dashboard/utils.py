import joblib
import pandas as pd

# Load model
model = joblib.load('dashboard/ml_model/multioutput_optuna_model1.pkl')  # Update path if needed
input_features= joblib.load('dashboard/ml_model/input_features1.pkl')  # Update path if needed
# Prediction function
historical_df = pd.read_csv('dashboard/ml_model/interpolated.csv')
historical_df.columns = historical_df.columns.str.strip()
historical_df['Timestamp'] = pd.to_datetime(historical_df['Timestamp'], errors='coerce')
historical_df = historical_df.dropna(subset=['Timestamp'])
historical_df.set_index('Timestamp', inplace=True)

column_map = {
    'gwa.03FI014N.pv - Average': 'Feed Flow',
    'gwa.03TIC202.pv - Average': 'Reactor Temp',
    'GWA.03TIC016.PV - Average': 'Product Temp',
    'GWA.03ti27.PV - Average': 'Pressure 27',
    'GWA.03ti10.PV - Average': 'Pressure 10',
    'GWA.03ti21.PV - Average': 'Pressure 10',
    'GWA.03ti130.PV - Average': 'Pressure 130',
    'GWA.03ti18.PV - Average': 'Pressure 18',
    'GWA.03FIC027.PV - Average': 'Flow 27',
    'GWA.03FIC025.PV - Average': 'Flow 25',
    'GWA.03FIC024.PV - Average': 'Flow 24',
    'GWA.03FIC015.PV - Average': 'Flow 15',
    'GWA.03ti623a.pv - Average': 'Pressure 623A',
    'CK (density )': 'CK Density',
    'CGO (density)': 'CGO Density',
    'CFO (density)': 'CFO Density',
    'CGO RCR': 'CGO RCR'
}

df = historical_df.rename(columns=column_map)

def get_input_features():
    return input_features

def get_default_values():
    example1 = [54.78, 365.54, 100.06, 158.99, 10.09, 13.64, 11.39, 107.61, 486.38]
    example2 = [62.31, 365.77, 100.07, 159.41, 14.1, 17.59, 12, 100.98, 487.32]
    return example1, example2

def predict_values(user_input):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    ck, cgo, cfo, rcr = prediction
    profit = 0.3 * ck + 0.3 * cgo + 0.3 * cfo + 0.1 * rcr

    # Try to match a row in historical data
    matched = df[df[input_df.columns].eq(input_df.iloc[0]).all(axis=1)]
    actual = None
    if not matched.empty:
        row = matched.iloc[0]
        actual = [row['CK Density'], row['CGO Density'], row['CFO Density'], row['CGO RCR']]
    return [ck, cgo, cfo, rcr], profit, actual
