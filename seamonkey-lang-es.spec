Summary:	Spanish resources for SeaMonkey
Summary(ca):	Recursos espanyols per a SeaMonkey
Summary(es):	Recursos españoles para SeaMonkey
Summary(pl):	Hiszpañskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-es
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://sunsite.rediris.es/mirror/NAVE/seamonkey/%{version}/descargas/seamonkey-%{version}.es-ES.langpack.xpi
# Source0-md5:	f2d8e9c61ead16eaee93557661698b4f
Source1:	gen-installed-chrome.sh
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
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{es-ES,es-unix}.jar > lang-es-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{es-ES,es-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-es-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/es-ES.jar
%{_chromedir}/es-unix.jar
%{_chromedir}/lang-es-installed-chrome.txt
