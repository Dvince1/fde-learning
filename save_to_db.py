import sqlite3
import pandas as pd
import os

def save_and_query():
    # 1. 检查昨天清洗好的 CSV 文件是否存在
    csv_file = 'cleaned_customer_data.csv'
    if not os.path.exists(csv_file):
        print(f" 找不到 {csv_file}，请先运行昨天的 api_data_cleaner.py")
        return

    print("1. 正在读取 CSV 数据...")
    df = pd.read_csv(csv_file)
    
    # 2. 连接 SQLite 数据库
    # 这里的 customer.db 是我们新生成的数据库文件
    conn = sqlite3.connect('customer.db')
    
    # 3. 将 DataFrame 写入数据库，表名定为 customers
    # if_exists='replace' 意味着如果表存在就覆盖，方便反复练习
    df.to_sql('customers', conn, if_exists='replace', index=False)
    print("2. 数据已成功写入数据库！")
    
    # 4. 执行 SQL 查询，找出城市为 'Gwenborough' 的客户
    query_sql = "SELECT * FROM customers WHERE city = 'Gwenborough'"
    cursor = conn.cursor()
    cursor.execute(query_sql)
    results = cursor.fetchall()
    
    # 5. 打印查询结果
    print("\n--- 查询结果 (城市为 Gwenborough 的客户) ---")
    if results:
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}, 邮箱: {row[2]}, 城市: {row[3]}")
    else:
        print("没有找到符合条件的数据。")
        
    # 6. 关闭数据库连接（FDE必备习惯）
    conn.close()
    print("\n3. 数据库连接已安全关闭。")

if __name__ == "__main__":
    save_and_query()