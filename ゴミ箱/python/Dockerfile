FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ===== ベース依存パッケージ（Chrome用ライブラリ込み） =====
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      curl wget gnupg ca-certificates \
      fonts-liberation \
      libasound2 \
      libatk1.0-0 \
      libatk-bridge2.0-0 \
      libcairo2 \
      libcups2 \
      libdbus-1-3 \
      libexpat1 \
      libfontconfig1 \
      libglib2.0-0 \
      libgdk-pixbuf-2.0-0 \
      libnspr4 \
      libnss3 \
      libpango-1.0-0 \
      libx11-6 \
      libx11-xcb1 \
      libxcb1 \
      libxcomposite1 \
      libxcursor1 \
      libxdamage1 \
      libxext6 \
      libxfixes3 \
      libxi6 \
      libxrandr2 \
      libxrender1 \
      libxss1 \
      libxtst6 \
      lsb-release \
      xdg-utils; \
    rm -rf /var/lib/apt/lists/*

# ===== Google Chrome（本体）インストール =====
RUN set -eux; \
    mkdir -p /etc/apt/keyrings; \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
      | gpg --dearmor -o /etc/apt/keyrings/google-linux-signing-keyring.gpg; \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends google-chrome-stable; \
    rm -rf /var/lib/apt/lists/*

# Selenium用に一応環境変数（なくても動くけどおまじない）
ENV CHROME_BIN=/usr/bin/google-chrome

# ===== Node.js 22 + Codex CLI =====
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends gnupg; \
    mkdir -p /etc/apt/keyrings; \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
      | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg; \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_22.x nodistro main" \
      > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends nodejs; \
    node -v; \
    npm -v; \
    rm -rf /var/lib/apt/lists/*

RUN npm config set prefix /usr/local \
  && npm install -g @openai/codex

RUN apt-get update && apt-get install -y fonts-dejavu
COPY meiryo.ttc /usr/share/fonts/truetype/meiryo.ttc




ENV PATH="/usr/local/bin:/usr/bin:/root/.npm-global/bin:${PATH}"

# ===== Python アプリ部分 =====
WORKDIR /usr/src/app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN fc-cache -fv
COPY . .

CMD ["bash"]