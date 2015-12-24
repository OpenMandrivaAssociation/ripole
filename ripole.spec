%define major 0
%define libname %mklibname ripole %{major}
%define devname %mklibname ripole -d
%define _disable_lto 1

Summary:	Extracts attachments out of mailpack format emails
Name:		ripole
Version:	0.2.0
Release:	28
License:	BSD
Group:		Networking/Mail
Url:		http://www.pldaniels.com/ripole/
Source0:	http://www.pldaniels.com/ripole/%{name}-%{version}.tar.bz2
Patch0:		ripole-0.1.4-shared.diff
Patch1:		ripole-0.2.0-dev.diff
Patch2:		ripole-0.2.0-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	libtool

%description
ripOLE is a small program/library designed to pull out attachments from OLE2
data files (ie, MS Office documents). ripOLE is BSD licenced meaning that
commercial projects can also use the code without worry of licence costs or
legal liabilities.

%files
%doc CHANGELOG CONTRIBUTORS LICENSE README
%{_bindir}/*

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Shared %{name} library
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared library for ripOLE.

%files -n %{libname}
%{_libdir}/libripole.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the development files for ripOLE.

%files -n %{devname}
%doc TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

%build
%serverbuild

%make -j1 \
	CFLAGS="%{optflags} -I. -fPIC -DPIC -D_REENTRANT" \
	libdir=%{_libdir} \
	LDFLAGS="%{ldflags}"

%install

%makeinstall_std \
	bindir=%{_bindir} \
	libdir=%{_libdir} \
	includedir=%{_includedir}

