Name:     unclutter-xfixes
Version:  1.6
Release:  1%{?dist}
Summary:  Hides the cursor on inactivity (rewrite of unclutter)
Packager: James Ho <ho.james142@gmail.com>

License:  MIT
URL:      https://github.com/Airblader/unclutter-xfixes
Source0:  %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXi-devel
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libev-devel
BuildRequires: asciidoc

Requires: libXi
Requires: libX11
Requires: libXfixes
Requires: libev

%description
This is a rewrite of the popular tool unclutter, but using the x11-xfixes extension. This means that this rewrite doesn't use fake windows or pointer grabbing and hence causes less problems with window managers and/or applications.


%prep
%autosetup


%build
CFLAGS='-g' %make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc README.md
%{_mandir}/man1/unclutter.1.gz
%{_bindir}/unclutter
%{_prefix}/share/licenses/unclutter/LICENSE


%changelog
* Wed Dec 01 2021 James Ho <ho.james142@gmail.com>
- Initial spec 
