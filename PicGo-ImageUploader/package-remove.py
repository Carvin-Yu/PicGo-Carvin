import os
import shutil

try:
    os.remove("imageUploader.spec")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
except:
    pass

os.system("taskkill /F /IM imageUploader.exe")
print("Success package-remove!")