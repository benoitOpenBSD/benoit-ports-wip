
COMMENT =		free Tektronix 4010, 4013, 4014 and 4015 terminal emulator

DISTNAME =		Tek4010-230214
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/rricharz/Tek4010

GH_ACCOUNT =		rricharz
GH_PROJECT =		Tek4010
GH_COMMIT =		656d078fb68842a409f3f09016590cce51bd3421

WANTLIB +=		c pthread
WANTLIB +=		atk-1.0 cairo cairo-gobject gdk-3 gdk_pixbuf-2.0 gio-2.0
WANTLIB +=		glib-2.0 gobject-2.0 gtk-3 harfbuzz intl pango-1.0
WANTLIB +=		pangocairo-1.0

MAKE_FILE =		makefile

LIB_DEPENDS =		x11/gtk+3

pre-build:
			cd ${WRKSRC} && make clean
			
do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/tek4010 ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/Tek4010
			${INSTALL_DATA} ${WRKSRC}/*.{plt,png,jpg,sh} ${PREFIX}/share/Tek4010
			${INSTALL_DATA_DIR} ${PREFIX}/share/Tek4010/manuals
			${INSTALL_DATA} ${WRKSRC}/manuals/* ${PREFIX}/share/Tek4010/manuals
			${INSTALL_DATA_DIR} ${PREFIX}/share/Tek4010/pltfiles
			cp -pr ${WRKSRC}/pltfiles/* ${PREFIX}/share/Tek4010/pltfiles
			${INSTALL_DATA_DIR} ${PREFIX}/share/Tek4010/ardsfiles
			${INSTALL_DATA} ${WRKSRC}/ardsfiles/* ${PREFIX}/share/Tek4010/ardsfiles
			${INSTALL_DATA_DIR} ${PREFIX}/share/Tek4010/tektests
			${INSTALL_DATA} ${WRKSRC}/tektests/* ${PREFIX}/share/Tek4010/ardsfiles
			
NO_TEST =		Yes

.include <bsd.port.mk>
