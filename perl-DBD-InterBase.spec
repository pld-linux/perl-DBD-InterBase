%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	InterBase
Summary:	DBD::InterBase perl module
Summary(pl):	Modu³ perla DBD::InterBase
Name:		perl-DBD-InterBase
Version:	0.30
Release:	0.2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	rpm-perlprov >= 3.0.3-16
#BR: InterBase libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::InterBase - DBI driver for InterBase RDBMS server.

%description -l pl
DBD::InterBase - sterownik DBI do serwera baz danych InterBase.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
#%{perl_sitearch}/???
%{_mandir}/man3/*
