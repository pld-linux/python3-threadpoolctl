#
# Conditional build:
%bcond_with	tests	# unit tests (some build step needed)

Summary:	Thread-pool controls
Summary(pl.UTF-8):	Sterowanie pulą wątków
Name:		python3-threadpoolctl
Version:	3.6.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/threadpoolctl/
Source0:	https://files.pythonhosted.org/packages/source/t/threadpoolctl/threadpoolctl-%{version}.tar.gz
# Source0-md5:	201b8ab8d03c9154d24290fa8dccee85
URL:		https://pypi.org/project/threadpoolctl/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python helpers to limit the number of threads used in the
threadpool-backed of common native libraries used for scientific
computing and data science (e.g. BLAS and OpenMP).

Fine control of the underlying thread-pool size can be useful in
workloads that involve nested parallelism so as to mitigate
oversubscription issues.

%description -l pl.UTF-8
Pythonowe funkcje pomocnicze do ograniczania liczby wątków używanych
przez korzystające z threadpoola popularne biblioteki natywne, służące
do obliczeń naukowych (np. BLAS czy OpenMP).

Dokładna kontrola rozmiaru puli wątków może być przydatna pod
obciążeniem związanym z zagnieżdżonym zrównolegleniem, a także pomóc
przy problemach ze zbyt dużym obciążeniem.

%prep
%setup -q -n threadpoolctl-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/threadpoolctl.py
%{py3_sitescriptdir}/__pycache__/threadpoolctl.cpython-*.py[co]
%{py3_sitescriptdir}/threadpoolctl-%{version}.dist-info
