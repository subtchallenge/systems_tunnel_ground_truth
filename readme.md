# README #

This repo provides data for the DARPA Subterranean Challenge Tunnel Circuit, including:

* ground truth data for Artifact types and locations\

* point cloud scans of the Experimental and Safety Research mines/courses at NIOSH in Pittsburgh, Pennsylvania

### Files ###

* Tunnel_Artifact_Ground_Truth.xlsx -- Spreadsheet listing each Artifact; its type; and x,y,z location in the relevant DARPA coordinate frame for each course (Experimental / Safety Research) and configuration (A / B).

* Tunnel_Artifact_Map.pdf -- Pdf format map showing approximate Artifact locations within each course.
    * Notes: 
        * Numbers next to yellow star icons on the map correspond to "Location #" in the Tunnel_Artifact_Ground_Truth.xlsx file.  
        * Map geometry, blockages, and relative dimensions are approximate.
        * Tunnel blockages and other course configurations are notionally represented in this map and are not necessarily indicative of the actual configuration.

* Tunnel_Fiducials_Ground_Truth.xlsx -- Spreadsheet listing reference frame fiducials for each course and a transformation matrix for each that approximately aligns the DARPA frame with UTM.

* Tunnel_Circuit_LowRes_Scan_EX_Frame.pcd -- Point cloud of the EX and SR courses, defined in the DARPA Cartesian coordinate frame for the Experimental course.

### Course Visualization in RViz ###

The two courses may be visualized as point clouds with artifact markers using ROS and RViz. This package depends on ROS and the `pcl_ros` package to build.

To visualize the point clouds and artifact locations, run `roslaunch tunnel_ground_truth view.launch`. Pass with arguments, e.g., `course:=ex config:=a` to visualize artifact locations for a particular course and configuration. Course may be `ex` or `sr`. Config may be `a` or `b`.

# Note on Coordinate Transforms #

Surveyed scan data is provided in a single file for both courses.
When using the *view.launch* file, the point cloud is provided in the `ex`
coordinate frame with transformations between `ex`, `sr`, and `utm` frames provided
on the */tf_static* ROS topic. These coordinate frames are defined as follows:

* `ex` = the DARPA Cartesian coordinate frame for the Experimental course

* `sr` = the DARPA Cartesian coordinate frame for the Safety Research course

* `utm` = a Cartesian coordinate frame, defined by UTM zone 17N


