import cv2
import numpy as np

'''
プログラムで処理したの画像表示のベースとなるプログラム
'''

if __name__ == "__main__":

    size = np.array([720, 1280, 3])

    # GBRで色を指定する. 
    redColor = np.array([0., 0., 255.])

    # 形状と値, 値の型を指定して行列を作成する
    # イメージとしては値を少しずつキャストしていくものかな
    # 1x3 -> 1280 x 3 -> 720 x 1280 x 3
    img = np.full(size, redColor, dtype = np.uint8)

    cv2.imshow("Red", img)
    
    # 静止画のときにはwaitは0にしておく
    cv2.waitKey(0)
    cv2.destroyAllWindows()


