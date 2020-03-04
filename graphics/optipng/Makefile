# $OpenBSD$

COMMENT=		advanced PNG Optimizer

DISTNAME=		optipng-0.6.4
CATEGORIES=		graphics

HOMEPAGE=		http://optipng.sourceforge.net/

MAINTAINER=		Benoit Lecocq <blq@arcane-labs.net>

# Open-Source (zlib/libpng license)
PERMIT_PACKAGE =	Yes

WANTLIB=		c

MASTER_SITES=		${MASTER_SITE_SOURCEFORGE:=optipng/}

#PATCHFILES=		${PKGNAME}.diff
#PATCH_DIST_STRIP=	-p1

MAKE_FLAGS=		CC="${CC}" LD="${CC}" CFLAGS="${CFLAGS} -I."

do-build:
			@cd ${WRKSRC}/src && ${MAKE_ENV} ${MAKE_PROGRAM} ${MAKE_FLAGS} -f scripts/gcc.mak
			                
do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/src/optipng ${PREFIX}/bin
			${INSTALL_MAN} ${WRKSRC}/man/optipng.1 ${PREFIX}/man/man1

NO_TEST =		Yes

.include <bsd.port.mk>
