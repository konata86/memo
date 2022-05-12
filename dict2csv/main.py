import numpy as np
import csv

def exp(x, shift):
    return np.exp(-x+shift)

def main():

    results = {} # 辞書型として定義
    
    results["train/loss"]  = []
    results["train/loss1"] = []
    results["train/loss2"] = []
    results["valid/loss"]  = []
    results["valid/loss1"] = []
    results["valid/loss2"] = []

    np.random.seed(86)

    # データの生成
    for i in range(100):
        
        eps = i * 0.1

        train_loss1 = exp(eps + np.random.randn(1), 5)
        train_loss2 = exp(eps + np.random.randn(1), 5)

        train_loss = train_loss1 + train_loss2

        valid_loss1 = exp(eps + np.random.randn(1), 10)
        valid_loss2 = exp(eps + np.random.randn(1), 10)

        valid_loss = valid_loss1 + valid_loss2

        results["train/loss"] .append(train_loss.item())
        results["train/loss1"].append(train_loss1.item())
        results["train/loss2"].append(train_loss2.item())
        results["valid/loss"] .append(valid_loss.item())
        results["valid/loss1"].append(valid_loss1.item())
        results["valid/loss2"].append(valid_loss2.item())

    # csv保存
    with open('loss.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(results.keys())

        for v in zip(*results.values()):
            writer.writerow(v)
        



if __name__ == '__main__':
    main()
