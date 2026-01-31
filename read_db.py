import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False # 讓負號也能正常顯示
db_path = r'C:\Dev\my_lab.db'
conn = sqlite3.connect(db_path)
sql = "SELECT * FROM 樣本表 ORDER BY 樣本質量 DESC"
df = pd.read_sql(sql, conn)
conn.close()
plt.figure(figsize=(10, 6)) # 設定圖片大小 (寬10, 高6)
plt.bar(df['樣本名稱'], df['樣本質量'], color='skyblue')
plt.title('實驗室樣本質量分佈圖', fontsize=16) # 大標題
plt.xlabel('樣本名稱', fontsize=12)           # X軸名稱
plt.ylabel('質量 (g)', fontsize=12)           # Y軸名稱
plt.grid(axis='y', linestyle='--', alpha=0.7) # 加一點虛線背景比較好讀
print("正在製圖中...")
plt.show()