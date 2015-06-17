Name:           feh
Version:        2.12
Release:        2%{?dist}
Summary:        Fast command line image viewer using Imlib2
Group:          Applications/Multimedia
License:        MIT
URL:            http://feh.finalrewind.org/
Source0:        http://feh.finalrewind.org/feh-%{version}.tar.bz2
Patch0:         feh-1.10.1-dejavu.patch

BuildRequires:  giblib-devel
BuildRequires:  imlib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libXt-devel
BuildRequires:  libXinerama-devel
%if 0%{?fedora} > 10
Requires:       dejavu-sans-fonts
%else
Requires:       dejavu-fonts
%endif
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slide-show or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.


%prep
%setup -q
%patch0 -p1 -b .dejavu


%build
# Propagate values into config.mk
sed -i \
  -e "s|^doc_dir =.*$|doc_dir = \$(DESTDIR)%{_pkgdocdir}|" \
  -e "s|^example_dir =.*$|example_dir = \$(doc_dir)/examples|" \
  -e "s|^CFLAGS ?=.*$|CFLAGS = ${RPM_OPT_FLAGS}|" \
  config.mk
make PREFIX=%{_prefix} %{?_smp_mflags}


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
rm %{buildroot}%{_datadir}/%{name}/fonts/yudit.ttf
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man[^3]/*


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Ben Boeckel <mathstuf@gmail.com> - 2.12-1
- Update to 2.12

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Ben Boeckel <mathstuf@gmail.com> - 2.9.3-1
- Update to 2.9.3
- Update URL

* Tue Aug 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.7-5
- Reflect docdir changes (FTBFS RHBZ#992244).
- Let package acknowledge RPM_OPT_FLAGS.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.7-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 2.7-1
- Update to 2.7

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 2.3-3
- Pass PREFIX to the build step

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Ben Boeckel <mathstuf@gmail.com> - 2.3-1
- Update to 2.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Ben Boeckel <mathstuf@gmail.com> - 2.1-1
- Update to 2.1

* Mon Jul 25 2011 Ben Boeckel <mathstuf@gmail.com> - 1.14.2-1
- Update to 1.14.2

* Fri Jun 24 2011 Ben Boeckel <mathstuf@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Andrew Potter <agpotter@gmail.com> 1.10.1-1
- New upstream release
- Closes CVE-2010-2246 by removing option -G, --wget-timestamp

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
