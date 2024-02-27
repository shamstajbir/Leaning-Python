import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('/Users/shamstajbirtonmoy/Downloads/Salary_Data.csv')

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

model = LinearRegression()
model.fit(X_train, Y_train)

score = model.score(X_test, Y_test)
print("Model Score:", score)

plt.scatter(X_train, Y_train, color='red')
plt.plot(np.sort(X_train, axis=0), model.predict(np.sort(X_train, axis=0)), color='blue')
plt.title('Salary Vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color='red')
plt.plot(np.sort(X_test, axis=0), model.predict(np.sort(X_test, axis=0)), color='blue')
plt.title('Salary Vs Experience (Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, y_pred)
rsq = r2_score(Y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", rsq)
print('Intercept (theta 0):', model.intercept_)
print('Coefficient (theta 1):', model.coef_)

pred = model.predict([[10]])
print("Predicted salary for 10 years of experience:", pred)
