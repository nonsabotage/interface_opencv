import cv2
import numpy as np

if __name__ == "__main__":
    print(f"cv2 version is {cv2.__version__}")

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    # 直線の描画
    cv2.ellipse(
        img = img, 
        center = (300, 200), 
        axes   = (100, 50), 
        angle  = 0, # 傾き角度
        startAngle = 0, # 描画の開始角度
        endAngle  = 300, # 描画の終了角度（閉じない）
        color     = color, 
        thickness = -1, # 塗りつぶし
        lineType  = cv2.LINE_AA, # アンチエイリアス
    )
    cv2.ellipse(
        img = img, 
        center = (300, 200), 
        axes   = (300, 100), 
        angle  = 340, # 傾き角度
        startAngle = 0, # 描画の開始角度
        endAngle  = 360, # 描画の終了角度
        color     = color, 
        thickness = 2, 
        lineType  = cv2.LINE_AA, # アンチエイリアス
    )


    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
