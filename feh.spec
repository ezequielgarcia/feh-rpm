Name:         	feh 
Version:        1.3.0
Release:        2
Summary:        Image viewer using Imlib2

Group:          Applications/Multimedia
License:        BSD
URL:            http://linuxbrit.co.uk/feh/
Source0:        http://linuxbrit.co.uk/feh/feh-1.3.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: giblib-devel imlib2-devel libjpeg-devel libpng-devel

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man[^3]/*

%changelog
* Wed May 30 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 0:1.3.0-2
  Spec file cleanup, plus would upgrade linuxbrit rpm.

* Fri May 25 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 0:1.3.0-1
- Initial Fedora RPM release.
