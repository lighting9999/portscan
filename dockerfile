FROM python:3.13.2-slim

# 设置工作目录
WORKDIR /app
COPY . /app

# 安装项目的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV FLASK_APP=webapp.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 启动 Flask 应用
CMD [CMD ["python", "app/webapp.py"]
