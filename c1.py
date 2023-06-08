



import os
import datetime

def delete_old_files(directory):
    current_date = datetime.datetime.now()
    three_months_ago = current_date - datetime.timedelta(days=3*30)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if creation_time < three_months_ago:
            os.remove(file_path)
            print(f"Deleted file: {filename}")
directory_path = "dir/log"
delete_old_files(directory_path)




