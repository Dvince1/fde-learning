import sqlite3
import pandas as pd

def save_and_query():
    # 1. 读取昨天清洗好的 CSV 文件
    print("1. 正在读取昨天清洗好的 CSV...")
    df = pd.read_csv('cleaned_customer_data.csv')
    
    # 2. 连接 SQLite 数据库（如果文件不存在，会自动创建）
    # 这里的 customer.db 就是我们的数据库文件
    conn = sqlite3.connect('customer.db')
    
    # 3. 将 DataFrame 写入数据库，表名定为 customers
    # if_exists='replace' 表示如果表已存在，就覆盖它
    df.to_sql('customers', conn, if_exists='replace', index=False)
    print("2. 数据已成功写入数据库！")
    
    # 4. 验证：编写 SQL 查询，找出城市为 'Gwenborough' 的客户
    cursor = conn.cursor()
    query_sql = "SELECT * FROM customers WHERE city = 'Gwenborough'"
    cursor.execute(query_sql)
    
    # 获取查询结果
    results = cursor.fetchall()
    
    print("\n--- 查询结果 (城市为 Gwenborough 的客户) ---")
    if results:
        for row in results:
            print(f"ID: {row[0]}, 姓名: {row[1]}, 邮箱: {row[2]}, 城市: {row[3]}")
    else:
        print("没有找到符合条件的数据。")
        
    # 5. 关闭数据库连接
    conn.close()
    print("\n3. 数据库连接已安全关闭。")

if __name__ == "__main__":
    save_and_query()