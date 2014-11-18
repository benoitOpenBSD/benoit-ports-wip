# $OpenBSD$

# Reasons why the port/package shouldn't be built
#
#ONLY_FOR_ARCHS =	???
#NOT_FOR_ARCHS =	???
#SHARED_ONLY =		???
#COMES_WITH =		???
#BROKEN =		reason

COMMENT =		simulator for Microchip PIC microcontrollers

DISTNAME =		gpsim-0.23.0

SHARED_LIBS +=		gpsim		0.0	# .0.0
SHARED_LIBS +=		gpsim_dspic	0.0	# .0.0
SHARED_LIBS +=		gpsim_eXdbm	0.0	# .0.0
SHARED_LIBS +=		gpsim_modules	0.0	# .0.0
SHARED_LIBS +=		gpsimcli	0.0	# .0.0
SHARED_LIBS +=		gpsimgui	0.0	# .0.0

CATEGORIES =		emulators

HOMEPAGE =		http://www.dattalo.com/gnupic/gpsim.html

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		c m z stdc++ pthread
WANTLIB +=		X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes
WANTLIB +=		Xi Xinerama Xrandr Xrender atk-1.0 cairo expat fontconfig
WANTLIB +=		freetype gdk-x11-2.0 gdk_pixbuf-2.0 gio-2.0 glib-2.0
WANTLIB +=		glitz gmodule-2.0 gobject-2.0 gthread-2.0 gtk-x11-2.0
WANTLIB +=		pango-1.0 pangocairo-1.0 pangoft2-1.0 pcre pixman-1
WANTLIB +=		png readline termcap
                                                
MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=gpsim/}

MODULES =		devel/gettext
#BUILD_DEPENDS =	???
RUN_DEPENDS =		::devel/gputils
LIB_DEPENDS =		popt::devel/popt \
			gtkextra-x11-2.0::x11/gtk+extra

USE_X11 =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
#CONFIGURE_SCRIPT =	??? (if other than configure)
CONFIGURE_ARGS +=	${CONFIGURE_SHARED}
CONFIGURE_ENV +=	LDFLAGS="-L${LOCALBASE}/lib" \
			CPPFLAGS="${CPPFLAGS} -I${LOCALBASE}/include" \
			CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include" \
			PKG_CONFIG_PATH="${LOCALBASE}/lib/pkgconfig:${X11BASE}/lib/pkgconfig"

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/gpsim
	${INSTALL_DATA} ${WRKSRC}/doc/gpsim.pdf ${PREFIX}/share/doc/gpsim
	${INSTALL_DATA} ${WRKSRC}/doc/gpsim.ps ${PREFIX}/share/doc/gpsim
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/gpsim
	${INSTALL_DATA} -d ${WRKSRC}/examples/* ${PREFIX}/share/examples/gpsim
                		         
.include <bsd.port.mk>
