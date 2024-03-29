#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jaraco.collections
Version  : 3.5.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/d1/e4/d3aa8de33e2a88207e4ade5a19e2680981a5fe2f54f2bc889e99cd32d65e/jaraco.collections-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/e4/d3aa8de33e2a88207e4ade5a19e2680981a5fe2f54f2bc889e99cd32d65e/jaraco.collections-3.5.0.tar.gz
Summary  : Collection objects similar to those in stdlib by jaraco
Group    : Development/Tools
License  : MIT
Requires: jaraco.collections-license = %{version}-%{release}
Requires: jaraco.collections-python = %{version}-%{release}
Requires: jaraco.collections-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(jaraco.classes)
BuildRequires : pypi(jaraco.text)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.collections.svg
:target: `PyPI link`_

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

%description python3
python3 components for the jaraco.collections package.


%prep
%setup -q -n jaraco.collections-3.5.0
cd %{_builddir}/jaraco.collections-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641234877
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jaraco.collections
cp %{_builddir}/jaraco.collections-3.5.0/LICENSE %{buildroot}/usr/share/package-licenses/jaraco.collections/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/jaraco/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/jaraco/__pycache__/__init__.*

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jaraco.collections/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
