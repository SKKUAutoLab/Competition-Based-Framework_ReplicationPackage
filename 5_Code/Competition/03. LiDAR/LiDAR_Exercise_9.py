# LiDAR Lib

import Lib_LiDAR as LiDAR
import cv2

if (__name__ == "__main__"):
    env = LiDAR.libLidar('COM22')
    env.init()
    count = 0
    env.setRPM(1000)

    for scan in env.scanning():

        # LiDAR 처음 동작 시
        if count == 0:
            scan = env.get_near_distance(scan, 150, 210)
            pre_data = scan[1]

            count = count + 1

        else:
            scan = env.get_near_distance(scan, 150, 210)
            scan_data = scan[1]

            print('--------------------------------')
            print('previous data is %d' % pre_data)
            print('scan data is %d' % scan_data)

            move = pre_data - scan_data

            # 1mm 이상 전진하여야 움직인걸로 가정
            if 1 < move:
                print('Front')
            # 1mm 이상 후진하여야 움직인걸로 가정
            elif move < -1:
                print('Rear')
            else:
                print('Mid')

            pre_data = scan[1]

        # q 를 누르면 프로그램 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            env.stop()
            break
