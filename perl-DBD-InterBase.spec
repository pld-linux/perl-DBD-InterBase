#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	InterBase
Summary:	DBD::InterBase perl module
Summary(pl):	Modu³ perla DBD::InterBase
Name:		perl-DBD-InterBase
Version:	0.40
Release:	0.2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	rpm-perlprov >= 4.0.2-104
#BR: InterBase libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::InterBase - DBI driver for InterBase RDBMS server.

%description -l pl
DBD::InterBase - sterownik DBI do serwera baz danych InterBase.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
#%%{perl_sitearch}/???
%{_mandir}/man3/*
