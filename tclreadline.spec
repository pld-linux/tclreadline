Summary:	Readline Tcl extension
Summary(pl):	Rozszerzenie Readline dla Tcl
Name:		tclreadline
Version:	2.1.0
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tclreadline/%{name}-%{version}.tar.gz
# Source0-md5:	219d0247a1373578080940ebde53bdd0
URL:		http://tclreadline.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	tcl-devel >= 8.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tclreadline package makes the GNU Readline library available for
interactive tcl shells. This includes history expansion and
file/command completion. Command completion for all tcl/tk commands is
provided and commmand completers for user defined commands can be
easily added. tclreadline can also be used for tcl scripts which want
to use a shell like input interface. In this case the
::tclreadline::readline read command has to be called explicitly.

The advantage of tclreadline is that it uses the callback handler
mechanism of the gnu readline while it processes tcl events. This way
X events from a wish gui will processed as well as events from the
tclreadline line interface.

%package devel
Summary:	Readline Tcl extension developement files
Summary(pl):	Pliki do tworzenia z wykorzystaniem tclreadline
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Readline Tcl extension developement files.

%description devel -l pl
Pliki do tworzenia z wykorzystaniem tclreadline.

%package static
Summary:	Static Readline Tcl extension libraries
Summary(pl):	Statyczne biblioteki tclreadline
Group:		Development/Languages/Tcl
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Readline Tcl extension libraries.

%description static -l pl
Statyczne biblioteki tclreadline.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root)  %{_libdir}/*.so
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
