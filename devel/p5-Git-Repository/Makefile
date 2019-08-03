# $OpenBSD: Makefile,v 1.12 2016/03/20 19:56:24 naddy Exp $

COMMENT = 	Perl interface to Git repositories

MODULES =	cpan
PKG_ARCH =	*
DISTNAME =	Git-Repository-1.321
CATEGORIES =	devel

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# perl
PERMIT_PACKAGE =	Yes

RUN_DEPENDS =		devel/p5-System-Command \
			devel/p5-namespace-clean \
			devel/p5-Git-Version-Compare
TEST_DEPENDS =		devel/git
#			devel/p5-Test-Requires-Git
MAKE_ENV +=		TEST_POD=1

.include <bsd.port.mk>
