Summary:	Assuan - an IPC library for non-persistent servers
Summary(pl):	Assuan - biblioteka IPC dla serwer�w nie dzia�aj�cych ci�gle
Name:		libassuan
Version:	0.6.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libassuan/%{name}-%{version}.tar.gz
# Source0-md5:	6cb7281eb0740b30372a7b58342a441e
Patch0:		%{name}-shared.patch
Patch1:		%{name}-info.patch
#URL:		http://www.gnurg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the IPC library used by GnuPG 1.9, gpgme and the old newpg
package. It used to be included with the latter packages but the
authors decided to make your life not too easy and separated it out to
a standalone library.

%description -l pl
To jest biblioteka komunikacji mi�dzyprocesowej (IPC) u�ywana przez
GnuPG 1.9, gpgme oraz stary pakiet newpg. By�a do��czana do tych
pakiet�w, ale autorzy zdecydowali, �eby ju� nie u�atwia� tak �ycia i
wydzielili j�.

%package devel
Summary:	Header files for assuan library
Summary(pl):	Pliki nag��wkowe biblioteki assuan
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for assuan library.

%description devel -l pl
Pliki nag��wkowe biblioteki assuan.

%package static
Summary:	Static assuan library
Summary(pl):	Statyczna biblioteka assuan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static assuan library.

%description static -l pl
Statyczna biblioteka assuan.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
