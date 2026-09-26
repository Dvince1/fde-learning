import requests
import pandas as pd

def fetch_and_clean_data():
    api_url = "https://jsonplaceholder.typicode.com/users"
    print("1. 正在请求客户系统 API...")
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        raw_data = response.json()
        print(f"2. 成功获取数据，共 {len(raw_data)} 条记录。")
    except requests.exceptions.RequestException as e:
        print(f"API 请求失败: {e}")
        return

    df = pd.DataFrame(raw_data)
    
    df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
    
    df_clean = df[['id', 'name', 'email', 'city']]
    
    df_clean['email'] = df_clean['email'].fillna('unknown@example.com')
    
    output_file = "cleaned_customer_data.csv"
    df_clean.to_csv(output_file, index=False)
    print(f"3. 数据清洗完毕！已保存到 {output_file}")
    print("\n--- 数据预览 ---")
    print(df_clean.head())

if __name__ == "__main__":
    fetch_and_clean_data()