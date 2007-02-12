# TODO:
# - fix add-dns.pl - remove hardcoded config entries
%include	/usr/lib/rpm/macros.perl
Summary:	autodns - configuration of secondary DNS via email
Summary(pl.UTF-8):	autodns - konfiguracja secondary DNS poprzez e-mail
Name:		autodns
Version:	0.0.8
Release:	0.9
License:	GPL
Group:		Applications/Networking
Source0:	http://www.earth.li/projectpurple/files/%{name}-%{version}.tar.gz
# Source0-md5:	2e86ed357f6ef6bf82be1e024d7a8f38
Source1:	%{name}.conf
Patch0:		%{name}-config.patch
URL:		http://www.earth.li/projectpurple/progs/autodns.html
Requires:	bind
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
autodns is an easy way to enable configuration of secondary DNS via
email. It's used by the author in conjunction with BIND, but with
minimal effort should work with any DNS server.

%description -l pl.UTF-8
autodns umożliwia łatwą konfigurację secondary DNS-a poprzez e-mail.
Jest używany przez autora w połączeniu z BINDem, ale minimalny wkład
pracy powinien umożliwić jego współpracę z dowolnym serwerem DNS.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/var/lib/%{name},/etc/%{name}}

install autodns.pl contrib/add-dns.pl $RPM_BUILD_ROOT%{_bindir}
install autodns.users $RPM_BUILD_ROOT/etc/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/%{name}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- autodns < 0.0.8
echo "Upgrading from version < 0.0.8"
if [ -e /etc/autodns.conf.rpmsave ]; then
        cp /etc/autodns/autodns.conf /etc/autodns/autodns.conf.rpmnew
        cp /etc/autodns.conf.rpmsave /etc/autodns/autodns.conf
fi

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS HISTORY README TODO
%attr(751,root,named) %dir /etc/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/%{name}/%{name}.conf
%attr(640,root,named) %config(noreplace) %verify(not md5 mtime size) /etc/%{name}/autodns.users
%attr(755,root,root) %{_bindir}/*
%attr(771,root,named) %dir /var/lib/%{name}
