import datetime
import os
import time

def collect_data():
    #Path direktori tempat untuk menyimpan file
    base_path = '/home/cron'
    # Format tanggal dan jam sesuai dengan waktu saat ini
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    time_str = datetime.datetime.now().strftime('%H_%M')
    file_name = f'cron_{date_str}_{time_str}.csv'
    file_path = os.path.join(base_path, file_name)


    # Contoh data yang akan dikumpulkan
    data_to_write = f"Timestamp,Data\n{datetime.datetime.now().isoformat()},Fauzan Fajar Saputra!."
    
    try:
        with open(file_path, 'w') as f:
            f.write(data_to_write)
        print(f"Data berhasil dikumpulkan dan disimpan di: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

if __name__ == "__main__":
    collect_data()