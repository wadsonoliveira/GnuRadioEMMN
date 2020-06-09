# Install script for directory: /home/wadson/gr-INPE/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/INPE" TYPE FILE FILES
    "/home/wadson/gr-INPE/python/__init__.py"
    "/home/wadson/gr-INPE/python/MQTTsink.py"
    "/home/wadson/gr-INPE/python/PDUcounter.py"
    "/home/wadson/gr-INPE/python/MQTT_source.py"
    "/home/wadson/gr-INPE/python/doppler_correction.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/INPE" TYPE FILE FILES
    "/home/wadson/gr-INPE/build/python/__init__.pyc"
    "/home/wadson/gr-INPE/build/python/MQTTsink.pyc"
    "/home/wadson/gr-INPE/build/python/PDUcounter.pyc"
    "/home/wadson/gr-INPE/build/python/MQTT_source.pyc"
    "/home/wadson/gr-INPE/build/python/doppler_correction.pyc"
    "/home/wadson/gr-INPE/build/python/__init__.pyo"
    "/home/wadson/gr-INPE/build/python/MQTTsink.pyo"
    "/home/wadson/gr-INPE/build/python/PDUcounter.pyo"
    "/home/wadson/gr-INPE/build/python/MQTT_source.pyo"
    "/home/wadson/gr-INPE/build/python/doppler_correction.pyo"
    )
endif()

