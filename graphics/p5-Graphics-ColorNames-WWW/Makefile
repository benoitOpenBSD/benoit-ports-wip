# $OpenBSD: Makefile,v 1.5 2010/12/03 11:45:38 ajacoutot Exp $

COMMENT=	WWW color names and equivalent RGB values

MODULES=	cpan
DISTNAME=	Graphics-ColorNames-WWW-1.13
CATEGORIES=	graphics www
USE_GROFF =	Yes

MAINTAINER=	Simon Bertrang <simon@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

RUN_DEPENDS=	graphics/p5-Graphics-ColorNames

REGRESS_DEPENDS =	devel/p5-Test-NoWarnings

.include <bsd.port.mk>
