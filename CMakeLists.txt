project(test LANGUAGES CXX)


check_include_file(execinfo.h HAVE_EXECINFO_H)

if (HAVE_EXECINFO_H)
    message(FATAL_ERROR "Execinfo enabled")
else()
    message("Execinfo not enabled")
endif()
