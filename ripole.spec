%define	major 0
%define libname %mklibname ripole %{major}
%define develname %mklibname ripole -d

Summary:	Extracts attachments out of mailpack format emails
Name:		ripole
Version:	0.2.2
Release:	1
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/ripole/
Source0:	http://www.pldaniels.com/ripole/%{name}-%{version}.tar.gz
Patch0:		ripole-0.1.4-shared.diff
BuildRequires:	libtool

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
%patch0 -p1

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
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a
#% {_libdir}/*.la
