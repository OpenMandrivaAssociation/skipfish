Name:		skipfish
Version:	1.69
Release:	%mkrel 0.0.beta1
Summary:	Collection of simple PIN or passphrase entry dialogs
#http://code.google.com/p/%{name}/downloads/detail?name=%{name}-%{version}b.tgz
Source0:	%{name}-%{version}b.tgz
License:	GPLv2
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://code.google.com/p/skipfish/
BuildRequires:	libopenssl-devel
BuildRequires:	libidn-devel
BuildRequires:	zlib1-devel


%description 
A fully automated, active web application security reconnaissance tool. Key features:
 * High speed: pure C code, highly optimized HTTP handling, minimal CPU footprint - easily achieving 2000 requests per second with responsive targets.
 * Ease of use: heuristics to support a variety of quirky web frameworks and mixed-technology sites, with automatic learning capabilities, on-the-fly wordlist creation, and form autocompletion.
 * Cutting-edge security logic: high quality, low false positive, differential security checks, capable of spotting a range of subtle flaws, including blind injection vectors.

%prep
%setup -q -n %{name}-%{version}b

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

