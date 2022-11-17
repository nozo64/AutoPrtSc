import time
import os
import datetime

import pyautogui
import img2pdf
from PIL import Image

#########################
# 変数定義
# (環境に応じて変更する)
#########################

# ページ数
total_pages = 5
# 取得範囲：左上座標
x1, y1 = 0, 0
# 取得範囲：右下座様
x2, y2 = 960, 540
# 開始準備時間(秒)
prep_time = 5
# スクショ間隔(秒)
interval = 1
# 出力フォルダ頭文字
dir_prefix = "output"
# 出力ファイル頭文字
file_prefix = "picture"

#########################
# 処理開始
#########################

# 待機時間
# (この間にスクショを取得するウィンドウをアクティブにする)

print(f'Please activate your target window in {prep_time} seconds!')
time.sleep(prep_time)

print('start!')

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
img_ext = ".png"
out_dir = dir_prefix + "_" + str(
    datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

os.mkdir(out_dir)

# ページ数分スクリーンショットをとる
for p in range(total_pages):

    page = str(p + 1).zfill(4)
    print(f'page {page}')

    # 出力ファイル名(頭文字_連番.png)
    out_filename = file_prefix + "_" + page + img_ext
    # スクリーンショット取得・保存
    s = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    s.save(out_dir + '/' + out_filename)
    # 右矢印キー押下
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    # 次のスクリーンショットまで待機
    time.sleep(interval)

# PDFに変換
pdf_fiename = out_dir + '/' + file_prefix + '.pdf'
with open(pdf_fiename, "wb") as f:
    f.write(
        img2pdf.convert([
            Image.open(out_dir + '/' + j).filename for j in os.listdir(out_dir)
            if j.endswith(img_ext)
        ]))
