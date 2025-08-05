import Lib_LiDAR as LiDAR

if (__name__ == "__main__"):
    env = LiDAR.libLidar('COM3')

    env.init()
    count = 0
    env.setRPM(1000)

    for scan in env.scanning():
        count += 1
        #scan = env.get_far_distance(scan, 60, 150)
        #print(scan)
        scan = env.get_near_distance(scan, 60, 150)
        print(scan)
        if count == 100:
            env.stop()
            break
