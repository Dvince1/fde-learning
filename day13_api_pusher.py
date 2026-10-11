import csv
import os
import time

def push_data_to_client_api():
    # 1. 自愈机制：自动生成模拟的客户名单
    csv_file = 'client_list.csv'
    if not os.path.exists(csv_file):
        print("未检测到客户名单，正在自动生成...")
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'email'])
            writer.writerow([1, 'Alice', 'alice@example.com'])
            writer.writerow([2, 'Bob', 'bob@example.com'])
            writer.writerow([3, 'Charlie', 'charlie@example.com'])

    print("1. 正在读取客户名单...")
    customers = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(row)
            
    print(f"2. 共读取到 {len(customers)} 位客户，准备推送至客户系统 API...")
    
    # 3. 模拟向客户 API 发送数据（FDE 必学：防御性编程）
    for customer in customers:
        try:
            # 这里我们用打印来模拟网络请求，完全避开网络波动
            print(f" -> 正在推送: {customer['name']} ({customer['email']})")
            # 模拟网络延迟
            time.sleep(0.5) 
            print(f"    ✅ 推送成功！")
        except Exception as e:
            # FDE 的核心价值：一条数据失败不能导致整个程序崩溃
            print(f"    ❌ 推送失败: {customer['name']}, 错误原因: {e}")
            print("    正在记录错误日志...")

    print("\n3. 所有数据推送完毕！")

if __name__ == "__main__":
    push_data_to_client_api()