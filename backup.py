import os
import shutil
import datetime

def backup_files(source, destination):
    today = datetime.date.today()
    backup_name = os.path.join(destination, f"backup_{today}")

    # Create .tar.gz archive
    shutil.make_archive(backup_name, 'gztar', source)

    print(f"Backup created: {backup_name}.tar.gz")

source = r"C:\Users\saisa\OneDrive\Desktop\DevOps\Python"
destination = r"C:\Users\saisa\OneDrive\Desktop\DevOps\Python\backups"

backup_files(source, destination)