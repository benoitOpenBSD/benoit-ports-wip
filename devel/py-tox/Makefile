# $OpenBSD$

COMMENT =		generic virtualenv management and test command line tool

MODPY_EGG_VERSION =	1.4.3
DISTNAME =		tox-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		devel

HOMEPAGE =		http://codespeak.net/tox

# GPLv2
PERMIT_PACKAGE_CDROM =		Yes

MASTER_SITES=		${MASTER_SITE_PYPI:=t/tox/}

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

# XXX: need py-py >1.4.9
RUN_DEPENDS =		devel/py-py \
			devel/py-virtualenv

TEST_DEPENDS =		devel/py-test \
			${RUN_DEPENDS}

do-test: fake
			@cd ${WRKSRC} && PYTHONPATH=${WRKINST}${MODPY_SITEPKG} \
			${MODPY_BIN} ./setup.py test

.include <bsd.port.mk>
