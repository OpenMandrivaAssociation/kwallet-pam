%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet-pam
Version: 5.5.5
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: PAM support for Kwallet
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libgcrypt)

%description
PAM support for Kwallet.
To enable it add these lines to /etc/pam.d/kde:

---------------------
-auth            optional        pam_kwallet5.so	kdehome=.kde4
-session         optional        pam_kwallet5.so
---------------------

%prep
%setup -q
%cmake_kde5 -DKWALLET5=1 -DCMAKE_INSTALL_LIBDIR=/%{_lib}

%build
%ninja -C build

%install
%ninja_install -C build

%files
/%{_lib}/security/pam_kwallet5.so
