# $OpenBSD$

COMMENT =		generic virtualenv management and test command line tool

MODPY_EGG_VERSION =	1.4.2
DISTNAME =		tox-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		devel

HOMEPAGE =		http://codespeak.net/tox

# GPLv2
PERMIT_PACKAGE_CDROM =		Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_DISTFILES_FTP =		Yes

MASTER_SITES=		${MASTER_SITE_PYPI:=t/tox/}

EXTRACT_SUFX =		.zip

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

# XXX: need py-py >1.4.9
RUN_DEPENDS =		devel/py-py \
			devel/py-virtualenv

REGRESS_DEPENDS =	devel/py-test \
			${RUN_DEPENDS}

do-regress: fake
			@cd ${WRKSRC} && PYTHONPATH=${WRKINST}${MODPY_SITEPKG} \
			${MODPY_BIN} ./setup.py test

.include <bsd.port.mk>
