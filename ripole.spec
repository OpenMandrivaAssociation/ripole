%define	major 0
%define libname %mklibname ripole %{major}
%define develname %mklibname ripole -d

Summary:	Extracts attachments out of mailpack format emails
Name:		ripole
Version:	0.2.0
Release:	22
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripole/
Source0:	http://www.pldaniels.com/ripole/%{name}-%{version}.tar.bz2
Patch0:		ripole-0.1.4-shared.diff
Patch1:		ripole-0.2.0-dev.diff
Patch2:		ripole-0.2.0-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities. 

%package -n	%{libname}
Summary:	Shared %{name} library
Group:          System/Libraries

%description -n	%{libname}
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities. 

%package -n	%{develname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel
Provides:	lib%{name}-devel
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname ripole 0 -d}

%description -n	%{develname}
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities. 

This package contains the development files for ripOLE.

%prep

%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

%build
%serverbuild 
export LDFLAGS="`rpm --eval %%configure|grep LDFLAGS|cut -d\\" -f2|sed -e 's/\$LDFLAGS\ //'`"

%make \
CFLAGS="$CFLAGS -I. -fPIC -DPIC -D_REENTRANT" \
    libdir=%{_libdir} LDFLAGS="$LDFLAGS"

%install

%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-15mdv2011.0
+ Revision: 669425
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-14mdv2011.0
+ Revision: 607366
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-13mdv2010.1
+ Revision: 519066
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.0-12mdv2010.0
+ Revision: 426939
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-11mdv2009.1
+ Revision: 316153
- fix build with -Werror=format-security (P2)
- use LDFLAGS from the %%configure macro

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-10mdv2009.0
+ Revision: 238930
- use -Wl,--as-needed -Wl,--no-undefined

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-9mdv2009.0
+ Revision: 225320
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-8mdv2008.1
+ Revision: 179436
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-7mdv2008.0
+ Revision: 90252
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdv2008.0
+ Revision: 83494
- bump release
- new devel name

* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-5mdv2008.0
+ Revision: 51026
- use the new %%serverbuild macro


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 17:56:59 (63392)
- rebuild

* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 17:55:22 (63391)
- Import ripole

* Fri Aug 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2007.0
- added P1 from the dev snap
- misc spec file fixes

* Wed Jan 11 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.2.0-2mdk
- add BuildRequires: libtool

* Mon Dec 12 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdk
- 0.2.0
- drop one upstream patch

* Sat Sep 17 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-6mdk
- use libtool when making the lib and binary

* Mon Jun 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-5mdk
- added P1 from ripmime-1.4.0.5

* Fri Dec 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1.4-4mdk
- revert latest "lib64 fixes"
- added another lib64 fix

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1.4-3mdk
- lib64 fixes

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1.4-2mdk
- make it rpmbuildupdate aware

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1.4-1mdk
- initial mandrake package

