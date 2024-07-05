#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.05.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		filelight
Summary:	Filelight
Name:		ka6-%{kaname}
Version:	24.05.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	56994006eeb79348cc84fba36c5ec8f2
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filelight allows you to understand exactly where your diskspace is
being used by graphically representating your filesystem as a set of
concentric segmented-rings.

%description -l pl.UTF-8
Filelight pozwala Ci zrozumieć gdzie dokładnie przestrzeń dyskowa jest
używana wyświetlając zestaw współśrodkowych wycinków koła
reprezentujących Twój system plików.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/filelightrc
%attr(755,root,root) %{_bindir}/filelight
%{_desktopdir}/org.kde.filelight.desktop
%{_iconsdir}/hicolor/128x128/apps/filelight.png
%{_iconsdir}/hicolor/16x16/apps/filelight.png
%{_iconsdir}/hicolor/22x22/apps/filelight.png
%{_iconsdir}/hicolor/32x32/apps/filelight.png
%{_iconsdir}/hicolor/48x48/apps/filelight.png
%{_iconsdir}/hicolor/64x64/apps/filelight.png
%{_datadir}/metainfo/org.kde.filelight.appdata.xml
%{_datadir}/qlogging-categories6/filelight.categories
