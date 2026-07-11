%global tl_name hardwrap
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Hard wrap text to a certain character length
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hardwrap
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hardwrap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package facilitates wrapping text to a specific character width,
breaking lines by words rather than, as done by TeX, by characters. The
primary use for these facilities is to aid the generation of messages
sent to the log file or console output to display messages to the user.
Package authors may also find this useful when writing out arbitrary
text to an external file.

