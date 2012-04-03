%define pkgname rcairo
Summary:	Cairo module for Ruby
Summary(pl.UTF-8):	Moduł Cairo dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.12.1
Release:	1
License:	GPL or custom (see COPYING)
Group:		Development/Languages
Source0:	http://cairographics.org/releases/rcairo-%{version}.tar.gz
# Source0-md5:	dae99e1159c6791b7671fe8f43c0ca26
Patch0:		%{name}-hdr.patch
URL:		http://cairographics.org/rcairo/
BuildRequires:	cairo-devel >= 1.12.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
BuildRequires:	ruby-pkg-config
Requires:	cairo >= 1.12.0
Requires:	ruby >= 1:1.8
# dropped?
Obsoletes:	ruby-rcairo-gtkcairo
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# TODO: move this to rpm macros.build
%define 	ruby_hdrdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubyhdrdir"]')

%description
Cairo module for Ruby.

%description -l pl.UTF-8
Moduł Cairo dla języka Ruby.

%package devel
Summary:	Header file for Ruby rcairo extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia rcairo dla języka Ruby
Group:		Development/Libraries
Requires:	cairo-devel >= 1.12.0
Requires:	ruby-devel >= 1:1.8

%description devel
Header file for Ruby rcairo extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia rcairo dla języka Ruby.

%prep
%setup -q -n rcairo-%{version}
%patch0 -p1

%build
ruby extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_hdrdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	RUBYHDRDIR=$RPM_BUILD_ROOT%{ruby_hdrdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.rdoc
%attr(755,root,root) %{ruby_archdir}/cairo.so
%{ruby_rubylibdir}/cairo
%{ruby_rubylibdir}/cairo.rb
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{ruby_hdrdir}/rb_cairo.h
