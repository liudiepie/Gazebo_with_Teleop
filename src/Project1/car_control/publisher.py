#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64




if __name__=="__main__":

    
    rospy.init_node('ConstantSpeed')
    rate = rospy.Rate(10)

    pub_moveBR = rospy.Publisher('/simple_car/BackRight_Control/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    pub_moveBL = rospy.Publisher('/simple_car/BackLeft_Control/command', Float64, queue_size=10)
   
    




    try:
        while not rospy.is_shutdown():
            pub_moveBR.publish(-10)
            pub_moveBL.publish(-10)
            rospy.loginfo("The speed is -10 %s" % rospy.get_time())
            rate.sleep()


    except:
        print (e)

    finally:

        pub_moveBR.publish(-10)
        pub_moveBL.publish(-10)


