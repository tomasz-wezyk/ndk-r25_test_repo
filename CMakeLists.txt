######################## Copied from glog's main CMakeLists.txt:
cmake_minimum_required (VERSION 3.0)

if (POLICY CMP0042)
  cmake_policy (SET CMP0042 NEW)
endif (POLICY CMP0042)

if (POLICY CMP0063)
  cmake_policy (SET CMP0063 NEW)
endif (POLICY CMP0063)

#######################



project(test LANGUAGES C CXX)

include (CheckIncludeFile)

check_include_file(execinfo.h HAVE_EXECINFO_H)

if (HAVE_EXECINFO_H)
    message(FATAL_ERROR "Execinfo enabled")
else()
    message("Execinfo not enabled")
endif()
