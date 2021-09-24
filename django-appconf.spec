#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-appconf
Version  : 1.0.5
Release  : 43
URL      : https://files.pythonhosted.org/packages/d6/dc/ab95f120aa249f215b1a7925a9062393c039481e1df77b4455e021ae6f67/django-appconf-1.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/dc/ab95f120aa249f215b1a7925a9062393c039481e1df77b4455e021ae6f67/django-appconf-1.0.5.tar.gz
Summary  : A helper class for handling configuration defaults of packaged apps gracefully.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-appconf-license = %{version}-%{release}
Requires: django-appconf-python = %{version}-%{release}
Requires: django-appconf-python3 = %{version}-%{release}
Requires: Django
BuildRequires : Django
BuildRequires : buildreq-distutils3

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
Provides: pypi(django_appconf)
Requires: pypi(django)

%description python3
python3 components for the django-appconf package.


%prep
%setup -q -n django-appconf-1.0.5
cd %{_builddir}/django-appconf-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632508234
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-appconf
cp %{_builddir}/django-appconf-1.0.5/LICENSE %{buildroot}/usr/share/package-licenses/django-appconf/a5771f371f97e15ece15ad91386b8897cb06a95a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-appconf/a5771f371f97e15ece15ad91386b8897cb06a95a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
