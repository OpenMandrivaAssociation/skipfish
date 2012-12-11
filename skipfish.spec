Name:		skipfish
Version:	2.02
Release:	%mkrel 0.beta.1
Summary:	Collection of simple PIN or passphrase entry dialogs
#http://code.google.com/p/%{name}/downloads/detail?name=%{name}-%{version}b.tgz
# Use: make download
URL:		http://code.google.com/p/skipfish/
Source0:	http://%{name}.googlecode.com/files/%{name}-%{version}b.tgz
Source1:	%{name}-starter
Patch0:		skipfish-1.92b-fhs.patch
License:	GPLv2
Group:		Monitoring
BuildRequires:	libopenssl-devel
BuildRequires:	libidn-devel
BuildRequires:	zlib1-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
A fully automated, active web application security reconnaissance tool. Key
features:
 * High speed: pure C code, highly optimized HTTP handling, minimal CPU
   footprint - easily achieving 2000 requests per second with responsive
   targets.
 * Ease of use: heuristics to support a variety of quirky web frameworks and
   mixed-technology sites, with automatic learning capabilities, on-the-fly
   wordlist creation, and form autocompletion.
 * Cutting-edge security logic: high quality, low false positive, differential
   security checks, capable of spotting a range of subtle flaws, including
   blind injection vectors.

%prep
%setup -q -n %{name}-%{version}b
%patch0 -p1

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -d %{buildroot}/%{_datadir}/%{name}
cp -r assets %{buildroot}/%{_datadir}/%{name}
install -m 644 dictionaries/*.wl %{buildroot}/%{_datadir}/%{name}
ln -s default.wl %{buildroot}/%{_datadir}/%{name}/%{name}.wl

cp dictionaries/README-FIRST README.dictionaries

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README README.dictionaries ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}



%changelog
* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-0.beta.1mdv2011
+ Revision: 689084
- new version
- wrap long lines in package description
- switch group to monitoring, as all other security-related tools

* Sun Jul 03 2011 Lonyai Gergely <aleph@mandriva.org> 2.01-0.0.beta.1
+ Revision: 688601
- 2.01b

* Mon Jun 27 2011 Lonyai Gergely <aleph@mandriva.org> 2.00-0.0.beta.1
+ Revision: 687422
- 2.00b

* Wed Jun 15 2011 Lonyai Gergely <aleph@mandriva.org> 1.94-0.0.beta.1
+ Revision: 685381
- 1.94b

* Fri Jun 10 2011 Lonyai Gergely <aleph@mandriva.org> 1.93-0.0.beta.1
+ Revision: 684129
- 1.93b

* Wed Jun 08 2011 Lonyai Gergely <aleph@mandriva.org> 1.92-0.0.beta.2
+ Revision: 683209
- CCBUG:63456

* Wed Jun 08 2011 Lonyai Gergely <aleph@mandriva.org> 1.92-0.0.beta.1
+ Revision: 683198
- 1.92b

* Sun Jun 05 2011 Lonyai Gergely <aleph@mandriva.org> 1.91-0.0.beta.1
+ Revision: 682779
- 1.91b

* Thu May 19 2011 Lonyai Gergely <aleph@mandriva.org> 1.88-0.0.beta.3
+ Revision: 676176
- Modify the skipfish wrapper script

* Wed May 11 2011 Lonyai Gergely <aleph@mandriva.org> 1.88-0.0.beta.2
+ Revision: 673456
- 1.88b

* Tue May 10 2011 Lonyai Gergely <aleph@mandriva.org> 1.87-0.0.beta.2
+ Revision: 673288
- release
- Update build dependency
- 1.87b
- Add dependency to 2010.2/bacports

* Thu Apr 07 2011 Lonyai Gergely <aleph@mandriva.org> 1.86-0.0.beta.1
+ Revision: 651422
- 1.86b

* Wed Mar 23 2011 Lonyai Gergely <aleph@mandriva.org> 1.85-0.0.beta.1
+ Revision: 647778
- 1.85b

* Thu Dec 16 2010 Lonyai Gergely <aleph@mandriva.org> 1.84-0.0.beta.1mdv2011.0
+ Revision: 622272
- Update the SOURCE0
- 1.84b

* Tue Nov 30 2010 Lonyai Gergely <aleph@mandriva.org> 1.81-0.0.beta.1mdv2011.0
+ Revision: 603591
- Change zlib to libzlib dependency
- 1.81b

* Mon Nov 29 2010 Lonyai Gergely <aleph@mandriva.org> 1.80-0.0.beta.0.1mdv2011.0
+ Revision: 602995
- 1.80b

* Thu Nov 25 2010 Lonyai Gergely <aleph@mandriva.org> 1.79-0.0.beta.0.1mdv2011.0
+ Revision: 601170
- 1.79b

* Mon Nov 22 2010 Lonyai Gergely <aleph@mandriva.org> 1.78-0.0.beta.0.1mdv2011.0
+ Revision: 599685
- 1.78b

* Thu Nov 18 2010 Lonyai Gergely <aleph@mandriva.org> 1.72-0.0.beta.0.1mdv2011.0
+ Revision: 598795
- 1.72b
  First working release.

* Fri Nov 05 2010 Lonyai Gergely <aleph@mandriva.org> 1.69-0.0.beta1mdv2011.0
+ Revision: 593685
- Initial version
  1.69b
- create skipfish

