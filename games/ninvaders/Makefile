# $OpenBSD$

COMMENT =	console based space invaders clone

DISTNAME =	ninvaders-0.1.1
CATEGORIES =	games
HOMEPAGE =	http://ninvaders.sf.net/

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =	c ncurses

MASTER_SITES =	${MASTER_SITE_SOURCEFORGE:=ninvaders/}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/nInvaders ${PREFIX}/bin/

.include <bsd.port.mk>
