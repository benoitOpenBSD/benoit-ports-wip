# $OpenBSD: Makefile,v 1.4 2007/09/15 22:36:53 merdely Exp $

COMMENT=	test performance of a remote TCP service

VERSION=	6.0.2
DISTNAME=	echoping-${VERSION}
CATEGORIES=	net

MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=echoping/}

HOMEPAGE=	http://echoping.sourceforge.net/

MAINTAINER=     Jakob Schlyter <jakob@openbsd.org>

# GPLv2
# See http://www.openssl.org/support/faq.html#LEGAL2 and
# http://lists.debian.org/debian-legal/2002/debian-legal-200210/msg00113.html
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes
WANTLIB=		c crypto m ssl

NO_REGRESS=		Yes
USE_GROFF =		Yes

LIB_DEPENDS=		devel/popt \
			databases/postgresql

CONFIGURE_STYLE=	gnu
CONFIGURE_ENV+=		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
CONFIGURE_ARGS+=	--enable-http \
			--enable-icp \
			--enable-smtp \
			--enable-tos \
			--without-libidn \
			--with-ssl=/usr \
			--enable-tcp-info

.include <bsd.port.mk>
