%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	FileDialog
Summary:	Tk::FileDialog Perl module - File Dialog widget for Perl/Tk
Summary(cs):	Modul Tk::FileDialog pro Perl
Summary(da):	Perlmodul Tk::FileDialog
Summary(de):	Tk::FileDialog Perl Modul
Summary(es):	Módulo de Perl Tk::FileDialog
Summary(fr):	Module Perl Tk::FileDialog
Summary(it):	Modulo di Perl Tk::FileDialog
Summary(ja):	Tk::FileDialog Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Tk::FileDialog ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Tk::FileDialog
Summary(pl):	Modu³ Perla Tk::FileDialog - okienko dialogowe wyboru plików dla modu³u Tk
Summary(pt):	Módulo de Perl Tk::FileDialog
Summary(pt_BR):	Módulo Perl Tk::FileDialog
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Tk::FileDialog
Summary(sv):	Tk::FileDialog Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Tk::FileDialog
Summary(zh_CN):	Tk::FileDialog Perl Ä£¿é
Name:		perl-Tk-FileDialog
Version:	1.3
Release:	11
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tk/FileDialog.pm
%{_mandir}/man3/*
