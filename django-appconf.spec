#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-appconf
Version  : 1.0.3
Release  : 29
URL      : https://files.pythonhosted.org/packages/8e/9e/0cf10dc64e69f553dd1f8d54b8c55c31fb632d60ddcaeab3f21c472005ca/django-appconf-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/9e/0cf10dc64e69f553dd1f8d54b8c55c31fb632d60ddcaeab3f21c472005ca/django-appconf-1.0.3.tar.gz
Summary  : A helper class for handling configuration defaults of packaged apps gracefully.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-appconf-license = %{version}-%{release}
Requires: django-appconf-python = %{version}-%{release}
Requires: django-appconf-python3 = %{version}-%{release}
Requires: six
BuildRequires : Django
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
django-appconf
==============
.. image:: http://codecov.io/github/django-compressor/django-appconf/coverage.svg?branch=develop
:alt: Code Coverage
:target: http://codecov.io/github/django-compressor/django-appconf?branch=develop

%package license
Summary: license components for the django-appconf package.
Group: Default

%description license
license components for the django-appconf package.


%package python
Summary: python components for the django-appconf package.
Group: Default
Requires: django-appconf-python3 = %{version}-%{release}

%description python
python components for the django-appconf package.


%package python3
Summary: python3 components for the django-appconf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django-appconf package.


%prep
%setup -q -n django-appconf-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552487745
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-appconf
cp LICENSE %{buildroot}/usr/share/package-licenses/django-appconf/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-appconf/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
