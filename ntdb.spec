Summary:	A not-so trivial keyword/data database system
Summary(pl.UTF-8):	Nie-Trywialna Baza danych
Name:		ntdb
Version:	1.0
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	http://samba.org/ftp/tdb/%{name}-%{version}.tar.gz
# Source0-md5:	57848538a61704505a6d73294d019ef3
URL:		http://tdb.samba.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NTDB is a Not-so Trivial Database. In concept, it is very much like
GDBM, and BSD's DB except that it allows multiple simultaneous writers
and uses locking internally to keep writers from trampling on each
other. NTDB is also extremely small.

%description -l pl.UTF-8
NTDB to Not-so Trivial Database, czyli już nie tak prosta baza danych
jak TDB. W założeniach jest bardzo podobna do GDBM lub DB z BSD z
wyjątkiem tego, że pozwala na zapis wielu procesom jednocześnie i
używa wewnętrznie blokowania, aby nie pozwolić piszącym na zadeptanie
się nawzajem. NTDB jest ponadto ekstremalnie mała.

%package devel
Summary:	Header files for NTDB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki NTDB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for NTDB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki NTDB.

%package -n python-ntdb
Summary:	Python bindings for NTDB
Summary(pl.UTF-8):	Pythonowy interfejs do NTDB
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq  python-libs

%description -n python-ntdb
Python bindings for NTDB.

%description -n python-ntdb -l pl.UTF-8
Pythonowy interfejs do NTDB.

%prep
%setup -q

%build
# note: configure in fact is waf call
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
PYTHONDIR=%{py_sitedir} \
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ntdbbackup
%attr(755,root,root) %{_bindir}/ntdbdump
%attr(755,root,root) %{_bindir}/ntdbrestore
%attr(755,root,root) %{_bindir}/ntdbtool
%attr(755,root,root) %{_libdir}/libntdb.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libntdb.so.1
%{_mandir}/man8/ntdbbackup.8*
%{_mandir}/man8/ntdbdump.8*
%{_mandir}/man8/ntdbrestore.8*
%{_mandir}/man8/ntdbtool.8*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt doc/*.pdf
%attr(755,root,root) %{_libdir}/libntdb.so
%{_includedir}/ntdb.h
%{_pkgconfigdir}/ntdb.pc
%{_mandir}/man3/ntdb.3*

%files -n python-ntdb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/ntdb.so
