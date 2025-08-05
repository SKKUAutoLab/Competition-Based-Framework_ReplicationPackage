import Lib_LiDAR as LiDAR

if (__name__ == "__main__"):
    env = LiDAR.libLidar('COM3')

    env.init()
    count = 0
    #env.stop()

    for scan in env.scanning():
        count += 1
        scan = env.revisedgetAngleRange(scan, 330, 30)

        print(scan)
        if count == 100:
            env.stop()
            break
