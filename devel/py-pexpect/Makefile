# $OpenBSD: Makefile,v 1.11 2010/08/30 22:24:15 jasper Exp $

COMMENT=	pure Python Expect-like module

MODPY_EGG_VERSION =	2.3
DISTNAME =	pexpect-${MODPY_EGG_VERSION}
PKGNAME=	py-${DISTNAME}
CATEGORIES=	devel

HOMEPAGE=	http://pexpect.sourceforge.net/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Python 
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=pexpect/}

MODULES=	lang/python

EXAMPLESDIR=	${PREFIX}/share/examples/py-pexpect
DOCDIR=		${PREFIX}/share/doc/py-pexpect

NO_REGRESS=	Yes

pre-build:
	@perl -pi -e "s,^\#\!/usr/bin/env python,#!${MODPY_BIN}," ${WRKSRC}/examples/*.py
        
post-install:
	${INSTALL_DATA_DIR} ${EXAMPLESDIR}
	${INSTALL_DATA} ${WRKSRC}/{ANSI,FSM,screen}.py ${EXAMPLESDIR}
	${INSTALL_DATA} ${WRKSRC}/examples/* ${EXAMPLESDIR}
	${INSTALL_DATA_DIR} ${DOCDIR}
	${INSTALL_DATA} ${WRKSRC}/doc/* ${DOCDIR}

.include <bsd.port.mk>
