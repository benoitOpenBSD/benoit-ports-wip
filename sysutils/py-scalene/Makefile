# $OpenBSD$

COMMENT =		high performance profiler for python

MODPY_EGG_VERSION =	0.9.21
DISTNAME =		scalene-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		sysutils

HOMEPAGE =		https://github.com/emeryberger/scalene

# Apache 2.0
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

RUN_DEPENDS =		devel/py-cloudpickle${MODPY_FLAVOR} \
			devel/py-rich${MODPY_FLAVOR}

.include <bsd.port.mk>
