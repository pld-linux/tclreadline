Summary:	Readline Tcl extension
Summary(pl.UTF-8):	Rozszerzenie Readline dla Tcl-a
Name:		tclreadline
Version:	2.1.0
Release:	4
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tclreadline/%{name}-%{version}.tar.gz
# Source0-md5:	219d0247a1373578080940ebde53bdd0
Patch0:		%{name}-amd64.patch
URL:		http://tclreadline.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	tcl-devel >= 8.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tclreadline package makes the GNU readline library available for
interactive Tcl shells. This includes history expansion and
file/command completion. Command completion for all Tcl/Tk commands is
provided and commmand completers for user defined commands can be
easily added. tclreadline can also be used for Tcl scripts which want
to use a shell like input interface. In this case the
::tclreadline::readline read command has to be called explicitly.

The advantage of tclreadline is that it uses the callback handler
mechanism of the GNU readline while it processes Tcl events. This way
X events from a wish GUI will processed as well as events from the
tclreadline line interface.

%description -l pl.UTF-8
Pakiet tclreadline udostępnia bibliotekę GNU Readline dla
interaktywnych powłok Tcl-a. Obejmuje to rozwijanie historii oraz
dopełnianie nazw plików i poleceń. Udostępnione jest dopełnianie
poleceń dla wszystkich poleceń Tcl/Tk, a obsługa dopełniania poleceń
zdefiniowanych przez użytkownika może być łatwo dodana. tclreadline
może być używany także dla skryptów Tcl chcących używać interfejsu
wejściowego w stylu powłoki. W tym przypadku polecenie czytające
::tclreadline::readline musi być wywołane explicite.

Zaletą tclreadline jest to, że używa mechanizmu obsługi przez callback
z GNU readline podczas przetwarzania zdarzeń Tcl. W ten sposób będą
przetwarzane zarówno zdarzenia X z interfejsu graficznego wish, jak i
te z interfejsu liniowego tclreadline.

%package devel
Summary:	Readline Tcl extension developement files
Summary(pl.UTF-8):	Pliki do tworzenia z wykorzystaniem tclreadline
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Readline Tcl extension developement files.

%description devel -l pl.UTF-8
Pliki do tworzenia z wykorzystaniem tclreadline.

%package static
Summary:	Static Readline Tcl extension libraries
Summary(pl.UTF-8):	Statyczne biblioteki tclreadline
Group:		Development/Languages/Tcl
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Readline Tcl extension libraries.

%description static -l pl.UTF-8
Statyczne biblioteki tclreadline.

%prep
%setup -q
%patch0 -p1

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal} -I aux
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

ln -sf libtclreadline-%{version}.so $RPM_BUILD_ROOT%{_libdir}/libtclreadline.so.0.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}%{version}
%{_libdir}/%{name}%{version}/*.tcl
%{_mandir}/mann/*.n*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
