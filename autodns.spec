Summary:	autodns - configuration of secondary DNS via email
Summary(pl):	autodns - konfiguracja secondary DNS poprzez e-mail
Name:		autodns
Version:	0.0.6
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.earth.li/projectpurple/files/%{name}-%{version}.tar.gz
# Source0-md5:  03c6a8a4d6447b99ed18d40c627733d3
URL:		http://www.earth.li/projectpurple/progs/autodns.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
autodns is an easy way to enable configuration of secondary DNS via
email. It's used by the author in conjunction with BIND, but with
minimal effort should work with any DNS server.

%description -l pl
autodns umo�liwia �atw� konfiguracj� secondary DNS-a poprzez e-mail.
Jest u�ywany przez autora w po��czeniu z BINDem, ale minimalny wk�ad
pracy powinien umo�liwi� jego wsp�prac� z dowolnym serwerem DNS.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install autodns.pl contrib/add-dns.pl $RPM_BUILD_ROOT%{_bindir}
install autodns.users $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS HISTORY README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
