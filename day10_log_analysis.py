import pandas as pd

def analyze_server_logs():
    print("1. 正在读取服务器日志...")
    df = pd.read_csv('server_logs.csv')
    
    # 2. 将字符串格式的时间转换为标准时间对象（FDE 必备技能）
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 3. 按照日期和日志级别进行分组统计
    # 比如：10月1日有1条ERROR，10月2日有1条ERROR
    daily_summary = df.groupby([df['timestamp'].dt.date, 'level']).size().unstack(fill_value=0)
    
    print("\n--- 每日日志统计报告 ---")
    print(daily_summary)
    
    # 4. 把所有的 ERROR 日志单独提取出来，交给客户
    error_df = df[df['level'] == 'ERROR']
    
    print("\n--- 严重错误明细 ---")
    for index, row in error_df.iterrows():
        print(f"时间: {row['timestamp']} | 详情: {row['message']}")

    # 5. 导出一份专门的错误报告 CSV
    error_df.to_csv('error_report.csv', index=False)
    print("\n5. 错误报告已生成：error_report.csv")

if __name__ == "__main__":
    analyze_server_logs()