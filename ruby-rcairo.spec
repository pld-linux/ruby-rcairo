%define pkgname rcairo
Summary:	Cairo module for Ruby
Summary(pl.UTF-8):	Moduł Cairo dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.16.6
Release:	1
License:	GPL v2+ or custom (see COPYING)
Group:		Development/Languages
Source0:	https://www.cairographics.org/releases/rcairo-%{version}.tar.gz
# Source0-md5:	b3890cc249d5b4cdee100fdb438faf53
Patch0:		%{name}-hdr.patch
Patch1:		no-native-packages.patch
URL:		https://www.cairographics.org/rcairo/
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.410
BuildRequires:	ruby-devel >= 1:1.8
BuildRequires:	ruby-native-package-installer >= 1.0.3
BuildRequires:	ruby-pkg-config >= 1.2.2
BuildRequires:	sed >= 4.0
Requires:	cairo >= 1.14.0
Requires:	ruby >= 1:1.8
# dropped?
Obsoletes:	ruby-rcairo-gtkcairo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TODO: move this to rpm macros.build
%define		ruby_hdrdir	%(%{__ruby} -r rbconfig -e 'print RbConfig::CONFIG["rubyhdrdir"]')

%description
Cairo module for Ruby.

%description -l pl.UTF-8
Moduł Cairo dla języka Ruby.

%package devel
Summary:	Header file for Ruby rcairo extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia rcairo dla języka Ruby
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.14.0
Requires:	ruby-devel >= 1:1.8

%description devel
Header file for Ruby rcairo extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia rcairo dla języka Ruby.

%prep
%setup -q -n rcairo-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,/usr/bin/env ruby,%{__ruby},' samples/*.rb samples/agg/*.rb

%build
%{__ruby} extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_hdrdir},%{_examplesdir}/%{name}-%{version}}

%{__make} -j1 install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_vendorlibdir} \
	RUBYHDRDIR=$RPM_BUILD_ROOT%{ruby_hdrdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_vendorarchdir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.rdoc
%attr(755,root,root) %{ruby_vendorarchdir}/cairo.so
%{ruby_vendorlibdir}/cairo
%{ruby_vendorlibdir}/cairo.rb
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{ruby_hdrdir}/rb_cairo.h
