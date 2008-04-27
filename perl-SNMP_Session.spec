Summary:	SNMP support for Perl 5
Name:		perl-SNMP_Session
Version:	1.12
Release:	%mkrel 1
Group:		Development/Perl
License:	Artistic
URL:		http://www.switch.ch/misc/leinen/snmp/perl/
Source0:	http://www.switch.ch/misc/leinen/snmp/perl/dist/SNMP_Session-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pure Perl SNMP v1 and SNMP v2 support for Perl 5.

The SNMP operations currently supported are "get", "get-next", "get-bulk"
and "set", as well as trap generation and reception. 

%prep

%setup -q -n SNMP_Session-%{version}
%{__perl} -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' test/*
chmod -c 644 test/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Artistic README README.SNMP_util index.html test/
%{perl_vendorlib}/*
