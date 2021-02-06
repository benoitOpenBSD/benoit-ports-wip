# $OpenBSD$

COMMENT =		portable multi-format linker

PKGNAME =		vlink-0.16g
DISTNAME =      	vlink0_16g

CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX A voir
PERMIT_PACKAGE =	Yes

MASTER_SITES =		http://server.owl.de/~frank/tags/ \
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
