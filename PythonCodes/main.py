import os

#pyngrok yukle
os.system('pip install pyngrok')
#bootsrap yukle
os.system("pip install flask-bootstrap")
#github klonla
os.system('git clone https://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@github.com/SezerBugday/photogrammetry_meshroom_colab_flask.git')

# meshroom dosyalarını sunucuya dahil et
os.system("wget -N https://github.com/alicevision/meshroom/releases/download/v2019.1.0/Meshroom-2019.1.0-linux.tar.gz")
os.system("mkdir meshroom")
os.system("tar xzf Meshroom-2019.1.0-linux.tar.gz -C ./meshroom")


#arka plan kaldıran kutuphane

os.system("pip install rembg")
os.system("pip install easygui")
#ghdccccccccccccccccccccccccccccccccccccccccccccccccccggggggggggg#

os.system("mkdir temiz")
os.system("mkdir kirli")

# obj to glb için kütüphane

os.system("npm install -g obj2gltf")
