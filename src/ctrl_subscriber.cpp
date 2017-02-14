#include "ros/ros.h" 
#include "ardrone_autonomy/Navdata.h"
#include "std_msgs/String.h"

class CB
{
public:
  void ctrlCB(const ardrone_autonomy::Navdata data)
    {
      ROS_INFO("[%f]",data.tags_orientation[0]);
    };
};


int main(int argc,char **argv)
{

ros::init(argc,argv,"ctrl_subscriber");
ros::NodeHandle n;

CB CBobject;
ros::Subscriber sub = n.subscribe("ardrone/navdata", 1000, &CB::ctrlCB,&CBobject);

ros::spin();

return 0;
}

