import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
import os

# Load dataset
data = pd.read_csv('data/rental_1000.csv')

# Features and target variable
X = data[['rooms', 'sqft']]
y = data['price']

# Load the trained model
model_path = 'models/model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Predict the target values
y_pred = model.predict(X)

# Evaluate the model
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Save the evaluation results
eval_results = pd.DataFrame({
    'Metric': ['Mean Squared Error', 'Mean Absolute Error', 'R2 Score'],
    'Value': [mse, mae, r2]
})

eval_results_path = 'eval_results/evaluation_results.csv'
os.makedirs(os.path.dirname(eval_results_path), exist_ok=True)
eval_results.to_csv(eval_results_path, index=False)

print(f"Evaluation results saved at {eval_results_path}")
