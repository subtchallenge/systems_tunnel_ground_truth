#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA

rospy.init_node('artifact_markers')

marker_pub = rospy.Publisher('artifact_markers', MarkerArray, queue_size=1)

artifacts = rospy.get_param('artifacts/artifacts')
frame_id = rospy.get_param('artifacts/frame_id', 'darpa')
color = rospy.get_param('artifacts/marker_color', [0.0, 0.7, 0.7])
name_scale = rospy.get_param('~name_scale', 3.0)
cube_scale = rospy.get_param('~cube_scale', 1.0)
sphere_radius = rospy.get_param('~sphere_radius', 5.0)
floor_threshold = rospy.get_param('~floor_threshold', -0.2)


marker_color = ColorRGBA()
marker_color.r = color[0]
marker_color.g = color[1]
marker_color.b = color[2]
marker_color.a = 1

artifacts_marker = MarkerArray()

now = rospy.Time.now()

index = 0

if artifacts is not None and isinstance(artifacts, list):
    for a in artifacts:
        rospy.logdebug(a)
        (x, y, z) = a['position']

        #################
        # Add cube marker
        cube = Marker()
        cube.header.frame_id = frame_id
        cube.header.stamp = now
        
        if (z<floor_threshold):
            cube.ns = 'artifact_cubes/lower'
        else:
            cube.ns = 'artifact_cubes/upper'

        cube.id = index
        cube.action = Marker.ADD
        cube.pose.position.x = x
        cube.pose.position.y = y
        cube.pose.position.z = z
        cube.pose.orientation.w = 1

        cube.color = marker_color

        cube.scale.x = cube.scale.y = cube.scale.z = 1.0

        cube.type = Marker.CUBE
        cube.frame_locked = True

        artifacts_marker.markers.append(cube)

        #################
        # Add name marker

        name = Marker()
        name.header.frame_id = frame_id
        name.header.stamp = now

        if (z<floor_threshold):
            name.ns = 'artifact_names/lower'
        else:
            name.ns = 'artifact_names/upper'
 
        name.id = index
        name.action = Marker.ADD
        name.scale.z = name_scale            
        name.pose.position.x = x
        name.pose.position.y = y - name_scale
        name.pose.position.z = z
        name.pose.orientation.w = 1

        name.color = marker_color

        name.type = Marker.TEXT_VIEW_FACING
        name.frame_locked = True

        name.text = a['type']

        index = index + 1
          
        artifacts_marker.markers.append(name)
        
        #################
        # Add sphere marker
        sphere = Marker()
        sphere.header.frame_id = frame_id
        sphere.header.stamp = now
       
        if (z<floor_threshold):
            sphere.ns = 'artifact_spheres/lower'
        else:
            sphere.ns = 'artifact_spheres/upper'
        
        sphere.id = index
        sphere.action = Marker.ADD
        sphere.pose.position.x = x
        sphere.pose.position.y = y
        sphere.pose.position.z = z
        sphere.pose.orientation.w = 1

        sphere.color = marker_color
        sphere.color.a = 0.35

        sphere.scale.x = sphere.scale.y = sphere.scale.z = 2 * sphere_radius

        sphere.type = Marker.SPHERE
        sphere.frame_locked = True
       
        artifacts_marker.markers.append(sphere)


while not rospy.is_shutdown():

    marker_pub.publish(artifacts_marker)

    rospy.sleep(0.5)
        
        
            
        

