# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build

# Include any dependencies generated for this target.
include src/third-party/CMakeFiles/lodepng.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/third-party/CMakeFiles/lodepng.dir/compiler_depend.make

# Include the progress variables for this target.
include src/third-party/CMakeFiles/lodepng.dir/progress.make

# Include the compile flags for this target's objects.
include src/third-party/CMakeFiles/lodepng.dir/flags.make

src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o: src/third-party/CMakeFiles/lodepng.dir/flags.make
src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o: ../src/third-party/lodepng/lodepng.cc
src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o: src/third-party/CMakeFiles/lodepng.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o"
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o -MF CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o.d -o CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o -c /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/src/third-party/lodepng/lodepng.cc

src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lodepng.dir/lodepng/lodepng.cc.i"
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/src/third-party/lodepng/lodepng.cc > CMakeFiles/lodepng.dir/lodepng/lodepng.cc.i

src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lodepng.dir/lodepng/lodepng.cc.s"
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/src/third-party/lodepng/lodepng.cc -o CMakeFiles/lodepng.dir/lodepng/lodepng.cc.s

# Object files for target lodepng
lodepng_OBJECTS = \
"CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o"

# External object files for target lodepng
lodepng_EXTERNAL_OBJECTS =

src/third-party/liblodepng.a: src/third-party/CMakeFiles/lodepng.dir/lodepng/lodepng.cc.o
src/third-party/liblodepng.a: src/third-party/CMakeFiles/lodepng.dir/build.make
src/third-party/liblodepng.a: src/third-party/CMakeFiles/lodepng.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library liblodepng.a"
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && $(CMAKE_COMMAND) -P CMakeFiles/lodepng.dir/cmake_clean_target.cmake
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lodepng.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/third-party/CMakeFiles/lodepng.dir/build: src/third-party/liblodepng.a
.PHONY : src/third-party/CMakeFiles/lodepng.dir/build

src/third-party/CMakeFiles/lodepng.dir/clean:
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party && $(CMAKE_COMMAND) -P CMakeFiles/lodepng.dir/cmake_clean.cmake
.PHONY : src/third-party/CMakeFiles/lodepng.dir/clean

src/third-party/CMakeFiles/lodepng.dir/depend:
	cd /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/src/third-party /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party /mnt/c/Users/yj6475/Desktop/aesgs/basler/Perception_Project/build/src/third-party/CMakeFiles/lodepng.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/third-party/CMakeFiles/lodepng.dir/depend

