# $OpenBSD$

COMMENT =		cross-development tools for the Motorola 6809/Hitachi 6309

DISTNAME =		lwtools-4.19
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MASTER_SITES =		http://lwtools.projects.l-w.ca/releases/lwtools/

HOMEPAGE =		http://lwtools.projects.l-w.ca/

WANTLIB +=		c

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/lwar/lwar ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/lwasm/lwasm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/lwlink/lwobjdump ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/lwlink/lwlink ${PREFIX}/bin/
	${INSTALL_DATA} ${WRKSRC}/lwlib/liblw.a ${PREFIX}/lib/

.include <bsd.port.mk>
