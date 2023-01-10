%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ros2bag
Version:        0.15.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2bag package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-ros2cli
Requires:       ros-humble-rosbag2-py
Requires:       ros-humble-rosbag2-transport
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-ros2cli
BuildRequires:  ros-humble-rosbag2-py
BuildRequires:  ros-humble-rosbag2-transport
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-launch-testing
BuildRequires:  ros-humble-launch-testing-ros
%endif

%description
Entry point for rosbag in ROS 2

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Jan 10 2023 Geoffrey Biggs <geoff@openrobotics.org> - 0.15.4-1
- Autogenerated by Bloom

* Wed Nov 09 2022 Geoffrey Biggs <geoff@openrobotics.org> - 0.15.3-1
- Autogenerated by Bloom

* Wed May 11 2022 Geoffrey Biggs <geoff@openrobotics.org> - 0.15.2-1
- Autogenerated by Bloom

* Wed Apr 20 2022 Geoffrey Biggs <geoff@openrobotics.org> - 0.15.1-2
- Autogenerated by Bloom

* Wed Apr 20 2022 Geoffrey Biggs <geoff@openrobotics.org> - 0.15.1-1
- Autogenerated by Bloom

