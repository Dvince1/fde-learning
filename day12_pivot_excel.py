import os
import pandas as pd

def generate_sales_pivot():
    # 1. 自愈机制：自动检查数据文件是否存在，不存在就帮客户/开发者建好
    if not os.path.exists('sales_data.csv'):
        print("未检测到销售数据，正在自动创建...")
        sample_data = """date,city,product,amount
2026-10-01,Beijing,A,100
2026-10-01,Beijing,B,200
2026-10-02,Shanghai,A,150
2026-10-02,Shanghai,C,300
2026-10-03,Beijing,A,120
2026-10-03,Shanghai,B,250"""
        with open('sales_data.csv', 'w', encoding='utf-8') as f:
            f.write(sample_data)

    print("1. 正在读取客户销售数据...")
    df = pd.read_csv('sales_data.csv')
    
    print("2. 正在生成多维透视表（按城市和产品分类统计）...")
    # 核心操作：pivot_table（数据透视表）
    # index=行(城市)，columns=列(产品)，values=值(金额)，aggfunc=聚合函数(求和)
    pivot_df = pd.pivot_table(df, index='city', columns='product', values='amount', aggfunc='sum', fill_value=0)
    
    print("\n--- 数据透视表预览 ---")
    print(pivot_df)
    
    print("\n3. 正在导出为 Excel 报表...")
    output_file = "sales_pivot_report.xlsx"
    # 将透视表结果导出为Excel文件
    pivot_df.to_excel(output_file)
    print(f"4. 导出成功！文件名为：{output_file}")

if __name__ == "__main__":
    generate_sales_pivot()