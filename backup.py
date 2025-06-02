import schedule as SH
import time
import os
import shutil
import datetime as DT
import zipfile

def job():
    
    timestamp = DT.datetime.now().strftime("%y.%m.%d_%H.%M")
    print ("I'm Working...")
    file = "Your_folder_where_are_all_files_you_want_to_backup"
    fileTo = "Your_destination_pathFolder" 
    filezip = "backup_" + timestamp + ".zip"
    srcpath = file + "\\" + filezip
    try:
        files = os.listdir(file)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Acces error: {e}")
        return
    with zipfile.ZipFile(filezip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for x in files:
            #For testing i was using same folder to containt files and backup folder. You can ignore it.
            if x != "backup":
                if os.path.exists(x):
                    zipf.write(x, os.path.basename(x))
                    print (f"Added {x} to Zip")
                else:
                    print (f"Lack of file {x}")
        print (f"I've created zip file {filezip}")
        
    shutil.move(srcpath, fileTo)


    #Here was part for copying every file by file to other folder, but i've decided ZIP is far more suitable. You can ignore or delete this part. 
    #print (files)
    #for x in files:
    #    dst_path = os.path.join(fileTo, f"{timestamp}_{x}")
    #    if x == "backup":
    #        continue
    #    shutil.copy(x, dst_path)
    #print ("Skończyłem.")
    

SH.every(30).seconds.do(job)


while True:
    try:
        SH.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print ("Zatrzymano ręcznie.")
        exit()