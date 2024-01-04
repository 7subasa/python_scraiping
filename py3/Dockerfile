# 使用する Python のバージョンを指定
FROM python:3.10

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# 必要な依存関係のインストール
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    chromium \
    chromium-driver

# requirements.txt には必要な Python ライブラリがリストされている
COPY requirements.txt .

# requirements.txt にリストされたライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコンテナ内にコピー
COPY . .
