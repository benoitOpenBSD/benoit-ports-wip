
COMMENT =		a C compiler in POSIX shell and generating POSIX shell

DISTNAME =		pnut-20240724
CATEGORIES =		lang

HOMEPAGE =		https://pnut.sh/

# BSD 2 clause
PERMIT_PACKAGE		= Yes

SITES =			${SITES_GITHUB}

GH_ACCOUNT =            udem-dlteam
GH_PROJECT =            pnut
GH_COMMIT =             1bc6a0d68de9e2284ddc2d9af889584cc6360616

WANTLIB =		c

NO_TEST =               Yes

do-build:
			cd ${WRKBUILD} && ${MAKE} && ${MAKE} pnut.sh

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/build/pnut-sh ${PREFIX}/bin/pnut
		${INSTALL_PROGRAM} ${WRKSRC}/build/pnut.sh ${PREFIX}/bin/pnut.sh
		${INSTALL_DATA_DIR} ${PREFIX}/share/pnut/examples
		cp -R ${WRKSRC}/examples/* ${PREFIX}/share/pnut/examples			
		${INSTALL_DATA_DIR} ${PREFIX}/share/pnut/tests
		cp -R ${WRKSRC}/tests/* ${PREFIX}/share/pnut/tests			
                        
.include <bsd.port.mk>
