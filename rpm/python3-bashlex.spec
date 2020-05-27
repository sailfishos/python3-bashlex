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
python3 -c 'import bashlex'
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/bashlex
%{python3_sitelib}/bashlex-*.egg-info/

