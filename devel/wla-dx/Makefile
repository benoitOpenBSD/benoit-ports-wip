# $OpenBSD$

COMMENT =		yet Another Multi Platform Cross Assembler

DISTNAME =		wla-dx-20210221
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/vhelin/wla-dx

GH_ACCOUNT =		vhelin
GH_PROJECT =		wla-dx
GH_COMMIT =		eba3774e8d06f9d92f7ec1d4f39a0f3b9a92b27d

WANTLIB +=		c m

MODULES =		devel/cmake

# XXX problem doc/sphinx/singletext.py WIP
BUILD_DEPENDS =		textproc/py-sphinx

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/wla-dx/tests
	cp -R ${WRKSRC}/tests/* ${PREFIX}/share/wla-dx/tests
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/wla-dx
	cp -R ${WRKSRC}/doc/* ${PREFIX}/share/doc/wla-dx

.include <bsd.port.mk>
