# $OpenBSD: Makefile,v 1.13 2013/03/11 10:50:21 espie Exp $

COMMENT =	simple interface to subversion's editor interface#'

DISTNAME =	SVN-Simple-0.28
CATEGORIES =	devel

CPAN_AUTHOR =	CLKAO
MODULES =	cpan

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM =	Yes

RUN_DEPENDS =	devel/subversion,-perl>=1.1.1
BUILD_DEPENDS =	${RUN_DEPENDS}

.include <bsd.port.mk>
