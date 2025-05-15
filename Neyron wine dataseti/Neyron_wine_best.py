
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import numpy as np

# Загрузим датасет Wine
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
class WineClassifier(nn.Module):
    def __init__(self):
        super(WineClassifier, self).__init__()
        self.fc1 = nn.Linear(13, 8)  # 13 признаков у Wine
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(8, 3)   # 3 класса

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
    accuracy = accuracy_score(y_test_tensor, predicted)
    precision = precision_score(y_test_tensor, predicted, average='weighted')
    recall = recall_score(y_test_tensor, predicted, average='weighted')
    f1 = f1_score(y_test_tensor, predicted, average='weighted')

    print(f'Test Accuracy: {accuracy * 100:.2f}%')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 Score: {f1:.2f}')

    # Confusion Matrix
    cm = confusion_matrix(y_test_tensor, predicted)
    print('Confusion Matrix:')
    print(cm)

    # Визуализация ошибок
    misclassified_idx = np.where(predicted != y_test_tensor)[0]
    true_labels = y_test_tensor[misclassified_idx]
    pred_labels = predicted[misclassified_idx]

    feature_names = wine.feature_names
    num_features = len(feature_names)

    plt.figure(figsize=(15, 10))
    for i in range(num_features):
        for j in range(i + 1, num_features):
            plt.figure()
            plt.scatter(X_test[:, i], X_test[:, j], c=y_test, cmap='viridis', marker='o', alpha=0.7)
            plt.scatter(X_test[misclassified_idx, i], X_test[misclassified_idx, j], c='red', marker='x', s=50)
            plt.title(f'{feature_names[i]} vs {feature_names[j]}')
            plt.xlabel(feature_names[i])
            plt.ylabel(feature_names[j])

    plt.show()
