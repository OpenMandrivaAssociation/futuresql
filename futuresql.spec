Name: futuresql
Version: 0.1.1
Release: 1
Source0: https://download.kde.org/stable/futuresql/futuresql-%{version}.tar.xz
#Source0: https://invent.kde.org/libraries/futuresql/-/archive/%{version}/futuresql-%{version}.tar.bz2
Summary: Non-blocking database framework for Qt
URL: https://api.kde.org/futuresql/html/index.html
License: LGPL-2.1 or LGPL-3.0
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(QCoro5Core)
BuildRequires: cmake(QCoro5)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(QCoro6Core)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(ECM)

%description
A non-blocking database framework for Qt.

FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access
by default, relatively boilderplate-free queries, automatic database
migrations and simple mapping to objects.

In order to make FutureSQL's use of templates less confusing, FutureSQL
uses C++20 concepts, and requires a C++20 compiler.

%prep
%autosetup -p1
%cmake \
	-DQT_MAJOR_VERSION=5 \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build6
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%build
%ninja_build -C build
%ninja_build -C build6

%install
%ninja_install -C build
%ninja_install -C build6

%libpackages

for v in 5 6; do
	cat >>%{specpartsdir}/%{mklibname -d futuresql$v}.specpart <<EOF
%{_includedir}/FutureSQL$v
%{_libdir}/cmake/FutureSQL$v
EOF
done
