Name:		texlive-nkarta
Version:	16437
Release:	2
Summary:	A "new" version of the karta cartographic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/nkarta
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A development of the karta font, offering more mathematical
stability in MetaFont. A version that will produce the glyphs
as Encapsulated PostScript, using MetaPost, is also provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/nkarta/nkarta.mf
%{_texmfdistdir}/fonts/source/public/nkarta/nkarta15.mf
%{_texmfdistdir}/fonts/source/public/nkarta/nkchars.mf
%{_texmfdistdir}/fonts/tfm/public/nkarta/nkarta15.tfm
%{_texmfdistdir}/metapost/nkarta/nkarta.mp
%{_texmfdistdir}/metapost/nkarta/nkchars.mp
%doc %{_texmfdistdir}/doc/fonts/nkarta/README
%doc %{_texmfdistdir}/doc/fonts/nkarta/figtable.pdf
%doc %{_texmfdistdir}/doc/fonts/nkarta/figtable.tex
%doc %{_texmfdistdir}/doc/fonts/nkarta/fonttable.pdf
%doc %{_texmfdistdir}/doc/fonts/nkarta/fonttable.tex
#- source
%doc %{_texmfdistdir}/source/latex/nkarta/nkarta.dtx
%doc %{_texmfdistdir}/source/latex/nkarta/nkarta.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost doc source %{buildroot}%{_texmfdistdir}
