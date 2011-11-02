Name:		texlive-hardwrap
Version:	0.2
Release:	1
Summary:	Hard wrap text to a certain character length
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hardwrap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package facilitates wrapping text to a specific character
width, breaking lines by words rather than, as done by TeX, by
characters. The primary use for these facilities is to aid the
generation of messages sent to the log file or console output
to display messages to the user. Package authors may also find
this useful when writing out arbitary text to an external file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
