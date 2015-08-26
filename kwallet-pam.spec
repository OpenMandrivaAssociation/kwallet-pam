%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet-pam
Version: 5.4.0
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: PAM support for Kwallet
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch0: kwallet-pam-5.4.0-fix-install.patch
BuildRequires: cmake(ECM)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libgcrypt)

%description
PAM support for Kwallet.

%prep
%setup -q
%apply_patches
%cmake_kde5 -DKWALLET5=1

%build
%ninja -C build

%install
%ninja_install -C build

%files
