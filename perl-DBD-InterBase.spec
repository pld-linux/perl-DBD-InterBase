#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database and interaction)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	InterBase
Summary:	DBD::InterBase - DBI driver for Firebird and InterBase RDBMS server
Summary(pl.UTF-8):	DBD::InterBase - sterownik DBI dla serwerów RDBMS Firebird i InterBase
Name:		perl-DBD-InterBase
Version:	0.44
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fae62d5448c612c2ef61572793800f4f
Patch0:		%{name}-libsonly.patch
BuildRequires:	Firebird-devel
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::InterBase is a Perl module which works with the DBI module to
provide access to Firebird and InterBase databases.

%description -l pl.UTF-8
DBD::InterBase jest modułem Perla współpracującym z modułem DBI i
umożliwiającym dostęp do baz danych Firebird i InterBase.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{!?with_tests:%patch0 -p1}

%build
%{__perl} Makefile.PL %{!?with_tests:</dev/null} \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%{_mandir}/man3/DBD*
