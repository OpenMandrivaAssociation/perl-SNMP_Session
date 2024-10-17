Summary:	SNMP support for Perl 5
Name:		perl-SNMP_Session
Version:	1.13
Release:	4
Group:		Development/Perl
License:	Artistic
URL:		https://code.google.com/p/snmp-session/
Source0:	http://snmp-session.googlecode.com/files/SNMP_Session-%{version}.tar.gz
Patch:      SNMP_Session-1.13-fix-ipv6-error-messages.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pure Perl SNMP v1 and SNMP v2 support for Perl 5.

The SNMP operations currently supported are "get", "get-next", "get-bulk"
and "set", as well as trap generation and reception. 

%prep
%setup -q -n SNMP_Session-%{version}
%patch -p 1
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' test/*

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Artistic README README.SNMP_util index.html test
%{perl_vendorlib}/SNMP_Session.pm
%{perl_vendorlib}/SNMP_util.pm
%{perl_vendorlib}/BER.pm

%changelog
* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2010.1
+ Revision: 468580
- add redhat patch to fix prototype mismatch error messages (#55027)
- new version
- spec cleanup

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.12-3mdv2010.0
+ Revision: 430537
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.12-2mdv2009.0
+ Revision: 268717
- rebuild early 2009.0 package (before pixel changes)

  + Oden Eriksson <oeriksson@mandriva.com>
    - 1.12

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.10-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdv2008.0
+ Revision: 81493
- Import perl-SNMP_Session



* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdv2008.0
- initial Mandriva package (fedora import)
