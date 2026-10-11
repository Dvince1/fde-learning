import os
import sqlite3
from datetime import datetime

def health_check():
    print(f"====== 系统巡检报告 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ======\n")
    report = []
    
    # 1. 检查文件系统（检查关键数据文件是否存在）
    print("1. 正在检查文件系统...")
    if os.path.exists('client_list.csv'):
        report.append("✅ 客户名单文件正常存在")
    else:
        report.append("❌ 客户名单文件丢失！")
        
    # 2. 检查数据库连接（FDE 核心：数据库连不上，系统就废了）
    print("2. 正在检查数据库连接...")
    try:
        conn = sqlite3.connect('customer.db')
        cursor = conn.cursor()
        # 尝试执行一条最简单的 SQL
        cursor.execute("SELECT 1")
        conn.close()
        report.append("✅ 数据库连接测试通过")
    except sqlite3.Error as e:
        report.append(f"❌ 数据库连接失败: {e}")

    # 3. 检查网络（模拟）
    print("3. 正在检查网络连通性...")
    report.append("✅ 外网连接测试通过 (模拟)")

    # 4. 打印汇总报告
    print("\n====== 巡检汇总结果 ======")
    for item in report:
        print(item)
    
    print("\n巡检结束。")

if __name__ == "__main__":
    health_check()