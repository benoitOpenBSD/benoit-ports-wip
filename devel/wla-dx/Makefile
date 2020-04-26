# $OpenBSD$

COMMENT =		yet Another Multi Platform Cross Assembler

DISTNAME =		wla-dx-20200419
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/vhelin/wla-dx

GH_ACCOUNT =		vhelin
GH_PROJECT =		wla-dx
GH_COMMIT =		9ee72c6a8342b6b9a687e7086014cb97d82f5177

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
