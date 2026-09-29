from fastapi import FastAPI
import sqlite3

# 创建 FastAPI 应用实例
app = FastAPI(title="FDE Customer API")

@app.get("/")
def read_root():
    return {"message": "欢迎来到 FDE 客户数据服务 API"}

@app.get("/customers")
def get_all_customers():
    # 连接昨天的 SQLite 数据库
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    
    # 将查询结果转换成字典列表，方便转换成 JSON 格式
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "city": row[3]
        })
    return result

@app.get("/customers/{city}")
def get_customers_by_city(city: str):
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    # 使用参数化查询，防止 SQL 注入（FDE 必须掌握的安全习惯）
    cursor.execute("SELECT * FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    conn.close()
    
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "city": row[3]
        })
    return result