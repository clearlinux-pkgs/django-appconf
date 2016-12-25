#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-appconf
Version  : 1.0.2
Release  : 18
URL      : https://pypi.python.org/packages/34/b9/d07195652ab494b026f7cb0341dd6e5f2e6e39be177abe05e2cec8bd46e4/django-appconf-1.0.2.tar.gz
Source0  : https://pypi.python.org/packages/34/b9/d07195652ab494b026f7cb0341dd6e5f2e6e39be177abe05e2cec8bd46e4/django-appconf-1.0.2.tar.gz
Summary  : A helper class for handling configuration defaults of packaged apps gracefully.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: django-appconf-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
django-appconf
==============
.. image:: http://codecov.io/github/django-compressor/django-appconf/coverage.svg?branch=develop
:alt: Code Coverage
:target: http://codecov.io/github/django-compressor/django-appconf?branch=develop

%package python
Summary: python components for the django-appconf package.
Group: Default

%description python
python components for the django-appconf package.


%prep
%setup -q -n django-appconf-1.0.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
