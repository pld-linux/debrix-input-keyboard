#
# TODO:
# - descriptions and summaries
# - requires/provides/obsoletes
#
%define		snap 20040628
#
Summary:	debrix keyboard driver
Summary(pl.UTF-8):   Driver klawiatury dla debriksa
Name:		debrix-input-keyboard
Version:	0.1.0
Release:	0.1
Epoch:		0
License:	??
Group:		X11/Xorg
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	29636d7ae668b9dbb936d4a92e5976a5
# not really debrix URL, but there is no other...
URL:		http://xserver.freedesktop.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	debrix-devel
BuildRequires:	libtool
Requires:	debrix
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/lib*.so*
%{_mandir}/man3/*
