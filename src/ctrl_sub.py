import roslib
import rospy


from ardrone_autonomy.msg import Navdata
from geometry_msgs.msg import Twist


class AR_Drone:

#Here we define the publisher and subscriber attributes for the Object, 
#and also initialize it with the reference parameters 
  def __init__(self):
    self.subNav=rospy.Subscriber('/ardrone/navdata', Navdata,self.ReceiveData)
    self.pubctrl=rospy.Publisher('cmd_vel',Twist,queue_size=1000)
    self.yaw = yaw_ref
    self.xpos = x_ref
    self.ypos = y_ref

#Here we define the CallBack function, which will be called everytime
#the subscribed topic '/ardrone/navdata' is published. The CB function
#will actualize the position data of the Drone
  def ReceiveData(self,data):
    if data.tags_orientation == ():
      self.yaw = yaw_ref
      self.xpos = x_ref
      self.ypos = y_ref
    else:
      self.yaw = data.tags_orientation[0]
      self.xpos = data.tags_xc[0]
      self.ypos = data.tags_yc[0]
  
#references which will be used to setup the object
yaw_ref=90
x_ref=450
y_ref=400

#Here we initialize this Node
rospy.init_node('ctrl_sub')



#Define Rate of Publishing Messages
r = rospy.Rate(200)


#Create the AR Object from the class AR_Drone
AR=AR_Drone()


#While ROS is working, we get the actual coordinates and compare with the referenceses obtaining the errors. So, we normalize this error to fit the [-1, 1] range that we can send to the AR Drone. Also, we define the Gain of the Proportional Controller.
while not rospy.is_shutdown():

#actual coordinates
  yaw=AR.yaw
  x=AR.xpos
  y=AR.ypos

#Normalized errors [-1,1]
  u_yaw=(yaw-yaw_ref)/360
  u_x=(x-x_ref)/450
  u_y=(y-y_ref)/450

#Proportional Gain
  k=1

  print (yaw,x,y)


#Create and Publish the Control Messages
  msg_xpos=Twist()
  msg_xpos.linear.x=(u_x)*k
  AR.pubctrl.publish(msg_xpos)

  msg_ypos=Twist()
  msg_ypos.linear.y=(u_y)*k
  AR.pubctrl.publish(msg_ypos)

  msg_yaw=Twist()
  msg_yaw.angular.z=(u_yaw)*k
  AR.pubctrl.publish(msg_yaw)





