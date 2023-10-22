
COMMENT =		software 3D model renderer

DISTNAME =		soft-renderer-20210207
CATEGORIES =		graphics

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/wangyu-/soft-renderer

GH_ACCOUNT =		wangyu-
GH_PROJECT =		soft-renderer
GH_COMMIT =		5b457842dd051b543880aa4755bcb6ff4a55ec9d

WANTLIB +=		c ${COMPILER_LIBCXX} m X11

MAKE_FILE =		makefile

NO_TEST =		Yes

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/soft-renderer/model
	cp -R ${WRKSRC}/model/* ${PREFIX}/share/soft-renderer/model
	${INSTALL_PROGRAM} ${WRKSRC}/render ${PREFIX}/bin/

.include <bsd.port.mk>
