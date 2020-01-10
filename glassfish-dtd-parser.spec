Name: glassfish-dtd-parser
Version: 1.2
Release: 0.8.20120120svn%{?dist}
Summary: Library for parsing XML DTDs
Group: Development/Libraries
License: CDDL 1.1 and GPLv2 with exceptions
Url: http://java.net/projects/dtd-parser

# svn export https://svn.java.net/svn/dtd-parser~svn/trunk/dtd-parser glassfish-dtd-parser-1.2-SNAPSHOT
# find glassfish-dtd-parser-1.2-SNAPSHOT/ -name '*.jar' -delete
# tar czf glassfish-dtd-parser-1.2-SNAPSHOT-src-svn.tar.gz glassfish-dtd-parser-1.2-SNAPSHOT
Source0: %{name}-%{version}-SNAPSHOT-src-svn.tar.gz

BuildRequires: maven-local

Requires: jpackage-utils

BuildArch: noarch


%description
Library for parsing XML DTDs.


%package javadoc
Group: Development/Libraries
Summary: Javadoc for %{name}
Requires: jpackage-utils


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n glassfish-dtd-parser-1.2-SNAPSHOT


%build
%mvn_build


%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-0.8.20120120svn
- Mass rebuild 2013-12-27

* Thu Oct 24 2013 Ade Lee <alee@redhat.com> - 1.2-0.7.20120120svn
- Resolves: rhbz#1017803 - glassfish-fastinfoset: mock build failed on RHEL 7

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.6.20120120svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-0.5.20120120svn
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.20120120svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.2-0.3.20120120svn
- Fixed the release number

* Mon Feb 13 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.2-0.2.20120120svn
- Updated license reference

* Mon Feb 13 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.2-0.1.20120120svn
- Initial packaging
