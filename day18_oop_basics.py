# day18_oop_basics.py

class Customer:
    # 1. 初始化方法：每次创建新客户时，自动执行，设定属性
    def __init__(self, customer_id, name, balance=0):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance

    # 2. 存款方法
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[{self.name}] 成功存入 {amount} 元，当前余额: {self.balance} 元")
        else:
            print(f"[{self.name}] 存款金额必须大于0！")

    # 3. 取款方法（包含业务规则校验）
    def withdraw(self, amount):
        if amount <= 0:
            print(f"[{self.name}] 取款金额必须大于0！")
        elif amount > self.balance:
            print(f"[{self.name}] 余额不足！当前余额: {self.balance} 元，无法取出 {amount} 元")
        else:
            self.balance -= amount
            print(f"[{self.name}] 成功取出 {amount} 元，当前余额: {self.balance} 元")

    # 4. 打印客户信息方法
    def show_info(self):
        print(f"账户ID: {self.customer_id}, 姓名: {self.name}, 余额: {self.balance}")

# 5. 主程序入口
def run_customer_system():
    print("1. 正在初始化客户系统...")
    
    # 创建两个具体的客户对象（实例化）
    c1 = Customer(101, "Alice", 1000)
    c2 = Customer(102, "Bob", 500)

    print("\n--- 初始信息 ---")
    c1.show_info()
    c2.show_info()

    print("\n--- 正在模拟业务操作 ---")
    c1.deposit(500)
    c1.withdraw(200)
    
    # 故意测试异常情况（看业务规则是否生效）
    c2.withdraw(1000)
    c2.deposit(-100)

    print("\n--- 操作后最终信息 ---")
    c1.show_info()
    c2.show_info()

if __name__ == "__main__":
    run_customer_system()