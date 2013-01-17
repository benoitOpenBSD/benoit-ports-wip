# $OpenBSD$

COMMENT =		packet filter module

MODPY_EGG_VERSION =	0.0.9
DISTNAME =		py-pf-${MODPY_EGG_VERSION}
CATEGORIES =		security

HOMEPAGE =		http://www.kernel-panic.it/software/py-pf/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=py-pf/}

MODULES =		lang/python

NO_REGRESS =		Yes

# XXX: Be careful with your pf rules
#do-regress: fake
#			cd ${WRKSRC} && ${SUDO} ${MODPY_BIN} setup.py test

.include <bsd.port.mk>
