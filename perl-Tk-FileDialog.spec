%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	FileDialog
Summary:	Tk::FileDialog Perl module - File Dialog widget for Perl/Tk
Summary(pl):	Modu³ Perla Tk::FileDialog - okienko dialogowe wyboru plików dla modu³u Tk
Name:		perl-Tk-FileDialog
Version:	1.3
Release:	10
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::FileDialog - A highly configurable File Dialog widget for Perl/Tk.

%description -l pl
Modu³ Tk::FileDialog - wysoko konfigurowalne okienko dialogowe wyboru
plików dla modu³u Tk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Tk/FileDialog.pm
%{_mandir}/man3/*
