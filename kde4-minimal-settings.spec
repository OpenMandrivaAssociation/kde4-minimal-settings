Name: kde4-minimal-settings
Version: 0.1
Release: 2

Group: Graphical desktop/KDE
Summary: Minimal KDE4 settings
Url: https://code.launchpad.net/kubuntu-low-fat-settings
License: GPLv3

BuildArch: noarch

Requires: gettext qmergeinifiles > 1.50

Source: %name.tar.gz
Source1: kubuntu-low-fat-settings.tar

BuildRequires: qmergeinifiles gettext kde4-macros

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
mkdir -p %buildroot/%_kde_appsdir/%name/config
install -m 0644 share/config/* %buildroot/%_kde_appsdir/%name/config
mkdir -p %buildroot/%_kde_appsdir/%name/autostart/
install -m 0644 share/autostart/* %buildroot/%_kde_appsdir/%name/autostart
mkdir -p %buildroot/%_kde_bindir/
install -m 0755 bin/%name %buildroot/%_kde_bindir/
mkdir -p %buildroot/%_kde_applicationsdir/
install -m 0644 share/applications/*.desktop %buildroot/%_kde_applicationsdir/
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
%_kde_bindir/%name
%_kde_appsdir/%name
%_kde_applicationsdir/*-setup.desktop



%changelog
* Thu Jan 12 2012 Александр Казанцев <kazancas@mandriva.org> 0.1-2
+ Revision: 760475
- build with propertly kde macros

* Thu Jan 12 2012 Александр Казанцев <kazancas@mandriva.org> 0.1-1
+ Revision: 760299
- use standart dir path
- imported package kde4-minimal-settings


* Thu Jan 12 2012 Alexander Kazancev <kazancas@mandriva.ru> 4.7-mdv1

* Fri Oct 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7-alt1
- initial build
