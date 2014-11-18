# $OpenBSD$

COMMENT =		???

DISTNAME =		wafp-0.01-26c3
CATEGORIES =		security

HOMEPAGE =		http://mytty.org/wafp/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB =		???

MASTER_SITES =		http://mytty.org/wafp/

MODULES =		lang/ruby
#BUILD_DEPENDS =	???
#RUN_DEPENDS =		???
LIB_DEPENDS =		sqlite3::databases/sqlite3 \
			::databases/ruby-sqlite3

NO_BUILD =		Yes
NO_TEST =		Yes

pre-configure:
		${SUBST_CMD} ${WRKSRC}/wafp.rb ${WRKSRC}/lib/wafp_https.rb
                        
do-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp/utils
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp/lib
		${INSTALL_DATA} ${WRKSRC}/utils/* ${PREFIX}/share/wafp/utils
		${INSTALL_DATA} ${WRKSRC}/lib/* ${PREFIX}/share/wafp/lib
		${INSTALL_DATA} ${WRKSRC}/*.db ${PREFIX}/share/wafp
		${INSTALL_SCRIPT} ${WRKSRC}/wafp.rb ${PREFIX}/bin

.include <bsd.port.mk>
