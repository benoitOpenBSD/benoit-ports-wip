# $OpenBSD$

COMMENT =	collection of command line tools for processing TZX files

V =		1.9.2
DISTNAME =	tsxtools-${V}
CATEGORIES =	sysutils

HOMEPAGE =	https://github.com/shred/tzxtools

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MASTER_SITES =          ${MASTER_SITES_GITHUB}
GH_ACCOUNT =            shred
GH_PROJECT =            tzxtools
GH_TAGNAME =            $V

MODPY_SETUPTOOLS =	Yes

FLAVORS =		python3
FLAVOR =		python3

RUN_DEPENDS =		graphics/py-png${MODPY_FLAVOR}

NO_TEST =		Yes

.include <bsd.port.mk>
