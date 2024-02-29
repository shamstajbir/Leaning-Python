import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


for dirname, _, filenames in os.walk('/Salary/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


data = pd.read_csv("/Users/shamstajbirtonmoy/Downloads/exp ml 4/Salary_Data.csv")

X = data.iloc[:, :-1]
Y = data.iloc[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

linear_model = LinearRegression()
linear_model.fit(X_train, Y_train)

score = linear_model.score(X_test, Y_test)
print("Linear Regression Model Score:", score)

plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, linear_model.predict(X_train), color='blue')
plt.title('Salary Vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color='red')
plt.plot(X_test, linear_model.predict(X_test), color='blue')
plt.title('Salary Vs Experience (Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary of employee')
plt.show()

y_pred = linear_model.predict(X_test)
mse = mean_squared_error(Y_test, y_pred)
rsq = r2_score(Y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", rsq)
print('Intercept (theta 0):', linear_model.intercept_)
print('Coefficient (theta 1):', linear_model.coef_)

pred = linear_model.predict([[10]])
print("Predicted salary for 10 years of experience:", pred)


threshold = 50000
data['Salary_binary'] = (data['Salary'] > threshold).astype(int)
X_logistic = data.iloc[:, :-2]
Y_logistic = data['Salary_binary']

X_train_logistic, X_test_logistic, Y_train_logistic, Y_test_logistic = train_test_split(X_logistic, Y_logistic, test_size=0.2, random_state=10)

logistic_model = LogisticRegression()
logistic_model.fit(X_train_logistic, Y_train_logistic)

Y_pred_logistic = logistic_model.predict(X_test_logistic)

accuracy_logistic = accuracy_score(Y_test_logistic, Y_pred_logistic)
print("Logistic Regression Accuracy:", accuracy_logistic)

print("Logistic Regression Classification Report:")
print(classification_report(Y_test_logistic, Y_pred_logistic))

print("Logistic Regression Confusion Matrix:")
print(confusion_matrix(Y_test_logistic, Y_pred_logistic))