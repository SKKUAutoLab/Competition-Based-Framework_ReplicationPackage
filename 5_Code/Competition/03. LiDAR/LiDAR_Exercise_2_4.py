# LiDAR Lib
import Lib_LiDAR as LiDAR

if (__name__ == "__main__"):
    env = LiDAR.libLidar('COM4')
    env.init()

    count = 0

    for scan in env.scanning():

        print('%d: Got %d measurments' % (count, len(scan)))
        if count == 29:
            env.setRPM(1000)
            break

        count += 1
