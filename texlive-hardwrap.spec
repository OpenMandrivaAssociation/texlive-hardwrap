Name:		texlive-hardwrap
Version:	21396
Release:	1
Summary:	Hard wrap text to a certain character length
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hardwrap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates wrapping text to a specific character
width, breaking lines by words rather than, as done by TeX, by
characters. The primary use for these facilities is to aid the
generation of messages sent to the log file or console output
to display messages to the user. Package authors may also find
this useful when writing out arbitary text to an external file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hardwrap/hardwrap.sty
%doc %{_texmfdistdir}/doc/latex/hardwrap/README
%doc %{_texmfdistdir}/doc/latex/hardwrap/hardwrap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hardwrap/hardwrap.dtx
%doc %{_texmfdistdir}/source/latex/hardwrap/hardwrap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
