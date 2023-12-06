
COMMENT =		fork of byuu bass assembler 

DISTNAME =		bass-18.20220512
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/ARM9/bass

GH_ACCOUNT =		ARM9
GH_PROJECT =		bass
GH_COMMIT =		c3962ec01f4768be1667db0d09c12141c28241f3

WANTLIB +=		${COMPILER_LIBCXX}
WANTLIB +=		c m pthread

USE_GMAKE =		Yes

do-build:
	cd ${WRKBUILD}/bass && ${GMAKE}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bass/out/bass ${PREFIX}/bin/
#	${INSTALL_MAN} ${WRKSRC}/bass/doc/* ${PREFIX}/man/man1

.include <bsd.port.mk>
