Summary:	Anroid fonts (Droid and Roboto)
Name:		android-fonts
Version:	4.0.1_r1.2
Release:	%mkrel 1
License:	Apache License
Group:		System/Fonts/True type
URL:		http://source.android.com
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
Fonts developed for Google Android project. Currently that are Droid and Roboto
families.

#------------------------------------------------------------------------------

%package -n fonts-ttf-droid
Summary:	Droid fonts

%description -n fonts-ttf-droid
The Droid family of fonts consists of Droid Sans, Droid Sans Mono and 
Droid Serif. Each contains extensive character set coverage including 
Western Europe, Eastern/Central Europe, Baltic, Cyrillic, Greek and 
Turkish support. The Droid Sans regular font also includes support for 
Simplified and Traditional Chinese, Japanese and Korean support for 
the GB2312, Big 5, JIS 0208 and KSC 5601 character sets respectively. 
Droid was designed by Ascender's Steve Matteson to provide optimal quality 
and comfort on a mobile handset when rendered in application menus, web 
browsers and for other screen text.

%files -n fonts-ttf-droid
%doc NOTICE README.txt
%dir %{_xfontdir}/TTF/droid
%{_xfontdir}/TTF/droid/*.ttf
%verify(not mtime) %{_xfontdir}/TTF/droid/fonts.dir
%{_xfontdir}/TTF/droid/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-droid:pri=50

#------------------------------------------------------------------------------

%package -n fonts-ttf-roboto
Summary:	Roboto fonts

%description -n fonts-ttf-roboto
Roboto is a sans-serif typeface family introduced with Android 4.0 "Ice Cream
Sandwich" operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%files -n fonts-ttf-roboto
%doc NOTICE README.txt
%dir %{_xfontdir}/TTF/roboto
%{_xfontdir}/TTF/roboto/*.ttf
%verify(not mtime) %{_xfontdir}/TTF/roboto/fonts.dir
%{_xfontdir}/TTF/roboto/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-roboto:pri=50

#------------------------------------------------------------------------------

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_xfontdir}/TTF/droid %{buildroot}%{_xfontdir}/TTF/roboto

install -m 644 Droid*.ttf %{buildroot}%{_xfontdir}/TTF/droid
ttmkfdir %{buildroot}%{_xfontdir}/TTF/droid -o %{buildroot}%{_xfontdir}/TTF/droid/fonts.dir
ln -s fonts.dir %{buildroot}%{_xfontdir}/TTF/droid/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/droid \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-droid:pri=50

install -m 644 Roboto*.ttf %{buildroot}%{_xfontdir}/TTF/roboto
ttmkfdir %{buildroot}%{_xfontdir}/TTF/roboto -o %{buildroot}%{_xfontdir}/TTF/roboto/fonts.dir
ln -s fonts.dir %{buildroot}%{_xfontdir}/TTF/roboto/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/roboto \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-roboto:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.0.1_r1.2-1mdv2011.0
+ Revision: 739461
- imported package android-fonts

