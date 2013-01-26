# $OpenBSD$

COMMENT =	Program to compute various message digests

DISTNAME =	md5deep-4.3
CATEGORIES =	security

HOMEPAGE =	http://md5deep.sourceforge.net/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Public domain, GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=md5deep/}

WANTLIB =		c m pthread stdc++

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu

REGRESS_DEPENDS =	shells/bash

do-regress: fake
			cd ${WRKSRC}/tests && GOOD_BIN=${WRKDIST}/src \
			/usr/local/bin/bash ./tests.sh

.include <bsd.port.mk>
