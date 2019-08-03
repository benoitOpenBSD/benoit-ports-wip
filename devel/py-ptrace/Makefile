# $OpenBSD$

COMMENT =		debugger using ptrace written in Python. 

MODPY_EGG_VERSION =	0.6.4
DISTNAME =		python-ptrace-${MODPY_EGG_VERSION}
PKGNAME =		py-ptrace-${MODPY_EGG_VERSION}
CATEGORIES =		devel

HOMEPAGE =		http://bitbucket.org/haypo/python-ptrace/wiki/Home

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=p/python-ptrace/}

MODULES =		lang/python

pre-configure:
			@${SUBST_CMD} ${WRKSRC}/setup.py

.include <bsd.port.mk>
