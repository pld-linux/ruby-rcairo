%define pkgname rcairo
Summary:	Cairo module for Ruby
Summary(pl.UTF-8):	Moduł Cairo dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.10.2
Release:	1
License:	GPL or custom (see COPYING)
Group:		Development/Languages
Source0:	http://cairographics.org/releases/rcairo-%{version}.tar.gz
# Source0-md5:	19587b3ace86a096ce8fcb316a2fb9e9
Patch0:		%{name}-hdr.patch
URL:		http://cairographics.org/rcairo/
BuildRequires:	cairo-devel >= 1.10.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
BuildRequires:	ruby-pkg-config
Requires:	cairo >= 1.10.2
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

%prep
%setup -q -n rcairo-%{version}
%patch0 -p1

%build
ruby extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_hdrdir},%{_examplesdir}/%{name}-%{version}}
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

# devel?
%{ruby_hdrdir}/rb_cairo.h
