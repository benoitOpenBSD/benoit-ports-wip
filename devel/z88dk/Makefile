
COMMENT =	z80 Development kit

DISTNAME =	z88dk-src-2.0
PKGNAME =	${DISTNAME:S/-src//}
CATEGORIES =	devel

HOMEPAGE =	https://www.z88dk.org/
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# The Clarified Artistic License
PERMIT_PACKAGE =	Yes

WANTLIB +=		c m

SITES =			${SITE_SOURCEFORGE:=z88dk/} \
			https://www.arcane-labs.net/download/OpenBSD/

EXTRACT_SUFX =		.tgz

USE_GMAKE =		Yes

WRKDIST=		${WRKDIR}/z88dk

DEBUG_PACKAGES =	${BUILD_PACKAGES}

.include <bsd.port.mk>
