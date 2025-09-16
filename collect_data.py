# collect_data.py
import datetime
import os
import csv

def collect_and_save_data():
    # Ganti bagian ini dengan logika pengumpulan data Anda
    # Misalnya, mengambil data dari API atau halaman web
    data_to_save = [
        ['Nama', 'Nilai'],
        ['Data1', 100],
        ['Data2', 200]
    ]

    # Mendapatkan tanggal dan jam saat ini
    now = datetime.datetime.now()
    date_str = now.strftime('%m%d%Y') # Format: 12192024
    time_str = now.strftime('%H.%M')  # Format: 15.00

    # Menentukan nama file
    file_name = f'cron_{date_str}_{time_str}.csv'
    file_path = os.path.join('/home/cron', file_name)

    # Memastikan direktori /home/cron ada
    os.makedirs('/home/cron', exist_ok=True)

    # Menyimpan data ke file CSV
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_to_save)

    print(f"Data berhasil disimpan di {file_path}")

if __name__ == '__main__':
    collect_and_save_data()