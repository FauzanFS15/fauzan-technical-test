import os
import datetime
import time

def cleanse_data():
    base_path = '/home/cron'
    # Hitung waktu satu bulan yang lalu
    now = datetime.datetime.now()
    one_month_ago = now - datetime.timedelta(days=30)
    
    print(f"Mulai proses pembersihan file di: {base_path}")

    # Iterasi melalui semua file di direktori
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)
        
        # Memastikan itu adalah file dan bukan direktori
        if os.path.isfile(file_path):
            # Waktu modifikasi terakhir file
            mod_time = os.path.getmtime(file_path)
            # Konversi waktu modifikasi ke objek datetime
            mod_datetime = datetime.datetime.fromtimestamp(mod_time)

            # Periksa apakah file lebih sudah terdapat lebih dari 1 bulan
            if mod_datetime < one_month_ago:
                try:
                    os.remove(file_path)
                    print(f"File lama berhasil dihapus: {file_name}")
                except Exception as e:
                    print(f"Gagal menghapus file {file_name}: {e}")

if __name__ == "__main__":
    cleanse_data()