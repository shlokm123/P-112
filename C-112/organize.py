import os
import shutil
from_dir ="C:/Users/Asus/Downloads"
to_dir = "C:/Users/Asus/OneDrive/Desktop/Python"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for f in list_of_files:
    name,extension = os.path.splitext(f)
    if extension == '':
        continue
    if extension in ['.doc','.docx','.pdf','.txt']:
        path1 = from_dir + '/' + f
        path2 = to_dir + '/' + "imagefile"
        path3 = to_dir + '/' + "imagefile" + '/' + f
        print("moving")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving")
        shutil.move(path1,path3)
