# ./Dockerfile
FROM python:3.12-slim

# Pythonの挙動を素直にするおまじない
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# まずは依存だけコピーしてインストール
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# あとからコードを全部コピー
COPY . .

# デフォルトは何もしない（docker-compose側で上書きする）
CMD ["python", "test.py"]
