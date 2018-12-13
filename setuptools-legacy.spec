Name     : setuptools-legacy
Version  : 39.0.1
Release  : 116
URL      : https://pypi.python.org/packages/72/c2/c09362ab29338413ab687b47dab03bab4a792e2bbb727a1eb5e0a88e3b86/setuptools-39.0.1.zip
Source0  : https://pypi.python.org/packages/72/c2/c09362ab29338413ab687b47dab03bab4a792e2bbb727a1eb5e0a88e3b86/setuptools-39.0.1.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT
Requires: setuptools-legacy-bin
Requires: setuptools-legacy-license
Requires: setuptools-legacy-python
Requires: certifi
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: https://pypi.org/project/setuptools

%package bin
Summary: bin components for the setuptools-legacy package.
Group: Binaries
Requires: setuptools-legacy-license

%description bin
bin components for the setuptools-legacy package.


%package extras
Summary: extras components for the setuptools-legacy package.
Group: Default

%description extras
extras components for the setuptools-legacy package.


%package -n setuptools-legacypython
Summary: legacypython components for the setuptools-legacy package.
Group: Default
Requires: python-core

%description -n setuptools-legacypython
legacypython components for the setuptools-legacy package.


%package license
Summary: license components for the setuptools-legacy package.
Group: Default

%description license
license components for the setuptools-legacy package.


%package python
Summary: python components for the setuptools-legacy package.
Group: Default

%description python
python components for the setuptools-legacy package.


%prep
%setup -q -n setuptools-39.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529164306
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/setuptools-legacy
cp LICENSE %{buildroot}/usr/share/doc/setuptools-legacy/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/easy_install-2.7
%exclude /usr/bin/easy_install

%files extras
%defattr(-,root,root,-)
/usr/bin/easy_install-2.7

%files -n setuptools-legacypython
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/setuptools/*.exe
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/setuptools-legacy/LICENSE

%files python
%defattr(-,root,root,-)
