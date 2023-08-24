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

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
# Leaving the "/" in here is _BAD_, but will generally work [packaging all
# files] for testing.
# Please replace it with an actual file list to prevent your package from
# owning all system directories.
/
