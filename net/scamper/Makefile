# $OpenBSD$

COMMENT =		Dual-stack traceroute software

VERSION =		20070523p
DISTNAME =		scamper-cvs-${VERSION}
PKGNAME =		scamper-${VERSION}
CATEGORIES =		net

HOMEPAGE =		http://www.wand.net.nz/scamper/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		c

MASTER_SITES =		http://www.wand.net.nz/scamper/

NO_REGRESS =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/scamper ${PREFIX}/bin
		${INSTALL_MAN_DIR} ${PREFIX}/man/man1
		${INSTALL_MAN} ${WRKSRC}/scamper.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
