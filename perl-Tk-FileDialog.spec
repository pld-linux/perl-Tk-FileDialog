%include	/usr/lib/rpm/macros.perl
Summary:	Tk-FileDialog perl module
Summary(pl):	Modu� perla Tk-FileDialog
Name:		perl-Tk-FileDialog
Version:	1.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tk/Tk-FileDialog-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Tk
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk-FileDialog perl module.

%description -l pl
Modu� perla Tk-FileDialog.

%prep
%setup -q -n Tk-FileDialog-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tk/FileDialog
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Tk/FileDialog.pm
%{perl_sitearch}/auto/Tk/FileDialog

%{_mandir}/man3/*
