import os

#pyngrok yukle
os.system('pip install pyngrok')

#github klonla
os.system('git clone https://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@github.com/SezerBugday/photogrammetry_meshroom_colab_flask.git')

# meshroom dosyalarını sunucuya dahil et
os.system("wget -N https://github.com/alicevision/meshroom/releases/download/v2019.1.0/Meshroom-2019.1.0-linux.tar.gz")
os.system("mkdir meshroom")
os.system("tar xzf Meshroom-2019.1.0-linux.tar.gz -C ./meshroom")


#arka plan kaldıran kutuphane
os.system("sudo apt install ffmpeg python3.6-dev")
os.system("pip install --upgrade pip")
os.system("pip install backgroundremover")


os.system("mkdir Uploads")
os.system("mkdir OutputFile")