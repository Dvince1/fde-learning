import os
import pandas as pd

def validate_and_clean_data():
    # 1. 自愈机制：自动生成模拟脏数据
    csv_file = 'dirty_client_data.csv'
    if not os.path.exists(csv_file):
        print("未检测到脏数据，正在自动生成...")
        raw_data = """id,name,email,amount
1,Alice,alice@example.com,100
2,,bob@example.com,200
3,Charlie,charlie_at_example.com,300
4,David,david@example.com,-50
5,Eve,eve@example.com,500"""
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.write(raw_data)

    print("1. 正在读取客户原始数据...")
    df = pd.read_csv(csv_file)
    
    print("2. 正在执行数据质量校验...")
    # 规则1：名字不能为空
    valid_name = df['name'].notna()
    # 规则2：邮箱必须包含 '@'
    valid_email = df['email'].apply(lambda x: isinstance(x, str) and '@' in x)
    # 规则3：金额必须大于 0
    valid_amount = df['amount'] > 0
    
    # 综合所有规则，生成布尔掩码
    valid_mask = valid_name & valid_email & valid_amount
    
    # 3. 把数据拆分成“干净”和“异常”两份
    clean_df = df[valid_mask]
    invalid_df = df[~valid_mask]
    
    print("\n---  清洗后的有效数据 ---")
    print(clean_df)
    
    print("\n---  异常数据（需退回给客户修改） ---")
    print(invalid_df)
    
    # 4. 分别导出为两个 CSV 文件
    clean_df.to_csv('clean_client_data.csv', index=False)
    invalid_df.to_csv('invalid_data_report.csv', index=False)
    
    print("\n3. 处理完成！")
    print(" -> 有效数据已保存至: clean_client_data.csv")
    print(" -> 异常报告已生成至: invalid_data_report.csv")

if __name__ == "__main__":
    validate_and_clean_data()