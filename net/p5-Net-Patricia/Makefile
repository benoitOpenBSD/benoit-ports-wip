# $OpenBSD: Makefile,v 1.8 2010/12/03 11:45:42 ajacoutot Exp $

SHARED_ONLY=	Yes

COMMENT=	Patricia Trie perl module for fast IP address lookups

MODULES=	cpan
DISTNAME=	Net-Patricia-1.19
CATEGORIES=	net
USE_GROFF =	Yes

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

RUN_DEPENDS =	net/p5-Net-CIDR-Lite \
		net/p5-Socket6

.include <bsd.port.mk>
