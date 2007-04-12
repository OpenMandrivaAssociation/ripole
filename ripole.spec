%define	major 0
%define libname	%mklibname ripole %{major}

Summary:	Extracts attachments out of mailpack format emails
Name:		ripole
Version:	0.2.0
Release:	%mkrel 4
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripole/
Source0:	http://www.pldaniels.com/ripole/%{name}-%{version}.tar.bz2
Patch0:		ripole-0.1.4-shared.diff
Patch1:		ripole-0.2.0-dev.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ripOLE is a small program/library designed to pull out attachments
from OLE2 data files (ie, MS Office documents).  ripOLE is BSD
licenced meaning that commercial projects can also use the code
without worry of licence costs or legal liabilities. 

%package -n	%{libname}
Summary:	Shared %{name} library
Group:          System/Libraries

%description -n	%{libname}
ripOLE is a small program/library designed to pull out attachments
from OLE2 data files (ie, MS Office documents).  ripOLE is BSD
licenced meaning that commercial projects can also use the code
without worry of licence costs or legal liabilities. 

%package -n	%{libname}-devel
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel
Provides:	lib%{name}-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
ripOLE is a small program/library designed to pull out attachments
from OLE2 data files (ie, MS Office documents).  ripOLE is BSD
licenced meaning that commercial projects can also use the code
without worry of licence costs or legal liabilities. 

%prep

%setup -q
%patch0 -p0
%patch1 -p1

%build

%make libdir=%{_libdir}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


