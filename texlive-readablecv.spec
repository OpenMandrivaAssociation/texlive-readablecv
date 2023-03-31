Name:		texlive-readablecv
Version:	61719
Release:	2
Summary:	A highly readable and good looking CV and letter class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/readablecv
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/readablecv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/readablecv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class provides, what I have found, to be an extremely
attractive and highly readable CV which will lead to your CV
being read rather than disgarded.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/readablecv
%doc %{_texmfdistdir}/doc/latex/readablecv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
