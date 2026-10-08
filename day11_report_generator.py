import os
import pandas as pd

def generate_client_report():
    # 1. 自愈机制：自动检查数据文件是否存在，不存在就帮客户/开发者建好
    if not os.path.exists('server_logs.csv'):
        print("未检测到日志文件，正在自动创建...")
        sample_data = """timestamp,level,message
2026-10-01 08:30:00,INFO,User login success
2026-10-02 09:15:00,INFO,Data sync complete
2026-10-01 10:20:00,ERROR,Database connection timeout
2026-10-02 11:45:00,ERROR,API returned 500
2026-10-03 14:00:00,INFO,User logout
2026-10-03 15:30:00,ERROR,Redis connection refused
2026-10-01 16:00:00,INFO,Health check passed"""
        with open('server_logs.csv', 'w', encoding='utf-8') as f:
            f.write(sample_data)

    print("1. 正在读取服务器日志...")
    df = pd.read_csv('server_logs.csv')
    
    # 2. 筛选出所有的 ERROR 日志
    error_df = df[df['level'] == 'ERROR']
    
    print("2. 正在将数据转化为 Markdown 报告...")
    # 3. 拼装 Markdown 格式文本（FDE 交付给客户的颜值天花板）
    report_content = "# 客户服务器异常分析报告\n\n"
    report_content += f"> 报告生成时间：{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report_content += f"本次分析共扫描日志 **{len(df)}** 条，发现严重错误 **{len(error_df)}** 条。\n\n"
    
    report_content += "## 🚨 错误明细表\n\n"
    report_content += "| 发生时间 | 错误详情 |\n"
    report_content += "| :--- | :--- |\n"
    
    for index, row in error_df.iterrows():
        report_content += f"| {row['timestamp']} | {row['message']} |\n"
        
    report_content += "\n## 💡 FDE 技术建议\n\n"
    report_content += "1. **Database connection timeout**：建议检查客户数据库连接池上限。\n"
    report_content += "2. **API returned 500**：建议排查对应后端服务的运行状态。\n"
    report_content += "3. **Redis connection refused**：建议检查缓存服务的端口和安全组。\n"

    # 4. 将报告写入文件
    output_filename = "error_report.md"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"3. 报告生成完毕！文件名为：{output_filename}")
    print("\n--- 报告内容预览 ---")
    print(report_content)

if __name__ == "__main__":
    generate_client_report()