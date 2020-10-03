# $OpenBSD$

COMMENT =		yet Another Multi Platform Cross Assembler

DISTNAME =		wla-dx-20200919
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/vhelin/wla-dx

GH_ACCOUNT =		vhelin
GH_PROJECT =		wla-dx
GH_COMMIT =		5b123afc1ddcbb003f4a80f3f27fb7d7c5fa26dc

WANTLIB +=		c m

MODULES =		devel/cmake

# XXX problem doc/sphinx/singletext.py WIP
BUILD_DEPENDS =		textproc/py-sphinx

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/wla-dx/examples
	cp -R ${WRKSRC}/examples/* ${PREFIX}/share/wla-dx/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/wla-dx
	cp -R ${WRKSRC}/doc/* ${PREFIX}/share/doc/wla-dx

.include <bsd.port.mk>
