# $OpenBSD$

COMMENT =		8085 Assembler 

DISTNAME =		asm85-20191111
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT Licence
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/TomNisbet/asm85

GH_ACCOUNT =		TomNisbet
GH_PROJECT =		asm85
GH_COMMIT =		c98cc8cbe2548b5ed85e64f04f5af1ed7bb7bfdb

WANTLIB +=		${COMPILER_LIBCXX} c m

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/src

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/asm85  ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/asm85/examples
			cp ${WRKDIST}/README.md  ${PREFIX}/share/asm85/
			cp ${WRKDIST}/examples/* ${PREFIX}/share/asm85/examples/

.include <bsd.port.mk>
