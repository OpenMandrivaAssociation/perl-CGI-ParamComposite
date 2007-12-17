%define real_name CGI-ParamComposite

Summary:	CGI-ParamComposite module for perl 
Name:		perl-%{real_name}
Version:	0.02
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(CGI)
BuildArch:	noarch

%description
Convert .-delimited CGI parameters to Perl classes/objects.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CGI/ParamComposite.pm
%{_mandir}/*/*




