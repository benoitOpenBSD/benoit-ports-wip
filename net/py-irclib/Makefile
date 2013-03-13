# $OpenBSD: Makefile,v 1.13 2013/03/11 11:35:55 espie Exp $

COMMENT=	Internet Relay Chat (IRC) protocol client library for Python

MODPY_EGG_VERSION = 	8.0.1
DISTNAME =		irc-${MODPY_EGG_VERSION}
PKGNAME =		py-irclib-${MODPY_EGG_VERSION}
CATEGORIES=	net

HOMEPAGE=	http://python-irclib.sourceforge.net/

# MIT
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=i/irc/}
EXTRACT_SUFX =		.zip

MODULES=	lang/python
MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		devel/py-hgtools \
			devel/pytest-runner
BUILD_DEPENDS =		${RUN_DEPENDS}

NO_TEST=	Yes

EXAMPLES =	dccreceive.py dccsend.py irccat.py irccat2.py servermap.py testbot.py
EXAMPLESDIR =	${PREFIX}/share/examples/py-irclib

pre-install:
		chmod 644 ${WRKSRC}/irc.egg-info/*

post-install:
	${INSTALL_DATA_DIR} ${EXAMPLESDIR}
.for f in ${EXAMPLES}
	${INSTALL_DATA} ${WRKSRC}/scripts/${f} ${EXAMPLESDIR}
.endfor

.include <bsd.port.mk>
