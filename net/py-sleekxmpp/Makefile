# $OpenBSD$

COMMENT =		Python XMPP (Jabber) Library

MODPY_EGG_VERSION =	1.0
DISTNAME =		fritzy-SleekXMPP-${MODPY_EGG_VERSION}
PKGNAME =		py-sleekxmpp-${MODPY_EGG_VERSION}
CATEGORIES =		net

HOMEPAGE =		http://sleekxmpp.com/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://github.com/fritzy/SleekXMPP/tarball/${MODPY_EGG_VERSION}/

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

WRKDIST =		${WRKDIR}/${DISTNAME:S/-${MODPY_EGG_VERSION}/-79f1aa0/}

do-regress:
			cd ${WRKSRC} && ${MODPY_BIN} testall.py --verbose
                        
.include <bsd.port.mk>
