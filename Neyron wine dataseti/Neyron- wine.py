import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine  # <-- o'zgartirildi
from sklearn.preprocessing import StandardScaler

# Загрузим датасет Wine (o'zgartirildi)
wine = load_wine()
X = wine.data
y = wine.target

# Стандартизируем данные
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделим данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Преобразуем данные в тензоры PyTorch
X_train_tensor = torch.FloatTensor(X_train)
X_test_tensor = torch.FloatTensor(X_test)
y_train_tensor = torch.LongTensor(y_train)
y_test_tensor = torch.LongTensor(y_test)

# Определение нейронной сети
class WineClassifier(nn.Module):  # <-- nomi o'zgartirildi
    def __init__(self):
        super(WineClassifier, self).__init__()
        self.fc1 = nn.Linear(13, 8)  # <-- 4 -> 13, Wine datasetda 13 feature
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(8, 3)  # 3 sinf bor: class_0, class_1, class_2

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Инициализация модели, функции потерь и оптимизатора
model = WineClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Обучение модели
epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}')

# Оценка модели на тестовом наборе
with torch.no_grad():
    outputs = model(X_test_tensor)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_test_tensor).sum().item() / len(y_test_tensor)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')
