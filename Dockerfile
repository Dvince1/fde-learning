# 1. 使用官方轻量级 Python 作为基础环境
FROM python:3.9-slim

# 2. 设置容器内的工作目录
WORKDIR /app

# 3. 把依赖清单复制进去，并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 把你写好的所有代码复制进容器
COPY . .

# 5. 暴露容器内的 8000 端口
EXPOSE 8000

# 6. 启动服务（必须是 0.0.0.0，否则外部无法访问）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]