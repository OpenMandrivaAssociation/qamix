%define name	qamix
%define version	0.0.7e
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Easily configurable ALSA mixer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.suse.de/~mana/kalsatools.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel libalsa-devel ImageMagick

%description
QAMix is a configurable mixer for ALSA. The GUI description is defined in an
XML file. Default interfaces for standard AC 97 cards and Soundblaster Live
are provided. QAMix can be controlled via MIDI. Any number of MIDI events can
be bound to any mixer control. 

%prep
%setup -q
perl -p -i -e 's/\(QT_BASE_DIR\)\/lib/\(QT_BASE_DIR\)\/%_lib/g' make_qamix
perl -p -i -e 's/\-O2\ \-g/%optflags/g' make_qamix

%build
%make -f make_qamix
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%_bindir,%_datadir/%name}
cp %name $RPM_BUILD_ROOT/%_bindir/
cp *.xml $RPM_BUILD_ROOT/%_datadir/%name/

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QAMix
Comment=ALSA Mixer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Mixer;
Encoding=UTF-8
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 multimedia.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 multimedia.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 multimedia.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README THANKS *.ams
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

