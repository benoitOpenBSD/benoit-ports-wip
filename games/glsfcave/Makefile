
COMMENT=	control a ribbon to avoid hitting walls

V=		1.1
DISTNAME= 	glsfcave-$V
CATEGORIES=	games
EXTRACT_SUFX=	.tar.bz2

HOMEPAGE=	http://user.ecc.u-tokyo.ac.jp/~s081016/glsfcave/
SITES =		${HOMEPAGE}

MAINTAINER=	Simon Bertrang <simon@openbsd.org>

# Public domain
PERMIT_DISTFILES_CDROM=	Yes

WANTLIB=	GL GLU X11 Xext Xi Xmu c m pthread-stubs xcb glut>=4

LIB_DEPENDS=	graphics/freeglut

WRKDIST=	${WRKDIR}/glsfcave

ALL_TARGET=	glsfcave

CFLAGS+=	-I${X11BASE}/include -I${LOCALBASE}/include

NO_TEST =	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/glsfcave ${PREFIX}/bin

.include <bsd.port.mk>
