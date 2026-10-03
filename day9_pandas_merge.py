import pandas as pd

def analyze_customer_orders():
    print("1. 正在读取客户信息表和订单表...")
    # 读取两张CSV表
    customer_df = pd.read_csv('customer_info.csv')
    orders_df = pd.read_csv('orders.csv')
    
    print("2. 正在把两张表拼接起来...")
    # 关键操作：以 customer_id 为纽带，把两张表连起来（类似Excel的VLOOKUP）
    merged_df = pd.merge(customer_df, orders_df, on='customer_id', how='inner')
    
    print("拼接后的完整数据：")
    print(merged_df)
    
    print("\n3. 正在按城市统计消费总额...")
    # 按城市分组，对金额求和
    result = merged_df.groupby('city')['amount'].sum().reset_index()
    
    print("\n--- 最终统计报告 ---")
    print(result)
    
    # 4. 把结果导出成新的CSV，交给客户
    result.to_csv('city_sales_report.csv', index=False)
    print("\n4. 报告已生成：city_sales_report.csv")

if __name__ == "__main__":
    analyze_customer_orders()