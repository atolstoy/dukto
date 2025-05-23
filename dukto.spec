%global	debug_package %{nil}
%define	commit 56d79455cdea0062e53068773d343b4be64bbe78
%define	commit_short %(echo %{commit} | head -c6)
Name:		dukto
Version:	6.0
Release:	git%{commit_short}
Summary:	File transfer tool
Group:		Networking/File transfer
License:	GPLv2+
URL:		https://github.com/WhiredPlanck
Source:		https://github.com/WhiredPlanck/%{name}/archive/%{commit}.tar.gz?/%{name}-%{commit}.tar.gz

BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
Requires:       qt5-qtdeclarative

%description
Dukto is an easy file transfer tool designed for LAN use.
You can use it to transfer files from one PC to another,
without worrying about users, permissions, operating systems,
protocols, clients, servers and so on... Just start dukto on
the two PCs and transfer files and folders by dragging
onto it's window. This is a working Qt5 version of Dukto R6.

%prep
%setup -q -n %{name}-%{commit}

%build
%qmake_qt5
%make

%install
%__install -D -m0755 -s %{name} "%{buildroot}%{_bindir}/%{name}"
%__install -D -m0644 data/%{name}.png "%{buildroot}%{_datadir}/pixmaps/%{name}.png"
desktop-file-install --dir "%{buildroot}%{_datadir}/applications" data/%{name}.desktop

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
