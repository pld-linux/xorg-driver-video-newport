Summary:	X.org video driver for SGI Indy's and Indigo2's Newport video cards
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Newport w SGI Indy i Indigo2
Name:		xorg-driver-video-newport
Version:	0.1.3.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-newport-%{version}.tar.bz2
# Source0-md5:	0021149bb435910e6b950714206d35c3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
ExclusiveArch:	mips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Newport (also called XL) video cards used in
SGI Indy and Indigo2 machines.

%description -l pl
Sterownik obrazu X.org dla kart graficznych Newport (zwanych tak�e XL)
w komputerach SGI Indy i Indigo2.

%prep
%setup -q -n xf86-video-newport-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README XF86Config.indy
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/newport_drv.so
%{_mandir}/man4/newport.4x*
