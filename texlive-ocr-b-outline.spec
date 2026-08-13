%global tl_name ocr-b-outline
%global tl_revision 20969

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	OCR-B fonts in Type 1 and OpenType
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ocr-b-outline
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b-outline.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package contains OCR-B fonts in Type1 and OpenType formats. They
were generated from the Metafont sources of the OCR-B fonts. The metric
files are not included here, so that original ocr-b package should also
be installed.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ocr-b-outline:
Map ocrb.map
TL_DROPIN_EOF
