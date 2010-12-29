# $OpenBSD: Makefile,v 1.18 2008/02/01 21:38:26 steven Exp $

COMMENT=		twm, plus support for multiple virtual screens, etc

DISTNAME=		ctwm-3.8a
PKGNAME=		${DISTNAME}
CATEGORIES=		x11

HOMEPAGE=		http://ctwm.free.lp.se/

# BSD-like/badly worded
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=		ICE SM X11 Xau Xdmcp Xext Xmu Xpm Xt c

LIB_DEPENDS=		jpeg.>=62::graphics/jpeg

MASTER_SITES=		${HOMEPAGE}dist/

pre-patch:
	cp  ${WRKSRC}/Imakefile.local-template ${WRKSRC}/Imakefile.local
	        
USE_X11=		Yes
CONFIGURE_STYLE=	imake
NO_REGRESS=		Yes

.include <bsd.port.mk>
