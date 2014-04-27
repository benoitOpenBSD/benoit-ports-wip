# $OpenBSD$

COMMENT =		Atari 800 emulator

DISTNAME =		atari800-3.1.0
CATEGORIES =		emulators

HOMEPAGE =		http://atari800.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c z m X11 ossaudio png pthread readline SDL termcap

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=atari800/}

WRKBUILD =		${WRKDIR}/${DISTNAME}/src

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS =	CFLAGS='${CFLAGS} -I${LOCALBASE}/include' \
			LDFLAGS='${LDFLAGS} -L${LOCALBASE}/lib' \
			--with-x

LIB_DEPENDS =		devel/sdl \
			graphics/png

NO_TEST =		Yes

pre-configure:
		${SUBST_CMD} ${WRKSRC}/src/atari800.man ${WRKSRC}/src/atari.c

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/atari800 ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/atari800 ${PREFIX}/share/atari800
		${INSTALL_DATA} ${WRKSRC}/DOC/* ${PREFIX}/share/doc/atari800
		${INSTALL_DATA} ${WRKBUILD}/atari800.man ${PREFIX}/man/man1/atari800.1

.include <bsd.port.mk>
