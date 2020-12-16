import cv2

target_file = "../docs/IF2101T/CQProjectBasics_1/MVI_0182.MP4"


if __name__ == "__main__":

    cap = cv2.VideoCapture(target_file)
    
    # ビデオキャプチャーが可能かを判定
    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Error")
            break

        cv2.imshow("Final result", img)
        
        # 10ミリ秒で画像を更新していく
        # つまり，ループが回る
        if cv2.waitKeyEx(100) > -1:
            break


