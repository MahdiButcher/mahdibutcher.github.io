---
title: هولدربات 
type: docs
next: docs/folder/leaf
weight: 3
sidebar:
  open: true
---

{{< github_info owner="erfjab" repo="holderbot" >}}


هولدربات 🚀 توسط عرفان برای مرزبان توسعه داده شده و به دلیل ارائه قابلیت هولد کردن یوزر در مرزبان، محبوبیت زیادی کسب کرده است. 🎉 این ویژگی در زمان خود توسط UI مرزبان پشتیبانی نمی‌شد.  
عرفان یکی از فعال‌ترین کانتریبیوترهای حوزه آزادی وب 🌐 است. می‌توانید او را در تلگرام 📱 و گیت‌هاب 🖥️ دنبال کنید.

{{< cards >}}
  {{< card link="https://t.me/erfjabs" title="تلگرام" icon="telegram" >}}
  {{< card link="https://github.com/erfjab/holderbot" title="گیتهاب پروژه" icon="github" >}}
{{< /cards >}}

{{% steps %}}

### ⚙️ تنظیم سرور

#### 🔄 به‌روزرسانی سرور

اطمینان حاصل کنید که سرور شما به‌روز است:

```bash
sudo apt update && sudo apt upgrade -y
```

#### 🐋 نصب داکر

برای نصب داکر، از دستور زیر استفاده کنید:

```bash
curl -fsSL https://get.docker.com | sh
```

---

### 📂 دانلود و پیکربندی

#### 🛠️ ایجاد پوشه و دانلود `docker-compose.yml`

پوشه موردنیاز را ایجاد کرده و فایل `docker-compose.yml` را دانلود کنید:

```bash
mkdir -p /opt/erfjab/holderbot/data
curl -o /opt/erfjab/holderbot/docker-compose.yml https://raw.githubusercontent.com/erfjab/holderbot/master/docker-compose.yml
cd /opt/erfjab/holderbot
```

#### 📝 دانلود و پیکربندی `.env`

فایل محیطی نمونه را دانلود کنید:

```bash
curl -o .env https://raw.githubusercontent.com/erfjab/holderbot/master/.env.example
```

سپس فایل `.env` را ویرایش کرده و **توکن ربات تلگرام** و **کلیدهای API** را اضافه کنید:  

```bash
nano .env
```

---

### 🤖 اجرای ربات

#### ⬇️ دانلود آخرین تصویر داکر

آخرین تصویر داکر برای ربات را دانلود کنید:

```bash
docker compose pull
```

#### ▶️ شروع ربات

ربات را در حالت جدا شده اجرا کنید:

```bash
docker compose up -d
```

#### 🛡️ بررسی اجرای ربات

وضعیت کانتینرهای در حال اجرا را بررسی کنید:

```bash
docker compose ps
```

---
{{% /steps %}}

### 🔄 به‌روزرسانی ربات

برای به‌روزرسانی ربات به آخرین نسخه:

1. ⬇️ آخرین تصویر داکر را دانلود کنید:

    ```bash
    docker compose pull
    ```

2. ▶️ ربات را مجدداً اجرا کنید:

    ```bash
    docker compose up -d
    ```

---

### 🛠️ مدیریت ربات با داکر

#### 🔁 راه‌اندازی مجدد ربات

```bash
docker compose restart
```

#### ⛔ توقف ربات

```bash
docker compose down
```

#### 📜 مشاهده لاگ‌ها به صورت زنده

```bash
docker compose logs -f
```

---

### 📬 تماس و پشتیبانی

- کانال تلگرام: [@ErfJabs](https://t.me/ErfJabs) 📢  

برای حمایت از پروژه، لطفاً به آن ⭐ دهید! 🌟  

[![Stargazers over time](https://starchart.cc/erfjab/holderbot.svg?variant=adaptive)](https://starchart.cc/erfjab/holderbot)

---