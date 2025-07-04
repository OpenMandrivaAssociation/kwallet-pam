%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: kwallet-pam
Version: 6.4.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kwallet-pam/-/archive/%{gitbranch}/kwallet-pam-%{gitbranchd}.tar.bz2#/kwallet-pam-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/kwallet-pam-%{version}.tar.xz
%endif
Summary: PAM support for Kwallet
URL: https://kde.org/
License: GPL
Group: System/Libraries
Patch0: pam_kwallet_init-use-unidirectional-mode-for-socat-v2.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6Wallet)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: socat
BuildRequires: gettext
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: socat
Requires: kf6-kwallet
# Renamed after Plasma 5 removal, after 6.0 2024-04-27
%rename plasma6-kwallet-pam

%description
PAM support for Kwallet.
To enable it add these lines to /etc/pam.d/kde:

---------------------
-auth            optional        pam_kwallet5.so
-session         optional        pam_kwallet5.so
---------------------

%files
%{_sysconfdir}/xdg/autostart/pam_kwallet_init.desktop
%{_libdir}/security/pam_kwallet5.so
%{_libdir}/libexec/pam_kwallet_init
%{_userunitdir}/plasma-kwallet-pam.service
