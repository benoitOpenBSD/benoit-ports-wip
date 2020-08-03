# $OpenBSD$

COMMENT =		library for rich text in the terminal

MODPY_EGG_VERSION =	5.0.0
DISTNAME =		rich-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		devel

HOMEPAGE =		https://github.com/willmcgugan/rich

# MIT
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

# Not working...
TEST_DEPENDS =		devel/py-typing-extensions${MODPY_FLAVOR} \
			textproc/py-pygments${MODPY_FLAVOR}

.include <bsd.port.mk>
