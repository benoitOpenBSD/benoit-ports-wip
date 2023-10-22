
#ONLY_FOR_ARCHS =	i386

COMMENT =		Ultimate packer for executables

DISTNAME =		upx-3.91-src
PKGNAME = 		${DISTNAME:S/-src//}
CATEGORIES =		archivers

HOMEPAGE =		http://upx.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c z stdc++ m

SITES =			${SITE_SOURCEFORGE:=upx/}

EXTRACT_SUFX =		.tar.bz2

BUILD_DEPENDS =		archivers/ucl \
			archivers/xz

USE_GMAKE =		Yes

NO_TEST =		Yes

UPXDOCS =		BUGS COPYING LICENSE NEWS PROJECTS README \
			README.1ST README.SRC THANKS TODO
UPXDOCSDIR =		${PREFIX}/share/doc/upx/

do-install:
			${INSTALL_MAN} ${WRKSRC}/doc/upx.1 ${PREFIX}/man/man1 
			${INSTALL_PROGRAM} ${WRKSRC}/src/upx.out ${PREFIX}/bin/upx
			${INSTALL_DATA_DIR} ${UPXDOCSDIR}
.for file in ${UPXDOCS}
				${INSTALL_DATA} ${WRKSRC}/${file} ${UPXDOCSDIR}
.endfor
			
.include <bsd.port.mk>
