#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-StackTrace-AsHTML
Version  : 0.15
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-0.15.tar.gz
Summary  : 'Displays stack trace in HTML'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-StackTrace-AsHTML-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::StackTrace)

%description
NAME
Devel::StackTrace::AsHTML - Displays stack trace in HTML
SYNOPSIS
use Devel::StackTrace::AsHTML;

my $trace = Devel::StackTrace->new;
my $html  = $trace->as_html;

%package dev
Summary: dev components for the perl-Devel-StackTrace-AsHTML package.
Group: Development
Provides: perl-Devel-StackTrace-AsHTML-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-StackTrace-AsHTML package.


%package license
Summary: license components for the perl-Devel-StackTrace-AsHTML package.
Group: Default

%description license
license components for the perl-Devel-StackTrace-AsHTML package.


%prep
%setup -q -n Devel-StackTrace-AsHTML-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-StackTrace-AsHTML
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-StackTrace-AsHTML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Devel/StackTrace/AsHTML.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::StackTrace::AsHTML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-StackTrace-AsHTML/LICENSE
