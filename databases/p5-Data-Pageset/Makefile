# $OpenBSD: Makefile,v 1.6 2010/12/03 11:44:24 ajacoutot Exp $

COMMENT=	pager utility

DISTNAME=	Data-Pageset-1.06
CATEGORIES=	databases
MODULES=	cpan
USE_GROFF =	Yes

# Perl
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

RUN_DEPENDS=	databases/p5-Data-Page
BUILD_DEPENDS = ${RUN_DEPENDS}

.include <bsd.port.mk>
