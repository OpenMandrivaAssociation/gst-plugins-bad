# Doesn't work for whatever reason
%global debug_package %{nil}

%define _disable_ld_no_undefined 1
%define build_amrwb	0
%define build_faac	0
%define build_faad	0
%define build_xvid	0
%define build_dts	0
%define build_dirac	0
%define build_gme	1

##########################
# Hardcode PLF build
%define build_plf	0
##########################
%if "%{disttag}" == "mdk"
%define build_plf	1
%endif

%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define build_amrwb	0
%define build_faac	1
%define build_faad	1
%define build_xvid	0
%define build_dirac	0
%define build_dts	1
%endif

%define bname	gstreamer%{api}
%define api	1.0
%define major	0
%define libadaptivedemux	%mklibname gstadaptivedemux %{api} %{major}
%define libbasecamerabinsrc	%mklibname gstbasecamerabinsrc %{api} %{major}
%define libphotography		%mklibname gstphotography %{api} %{major}
%define libcodecparsers		%mklibname gstcodecparsers %{api} %{major}
%define libmpegts		%mklibname gstmpegts %{api} %{major}
%define libwebrtc		%mklibname gstwebrtc %{api} %{major}
%define liburidownloader	%mklibname gsturidownloader %{api} %{major}
%define libinsertbin		%mklibname gstinsertbin %{api} %{major}
%define girname			%mklibname gstreamer-plugins-bad-gir %{api}
%define libbadaudio		%mklibname gstbadaudio %{api} %{major}
%define libisoff		%mklibname gstisoff %{api} %{major}
%define libbadvideo		%mklibname gstbadvideo %{api} %{major}
%define libgstwayland		%mklibname gstwayland %{api} %{major}
%define libgstplayer		%mklibname gstplayer %{api} %{major}
%define libgstsctp		%mklibname gstsctp %{api} %{major}
%define libgstopencv		%mklibname gstopencv %{api} %{major}
%define libwebrtc		%mklibname gstwebrtc %{api} %{major}
%define devname			%mklibname -d %{name} %{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-bad
Version:	1.16.2
Release:	7%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{name}-%{version}.tar.xz
#Patch0:		gst-plugins-bad-1.14.0-wildmidi-timidity.cfg.patch
Patch1:		gst-force-opencv-4.3-and-fix-build-with-vulkan-sdk-140.patch
Patch2:		gst-plugins-bad-neon-0.31.patch

%ifarch %{ix86} %{x86_64}
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	gettext-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	gobject-introspection-devel
BuildRequires:	kernel-release-headers
BuildRequires:	ladspa-devel
BuildRequires:	flite-devel
BuildRequires:	pkgconfig(aom)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(libbs2b) >= 3.1.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.9.2
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dvdnav) >= 4.1.2
BuildRequires:	pkgconfig(dvdread) >= 4.1.2
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gio-2.0) >= 2.25.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gmodule-no-export-2.0)
BuildRequires:	pkgconfig(gnutls) >= 2.11.3
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= 1.12.3
BuildRequires:	pkgconfig(gstreamer-%{api}) >= 1.12.3
BuildRequires:	pkgconfig(gstreamer-video-%{api}) >= 1.12.3
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(kate)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:	pkgconfig(libexif) >= 0.6.16
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsrtp2)
BuildRequires:	pkgconfig(libofa) >= 0.9.3
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opencv4)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:	pkgconfig(openh264)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.36
BuildRequires:	pkgconfig(librtmp)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(sbc) >= 1.0
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(spandsp) >= 0.0.6
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zvbi-0.2)
BuildRequires:	pkgconfig(libva-drm)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(valgrind)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(nice)
BuildRequires:	pkgconfig(webrtc-audio-processing)
BuildRequires:  pkgconfig(ffnvcodec)
%if %{build_plf}
BuildRequires:	pkgconfig(vo-aacenc)
BuildRequires:	pkgconfig(vo-amrwbenc)
BuildRequires:	pkgconfig(x265)
BuildRequires:	pkgconfig(fdk-aac)
%endif
BuildRequires:	wildmidi-devel
# For Qt sink
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5WaylandClient)
# vulkan support
BuildRequires:	%{_lib}vulkan-devel
BuildRequires:	egl-devel
%rename gstreamer1.0-plugins-bad

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package -n %{bname}-plugins-bad
Summary:	Sound
Group:		System/Libraries
Obsoletes:	%{libbadvideo} < %{EVRD}
Obsoletes:	%{bname}-musepack < %{EVRD}

%description -n %{bname}-plugins-bad
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package -n %{libadaptivedemux}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libadaptivedemux}
This package contains the libraries for %{name}%{api}.

%package -n %{libbasecamerabinsrc}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libbasecamerabinsrc}
This package contains the libraries for %{name}%{api}.

%package -n %{libphotography}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libphotography}
This package contains the libraries for %{name}%{api}.

%package -n %{libcodecparsers}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libcodecparsers}
This package contains the libraries for %{name}%{api}.

%package -n %{libbadaudio}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libbadaudio}
This package contains the libraries for %{name}%{api}.

%package -n %{libwebrtc}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libwebrtc}
This package contains the libraries for %{name}%{api}.

%package -n %{libbadvideo}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libbadvideo}
This package contains the libraries for %{name}%{api}.

%package -n %{libgstwayland}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstwayland}
This package contains the libraries for %{name}%{api}.

%package -n %{libgstplayer}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstplayer}
This package contains the libraries for %{name}%{api}.

%package -n %{libgstsctp}
Summary:	SCTP library for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstsctp}
This package contains the SCTP library for %{name}%{api}.

%package -n %{libgstopencv}
Summary:	Libraries for GStreamer OpenCV framework
Group:		System/Libraries

%description -n %{libgstopencv}
This package contains the libraries for %{name}%{api}.

#package -n %{libgl}
#Summary:	Libraries for GStreamer streaming-media framework
#Group:		System/Libraries

#description -n %{libgl}
#GStreamer is a streaming-media framework, based on graphs of filters which
#operate on media data. Applications using this library can do anything
#from real-time sound processing to playing videos, and just about anything
#else media-related.  Its plugin-based architecture means that new data
#types or processing capabilities can be added simply by installing new
#plugins.

#This package contains the libraries.

%package -n %{libinsertbin}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libinsertbin}
This package contains the libraries for %{name}%{api}.

%package -n %{libmpegts}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libmpegts}
This package contains the libraries for %{name}%{api}.

%package -n %{liburidownloader}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{liburidownloader}
This package contains the libraries for %{name}%{api}.

%package -n %{libisoff}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libisoff}
This package contains the libraries for %{name}%{api}.

%package -n %{devname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libadaptivedemux} = %{version}-%{release}
Requires:	%{libbasecamerabinsrc} = %{version}-%{release}
Requires:	%{libphotography} = %{version}-%{release}
Requires:	%{libcodecparsers} = %{version}-%{release}
Requires:	%{libinsertbin} = %{version}-%{release}
Requires:	%{libisoff} = %{version}-%{release}
Requires:	%{libgstwayland} = %{version}-%{release}
Requires:	%{libbadaudio} = %{version}-%{release}
Requires:	%{libgstplayer} = %{version}-%{release}
Requires:	%{libgstsctp} = %{EVRD}
Requires:	%{libgstopencv} = %{version}-%{release}
Requires:	%{libmpegts} = %{version}-%{release}
Requires:	%{liburidownloader} = %{version}-%{release}
Requires:	%{libwebrtc} = %{version}-%{release}


#Requires:	%{libgstbadallocators} = %{version}-%{release}
Provides:	%{name}%{api}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development libraries and includes files necessary to 
develop applications and plugins for GStreamer.

%package -n %{bname}-curl
Summary:	GStreamer Curl plugin
Group:		Networking/Other
BuildRequires:	pkgconfig(libcurl)

%description -n %{bname}-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %{bname}-curl
%{_libdir}/gstreamer-%{api}/libgstcurl.so

%package -n %{bname}-closedcaption
Summary:	GStreamer Closed Caption plugin
Group:		Networking/Other

%description -n %{bname}-closedcaption
This is a Closed Caption plugin for GStreamer

%files -n %{bname}-closedcaption
%{_libdir}/gstreamer-%{api}/libgstclosedcaption.so

%package -n %{bname}-mpeg2enc
Summary:	GStreamer mjpegtools plug-in
Group:		Video
BuildRequires:	pkgconfig(mjpegtools)

%description -n %{bname}-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %{bname}-mpeg2enc
%{_libdir}/gstreamer-%{api}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{api}/libgstmplex.so

%package -n %{bname}-musepack
Summary:	GStreamer musepack plug-in
Group:		Video

%description -n %{bname}-musepack
musepack encoding and decoding plug-in.

%if %{build_gme}
%package -n %{bname}-gme
Summary:	GStreamer Game Music plug-in
Group:		Sound
BuildRequires:	libgme-devel

%description -n %{bname}-gme
Game Music decoding plug-in.

%files -n %{bname}-gme
%{_libdir}/gstreamer-%{api}/libgstgme.so
%endif

%if %{build_dirac}
%package -n %{bname}-dirac
Summary:	GStreamer dirac plug-in
Group:		Video
BuildRequires:	pkgconfig(dirac) >= 0.9

%description -n %{bname}-dirac
Dirac encoding and decoding plug-in.

%files -n %{bname}-dirac
%{_libdir}/gstreamer-%{api}/libgstdirac.so
%endif

%if %{build_dts}
%package -n %{bname}-dts
Summary:	GStreamer plug-ins for DTS audio playback
Group:		Sound
BuildRequires:	dtsdec-devel

%description -n %{bname}-dts
Plug-ins for decoding DTS audio.

%files -n %{bname}-dts
%{_libdir}/gstreamer-%{api}/libgstdtsdec.so
%endif

%if %{build_xvid}
%package -n %{bname}-xvid
Summary:	GStreamer plug-ins for XVID video encoding and decoding
Group:		Video
BuildRequires:	xvid-devel >= 1.1

%description -n %{bname}-xvid
Plug-ins for encoding and decoding XVID video.

This package is in restricted repository as it violates some patents.

%files -n %{bname}-xvid
%{_libdir}/gstreamer-%{api}/libgstxvid.so
%endif

%package -n %{bname}-mms
Summary:	GStreamer plug-in for mms streams
Group:		System/Libraries
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{api}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{api}/libgstrtmp.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(soundtouch)

%description -n %{bname}-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %{bname}-soundtouch
%{_libdir}/gstreamer-%{api}/libgstsoundtouch.so

%package -n %{bname}-libass
Summary:	GStreamer subtitles plugin
Group:		Video
BuildRequires:	pkgconfig(libass)

%description -n %{bname}-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %{bname}-libass
%{_libdir}/gstreamer-%{api}/libgstassrender.so

%if %{build_faad}
%package -n %{bname}-faad
Summary:	GStreamer plug-in for AAC audio playback
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	faad2-devel

%description -n %{bname}-faad
Plug-ins for playing AAC audio

This package is in restricted repository as it violates some patents.
%endif

%if %{build_faac}
%package -n %{bname}-faac
Summary:	GStreamer plug-ins for AAC audio encoding
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	faac-devel

%description -n %{bname}-faac
Plug-ins for encoding AAC audio

This package is in restricted repository as it violates some patents.
%endif

%package -n %{bname}-wayland
Summary:	GStreamer plugin for Wayland support
Group:		Sound
Requires:	%{bname}-plugins-base

%description -n %{bname}-wayland
GStreamer plugin for Wayland support

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %{bname}-swfdec
Summary:	GStreamer Flash rendering plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins-base
BuildRequires:	libswfdec-devel => 0.3.0

%description -n %{bname}-swfdec
Plug-in for rendering Flash animations using swfdec library
%endif

%if %{build_amrwb}
%package -n %{bname}-amrwb
Summary:	GStreamer plug-in for AMR-WB support
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(opencore-amrwb)

%description -n %{bname}-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in restricted repository as it violates some patents.
%endif

%package -n %{girname}
Group:		System/Libraries
Summary:	Object Introspection interface description for %{name}
#Requires:	%{libgl} = %{version}
Requires:	%{libinsertbin} = %{version}
Requires:	%{libmpegts} = %{version}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%autosetup -p1

%build
# (tpg) fix finding libmpcdec
sed -i -e 's#mpc/mpcdec.h#mpcdec/mpcdec.h#g' $(grep -ril 'mpc/mpcdec.h' *)

export CFLAGS="$CFLAGS -Wno-mismatched-tags -Wno-header-guard -Wno-deprecated-register"
export CXXFLAGS="$CXXFLAGS -Wno-mismatched-tags -Wno-header-guard -Wno-deprecated-register -std=gnu++17 -Wno-dynamic-exception-spec -Wno-register"
%meson \
	-Ddirectfb=disabled \
	-Dpackage-name='OpenMandriva %{name} %{version}-%{release}' \
	-Dpackage-origin='%{disturl}' \
%if ! %{build_faac}
	-Dfaac=disabled \
	-Dfdkaac=disabled \
%endif
%if ! %{build_faad}
	-Dfaad=disabled \
%endif
%if ! %{build_dts}
	-Ddts=disabled \
%endif
%if ! %{build_plf}
	-Dvoaacenc=disabled \
	-Dvoamrwbenc=disabled \
	-Dlibde265=disabled \
	-Dx265=disabled \
%endif
	-Dwayland=enabled \
	-Dmsdk=disabled \
	-Dopensles=disabled \
	-Dtinyalsa=disabled \
	-Dwasapi=disabled \
	-Dnvdec=disabled \
	-Dnvenc=disabled \
	-Diqa=disabled \
	-Dmusepack=disabled \
	-Dopenmpt=disabled \
	-Dopenni2=disabled \
	-Dsctp=disabled \
	-Dsrt=disabled \
	-Dwpe=disabled \
	-Dzbar=disabled

%meson_build

%install
%meson_install

%find_lang %{name}-%{api}

%files -n %{bname}-plugins-bad -f %{name}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/playout
%{_libdir}/gstreamer-%{api}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{api}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{api}/libgstasfmux.so
%{_libdir}/gstreamer-%{api}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{api}/libgstautoconvert.so
%{_libdir}/gstreamer-%{api}/libgstbayer.so
%{_libdir}/gstreamer-%{api}/libgstbluez.so
%{_libdir}/gstreamer-%{api}/libgstbs2b.so
%{_libdir}/gstreamer-%{api}/libgstcamerabin.so
%{_libdir}/gstreamer-%{api}/libgstchromaprint.so
%{_libdir}/gstreamer-%{api}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{api}/libgstdc1394.so
%{_libdir}/gstreamer-%{api}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{api}/libgstdtls.so
%{_libdir}/gstreamer-%{api}/libgstdvb.so
%{_libdir}/gstreamer-%{api}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{api}/libgstdvdspu.so
%{_libdir}/gstreamer-%{api}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{api}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{api}/libgstfaceoverlay.so
#%{_libdir}/gstreamer-%{api}/libgstgtk.so
#{_libdir}/gstreamer-%{api}/libgstkms.so
%{_libdir}/gstreamer-%{api}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{api}/libgstteletext.so
%{_libdir}/gstreamer-%{api}/libgstttmlsubs.so
%if %{build_plf}
%{_libdir}/gstreamer-%{api}/libgstfdkaac.so
%endif
%{_libdir}/gstreamer-%{api}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{api}/libgstfestival.so
%{_libdir}/gstreamer-%{api}/libgstfluidsynthmidi.so
%{_libdir}/gstreamer-%{api}/libgstfrei0r.so
%{_libdir}/gstreamer-%{api}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{api}/libgstid3tag.so
%{_libdir}/gstreamer-%{api}/libgstinter.so
%{_libdir}/gstreamer-%{api}/libgstinterlace.so
%{_libdir}/gstreamer-%{api}/libgstjpegformat.so
%{_libdir}/gstreamer-%{api}/libgstkate.so
%{_libdir}/gstreamer-%{api}/libgstladspa.so
%{_libdir}/gstreamer-%{api}/libgstlv2.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{api}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{api}/libgstofa.so
%{_libdir}/gstreamer-%{api}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{api}/libgstpcapparse.so
%{_libdir}/gstreamer-%{api}/libgstpnm.so
%{_libdir}/gstreamer-%{api}/libgstremovesilence.so
%{_libdir}/gstreamer-%{api}/libgstresindvd.so
%{_libdir}/gstreamer-%{api}/libgstrsvg.so
%{_libdir}/gstreamer-%{api}/libgstrtponvif.so
%{_libdir}/gstreamer-%{api}/libgstsbc.so
%{_libdir}/gstreamer-%{api}/libgstsdpelem.so
%{_libdir}/gstreamer-%{api}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{api}/libgstshm.so
%{_libdir}/gstreamer-%{api}/libgstsiren.so
%{_libdir}/gstreamer-%{api}/libgstsmooth.so
%{_libdir}/gstreamer-%{api}/libgstspeed.so
%{_libdir}/gstreamer-%{api}/libgstsubenc.so
%{_libdir}/gstreamer-%{api}/libgsttimecode.so
%{_libdir}/gstreamer-%{api}/libgstbz2.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{api}/libgstuvch264.so
%{_libdir}/gstreamer-%{api}/libgstvdpau.so
%{_libdir}/gstreamer-%{api}/libgstvideoparsersbad.so
#{_libdir}/gstreamer-%{api}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{api}/libgstwebp.so
%{_libdir}/gstreamer-%{api}/libgstwildmidi.so
%if %{build_plf}
%{_libdir}/gstreamer-%{api}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{api}/libgstvoamrwbenc.so
%{_datadir}/gstreamer-%{api}/presets/GstVoAmrwbEnc.prs
%endif
%{_libdir}/gstreamer-%{api}/libgstmodplug.so
%{_libdir}/gstreamer-%{api}/libgsty4mdec.so
%{_libdir}/gstreamer-%{api}/libgstaccurip.so
%{_libdir}/gstreamer-%{api}/libgstaiff.so
%{_libdir}/gstreamer-%{api}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{api}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{api}/libgstdashdemux.so
%{_libdir}/gstreamer-%{api}/libgstdecklink.so
%{_libdir}/gstreamer-%{api}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{api}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{api}/libgstfreeverb.so
%{_datadir}/gstreamer-%{api}/presets/GstFreeverb.prs
%{_libdir}/gstreamer-%{api}/libgstivtc.so
%{_libdir}/gstreamer-%{api}/libgsthls.so
%{_libdir}/gstreamer-%{api}/libgstmidi.so
%{_libdir}/gstreamer-%{api}/libgstmxf.so
%{_libdir}/gstreamer-%{api}/libgstnetsim.so
%{_libdir}/gstreamer-%{api}/libgstopenal.so
%{_libdir}/gstreamer-%{api}/libgstopusparse.so
%{_libdir}/gstreamer-%{api}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{api}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{api}/libgstspandsp.so
%{_libdir}/gstreamer-%{api}/libgstsrtp.so
%{_libdir}/gstreamer-%{api}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{api}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{api}/libgstyadif.so
%if %{build_plf}
%{_libdir}/gstreamer-%{api}/libgstx265.so
%endif
%{_libdir}/gstreamer-%{api}/libgstivfparse.so
%{_libdir}/gstreamer-%{api}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{api}/libgstopenexr.so
%{_libdir}/gstreamer-%{api}/libgstsndfile.so
%{_libdir}/gstreamer-%{api}/libgstvideosignal.so
%{_libdir}/gstreamer-%{api}/libgstvmnc.so
%{_libdir}/gstreamer-%{api}/libgstflite.so
%{_libdir}/gstreamer-%{api}/libgstproxy.so
%{_libdir}/gstreamer-%{api}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{api}/libgstvulkan.so
%{_libdir}/gstreamer-1.0/libgstaom.so
%{_libdir}/gstreamer-1.0/libgstkms.so
%{_libdir}/gstreamer-1.0/libgstopenh264.so
%{_libdir}/gstreamer-1.0/libgstwebrtc.so
%{_libdir}/gstreamer-1.0/libgstwebrtcdsp.so

%files -n %{bname}-wayland
%{_libdir}/gstreamer-1.0/libgstwaylandsink.so

%if %{build_faad}
%files -n %{bname}-faad
%{_libdir}/gstreamer-%{api}/libgstfaad.so
%endif

%if %{build_faac}
%files -n %{bname}-faac
%{_libdir}/gstreamer-%{api}/libgstfaac.so
%endif

%files -n %{bname}-gsm
%{_libdir}/gstreamer-%{api}/libgstgsm.so

%if 0
### SWFDEC FLASH PLUGIN ###
%files -n %{bname}-swfdec
%{_libdir}/gstreamer-%{api}/libgstswfdec.so
%endif

%if %{build_amrwb}
%files -n %{bname}-amrwb
%{_datadir}/gstreamer-%{api}/presets/GstAmrwbEnc.prs
%{_libdir}/gstreamer-%{api}/libgstamrwbenc.so
%endif

%files -n %{libadaptivedemux}
%{_libdir}/libgstadaptivedemux-%{api}.so.%{major}*

%files -n %{libbasecamerabinsrc}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so.%{major}*

%files -n %{libphotography}
%{_libdir}/libgstphotography-%{api}.so.%{major}*

%files -n %{libcodecparsers}
%{_libdir}/libgstcodecparsers-%{api}.so.%{major}*

%files -n %{libisoff}
%{_libdir}/libgstisoff-%{api}.so.%{major}*

%files -n %{libinsertbin}
%{_libdir}/libgstinsertbin-%{api}.so.%{major}*

%files -n %{libmpegts}
%{_libdir}/libgstmpegts-%{api}.so.%{major}*

%files -n %{liburidownloader}
%{_libdir}/libgsturidownloader-%{api}.so.%{major}*

%files -n %{libbadaudio}
%{_libdir}/libgstbadaudio-%{api}.so.%{major}*

%files -n %{libwebrtc}
%{_libdir}/libgstwebrtc-%{api}.so.%{major}*

%files -n %{libgstwayland}
%{_libdir}/libgstwayland-%{api}.so.%{major}*

%files -n %{libgstplayer}
%{_libdir}/libgstplayer-%{api}.so.%{major}*

%files -n %{libgstsctp}
%{_libdir}/libgstsctp-%{api}.so.%{major}*

%files -n %{libgstopencv}
%{_libdir}/libgstopencv-%{api}.so.%{major}*
%{_libdir}/gstreamer-1.0/libgstopencv.so

#%files -n %{libgstwebrtc}
#%{_libdir}/libgstbadallocators-%{api}.so.%{major}*

%files -n %{devname}
%doc docs/plugins/html
%{_libdir}/libgstadaptivedemux-%{api}.so
%{_libdir}/libgstbasecamerabinsrc-%{api}.so
%{_libdir}/libgstcodecparsers-%{api}.so
%{_libdir}/libgstphotography-%{api}.so
%{_libdir}/libgstinsertbin-%{api}.so
%{_libdir}/libgstmpegts-%{api}.so
%{_libdir}/libgsturidownloader-%{api}.so
%{_libdir}/libgstbadaudio-%{api}.so
%{_libdir}/libgstwebrtc-%{api}.so
%{_libdir}/libgstwayland-%{api}.so
%{_libdir}/libgstplayer-%{api}.so
%{_libdir}/libgstopencv-%{api}.so
%{_libdir}/libgstsctp-%{api}.so
%{_libdir}/libgstisoff-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/audio/
%{_includedir}/gstreamer-%{api}/gst/basecamerabinsrc/
%{_includedir}/gstreamer-%{api}/gst/codecparsers/
%{_includedir}/gstreamer-%{api}/gst/webrtc/
%{_includedir}/gstreamer-%{api}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{api}/gst/insertbin
%{_includedir}/gstreamer-%{api}/gst/mpegts
%{_includedir}/gstreamer-%{api}/gst/player
%{_includedir}/gstreamer-%{api}/gst/uridownloader
%{_includedir}/gstreamer-%{api}/gst/isoff
%{_includedir}/gstreamer-%{api}/gst/opencv
%{_includedir}/gstreamer-%{api}/gst/sctp
%{_datadir}/gir-1.0/GstInsertBin-%{api}.gir
%{_datadir}/gir-1.0/GstMpegts-%{api}.gir
%{_datadir}/gir-1.0/GstPlayer-%{api}.gir
%{_datadir}/gir-1.0/GstWebRTC-%{api}.gir
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-sctp-%{api}.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/GstInsertBin-%{api}.typelib
%{_libdir}/girepository-1.0/GstMpegts-%{api}.typelib
%{_libdir}/girepository-1.0/GstPlayer-%{api}.typelib
%{_libdir}/girepository-1.0/GstWebRTC-%{api}.typelib
