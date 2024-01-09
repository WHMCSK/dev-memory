Mac安装ros


1.安装miniconda

https://docs.conda.io/en/latest/miniconda.html#macosx-installers


下载安装3.9就可以
2.终端输入命令安装
comand+space(空格键) 输入ter ，打开终端app
输入以下命令
conda create -n ROS python=3.8
conda activate ROS
conda config --add channels conda-forge
conda config --add channels robostack
conda config --set channel_priority strict
# install asio and tinyxml2 for Fast-RTPS
brew install asio tinyxml2
# install dependencies for robot state publisher
brew install tinyxml eigen pcre poco
# OpenCV isn't a dependency of ROS 2, but it is used by some demos.
brew install opencv
# install OpenSSL for DDS-Security
brew install openssl
# if you are using ZSH, then replace '.bashrc' with '.zshrc'
echo "export OPENSSL_ROOT_DIR=$(brew --prefix openssl)" >> ~/.bashrc
# install Qt for RViz
brew install qt freetype assimp
# install console_bridge for rosbag2
brew install console_bridge
# install dependencies for rcl_logging_log4cxx
brew install log4cxx spdlog
# install CUnit for Cyclone DDS
brew install cunit


Install ros2 doctor dependencies

python3 -m pip install rosdistro

Install rqt dependencies

brew install sip pyqt5


conda install ros-noetic-desktop-full
conda install compilers cmake pkg-config make ninja catkin_tools
conda deactivate
conda activate ros

照着输就行，基本过程就是搞些配置，安装编译啥的，看单词就懂（安装包里有Mysql，qt,pyqt cmake make,等等，无聊有兴趣的可以盯着看看）注意虽然安装的是3.9但是python=3.8，3.9后面conda install ros-noetic-desktop-full 命令会报错

记住conda deactivate
conda activate ros 两条指令，相当于启动退出

试试开搞：
最后（ros）输入 roscore


然后新开一个窗口请添加图片描述
（ros）输入rviz

这个时候风扇会转的像飞驰的摩托车，弹出一个一看就知道是opengl做的框框




