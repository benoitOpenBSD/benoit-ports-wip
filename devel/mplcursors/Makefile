
COMMENT =		interactive data selection cursors for Matplotlib

MODPY_EGG_VERSION =     0.7
GH_ACCOUNT =    	anntzer
GH_PROJECT =    	mplcursors
GH_TAGNAME =		v${MODPY_EGG_VERSION}

CATEGORIES =		devel

HOMEPAGE =		https://github.com/anntzer/mplcursors

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Zlib
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PYBUILD =		setuptools_scm
MODPY_PYTEST =		Yes

RUN_DEPENDS =		graphics/py-matplotlib \
			math/py-numpy \
			devel/py-importlib-metadata

#NO_TEST =		Yes

.include <bsd.port.mk>
