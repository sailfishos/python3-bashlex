# fixme: should be defined in base system side
%define python3_sitelib %(%{__python3} -Ic "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name: python3-bashlex
Summary: Python parser for bash
Version: bashlex
Release: 0.14
License: GPLv3
Group: Development/Languages
URL: https://github.com/idank/bashlex.git
Source0: %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
bashlex is a Python port of the parser used internally by GNU bash.

%prep
%setup -q -n %{name}-%{version}/python-bashlex

%build
%{__python3} -c 'import bashlex'
CFLAGS="%{optflags}" %{__python3} setup.py build %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/bashlex
%{python3_sitelib}/bashlex-*.egg-info/

