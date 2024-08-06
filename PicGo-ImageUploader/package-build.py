import os
import shutil

try:
    os.remove("imageUploader.spec")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
except:
    pass

os.system("taskkill /F /IM imageUploader.exe")
os.system(f'pyinstaller --onefile --exclude-module PySide2 -w imageUploader.py')
print("Success package-build!")