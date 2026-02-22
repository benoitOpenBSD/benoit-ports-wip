COMMENT =		Python IDE for beginners

MODPY_EGG_VERSION =	4.1.7

DISTNAME =		thonny-${MODPY_EGG_VERSION}

CATEGORIES =		editors

HOMEPAGE =		https://thonny.org

# MIT
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =    	thonny
GH_PROJECT =    	thonny
GH_TAGNAME =    	v${MODPY_EGG_VERSION}

MODULES =		lang/python
MODPY_PYBUILD =		setuptools

RUN_DEPENDS =		devel/py-astroid${MODPY_FLAVOR} \
			devel/py-asttokens${MODPY_FLAVOR} \
			devel/py-jedi${MODPY_FLAVOR} \
			devel/py-mypy${MODPY_FLAVOR} \
			devel/py-send2trash${MODPY_FLAVOR} \
			devel/py-serial${MODPY_FLAVOR} \
			devel/pylint${MODPY_FLAVOR} \
			lang/python/${MODPY_VERSION},-tkinter \
			textproc/py-docutils${MODPY_FLAVOR} \
			${MODPY_TKINTER_DEPENDS}

.include <bsd.port.mk>
