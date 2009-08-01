%define upstream_name	 Net-OpenDHT
%define upstream_version 0.33

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module to access the Open Distributed Hash Table (Open DHT)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(App::Cache)
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(XML::LibXML)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Exception)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# (misc) test are disabled because they do not work on the cluster
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/man3/*
