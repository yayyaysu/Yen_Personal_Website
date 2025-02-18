# 1. 使用 Python 3.11版本作為基礎映像
FROM python:3.11-slim

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 複製所有 Flask 檔案
COPY . .

# 5. 對外暴露 Flask 服務的端口
EXPOSE 5000

# 6. 啟動 Flask 應用
CMD ["python", "app.py"]
