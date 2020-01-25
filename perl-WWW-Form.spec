#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	WWW
%define		pnam	Form
Summary:	Object-oriented module for HTML form input validation and display
Summary(pl.UTF-8):	Obiektowo zorientowany moduł do sprawdzania poprawności i wyświetlania formularzy HTML
Name:		perl-WWW-Form
Version:	1.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3de0bb7571a73d3316536b947077ede
URL:		http://search.cpan.org/dist/WWW-Form/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented module for HTML form input validation and display.

%description -l pl.UTF-8
Obiektowo zorientowany moduł do sprawdzania poprawności i wyświetlania
formularzy HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/*
%{_mandir}/man3/*
