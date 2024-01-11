Summary: X.Org X11 libXpm runtime library
Name: libXpm
Version: 3.5.12
Release: 9%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: gettext
BuildRequires: pkgconfig(xext) pkgconfig(xt) pkgconfig(xau)
BuildRequires: ncompress gzip

Patch0: 0001-After-fdopen-use-fclose-instead-of-close-in-error-pa.patch

# CVE-2022-46285
Patch0001: 0001-Fix-CVE-2022-46285-Infinite-loop-on-unclosed-comment.patch
# CVE-2022-44617
Patch0002: 0002-Fix-CVE-2022-44617-Runaway-loop-with-width-of-0-and-.patch
Patch0003: 0003-Prevent-a-double-free-in-the-error-code-path.patch
# CVE-2022-4883
Patch0004: 0004-configure-add-disable-open-zfile-instead-of-requirin.patch
Patch0005: 0005-Fix-CVE-2022-4883-compression-commands-depend-on-PAT.patch
Patch0006: 0006-Use-gzip-d-instead-of-gunzip.patch

%description
X.Org X11 libXpm runtime library

%package devel
Summary: X.Org X11 libXpm development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXpm development package

%prep
%setup -q
%patch0 -p1 -b .covscan
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
#%dir %{_mandir}/man1x
%{_mandir}/man1/*.1*
#%{_mandir}/man1/*.1x*

%changelog
* Mon Jan 16 2023 Peter Hutterer <peter.hutterer@redhat.com> - 3.5.12-9
- Fix CVE-2022-46285: infinite loop on unclosed comments (#2161800)
- Fix CVE-2022-44617: runaway loop with width of 0 (#2161808)
- Fix CVE-2022-4883: compression depends on $PATH (#2160238)

* Mon Dec 09 2019 Benjamin Tissoires <benjamin.tissoires@redhat.com> 3.5.12-8
- add covscan fixes (#1602606)

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 3.5.12-7
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 3.5.12-6
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 3.5.12-1
- libXpm 3.5.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Adam Jackson <ajax@redhat.com> 3.5.11-1
- libXpm 3.5.11
- Drop pre-F18 changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 3.5.10-4
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Adam Jackson <ajax@redhat.com> 3.5.10-1
- libXpm 3.5.10
