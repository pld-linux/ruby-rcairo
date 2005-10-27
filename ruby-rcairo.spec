%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Cairo module for Ruby
Summary(pl):	Modu³ Cairo dla jêzyka Ruby
Name:		ruby-rcairo
Version:	1.0.0
Release:	1
License:	GPL or custom (see COPYING)
Group:		Development/Languages
Source0:	http://cairographics.org/releases/rcairo-%{version}.tar.gz
# Source0-md5:	e6c6442b24155146ba986dc7774e45e3
URL:		http://cairographics.org/rcairo
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	ruby-devel >= 1:1.8
Requires:	ruby >= 1:1.8
# dropped?
Obsoletes:	ruby-rcairo-gtkcairo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo module for Ruby.

%description -l pl
Modu³ Cairo dla jêzyka Ruby.

%prep
%setup -q -n rcairo-%{version}

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_examplesdir}/%{name}-%{version}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a samples/* $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ChangeLog NEWS
%attr(755,root,root) %{ruby_archdir}/cairo.so
%{ruby_rubylibdir}/cairo.rb
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/png* 
%{_examplesdir}/%{name}-%{version}/pdf*
%{_examplesdir}/%{name}-%{version}/ps*

# devel?
%{ruby_archdir}/rb_cairo.h
