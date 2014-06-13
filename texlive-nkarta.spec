# revision 16437
# category Package
# catalog-ctan /fonts/nkarta
# catalog-date 2009-12-20 19:35:44 +0100
# catalog-license pd
# catalog-version 0.2
Name:		texlive-nkarta
Version:	0.2
Release:	7
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 754348
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719122
- texlive-nkarta
- texlive-nkarta
- texlive-nkarta
- texlive-nkarta

