%define upstream_name	 Net-OpenDHT
%define upstream_version 0.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Module to access the Open Distributed Hash Table (Open DHT)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(App::Cache)
BuildRequires:	perl(Class::Accessor::Chained)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
The Net::OpenDHT module provides a simple interface to the Open DHT service. 
Open DHT is a publicly accessible distributed hash table (DHT) service. In 
contrast to the usual DHT model, clients of Open DHT do not need to run a 
DHT node in order to use the service. Instead, they can issue put and get 
operations to any DHT node, which processes the operations on their behalf. No
credentials or accounts are required to use the service, and the available 
storage is fairly shared across all active clients.

This service model of DHT usage greatly simplifies deploying client 
applications. By using Open DHT as a highly-available naming and storage 
service, clients can ignore the complexities of deploying and maintaining 
a DHT and instead concentrate on developing more sophisticated distributed 
applications.

What this essentially gives you as a Perl author is robust storage for a small 
amount of data. This can be used as a distributed cache or data store.

Read the following for full semantics about the Open DHT:

  http://opendht.org/users-guide.html


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# (misc) test are disabled because they do not work on the cluster
#make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 406172
- rebuild using %%perl_convert_version

* Fri Mar 06 2009 Michael Scherer <misc@mandriva.org> 0.33-6mdv2009.1
+ Revision: 349900
- rebuild
- disable test as they are not working on the cluster ( trying to access network to
  check the DHT )

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-2mdv2008.0
+ Revision: 88411
- rebuild


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2007.0
- New release 0.33
- spec cleanup

* Fri Jan 06 2006 Michael Scherer <misc@mandriva.org> 0.32-4mdk
- fix missing BuildRequires

* Wed Jan 04 2006 Michael Scherer <misc@mandriva.org> 0.32-3mdk
- Do not ship empty dir

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.32-2mdk
- Fix BuildRequires

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 0.32-1mdk
- First mandriva package

