# Pythonによる画像処理100

- Interface, 2021, No.1

GPU版のプログラムも提供されているが，
opencvをソースからビルドする必要があり難しそうなので
ここでは大人しくCPU版を活用する．

GPU版のプログラムをざっとみた限り，
プログラム自体はそこまで難しくなさそう．
基本的にGPUへデータを転送して，GPUで処理して，CPUに返すというもの. 
関数もプレフィクスとして`cuda`がつくだけ. 


## サンプルプログラム

基本的には./docs/IF2101T/CQProjectBasics_1に基礎編の画像処理プログラムがある. 
サポートベージからダウンロードが可能である．
著作権等の問題もあるかもしれないがそもそも重たいためGitは使えない. 

## 環境について

- pythonは3.6にすること
- python fileで実行すること
    - ipythonやjupyterからだと動作がおかしいことがる



## 作業メモ

### 準備
- opencv-pythonはpipからインストール
- opencvで動画や画像を表示するにはフレームごとに読み込んで出力というループ
- クリック等で止めることは出来ないのかな？
    - 特段設定していなくてもWindowsをアクティブにしてqを押すと止まる
- GPUでの処理は繰り返しがない場合などでは効果を得られないこともある.
- 画像処理の場合，データをBGRのまま扱うことは少なく，グレースケールに変換したりする


# プログラムの解説

## 画像の下準備

- 01_CameraBase.py
    - USBカメラ等を想定してビデオキャプチャーを行う
- 02_VideoBase.py
    - 動画ファイルを想定してビデオキャプチャーをおこなう
    - `waitKeyEx`は引数にミリ秒を取る
        - その時間，停止することで画像更新のループが止まる
- 03_matbase.py
    - プログラムから作成したファイルを表示
    - 静止画は`waitKey(0)`とすれば表示することが出来る
- 04_CudaBase.py
    - gpu用のプログラムのため動かない
    - opencvでgpuを使うにはCUDA support込みでコンパイルする必要がある
- 05_Gray.py
    - 画像のグレースケール化
- 06_Binary.py
    - カラーとグレー画像の２値化
    - カラー画像を２値化しても意味がなく，グレースケールを挟む必要がある
    - 2値の種類としては次がある
        - cv2.TRESH_BINARY
        - cv2.TRESH_BINARY_INV
        - cv2.TRESH_BINARY + cv2.TRESH_OTHU
        - cv2.TRESH_BINARY + cv2.TRESH_TRIANGLE
        - cv2.TRESH_TOZERO_INV
- 07_Binary_Tozero_inv.py
    - cv2.TRESH_TOZERO_INVを利用
        - 閾値以下の値は残り，それ以外は０
        - 赤(0, 0, 255)を128を閾値にすると(0, 0, 0)になる
- 08_Binary_TRUN.py
    - 私の環境にはTHRESH_TRUNなどないのでTHRESH_TRUNCを使った

> [x for x in dir(cv2) if re.match("THRESH", x)]
> Out[7]: 
> ['THRESH_BINARY',    
>  'THRESH_BINARY_INV',
>  'THRESH_MASK',      
>  'THRESH_OTSU',      
>  'THRESH_TOZERO',    
>  'THRESH_TOZERO_INV',
>  'THRESH_TRIANGLE',
>  'THRESH_TRUNC']

- 12_Separation.py
    - GBR画像を画層ごとに分割
    - cv2.cplit


