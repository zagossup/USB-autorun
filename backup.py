import os
import shutil
import datetime

# اسم الفلاشة (عدّله حسب اسم فلاشتك)
usb_name = "MYUSB"
usb_path = f"H:\\Backup_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# قائمة المجلدات التي سيتم نسخها
folders_to_backup = [
    os.path.expanduser("~\\Desktop"),   # سطح المكتب
    os.path.expanduser("~\\Documents"), # المستندات
    os.path.expanduser("~\\Downloads")  # التنزيلات
]

# إنشاء مجلد داخل الفلاشة لحفظ النسخ الاحتياطية
if not os.path.exists(usb_path):
    os.makedirs(usb_path)

# نسخ الملفات إلى الفلاشة
for folder in folders_to_backup:
    if os.path.exists(folder):
        dest_folder = os.path.join(usb_path, os.path.basename(folder))
        shutil.copytree(folder, dest_folder, dirs_exist_ok=True)

print("✅ تم النسخ الاحتياطي بنجاح!")