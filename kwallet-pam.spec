%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet-pam
Version: 5.21.3
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: PAM support for Kwallet
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch0: pam_kwallet_init-use-unidirectional-mode-for-socat-v2.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Wallet)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: socat
BuildRequires: qmake5
Requires: socat
Requires: kwallet

%description
PAM support for Kwallet.
To enable it add these lines to /etc/pam.d/kde:

---------------------
-auth            optional        pam_kwallet5.so	kdehome=.kde4
-session         optional        pam_kwallet5.so
---------------------

%prep
%autosetup -p1
%cmake_kde5 -DKWALLET5=1 -DCMAKE_INSTALL_LIBDIR:PATH="/%{_lib}" -DQMAKE_EXECUTABLE=%{_bindir}/qmake-qt5

%build
%ninja -C build

%install
%ninja_install -C build
mkdir -p %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/security %{buildroot}/%{_lib}/

%files
%{_sysconfdir}/xdg/autostart/pam_kwallet_init.desktop
/%{_lib}/security/pam_kwallet5.so
%{_libdir}/libexec/pam_kwallet_init
