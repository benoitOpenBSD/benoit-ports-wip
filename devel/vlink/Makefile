
COMMENT =		portable multi-format linker

PKGNAME =		vlink-0.18a
DISTNAME =      	vlink0_18a

CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX A voir
PERMIT_PACKAGE =	Yes

SITES =			http://server.owl.de/~frank/tags/ \
			https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://sun.hasenbraten.de/vlink/

WANTLIB +=		c m

USE_GMAKE =		Yes
ALL_TARGET =		vlink

WRKDIST =		${WRKDIR}/vlink

NO_TEST =		Yes

#do-install:
#	${INSTALL_PROGRAM} ${WRKBUILD}/vlink  ${PREFIX}/bin

.include <bsd.port.mk>
