# $OpenBSD$

COMMENT =		a TRS-80 Emulator

DISTNAME =		sdltrs_1_1_0
PKGNAME =		sdltrs-1.1.0
CATEGORIES =		emulators

HOMEPAGE =		http://sdltrs.sourceforge.net

MAINTAINER =		Tom Murphy <openbsd@pertho.net> 

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=sdltrs/}

BUILD_DEPENDS =		devel/sdl

LIB_DEPENDS =		devel/sdl

WANTLIB =		c SDL X11 Xt

WRKBUILD =	${WRKSRC}/src/linux
USE_GMAKE=	Yes
NO_TEST=	Yes

DOCSBASE =	${WRKDIST}/docs
DISKIMAGES =	${WRKDIST}/diskimages
HTMLDOCS =	${DOCSBASE}/*.html
HTMLGRAPHICS =	${DOCSBASE}/images/*
DOCSDIR =	${PREFIX}/share/doc/sdltrs

do-install:
	${INSTALL_PROGRAM}	${WRKBUILD}/sdltrs ${PREFIX}/bin

post-install:
	${INSTALL_DATA_DIR} ${DOCSDIR}
	${INSTALL_DATA} ${HTMLDOCS} ${DOCSDIR}
	${INSTALL_DATA_DIR} ${DOCSDIR}/images
	${INSTALL_DATA} ${HTMLGRAPHICS} ${DOCSDIR}/images/
	${INSTALL_DATA_DIR} ${DOCSDIR}/diskimages
	${INSTALL_DATA} ${DISKIMAGES}/* ${DOCSDIR}/diskimages/

.include <bsd.port.mk>
