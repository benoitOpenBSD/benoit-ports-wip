# $OpenBSD$

COMMENT =		transferring files between a qemu host and guest

DISTNAME =		qemu-copy-tools-20210612
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/tschak909/qemu-copy-tools

GH_ACCOUNT =		tschak909
GH_PROJECT =		qemu-copy-tools
GH_COMMIT =		caa30b45fad521c645b21b81da6ed16dea3fe624

WANTLIB +=		c

NO_TEST =		Yes

do-build:
		cd ${WRKSRC} && env -i ${MAKE_ENV} ${CC} -o qh qh.c && \
		env -i ${MAKE_ENV} ${CC} -o qg qg.c

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/qh ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKSRC}/qg ${PREFIX}/bin

.include <bsd.port.mk>
