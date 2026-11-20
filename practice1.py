from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("k =", model.coef_[0])
print("b =", model.intercept_)

import matplotlib.pyplot as plt

y_pred = model.predict(X_test)

plt.figure(figsize=(8, 6))

plt.scatter(X_test, y_test, color="tab:blue", label="Фактические данные")
plt.plot(X_test, y_pred, color="tab:orange", linewidth=2, label="Прогноз модели")

plt.xlabel("Признак X")
plt.ylabel("Целевая переменная y")
plt.title("Линейная регрессия: прогноз vs факт")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("regression_plot.png", dpi=150)
plt.show()