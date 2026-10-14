import os
import pandas as pd

def generate_customer_tags():
    # 1. 自愈机制：自动生成模拟的客户数据
    csv_file = 'customers.csv'
    if not os.path.exists(csv_file):
        print("未检测到客户数据，正在自动生成...")
        raw_data = """id,name,city,total_spend
101,Alice,Beijing,1500
102,Bob,Shanghai,800
103,Charlie,Shenzhen,300
104,David,Beijing,600
105,Eve,Hangzhou,2000
106,Frank,Chengdu,100"""
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.write(raw_data)

    print("1. 正在读取客户数据...")
    df = pd.read_csv(csv_file)
    
    # 2. 定义业务规则函数
    def get_tag(row):
        spend = row['total_spend']
        city = row['city']
        
        # 业务规则：按消费金额分层
        if spend > 1000:
            tag = 'VIP'
        elif spend >= 500:
            tag = 'Potential'
        else:
            tag = 'Normal'
            
        # 业务规则：一线城市加星号
        if city in ['Beijing', 'Shanghai']:
            tag += '*'
            
        return tag

    print("2. 正在应用业务规则生成客户标签...")
    # 3. 将规则应用到每一行数据
    df['tag'] = df.apply(get_tag, axis=1)
    
    print("\n--- 打标后的数据预览 ---")
    print(df[['id', 'name', 'city', 'total_spend', 'tag']])

    print("\n3. 正在按标签统计客户数量...")
    # 4. 按标签分组统计
    summary = df.groupby('tag')['id'].count().reset_index()
    summary.columns = ['tag', 'customer_count']
    print(summary)

    # 5. 导出结果
    output_file = "tagged_customers.csv"
    df.to_csv(output_file, index=False)
    print(f"\n4. 结果已保存至: {output_file}")

if __name__ == "__main__":
    generate_customer_tags()