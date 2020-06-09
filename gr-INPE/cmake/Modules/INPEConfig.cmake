INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_INPE INPE)

FIND_PATH(
    INPE_INCLUDE_DIRS
    NAMES INPE/api.h
    HINTS $ENV{INPE_DIR}/include
        ${PC_INPE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    INPE_LIBRARIES
    NAMES gnuradio-INPE
    HINTS $ENV{INPE_DIR}/lib
        ${PC_INPE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/INPETarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(INPE DEFAULT_MSG INPE_LIBRARIES INPE_INCLUDE_DIRS)
MARK_AS_ADVANCED(INPE_LIBRARIES INPE_INCLUDE_DIRS)
