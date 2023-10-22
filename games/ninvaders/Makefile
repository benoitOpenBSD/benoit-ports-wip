
COMMENT =	console based space invaders clone

DISTNAME =	ninvaders-0.1.1
CATEGORIES =	games
HOMEPAGE =	http://ninvaders.sf.net/

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =	c ncurses

SITES =		${SITE_SOURCEFORGE:=ninvaders/}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/nInvaders ${PREFIX}/bin/

NO_TEST =	Yes

.include <bsd.port.mk>
