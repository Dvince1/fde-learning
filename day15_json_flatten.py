import os
import json
import pandas as pd

def flatten_nested_json():
    # 1. 自愈机制：自动生成模拟的嵌套 JSON 数据
    json_file = 'nested_client_data.json'
    if not os.path.exists(json_file):
        print("未检测到嵌套 JSON 数据，正在自动生成...")
        sample_json = [
            {
                "id": 101,
                "name": "Alice",
                "address": {"city": "Beijing", "zipcode": "100001"},
                "contact": {"email": "alice@example.com", "phone": "13800000001"}
            },
            {
                "id": 102,
                "name": "Bob",
                "address": {"city": "Shanghai", "zipcode": "200001"},
                "contact": {"email": "bob@example.com", "phone": "13800000002"}
            }
        ]
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(sample_json, f, ensure_ascii=False, indent=2)

    print("1. 正在读取嵌套 JSON 数据...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("2. 正在将多层嵌套数据拍平（Flatten）...")
    # 核心操作：pd.json_normalize 将嵌套结构自动解析成扁平列
    df = pd.json_normalize(data)
    
    # 3. 重命名列名，去掉点号，方便后续使用 (比如 address.city 变成 city)
    df.columns = [col.replace('address.', '').replace('contact.', '') for col in df.columns]
    
    print("\n--- 拍平后的数据结构预览 ---")
    print(df)

    # 4. 导出为 CSV 客户报表
    output_file = "flattened_client_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\n3. 数据扁平化完成！已导出为：{output_file}")

if __name__ == "__main__":
    flatten_nested_json()