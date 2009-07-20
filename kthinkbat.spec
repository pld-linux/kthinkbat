Summary:	A laptop battery monitor for the KDE
Summary(pl.UTF-8):	Monitor baterii laptopa dla KDE
Name:		kthinkbat
Version:	0.2.9
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://lepetitfou.dyndns.org/download/kthinkbat/src/kthinkbat-0.2.x/%{name}-%{version}.tar.bz2
# Source0-md5:	aaf3a1e84b833a500b42a99dc5c0fd84
Patch0:		%{name}-assert.patch
Patch1:		kde-ac260-lt.patch
URL:		http://www.thinkwiki.org/wiki/KThinkBat
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

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

%description -l pl.UTF-8
Monitor baterii laptopa dla KDE. Oprócz tego KThinkBat pokazuje
aktualny pobór energii przez laptopa, dodaje obsługę drugiej baterii,
a jego wygląd jest w dużej mierze konfigurowalny.

Możliwości KThinkBata:
- wyświetlanie aktualnego stanu naładowania baterii w procentach i
  wizualnie jako licznika
- wyświetlanie aktualnego stanu online/offline
- wyświetlanie aktualnego poboru energii w watach (lub amperach na
  laptopach Asusa)
- opcjonalnie używa BIOS-u SMAPI ThinkPadów poprzez interfejs sysfs
  udostępniony przez sterownik tp_smapi (automatycznie wykrywany)
- baterie mogą być wyświetlane oddzielnie lub łącznie
- w pełni konfigurowalny wygląd, włącznie z położeniem, rozmiarami,
  kolorami, fontami, wartościami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_iconsdir}/hicolor/*/*/*
