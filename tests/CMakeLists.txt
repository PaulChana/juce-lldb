cmake_minimum_required (VERSION 3.20 FATAL_ERROR)

set (CMAKE_CXX_STANDARD 17)
set (CMAKE_XCODE_GENERATE_SCHEME ON CACHE BOOL INTERNAL FORCE)
set (CMAKE_OSX_ARCHITECTURES "arm64;x86_64"
     CACHE STRING "macOS universal binary architecture defines")
set (CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
set (CMAKE_OSX_DEPLOYMENT_TARGET 11.1 CACHE STRING "Minimum macOS version"
                                            FORCE)
set (CMAKE_XCODE_ATTRIBUTE_SUPPORTED_PLATFORMS macosx CACHE STRING
                                                            "Build for macos")
set (CMAKE_XCODE_ATTRIBUTE_SDKROOT macosx CACHE STRING "Build for macos")

project ("Juce LLDB" LANGUAGES CXX)

set(CPM_DOWNLOAD_VERSION 0.36.0)

if(CPM_SOURCE_CACHE)
  set(CPM_DOWNLOAD_LOCATION "${CPM_SOURCE_CACHE}/cpm/CPM_${CPM_DOWNLOAD_VERSION}.cmake")
elseif(DEFINED ENV{CPM_SOURCE_CACHE})
  set(CPM_DOWNLOAD_LOCATION "$ENV{CPM_SOURCE_CACHE}/cpm/CPM_${CPM_DOWNLOAD_VERSION}.cmake")
else()
  set(CPM_DOWNLOAD_LOCATION "${CMAKE_BINARY_DIR}/cmake/CPM_${CPM_DOWNLOAD_VERSION}.cmake")
endif()

get_filename_component(CPM_DOWNLOAD_LOCATION ${CPM_DOWNLOAD_LOCATION} ABSOLUTE)
if(NOT (EXISTS ${CPM_DOWNLOAD_LOCATION}))
  message(STATUS "Downloading CPM.cmake to ${CPM_DOWNLOAD_LOCATION}")
  file(DOWNLOAD
          https://github.com/cpm-cmake/CPM.cmake/releases/download/v${CPM_DOWNLOAD_VERSION}/CPM.cmake
          ${CPM_DOWNLOAD_LOCATION})
endif()

include(${CPM_DOWNLOAD_LOCATION})

cpmaddpackage("gh:juce-framework/JUCE#7.0.5")
message(STATUS "JUCE_SOURCE_DIR: ${JUCE_SOURCE_DIR}")
juce_add_console_app(lldbtest VERSION 1.0.0)
juce_generate_juce_header(lldbtest)
target_sources (lldbtest
        PRIVATE
        LLDBTest.cpp)
target_include_directories(lldbtest
        PRIVATE
        ${JUCE_SOURCE_DIR}/modules)
target_compile_definitions(lldbtest
        PRIVATE
        DONT_SET_USING_JUCE_NAMESPACE=1
        JUCE_GLOBAL_MODULE_SETTINGS_INCLUDED=1
        $<IF:$<CONFIG:DEBUG>,DEBUG=1 _DEBUG=1,NDEBUG=1 _NDEBUG=1>)
target_link_libraries(lldbtest
        PRIVATE
        juce::juce_core
        juce::juce_graphics
        juce::juce_gui_basics)
#target_compile_features(lldbtest INTERFACE cxx_std_17)
#
#        JUCE_WEB_BROWSER=0
#        JUCE_USE_CURL=0
#        JUCE_ENABLE_LIVE_CONSTANT_EDITOR=0
#        JUCE_USE_WIN_WEBVIEW2=0
#        JUCE_DISPLAY_SPLASH_SCREEN=0
#        JUCE_REPORT_APP_USAGE=0
#        JUCE_DONT_DECLARE_PROJECTINFO=1
#        JUCE_DISABLE_JUCE_VERSION_PRINTING=1
#
#        NOMINMAX=1
#        JUCE_GLOBAL_MODULE_SETTINGS_INCLUDED=1)
#
#set_target_properties (lldbtest PROPERTIES CXX_STANDARD 17 CXX_EXTENSIONS OFF)
#
#if (APPLE)
#  target_compile_definitions (
#    lldbtest PUBLIC $<IF:$<CONFIG:Debug>,_DEBUG=1,_NDEBUG=1>
#                    $<IF:$<CONFIG:Debug>,DEBUG=1,NDEBUG=1>)
#
#  target_compile_options (
#    lldbtest
#    PRIVATE -Wall
#            -Wextra
#            -Wshadow
#            -Werror
#            -Wreorder
#            -Wstring-conversion
#            -Wimplicit-int-float-conversion
#            -Wnon-virtual-dtor
#            -Wunused-private-field
#            $<IF:$<CONFIG:Debug>,-DDEBUG,-DNDEBUG>
#            $<$<CONFIG:Release>:-DRELEASE>)
#endif ()
#if (MSVC)
#  target_compile_options (
#    lldbtest
#    PRIVATE $<IF:$<CONFIG:Debug>,/Od,/Ox>
#            $<$<CONFIG:Release>:/O2>
#            /W4
#            /WX
#            /MP)
#
#  target_link_options (lldbtest PRIVATE $<$<CONFIG:Release>:/MAP>
#                       $<$<CONFIG:Release>:/DEBUG:FULL>)
#endif ()
