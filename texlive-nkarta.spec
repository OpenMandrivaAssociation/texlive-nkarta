%global tl_name nkarta
%global tl_revision 16437

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A new version of the karta cartographic fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/nkarta
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A development of the karta font, offering more mathematical stability in
Metafont. A version that will produce the glyphs as Encapsulated
PostScript, using MetaPost, is also provided.

