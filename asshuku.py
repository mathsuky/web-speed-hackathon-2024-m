import os
import glob
from PIL import Image

# 現在のディレクトリからすべてのサブディレクトリを探す
for dirpath, dirnames, filenames in os.walk('.'):
    # pngまたはjpgファイルを探す
    for filename in glob.glob(os.path.join(dirpath, '*.png')) + glob.glob(os.path.join(dirpath, '*.jpg')):
        # 画像を開く
        img = Image.open(filename)
        # 画像を圧縮する
        img.save(filename, optimize=True, quality=10)
