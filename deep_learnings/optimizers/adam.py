import torch
from torch.utils.data import TensorDataset, DataLoader

# Regression: Predicting continuous values
loss_fn = torch.nn.MSELoss()

# Binary classification
# loss_fn = torch.nn.BCEWithLogitsLoss()
# Multi-class classification
# loss_fn = torch.nn.CrossEntropyLoss()



X = torch.randn(100, 10)
y = torch.randn(100, 1)

dataset = TensorDataset(X, y)
data = DataLoader(dataset, batch_size=16, shuffle=True)


model = torch.nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9, 0.999), eps=1e-8)


for epoch in range(140):
    total_loss = 0.0
    for x_batch, y_batch in data:
        optimizer.zero_grad()
        pred = model(x_batch)
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(data)

    # print(f"Epoch {epoch}: loss = {loss.item():.4f}")
    print(f"Epoch {epoch}: avg loss = {avg_loss:.4f}")
