Summary:	A laptop battery monitor for the KDE
Summary(pl):	Monitor baterii laptopa dla KDE
Name:		kthinkbat
Version:	0.2.3
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://lepetitfou.dyndns.org/download/kthinkbat/src/kthinkbat-0.2.x/%{name}-%{version}.tar.bz2
# Source0-md5:	edea76c527e7a89da92da14578c2be68
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

Features of KThinkBat:
- display of current battery fuel in percent and visual as gauge
- display of the current online/offline state
- display of the current power consumption in W (or A on Asus Laptops)
- optional use of the ThinkPad SMAPI BIOS through the sysfs interface
  provided by the tp_smapi driver (automatically detected)
- batteries can be display separatelly or in an combined/summarized
  view
- complete customizable layout including positions, sizes, color,
  fonts, values.

%description -l pl
Monitor baterii laptopa dla KDE. Oprócz tego KThinkBat pokazuje
aktualny pobór energii przez laptopa, dodaje obs³ugê drugiej baterii,
a jego wygl±d jest w du¿ej mierze konfigurowalny.

Mo¿liwo¶ci KThinkBata:
- wy¶wietlanie aktualnego stanu na³adowania baterii w procentach i
  wizualnie jako licznika
- wy¶wietlanie aktualnego stanu online/offline
- wy¶wietlanie aktualnego poboru energii w watach (lub amperach na
  laptopach Asusa)
- opcjonalnie u¿ywa BIOS-u SMAPI ThinkPadów poprzez interfejs sysfs
  udostêpniony przez sterownik tp_smapi (automatycznie wykrywany)
- baterie mog± byæ wy¶wietlane oddzielnie lub ³±cznie
- w pe³ni konfigurowalny wygl±d, w³±cznie z po³o¿eniem, rozmiarami,
  kolorami, fontami, warto¶ciami.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
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
%{_iconsdir}/hicolor/*/*/*
