
COMMENT =		program for controlling the MiniPRO TL866xx

DISTNAME =		minipro-20231008
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

SITES =			https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		https://gitlab.com/DavidGriffith/minipro/

WANTLIB +=		c m usb-1.0

LIB_DEPENDS =		devel/libusb1

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/minipro

DEBUG_PACKAGES =	${BUILD_PACKAGES}

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/minipro ${PREFIX}/bin
	${INSTALL_MAN_DIR} ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/man/minipro.1 ${PREFIX}/man/man1
	${INSTALL_DATA_DIR} ${PREFIX}/share/minipro
	${INSTALL_DATA} ${WRKSRC}/infoic.xml ${PREFIX}/share/minipro
	${INSTALL_DATA} ${WRKSRC}/logicic.xml ${PREFIX}/share/minipro

.include <bsd.port.mk>
