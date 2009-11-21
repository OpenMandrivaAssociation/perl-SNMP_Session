Summary:	SNMP support for Perl 5
Name:		perl-SNMP_Session
Version:	1.13
Release:	%mkrel 1
Group:		Development/Perl
License:	Artistic
URL:		http://code.google.com/p/snmp-session/
Source0:	http://snmp-session.googlecode.com/files/SNMP_Session-%{version}.tar.gz
Patch:      SNMP_Session-1.13-fix-ipv6-error-messages.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Pure Perl SNMP v1 and SNMP v2 support for Perl 5.

The SNMP operations currently supported are "get", "get-next", "get-bulk"
and "set", as well as trap generation and reception. 

%prep
%setup -q -n SNMP_Session-%{version}
%patch -p 1
%{__perl} -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' test/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Artistic README README.SNMP_util index.html test
%{perl_vendorlib}/SNMP_Session.pm
%{perl_vendorlib}/SNMP_util.pm
%{perl_vendorlib}/BER.pm
