
import cv2


if __name__ == "__main__":

    # USBカメラがある場合には0により指定することが出来る
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break

        # 第一引数はタイトル
        cv2.imshow("Final result", img)
        
        # keyの待ち時間の設定(ミリ秒)
        if cv2.waitKey(10) > -1:
            break


    cap.release()
    cv2.destroyAllWindows()

