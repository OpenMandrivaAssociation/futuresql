Name: futuresql
Version: 0.1
Release: 1
Source0: https://invent.kde.org/libraries/futuresql/-/archive/%{version}/futuresql-%{version}.tar.bz2
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
BuildRequires: cmake(ECM)

%description
A non-blocking database framework for Qt.

FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access
by default, relatively boilderplate-free queries, automatic database
migrations and simple mapping to objects.

In order to make FutureSQL's use of templates less confusing, FutureSQL
uses C++20 concepts, and requires a C++20 compiler.

%define libname %mklibname futuresql5
%define devname %mklibname -d futuresql5

%package -n %{libname}
Summary: Non-blocking database framework for Qt
Group: System/Libraries

%description -n %{libname}
A non-blocking database framework for Qt.

FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access
by default, relatively boilderplate-free queries, automatic database
migrations and simple mapping to objects.

In order to make FutureSQL's use of templates less confusing, FutureSQL
uses C++20 concepts, and requires a C++20 compiler.

%package -n %{devname}
Summary: Non-blocking database framework for Qt (Development files)
Group: Development/C and C++

%description -n %{devname}
A non-blocking database framework for Qt.

FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access
by default, relatively boilderplate-free queries, automatic database
migrations and simple mapping to objects.

In order to make FutureSQL's use of templates less confusing, FutureSQL
uses C++20 concepts, and requires a C++20 compiler.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libfuturesql5.so*

%files -n %{devname}
%{_includedir}/FutureSQL5
%{_libdir}/cmake/FutureSQL5
