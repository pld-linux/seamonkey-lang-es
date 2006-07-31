%define	_lang	es
%define	_reg	ES
%define	_lare	%{_lang}-%{_reg}
Summary:	Spanish resources for SeaMonkey
Summary(ca):	Recursos espanyols per a SeaMonkey
Summary(es):	Recursos españoles para SeaMonkey
Summary(pl):	Hiszpañskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-es
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://sunsite.rediris.es/mirror/NAVE/seamonkey/%{version}/descargas/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	8470f74ad958da540d710fb5c069dcba
Source1:	http://sunsite.rediris.es/mirror/NAVE/seamonkey/%{version}/descargas/seamonkey-%{version}.%{_lare}.regpack.xpi
# Source1-md5:	fc06a54988e23020fb1ee3e1b9c4ff59
Source2:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lare}-0.9x.xpi
# Source2-md5:	4e147df61d36030bb2754ab702da8491
Source3:	gen-installed-chrome.sh
URL:		http://nave.hispalinux.es/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Spanish resources for SeaMonkey.

%description -l ca
Recursos espanyols per a SeaMonkey.

%description -l es
Recursos españoles para SeaMonkey.

%description -l pl
Hiszpañskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
%{__unzip} -o -qq %{SOURCE2}
install %{SOURCE3} .
./gen-installed-chrome.sh locale \
	chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
		> lang-%{_lang}-installed-chrome.txt
rm bin/searchplugins/{dmoz,google,jeeves}.*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
	$RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/searchplugins $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
