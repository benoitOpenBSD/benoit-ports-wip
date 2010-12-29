# $OpenBSD: Makefile,v 1.5 2009/05/27 20:52:15 benoit Exp $

COMMENT =	unit test framework for C programs

DISTNAME =	check-0.9.8
SHARED_LIBS +=	check	2.0	# .0.0
CATEGORIES =	devel

HOMEPAGE =	http://check.sf.net/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# LGPLv2.1
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =	${MASTER_SITE_SOURCEFORGE:=check/}

USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
                        
.include <bsd.port.mk>
