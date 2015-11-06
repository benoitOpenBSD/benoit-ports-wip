# $OpenBSD: Makefile$

COMMENT =		use Markdown for your project description

MODPY_EGG_VERSION =	0.2
DISTNAME =		setuptools-markdown-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		textproc

HOMEPAGE =		https://github.com/msabramo/setuptools-markdown

# MIT
PERMIT_PACKAGE_CDROM =	Yes

MODPY_PI =		Yes

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		textproc/pypandoc

.include <bsd.port.mk>
