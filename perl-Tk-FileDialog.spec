%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	FileDialog
Summary:	Tk::FileDialog Perl module - File Dialog widget for Perl/Tk
Summary(cs):	Modul Tk::FileDialog pro Perl
Summary(da):	Perlmodul Tk::FileDialog
Summary(de):	Tk::FileDialog Perl Modul
Summary(es):	M�dulo de Perl Tk::FileDialog
Summary(fr):	Module Perl Tk::FileDialog
Summary(it):	Modulo di Perl Tk::FileDialog
Summary(ja):	Tk::FileDialog Perl �⥸�塼��
Summary(ko):	Tk::FileDialog �� ����
Summary(no):	Perlmodul Tk::FileDialog
Summary(pl):	Modu� Perla Tk::FileDialog - okienko dialogowe wyboru plik�w dla modu�u Tk
Summary(pt):	M�dulo de Perl Tk::FileDialog
Summary(pt_BR):	M�dulo Perl Tk::FileDialog
Summary(ru):	������ ��� Perl Tk::FileDialog
Summary(sv):	Tk::FileDialog Perlmodul
Summary(uk):	������ ��� Perl Tk::FileDialog
Summary(zh_CN):	Tk::FileDialog Perl ģ��
Name:		perl-Tk-FileDialog
Version:	1.3
Release:	10
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::FileDialog - A highly configurable File Dialog widget for Perl/Tk.

%description -l pl
Modu� Tk::FileDialog - wysoko konfigurowalne okienko dialogowe wyboru
plik�w dla modu�u Tk.

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
