
COMMENT =		yet Another Multi Platform Cross Assembler

DISTNAME =		wla-dx-20251228
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/vhelin/wla-dx

GH_ACCOUNT =		vhelin
GH_PROJECT =		wla-dx
GH_COMMIT =		0143a1e5aad5ca794e64b8fefe1edaa495d11d7e

WANTLIB +=		c m

MODULES =		devel/cmake

# XXX problem doc/sphinx/singletext.py WIP -> doas pkg_add py3-sphinx
BUILD_DEPENDS =		textproc/py-sphinx${MODPY_FLAVOR}

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/wla-dx/tests
	cp -R ${WRKSRC}/tests/* ${PREFIX}/share/wla-dx/tests
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/wla-dx
	cp -R ${WRKSRC}/doc/* ${PREFIX}/share/doc/wla-dx

.include <bsd.port.mk>
