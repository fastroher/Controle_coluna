import torch
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

class SyntheticRegressionData:
    """Synthetic data for linear regression."""
    def __init__(self, w, b, noise=0.01, num_train=1000, num_val=1000, batch_size=32):
        # Armazena os hiperparâmetros manualmente
        self.w = w
        self.b = b
        self.noise = noise
        self.num_train = num_train
        self.num_val = num_val
        self.batch_size = batch_size
        
        # Gera os dados
        n = num_train + num_val
        self.X = torch.randn(n, len(w))
        noise_tensor = torch.randn(n, 1) * noise
        self.y = torch.matmul(self.X, w.reshape((-1, 1))) + b + noise_tensor
        
        # Divide em treino e validação
        self.X_train = self.X[:num_train]
        self.y_train = self.y[:num_train]
        self.X_val = self.X[num_train:num_train + num_val]
        self.y_val = self.y[num_train:num_train + num_val]
        
        # Cria datasets
        self.train_dataset = TensorDataset(self.X_train, self.y_train)
        self.val_dataset = TensorDataset(self.X_val, self.y_val)
    
    def get_dataloaders(self):
        """Retorna DataLoaders para treino e validação"""
        train_loader = DataLoader(
            self.train_dataset, 
            batch_size=self.batch_size, 
            shuffle=True
        )
        val_loader = DataLoader(
            self.val_dataset, 
            batch_size=self.batch_size, 
            shuffle=False
        )
        return train_loader, val_loader
    
    def get_tensors(self):
        """Retorna os tensores diretamente (para uso sem DataLoader)"""
        return self.X_train, self.y_train, self.X_val, self.y_val
    
    def visualize(self, num_samples=100):
        """Visualiza os dados (apenas para 1D)"""
        if self.X.shape[1] != 1:
            print("Visualização disponível apenas para dados 1D")
            return
            
        plt.figure(figsize=(10, 6))
        plt.scatter(self.X_train[:num_samples].numpy(), 
                   self.y_train[:num_samples].numpy(), 
                   alpha=0.7, label='Treino')
        plt.scatter(self.X_val[:num_samples].numpy(), 
                   self.y_val[:num_samples].numpy(), 
                   alpha=0.7, label='Validação')
        
        # Linha verdadeira
        x_range = torch.linspace(self.X.min(), self.X.max(), 100)
        y_true = x_range * self.w[0] + self.b
        plt.plot(x_range.numpy(), y_true.numpy(), 'r-', label='Verdadeiro', linewidth=2)
        
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.title('Dados Sintéticos de Regressão')
        plt.show()

# Exemplo de uso:
if __name__ == "__main__":
    # Parâmetros verdadeiros
    true_w = torch.tensor([2.0, -3.4])
    true_b = 4.2
    
    # Cria dados sintéticos
    data = SyntheticRegressionData(w=true_w, b=true_b, num_train=1000, num_val=200)
    
    # Obtém DataLoaders
    train_loader, val_loader = data.get_dataloaders()
    
    # Ou obtém tensores diretamente
    X_train, y_train, X_val, y_val = data.get_tensors()
    
    print(f"Forma de X_train: {X_train.shape}")
    print(f"Forma de y_train: {y_train.shape}")
    print(f"Forma de X_val: {X_val.shape}")
    print(f"Forma de y_val: {y_val.shape}")
    
    # Visualiza (para 1D - modifique w para tensor 1D para ver)
    if X_train.shape[1] == 1:
        data.visualize()

print('features:', data.X[0],'\nlabel:', data.y[0])