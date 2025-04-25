from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Iris ma'lumotlar to'plamini yuklash
data = load_iris()
X = data.data
y = data.target

# Ma'lumotlarni ta'lim va test to'plamlariga ajratish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model yaratish
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test to'plamida modelni baholash
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Modelning aniqligi:", accuracy)
