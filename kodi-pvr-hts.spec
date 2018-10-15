%global commit 7c7c6cefc785ccd5ee7015eb997e0c688258a4e0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180825

%global kodi_addon pvr.hts
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        4.3.6
Release:        2%{?dist}
Summary:        TVHeadEnd PVR for Kodi

# Addon is GPLv2+. SHA1 implementation from FFmpeg bundled in
# lib/libhts is LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
Provides:       bundled(sha1-ffmpeg)
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit}


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.3.6-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.3.6-1
- Update to 4.3.6
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:4.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.2.13-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:3.4.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.28-1
- Update to 3.4.28

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:3.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.23-1
- Update to latest stable release for Kodi 17

* Tue Jul 05 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.2.20-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.1.16-1
- Initial RPM release
