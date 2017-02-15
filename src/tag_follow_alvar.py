import roslib
import rospy


from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist


class AR_Drone:

#Here we define the publisher and subscriber attributes for the Object, 
#and also initialize it with the reference parameters 
  def __init__(self):
    self.subNav=rospy.Subscriber('/ar_pose_marker', AlvarMarkers,self.ReceivePose)
    self.pubctrl=rospy.Publisher('cmd_vel',Twist,queue_size=1)
    self.yaw = yaw_ref
    self.dist = dist_ref




#Here we define the CallBack function, which will be called everytime
#the subscribed topic '/ardrone/navdata' is published. The CB function
#will actualize the position data of the Drone
  def ReceivePose(self,data):
    if data.markers == []:
      self.yaw = 0
      self.dist =0.5
    else:
      self.yaw = data.markers[0].pose.pose.position.x
      self.dist = data.markers[0].pose.pose.position.z

  
#references which will be used to setup the object
yaw_ref=0
dist_ref=0.5


#Here we initialize this Node
rospy.init_node('ctrl_sub')



#Create the AR Object from the class AR_Drone
AR=AR_Drone()
msg_dist=Twist()
msg_yaw=Twist()


#While ROS is working, we get the actual coordinates and compare with the referenceses obtaining the errors. So, we normalize this error to fit the [-1, 1] range that we can send to the AR Drone. Also, we define the Gain of the Proportional Controller.
while not rospy.is_shutdown():

#actual coordinates
  yaw=AR.yaw
  dist=AR.dist


#Normalized errors [-1,1]

  u_yaw=(yaw_ref-yaw)/0.3
  u_dist=(dist-dist_ref)/0.3


#Proportional Gain
  k=1

  print (yaw,dist)


#Publish the Control Messages


  msg_yaw.angular.z=(u_yaw)*k
  AR.pubctrl.publish(msg_yaw)


  msg_dist.linear.x=(u_dist)*k
  AR.pubctrl.publish(msg_dist)









