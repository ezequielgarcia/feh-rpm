# No desktop file for feh. It may be a GUI program, but it needs 
# file names or it just spits out the help.

Name:           feh
Version:        1.3.4
Release:        13%{?dist}
Summary:        Fast command line image viewer using Imlib2
Group:          Applications/Multimedia
License:        MIT
URL:            http://linuxbrit.co.uk/feh/
# This is: http://linuxbrit.co.uk/downloads/feh-%{version}.tar.gz with
# feh-1.3.4/src/menubg_britney.png (which is non free) removed
Source0:        %{name}-%{version}.tar.gz
Patch0:         feh-1.3.4-missing-protos.patch
Patch1:         feh-1.3.4-remove_britney_references.patch
Patch2:         feh-1.3.4-svn-fixes.patch
Patch3:         feh-1.3.4-man.patch
Patch4:         feh-1.3.4-bz441527.patch
Patch5:         feh-1.3.4-dejavu.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  giblib-devel imlib2-devel libjpeg-devel libpng-devel
BuildRequires:  libXt-devel
%if 0%{?fedora} > 10
Requires:       dejavu-sans-fonts
%else
Requires:       dejavu-fonts
%endif

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/yudit.ttf
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
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-11
- Fix font Requires

* Mon Dec 22 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-10
- Fix thinko in DejaVu package name

* Sun Dec 21 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.3.4-9
- Switch from included font to DejaVu Sans

* Thu Apr 10 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-8
- Remove non free menubg_britney.png from sources
- Apply various fixes from svn
- Some makeup fixes to the manpage (courtesy of debian)
- Fix escaping of filenames in "feh --bg-scale" (bz 441527)

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.4-7
- Fix missing prototype compiler warnings

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
