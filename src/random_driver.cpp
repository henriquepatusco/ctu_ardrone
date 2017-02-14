#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdlib.h>

int main(int argc, char **argv) 
{
	ros::init(argc,argv,"random_ardrone_commands");
	ros::NodeHandle nh;

	ros::Publisher pub=nh.advertise<geometry_msgs::Twist>("/cmd_vel",10);

	while(ros::ok()){
	geometry_msgs::Twist msg1;
	geometry_msgs::Twist msg2;
	msg1.angular.z=0.5;
	msg2.angular.z=-0.5;
	pub.publish(msg1);
	ros::Duration(1).sleep();
	pub.publish(msg2);
	ros::Duration(1).sleep();
	}
}
