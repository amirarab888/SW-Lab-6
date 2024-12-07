همانطور که مشاهده میشود, سرور با fastapi توسط داگر کامپوز همراه یک دیتابیس بالا آورده شده و درخواست های 200 گرفته شده:
![image](https://github.com/user-attachments/assets/15af87b5-768b-4551-9236-6f627ab0d6fb)
![image](https://github.com/user-attachments/assets/ccd4c438-11fb-42b6-ad74-6ad95206d916)

جواب سوال ها:
1: سوال اول:
Stateless به این معنا است که هر درخواست کاملاً مستقل و خودکفا است و هیچ وابستگی به درخواست‌های قبلی ندارد.
در پیاده‌سازی ما، از حالت stateless به چند روش استفاده شده است:
•	هر سرور بک‌اند می‌تواند هر درخواستی را پردازش کند زیرا هیچ حالت سشن بر روی سرورها ذخیره نمی‌شود.
•	تمامی داده‌های پایدار در پایگاه داده مشترک PostgreSQL ذخیره می‌شوند.
•	چندین نمونه API می‌توانند درخواست‌ها را به‌طور متناوب از طریق متوازن‌کننده بار (load balancer) سرویس‌دهی کنند.
•	هر درخواست تمام اطلاعات مورد نیاز برای پردازش را در خود دارد.


2:
بارگذاری متوازن در لایه 4 (لایه حمل و نقل):
•	در سطح TCP/UDP کار می‌کند
•	سریع‌تر و کم‌هزینه‌تر از نظر منابع
•	نمی‌تواند محتوای واقعی درخواست‌ها را مشاهده کند
•	مناسب برای توزیع ترافیک ساده
بارگذاری متوازن در لایه 7 (لایه کاربرد):
•	در سطح HTTP/HTTPS کار می‌کند
•	می‌تواند تصمیمات خود را بر اساس محتوای درخواست بگیرد
•	پرهزینه‌تر از نظر منابع اما هوشمندتر
•	قادر به مدیریت مسیریابی بر اساس محتوا
در آزمایش ما، از بارگذاری متوازن لایه 7 با Nginx استفاده کردیم زیرا:
•	Nginx را با تنظیمات خاص HTTP (مثل proxy_set_header Host $host) پیکربندی کردیم
•	متوازن‌کننده بار ما می‌تواند درخواست‌های HTTP را درک و مسیریابی کند
•	می‌توانیم بررسی سلامت در سطح برنامه را مشاهده کنیم
•	مسیریابی نقطه پایانی /health در سطح HTTP انجام می‌شود
این به ما این امکان را می‌دهد که کنترل بیشتری بر توزیع درخواست‌ها داشته باشیم و نظارت بهتری بر خدمات خود انجام دهیم.
