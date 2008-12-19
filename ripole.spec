%define	major 0
%define libname %mklibname ripole %{major}
%define develname %mklibname ripole -d

Summary:	Extracts attachments out of mailpack format emails
Name:		ripole
Version:	0.2.0
Release:	%mkrel 11
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
rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

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
%{_libdir}/*.a
%{_libdir}/*.la
