from controller import Robot, DistanceSensor, Motor, Lidar, Camera 
TIME_STEP=32

# robot instance.
robot = Robot()

# motors 
leftMotor = robot.getDevice('left_wheel_joint')
rightMotor = robot.getDevice('right_wheel_joint')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)


# lidar 
lidar = robot.getDevice('rplidar') 
lidar.enable(TIME_STEP)

# bumper 
bumper_fc = robot.getDevice('bump_front_center') 
bumper_fc.enable(TIME_STEP)

bumper_fcr = robot.getDevice('bump_front_center_right') 
bumper_fcr.enable(TIME_STEP)


# camera 
camera = robot.getDevice('rgb_camera')
camera.enable(TIME_STEP)

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:

    leftMotor.setVelocity(1.0)
    rightMotor.setVelocity(1.0)
    
    #get LiDAR ranges 
    ranges = lidar.getRangeImage()
    
    #get camera image 
    #image is coded as a sequence of four bytes representing the blue, green, red and alpha levels of a pixel.
    img = camera.getImage() 
    
    bp = [bumper_fc.getValue(), bumper_fcr.getValue()] 
    print(bp)
    
    # read sensors outputs
    # process behavior
    # write actuators inputs