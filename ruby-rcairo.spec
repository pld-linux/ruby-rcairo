%define pkgname rcairo
Summary:	Cairo module for Ruby
Summary(pl.UTF-8):	Moduł Cairo dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.8.1
Release:	1
License:	GPL or custom (see COPYING)
Group:		Development/Languages
Source0:	http://cairographics.org/releases/rcairo-%{version}.tar.gz
# Source0-md5:	14efc24f0cbe281b32882d64f1b0d4b9
URL:		http://cairographics.org/rcairo
BuildRequires:	cairo-devel >= 1.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
Requires:	cairo >= 1.8.0
Requires:	ruby >= 1:1.8
# dropped?
Obsoletes:	ruby-rcairo-gtkcairo
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo module for Ruby.

%description -l pl.UTF-8
Moduł Cairo dla języka Ruby.

%prep
%setup -q -n rcairo-%{version}

%build
ruby extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ChangeLog NEWS
%attr(755,root,root) %{ruby_archdir}/cairo.so
%{ruby_rubylibdir}/cairo
%{ruby_rubylibdir}/cairo.rb
%{_examplesdir}/%{name}-%{version}

# devel?
%{ruby_archdir}/rb_cairo.h
