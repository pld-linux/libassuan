Summary:	Assuan - an IPC library for non-persistent servers
Summary(pl):	Assuan - biblioteka IPC dla serwerów nie dzia³aj±cych ci±gle
Name:		libassuan
Version:	0.6.2
Release:	2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libassuan/%{name}-%{version}.tar.gz
# Source0-md5:	ff59b657aae3e3d87f6356fc0e165439
Patch0:		%{name}-shared.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-am18.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7.6
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to make your life not too easy and separated it out to
a standalone library.

%description -l pl
To jest biblioteka komunikacji miêdzyprocesowej (IPC) u¿ywana przez
GnuPG 1.9, gpgme oraz stary pakiet newpg. By³a do³±czana do tych
pakietów, ale autorzy zdecydowali, ¿eby ju¿ nie u³atwiaæ tak ¿ycia i
wydzielili j±.

%package devel
Summary:	Header files for assuan library
Summary(pl):	Pliki nag³ówkowe biblioteki assuan
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files for assuan library.

%description devel -l pl
Pliki nag³ówkowe biblioteki assuan.

%package static
Summary:	Static assuan library
Summary(pl):	Statyczna biblioteka assuan
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static assuan library.

%description static -l pl
Statyczna biblioteka assuan.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libassuan-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*.m4
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
