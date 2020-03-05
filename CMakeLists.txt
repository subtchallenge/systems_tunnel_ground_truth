cmake_minimum_required(VERSION 2.8.3)
project(tunnel_ground_truth)

set(PKG_DEPENDS
  pcl_ros
  )
set(BUILD_DEPENDS
  ${PKG_DEPENDS}
  )
set(RUN_DEPENDS
  ${PKG_DEPENDS}
  )

#######################################
## Find dependencies
#######################################

find_package(Boost REQUIRED COMPONENTS system filesystem thread)

find_package(PCL REQUIRED COMPONENTS core features filters io segmentation surface)

if(NOT "${PCL_LIBRARIES}" STREQUAL "")
  # For debian: https://github.com/ros-perception/perception_pcl/issues/139
  list(REMOVE_ITEM PCL_LIBRARIES
    "vtkGUISupportQt"
    "vtkGUISupportQtOpenGL"
    "vtkGUISupportQtSQL"
    "vtkGUISupportQtWebkit"
    "vtkViewsQt"
    "vtkRenderingQt")
endif()
if(NOT "${PCL_INCLUDE_DIRS}" STREQUAL "")
  foreach(item ${PCL_INCLUDE_DIRS})
    string(REGEX MATCH "/usr/include/.*-linux-gnu/freetype2" item ${item})
    if(item)
      list(REMOVE_ITEM PCL_INCLUDE_DIRS ${item})
    endif()
  endforeach()
endif()

find_package(catkin REQUIRED ${BUILD_DEPENDS})

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}

  )

#######################################
## Declare Catkin package and installation
#######################################

catkin_package(
  CATKIN_DEPENDS ${RUN_DEPENDS}
  DEPENDS
   PCL
  )


add_executable(load_pcd src/load_pcd.cpp)
target_link_libraries(load_pcd ${Boost_LIBRARIES} ${catkin_LIBRARIES} ${PCL_LIBRARIES})
