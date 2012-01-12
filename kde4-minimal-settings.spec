Name: kde4-minimal-settings
Version: 0.1
Release: 1

Group: Graphical desktop/KDE
Summary: Minimal KDE4 settings
Url: https://code.launchpad.net/kubuntu-low-fat-settings
License: GPLv3

BuildArch: noarch

Requires: gettext qmergeinifiles > 1.50

Source: %name.tar.gz
Source1: kubuntu-low-fat-settings.tar

BuildRequires: qmergeinifiles gettext

%description
This package allow to set minimal KDE4 settings to gain additional system resources


%prep
%setup -q -n %name -a1
# cleanup
rm -rf kubuntu-low-fat-settings/share/autostart/
rm -f kubuntu-low-fat-settings/share/config/kdeglobals
rm -f kubuntu-low-fat-settings/share/config/kwinrc

%build
# config
for conf in kubuntu-low-fat-settings/share/config/*
do
    outname=`basename $conf`
    qmergeinifiles --no-override share/config/$outname $conf
done
# autostart
#mkdir -p share/autostart
#for desktop in kubuntu-low-fat-settings/share/autostart/*.desktop
#do
#    outname=`basename $desktop`
#    qmergeinifiles --no-override share/autostart/$outname $conf
#    cp -ar $desktop share/autostart/$outname
#done

%install
mkdir -p %buildroot/%{_datadir}/apps/%name/config
install -m 0644 share/config/* %buildroot/%{_datadir}/apps/%name/config
mkdir -p %buildroot/%{_datadir}/apps/%name/autostart/
install -m 0644 share/autostart/* %buildroot/%{_datadir}/apps/%name/autostart
mkdir -p %buildroot/%{_bindir}/
install -m 0755 bin/%name %buildroot/%{_bindir}/
mkdir -p %buildroot/%{_datadir}/applications/kde4
install -m 0644 share/applications/*.desktop %buildroot/%{_datadir}/applications/kde4
# translations
find po/* -type d | \
while read d
do
    lang=`basename $d`
    mkdir -p %buildroot/%_datadir/locale/$lang/LC_MESSAGES
    msgfmt -o %buildroot/%_datadir/locale/$lang/LC_MESSAGES/%name.mo $d/%name.po
done

%find_lang %name

%files -f %name.lang
%{_bindir}/%name
%{_datadir}/apps/%name
%{_datadir}/applications/kde4/*-setup.desktop

