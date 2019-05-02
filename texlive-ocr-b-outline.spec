# revision 20969
# category Package
# catalog-ctan /fonts/ocr-b-outline
# catalog-date 2011-01-07 10:11:51 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-ocr-b-outline
Version:	20190228
Release:	1
Summary:	OCR-B fonts in Type 1 and OpenType
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ocr-b-outline
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains OCR-B fonts in Type1 and OpenType formats.
They were generated from the MetaFont sources of the OCR-B
fonts. The metric files are not included here, so that original
ocr-b package should also be installed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/ocr-b-outline/ocrb.map
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb10.otf
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb5.otf
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb6.otf
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb7.otf
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb8.otf
%{_texmfdistdir}/fonts/opentype/public/ocr-b-outline/ocrb9.otf
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb10.pfb
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb5.pfb
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb6.pfb
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb7.pfb
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb8.pfb
%{_texmfdistdir}/fonts/type1/public/ocr-b-outline/ocrb9.pfb
%doc %{_texmfdistdir}/doc/fonts/ocr-b-outline/README
%doc %{_texmfdistdir}/doc/fonts/ocr-b-outline/xe-test.tex
#- source
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb10.sfd
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb5.sfd
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb6.sfd
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb7.sfd
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb8.sfd
%doc %{_texmfdistdir}/source/fonts/ocr-b-outline/ocrb9.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110107-2
+ Revision: 754501
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110107-1
+ Revision: 719151
- texlive-ocr-b-outline
- texlive-ocr-b-outline
- texlive-ocr-b-outline
- texlive-ocr-b-outline

