# revision 16437
# category Package
# catalog-ctan /fonts/nkarta
# catalog-date 2009-12-20 19:35:44 +0100
# catalog-license pd
# catalog-version 0.2
Name:		texlive-nkarta
Version:	0.2
Release:	1
Summary:	A "new" version of the karta cartographic fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/nkarta
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nkarta.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A development of the karta font, offering more mathematical
stability in MetaFont. A version that will produce the glyphs
as Encapsulated PostScript, using MetaPost, is also provided.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
