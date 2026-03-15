# Django Darslari 2

Ushbu repository Django bo‘yicha o‘quv loyihalar to‘plami bo‘lib, ichida **3 ta alohida project** mavjud. Har bir project bir nechta app-larni o‘z ichiga oladi va Django `models`, `views`, `serializers` va `templates` bilan ishlashni ko‘rsatadi.

---

## 📁 Projectlar va ularning App-lari

### 1️⃣ Project 1 – Dorixona va Mijozlar
- **Apps:** Dorixona, Mijozlar  
- **Tavsif:** Dorixona va mijozlar ma’lumotlarini boshqarish loyihasi.  
- **Ishga tushirish:**  
```bash
cd project1
python manage.py migrate
python manage.py runserver
2️⃣ Project 2 – Books va Authors
Apps: Books, Authors

Tavsif: Kitoblar va mualliflarni boshqarish loyihasi.

Ishga tushirish:

cd project2
python manage.py migrate
python manage.py runserver
3️⃣ Project 3 – Users va Posts
Apps: Users, Posts

Tavsif: Foydalanuvchilar va postlarni boshqarish loyihasi.

Ishga tushirish:

cd project3
python manage.py migrate
python manage.py runserver
⚡ O‘rnatish bo‘yicha ko‘rsatmalar
Repository-ni clone qiling:

git clone https://github.com/JonibekXalimov/django_projects.git
Virtual environment yarating va uni aktivlashtiring:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Kutubxonalarni o‘rnating:

pip install -r requirements.txt
Ma’lumotlar bazasini migrate qiling va serverni ishga tushiring:

python manage.py migrate
python manage.py runserver
📝 Izohlar
Har bir project alohida Django project sifatida ishlaydi.

Har bir app models, views, serializers va templates bilan amaliy mashqlarni ko‘rsatadi.

Bu repository Django bo‘yicha o‘quv va amaliy mashqlar uchun mo‘ljallangan.

📂 Folder tuzilmasi (misol)
django_darslari2/
│
├─ project1/
│   ├─ dorixona/
│   └─ mijozlar/
│
├─ project2/
│   ├─ books/
│   └─ authors/
│
├─ project3/
│   ├─ users/
│   └─ posts/
│
└─ README.md
