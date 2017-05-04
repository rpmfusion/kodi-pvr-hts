%global commit 5629396a42b290f4cd7f19f35508815e9d247620
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170419

%global kodi_addon pvr.hts
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        3.4.23
Release:        1%{?dist}
Summary:        Kodi's frontend for Tvheadend

Group:          Applications/Multimedia
# Addon is GPLv2+. Portions of lib/libhts are LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
Provides:       bundled(sha1-niedermayer)
ExclusiveArch:  i686 x86_64

%description
Tvheadend frontend; supporting streaming of Live TV and recordings, EPG, timers.


%prep
%autosetup -n %{kodi_addon}-%{commit}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Wed Apr 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.23-1
- Update to latest stable release for Kodi 17

* Tue Jul 05 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.2.20-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.1.16-1
- Initial RPM release
