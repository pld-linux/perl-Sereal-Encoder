# TODO: system libcsnappy, libminiz?
#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Sereal
%define		pnam	Encoder
Summary:	Sereal::Encoder - Fast, compact, powerful binary serialization
Summary(pl.UTF-8):	Sereal::Encoder - szybka, zwarta, potężna serializacja binarna
Name:		perl-Sereal-Encoder
Version:	4.025
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/Y/YV/YVES/Sereal-Encoder-%{version}.tar.gz
# Source0-md5:	feaedc77816634c6d6681c0b971eceb9
URL:		https://metacpan.org/release/Sereal-Encoder
BuildRequires:	perl-ExtUtils-MakeMaker >= 7.0
BuildRequires:	perl-ExtUtils-ParseXS >= 2.21
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	zstd-devel
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Sereal-Decoder >= 4.002
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-LongString
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Warn
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements an efficient, compact-output, and feature-rich
serializer using a binary protocol called Sereal. Its sister module
Sereal::Decoder implements a decoder for this format. The two are
released separately to allow for independent and safer upgrading. If
you care greatly about performance, consider reading the
Sereal::Performance documentation.

The Sereal protocol version emitted by this encoder implementation is
currently protocol version 3 by default.

The protocol specification and many other bits of documentation can be
found in the github repository at <https://github.com/Sereal/Sereal>.

%description -l pl.UTF-8
Ten moduł implementuje wydajny, mający zwarte wyjście i wiele
możliwości, serializer wykorzystujący binary protokół o nazwie Sereal.
Siostrzany moduł Sereal::Decoder implementuje dekoder dla tego
formatu. Moduły wydawane są osobno, aby umożliwić niezależne i
bezpieczniejsze aktualizacje. Informacje na temat wydajności można
znaleźć w dokumentacji Sereal::Performance.

Ta implementacja kodera domyślnie produkuje wyjście zgodne z
protokołem Sereal w wersji 3.

Specyfikację protokołu i inną dokumentację można znaleźć w
repozytorium github <https://github.com/Sereal/Sereal>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1 \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorarch}/Sereal
%{perl_vendorarch}/Sereal/Encoder.pm
%dir %{perl_vendorarch}/Sereal/Encoder
%{perl_vendorarch}/Sereal/Encoder/*.pm
%dir %{perl_vendorarch}/auto/Sereal
%dir %{perl_vendorarch}/auto/Sereal/Encoder
%attr(755,root,root) %{perl_vendorarch}/auto/Sereal/Encoder/Encoder.so
%{_mandir}/man3/Sereal::Encoder.3pm*
