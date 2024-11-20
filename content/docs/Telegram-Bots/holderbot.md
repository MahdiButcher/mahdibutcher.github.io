---
title: HolderBot
type: docs
next: docs/folder/leaf
weight: 3
sidebar:
  open: true
---


{{% steps %}}

### به‌روزرسانی سرور

اطمینان حاصل کنید که سرور شما به‌روز است:

```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2: نصب داکر

برای نصب داکر از این دستور استفاده کنید:

<!-- ```bash
curl -fsSL https://get.docker.com | sh
``` -->

{{% /steps %}}


## 2. دانلود و پیکربندی

### 2.1: ایجاد پوشه و دانلود `docker-compose.yml`

پوشه موردنیاز را ایجاد کرده و فایل `docker-compose.yml` را دانلود کنید:

```bash
mkdir -p /opt/erfjab/holderbot/data
curl -o /opt/erfjab/holderbot/docker-compose.yml https://raw.githubusercontent.com/erfjab/holderbot/master/docker-compose.yml
cd /opt/erfjab/holderbot
```

### 2.2: دانلود و پیکربندی `.env`

فایل محیطی نمونه را دانلود کنید:

```bash
curl -o .env https://raw.githubusercontent.com/erfjab/holderbot/master/.env.example
```

فایل `.env` را برای اضافه کردن **توکن ربات تلگرام** و **کلیدهای API** ویرایش کنید:

```bash
nano .env
```

---

## 3. اجرای ربات

### 3.1: دانلود آخرین تصویر داکر

آخرین تصویر داکر برای ربات را دانلود کنید:

```bash
docker compose pull
```

### 3.2: شروع ربات

ربات را در حالت جدا شده اجرا کنید:

```bash
docker compose up -d
```

### 3.3: بررسی اجرای ربات

وضعیت کانتینرهای در حال اجرا را بررسی کنید:

```bash
docker compose ps
```

---

## به‌روزرسانی ربات

برای به‌روزرسانی ربات به آخرین نسخه:

1. آخرین تصویر داکر را دانلود کنید:

    ```bash
    docker compose pull
    ```

2. ربات را مجدداً اجرا کنید:

    ```bash
    docker compose up -d
    ```

---

## مدیریت ربات با داکر

### راه‌اندازی مجدد ربات

```bash
docker compose restart
```

### توقف ربات

```bash
docker compose down
```

### مشاهده لاگ‌ها به صورت زنده

```bash
docker compose logs -f
```

---

