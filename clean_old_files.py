# clean_old_files.py
import os
import datetime

def clean_old_files(directory):
    # Hitung waktu satu bulan yang lalu
    now = datetime.datetime.now()
    one_month_ago = now - datetime.timedelta(days=30)

    # Loop melalui semua file di direktori
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Hanya proses file
        if os.path.isfile(file_path):
            # Dapatkan waktu modifikasi file
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            # Hapus file jika lebih tua dari satu bulan
            if modification_time < one_month_ago:
                os.remove(file_path)
                print(f"Menghapus file lama: {file_path}")

if __name__ == '__main__':
    # Tentukan direktori yang akan dibersihkan
    data_directory = '/home/cron'
    clean_old_files(data_directory)