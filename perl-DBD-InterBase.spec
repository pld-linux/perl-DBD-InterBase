#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database and interaction)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	InterBase
Summary:	DBD::InterBase perl module
Summary(pl):	Modu³ perla DBD::InterBase
Name:		perl-DBD-InterBase
Version:	0.41
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dde9cfd991cd73eae925c82a42405e07
Patch0:		%{name}-libsonly.patch
BuildRequires:	Firebird-devel
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::InterBase - DBI driver for InterBase RDBMS server.

%description -l pl
DBD::InterBase - sterownik DBI do serwera baz danych InterBase.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{!?with_tests:%patch -p1}

%build
%{__perl} Makefile.PL %{!?with_tests:</dev/null} \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/DBD/InterBase.pm
%dir %{perl_vendorarch}/DBD/InterBase
%{perl_vendorarch}/DBD/InterBase/GetInfo.pm
%dir %{perl_vendorarch}/auto/DBD/InterBase
%{perl_vendorarch}/auto/DBD/InterBase/InterBase.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/InterBase/InterBase.so
%{_mandir}/man3/*
