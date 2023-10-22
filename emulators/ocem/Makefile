
COMMENT =		ocem emulator COCO 3/OS-9

DISTNAME =		ocem-981011
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX
PERMIT_PACKAGE =	Yes

SITES =			http://atjs.mbnet.fi/mc6809/6809Computers/

WANTLIB +=		c

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/os9/os9 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/coco/emulator.coco ${PREFIX}/bin/

.include <bsd.port.mk>
