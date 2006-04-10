Summary:	A laptop battery monitor for the KDE
Name:		kthinkbat
Version:	0.1.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	https://lepetitfou.dyndns.org/download/kthinkbat/%{name}-%{version}.tar.bz2
# Source0-md5:	769f39b9ba04fd011a3304f6c916b477
Patch0:		%{name}-assert.patch
URL:		https://lepetitfou.dyndns.org/wiki/view/Werkstatt/KThinkBat
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A laptop battery monitor for the KDE. Additionally, KThinkBat shows
the current power consumption of the laptop, brings support for a
second battery and its layout is highly customizable.

Features of KThinBat:
- display of current battery fuel in percent and visual as gauge
- display of the current online/offline state
- display of the current power consumption in W (or A on Asus Laptops)
- optional use of the ThinkPad SMAPI BIOS through the sysfs interface
  provided by the tp_smapi driver (automatically detected)
- batteries can be display separatelly or in an combined/summarized
  view
- complete customizable Layout including, positions, sizes, color,
  fonts, values.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--libdir=%{_libdir}/kde3 \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kde_htmldir=%{_datadir}/doc/kde/HTML \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/config.kcfg/*.kcfg
