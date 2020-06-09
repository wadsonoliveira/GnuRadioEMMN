INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FLORIPASAT floripasat)

FIND_PATH(
    FLORIPASAT_INCLUDE_DIRS
    NAMES floripasat/api.h
    HINTS $ENV{FLORIPASAT_DIR}/include
        ${PC_FLORIPASAT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FLORIPASAT_LIBRARIES
    NAMES gnuradio-floripasat
    HINTS $ENV{FLORIPASAT_DIR}/lib
        ${PC_FLORIPASAT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/floripasatTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FLORIPASAT DEFAULT_MSG FLORIPASAT_LIBRARIES FLORIPASAT_INCLUDE_DIRS)
MARK_AS_ADVANCED(FLORIPASAT_LIBRARIES FLORIPASAT_INCLUDE_DIRS)
