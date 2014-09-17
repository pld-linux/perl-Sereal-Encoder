#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Sereal
%define		pnam	Encoder
%include	/usr/lib/rpm/macros.perl
Summary:	Sereal::Encoder - Fast, compact, powerful binary serialization
Name:		perl-Sereal-Encoder
Version:	3.002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YV/YVES/Sereal-Encoder-%{version}.tar.gz
# Source0-md5:	18e88a20ae5842f98e2874557d8d525c
URL:		http://search.cpan.org/dist/Sereal-Encoder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Sereal::Decoder) >= 3.00
BuildRequires:	perl-Test-LongString
BuildRequires:	perl-Test-Warn
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements an efficient, compact-output, and feature-rich
serializer using a binary protocol called Sereal. Its sister module
Sereal::Decoder implements a decoder for this format. The two are
released separately to allow for independent and safer upgrading. If
you care greatly about performance, consider reading the
Sereal::Performance documentation after finishing this document.

The Sereal protocol version emitted by this encoder implementation is
currently protocol version 3 by default.

The protocol specification and many other bits of documentation can be
found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod, there is
a discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the
output of our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs. For
more information on getting the best performance out of Sereal, have a
look at the /"PERFORMANCE" section below.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/Sereal/*.pm
%dir %{perl_vendorarch}/Sereal/Encoder
%{perl_vendorarch}/Sereal/Encoder/*.pm
%dir %{perl_vendorarch}/auto/Sereal
%dir %{perl_vendorarch}/auto/Sereal/Encoder
%attr(755,root,root) %{perl_vendorarch}/auto/Sereal/Encoder/*.so
%{_mandir}/man3/*
