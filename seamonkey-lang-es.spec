%define	_lang	es
%define	_reg	ES
%define	_lare	%{_lang}-%{_reg}
Summary:	Spanish resources for SeaMonkey
Summary(ca.UTF-8):	Recursos espanyols per a SeaMonkey
Summary(es.UTF-8):	Recursos españoles para SeaMonkey
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-es
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized//seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	af5bec70f682d09ba1c6f811c51ce3e8
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lare}-0.9x.xpi
# Source1-md5:	b4600f86bce0ab816bb2896a936eecaa
Source2:	gen-installed-chrome.sh
URL:		http://nave.hispalinux.es/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
Obsoletes:	mozilla-lang-es
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Spanish resources for SeaMonkey.

%description -l ca.UTF-8
Recursos espanyols per a SeaMonkey.

%description -l es.UTF-8
Recursos españoles para SeaMonkey.

%description -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale \
	chrome/{%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
		> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
	$RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
