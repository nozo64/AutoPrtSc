# AutoPrtSc
Print screen automation and generating pdf.

## Install
`pip install -r requirements.txt`

## Configuration
`auto_prtsc.py`
```
# ページ数
total_pages = 5
# 取得範囲：左上座標
x1, y1 = 100, 0
# 取得範囲：右下座様
x2, y2 = 1920, 1080
# 開始準備時間(秒)
prep_time = 5
# スクショ間隔(秒)
interval = 1
# 出力フォルダ頭文字
dir_prefix = "output"
# 出力ファイル頭文字
file_prefix = "picture"
```

## Execute
`python auto_prtsc.py`

`prep_time`の間に対象ウィンドウをアクティブにする.

以上
　