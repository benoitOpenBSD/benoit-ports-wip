# $OpenBSD: Makefile,v 1.6 2008/06/13 19:28:55 brad Exp $

COMMENT=	GNU oSIP library

DISTNAME=	libosip2-3.3.0
SHARED_LIBS +=	osipparser2	4.0	# .6.0
SHARED_LIBS +=	osip2		4.0	# .6.0

CATEGORIES=	telephony devel

HOMEPAGE=	http://www.gnu.org/software/osip/

# LGPLv2.1+
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

MASTER_SITES=	${MASTER_SITE_GNU:=osip/}

USE_LIBTOOL=	Yes

CONFIGURE_STYLE=gnu
CONFIGURE_ARGS=	--disable-debug \
		--enable-test

REGRESS_TARGET=	check

.include <bsd.port.mk>
