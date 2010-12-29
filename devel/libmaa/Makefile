# $OpenBSD$

COMMENT=	General purpose data structures and functions

DISTNAME=	libmaa-1.1.1
SHARED_LIBS=	maa	0.0	# .1.0
CATEGORIES=	devel

HOMEPAGE=	http://www.dict.org/bin/Dict

MAINTAINER=	Benoit Lecocq <blq@arcane-labs.net>
		
# GPLv2 / LGPLv2
PERMIT_PACKAGE_CDROM=   Yes
PERMIT_PACKAGE_FTP=     Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=   Yes

WANTLIB=		c m
                
MASTER_SITES=   	${MASTER_SITE_SOURCEFORGE:=dict/}

USE_LIBTOOL=		Yes
USE_GMAKE=		Yes

CONFIGURE_STYLE=	gnu
  
REGRESS_TARGET=		test

post-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/libmaa
		${INSTALL_DATA} ${WRKSRC}/doc/libmaa.600dpi.ps ${PREFIX}/share/doc/libmaa
                                
.include <bsd.port.mk>
