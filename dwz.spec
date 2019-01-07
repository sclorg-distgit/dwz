%{?scl:%scl_package gcc}
Summary: DWARF optimization and duplicate removal tool
Name: %{?scl_prefix}dwz
Version: 0.12
Release: 1.1.bs1%{?dist}
License: GPLv2+ and GPLv3+
Group: Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=dwz-%{version}/ dwz-%{version} \
#   | bzip2 -9 > dwz-%{version}.tar.bz2
Source: dwz-%{version}.tar.bz2
BuildRequires: elfutils-libelf-devel
%{?scl:Requires:%scl_runtime}

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup -q -n dwz-%{version}

%build
make %{?_smp_mflags} CFLAGS='%{optflags}' prefix=%{_prefix} \
  mandir=%{_mandir} bindir=%{_bindir}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir} \
  install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz.1*

%changelog
* Fri Jul 13 2018 Marek Polacek <polacek@redhat.com> 0.12-1
- new package
