import cv2
import numpy as np

if __name__ == "__main__":
    print(cv2.__version__)

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    # 直線の描画
    cv2.circle(
        img = img, 
        center = (200, 200), 
        radius = 100,
        color = color, 
        thickness = -1, # 塗りつぶし
        lineType  = cv2.LINE_AA, # アンチエイリアス
    )
    cv2.circle(
        img = img, 
         center = (400, 200), 
        radius = 100,
        color = color, 
        thickness = 2,
    )

    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
