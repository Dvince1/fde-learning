# log_analyzer.py - 日志分析脚本
import datetime

def analyze_log(file_path):
    # 用于存放报错行
    error_lines = []
    total_lines = 0

    try:
        # 打开文件读取
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                total_lines += 1
                # 如果这一行包含 ERROR，就记录下来
                if "ERROR" in line:
                    error_lines.append(line.strip())  # strip() 去掉行末的换行符

        # 打印汇总结果
        print(f"====== 分析报告 ======")
        print(f"分析时间: {datetime.datetime.now()}")
        print(f"共读取日志: {total_lines} 行")
        print(f"发现错误: {len(error_lines)} 条")
        print(f"====== 错误详情 ======")
        for err in error_lines:
            print(f" -> {err}")

    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}，请检查路径！")

# 程序入口
if __name__ == "__main__":
    analyze_log("server.log")