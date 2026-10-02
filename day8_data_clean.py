import pandas as pd

def process_customer_data():
    print("1. 正在读取客户原始数据...")
    df = pd.read_csv('raw_data.csv')
    
    print("2. 开始数据清洗...")
    # 1. 去除名字和城市两边的空格
    df['name'] = df['name'].str.strip()
    df['city'] = df['city'].str.strip()
    
    # 2. 统一城市为小写，防止 Beijing 和 beijing 被当成两个城市
    df['city'] = df['city'].str.lower()
    
    # 3. 处理缺失的金额，填为 0
    df['amount'] = df['amount'].fillna(0)
    
    # 4. 将金额转换为整数（客户系统导出时常带小数点）
    df['amount'] = df['amount'].astype(int)
    
    print("3. 清洗完成！清洗后的数据如下：")
    print(df)
    
    print("\n4. 正在按城市统计消费总额...")
    # 按城市分组，并对 amount 列求和
    result = df.groupby('city')['amount'].sum()
    
    print("\n--- 最终统计报告 ---")
    print(result)

if __name__ == "__main__":
    process_customer_data()