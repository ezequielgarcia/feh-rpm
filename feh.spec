# No desktop file for feh. It may be a GUI program, but it needs 
# file names or it just spits out the help.

Name:         	feh 
Version:        1.3.4
Release:        6%{?dist}
Summary:        Fast command line image viewer using Imlib2
Group:          Applications/Multimedia
License:        MIT
URL:            http://linuxbrit.co.uk/feh/
Source0:        http://linuxbrit.co.uk/downloads/feh-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  giblib-devel imlib2-devel libjpeg-devel libpng-devel
BuildRequires:  libXt-devel

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
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.4-6
- Autorebuild for GCC 4.3

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-5
- Update License tag for new Licensing Guidelines compliance

* Thu Aug 31 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-4
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-3
- Rebuild for Fedora Extras 5

* Tue Jan 31 2006 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-2
- change to new modular X devel BuildReqs

* Wed Aug 31 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.4-1
- bump to 1.3.4

* Thu Jun 16 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-3
- do it right this time

* Wed Jun 01 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-2
- proper dist tag

* Tue May 03 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.1-1
  Bump to 1.3.1

* Mon Apr 25 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-3
  Spec file cleanup, dist tag

* Wed Mar 30 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-2
  Spec file cleanup, plus would upgrade linuxbrit rpm

* Fri Mar 25 2005 Aaron Kurtz <a.kurtz@hardsun.net> - 1.3.0-1
- Initial Fedora RPM release
