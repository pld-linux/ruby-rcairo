%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Cairo module for Ruby
Summary(pl):	Modu³ Cairo dla Ruby
Name:		ruby-rcairo
Version:	0.1
%define snap 20050208
Release:	0.%{snap}.1
License:	GPL
Group:		Development/Languages
Source0:	http://cairographics.org/~pippin/cairo/ruby/rcairo-%{snap}.tar.gz
# Source0-md5:	a3b550934bce96eeebb9c458fe6e7237
URL:		http://www2.giganet.net/~yoshi/
BuildRequires:	cairo-devel
BuildRequires:	gtkcairo-devel
BuildRequires:	pkgconfig
BuildRequires:	ruby-devel
# mkmf-gnome2.rb
BuildRequires:	ruby-gnome2
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo module for Ruby.

%description -l pl
Modu³ Cairo dla Ruby.

%package gtkcairo
Summary: 	GTKCairo Library for Ruby
Summary(pl):	Biblioteki GTKCairo dla Ruby
Group:		Development/Languages

%description gtkcairo
GTKCairo Library for Ruby.

%description gtkcairo -l pl
Biblioteki GTKCairo dla Ruby.

%prep
%setup -q -n rcairo

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
%doc README
%attr(755,root,root) %{ruby_archdir}/cairo.so
%{ruby_rubylibdir}/cairo.rb
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/png* 
%{_examplesdir}/%{name}-%{version}/pdf*
%{_examplesdir}/%{name}-%{version}/ps*

%files gtkcairo
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/gtkcairo.so
%{ruby_rubylibdir}/canvas.rb
%{_examplesdir}/%{name}-%{version}/gtk*
%{_examplesdir}/%{name}-%{version}/canvas
