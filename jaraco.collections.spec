#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jaraco.collections
Version  : 3.0.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/74/ed/8ee1599924eb6c42b02e26a13e79f5069012b170401a42a8b8d6afe1f289/jaraco.collections-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/ed/8ee1599924eb6c42b02e26a13e79f5069012b170401a42a8b8d6afe1f289/jaraco.collections-3.0.0.tar.gz
Summary  : Collection objects similar to those in stdlib by jaraco
Group    : Development/Tools
License  : MIT
Requires: jaraco.collections-license = %{version}-%{release}
Requires: jaraco.collections-python = %{version}-%{release}
Requires: jaraco.collections-python3 = %{version}-%{release}
Requires: jaraco.classes
Requires: jaraco.text
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : jaraco.classes
BuildRequires : jaraco.text
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.collections.svg
:target: https://pypi.io/project/jaraco.collections

%package license
Summary: license components for the jaraco.collections package.
Group: Default

%description license
license components for the jaraco.collections package.


%package python
Summary: python components for the jaraco.collections package.
Group: Default
Requires: jaraco.collections-python3 = %{version}-%{release}

%description python
python components for the jaraco.collections package.


%package python3
Summary: python3 components for the jaraco.collections package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.collections)
Requires: pypi(jaraco.classes)
Requires: pypi(jaraco.text)
Requires: pypi(six)

%description python3
python3 components for the jaraco.collections package.


%prep
%setup -q -n jaraco.collections-3.0.0
cd %{_builddir}/jaraco.collections-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583538590
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jaraco.collections
cp %{_builddir}/jaraco.collections-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/jaraco.collections/a1474494d96f6ddb3a9a0d767a09871ffc388faf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__init__.py
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__pycache__/__init__.*

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jaraco.collections/a1474494d96f6ddb3a9a0d767a09871ffc388faf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
