%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	FileDialog
Summary:	Tk::FileDialog Perl module - file dialog widget for Perl/Tk
Summary(pl.UTF-8):	Moduł Perla Tk::FileDialog - okienko dialogowe wyboru plików dla modułu Perla Tk
Name:		perl-Tk-FileDialog
Version:	1.3
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85e87b83edc4f7d4ce8bd974e1c53497
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::FileDialog - A highly configurable File Dialog widget for Perl/Tk.

%description -l pl.UTF-8
Moduł Tk::FileDialog - wysoko konfigurowalne okienko dialogowe wyboru
plików dla modułu Tk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tk/FileDialog.pm
%{_mandir}/man3/*
