# $OpenBSD$

ONLY_FOR_ARCHS =	i386

COMMENT =		Ultimate packer for executables

DISTNAME =		upx-3.03-src
PKGNAME = 		${DISTNAME:S/-src//}
CATEGORIES =		archivers

HOMEPAGE =		http://upx.sourceforge.net/

MAINTAINER =		Benoit Lecocq <blq@arcane-labs.net>

# GPLv2
PERMIT_PACKAGE_CDROM =		Yes 
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes 
PERMIT_DISTFILES_FTP =		Yes 

WANTLIB =		c z stdc++ m

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=upx/}

EXTRACT_SUFX =		.tar.bz2

BUILD_DEPENDS =		archivers/ucl \
			archivers/lzma

USE_GMAKE =		Yes

NO_REGRESS =		Yes

UPXDOCS =		BUGS COPYING LICENSE NEWS PROJECTS README \
			README.1ST README.SRC THANKS TODO
UPXDOCSDIR =		${PREFIX}/share/doc/upx/

do-install:
			${INSTALL_MAN} ${WRKSRC}/doc/upx.1 ${PREFIX}/man/man1 
			${INSTALL_PROGRAM} ${WRKSRC}/src/upx ${PREFIX}/bin/upx
			${INSTALL_DATA_DIR} ${UPXDOCSDIR}
			.for file in ${UPXDOCS}
				${INSTALL_DATA} ${WRKSRC}/doc/${file} ${UPXDOCSDIR}
			.endfor
			
.include <bsd.port.mk>
