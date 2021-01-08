# $OpenBSD: Makefile,v 1.10 2007/09/15 18:44:36 steven Exp $

COMMENT=	monte carlo simulation software

V=		6.2.0
DISTNAME =	mcsim-${V}
CATEGORIES=	math

HOMEPAGE=	http://www.gnu.org/software/mcsim/

MASTER_SITES=	${MASTER_SITE_GNU:=mcsim/}

MAINTAINER=	Peter Valchev <pvalchev@openbsd.org>

FAKE_FLAGS=	PREFIX="${WRKINST}${PREFIX}"
#WRKDIST=	${WRKDIR}/mcsim

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB=		c m

CONFIGURE_STYLE=        gnu
CONFIGURE_ENV+=		CPPFLAGS="-I${LOCALBASE}/include -I${LOCALBASE}/include/gsl" \
			LDFLAGS="-L${LOCALBASE}/lib"

LIB_DEPENDS +=		devel/gsl

USE_GMAKE=		Yes
ALL_TARGET=		one

#do-build:
#	@(cd ${WRKSRC}/mod && ${SETENV} ${MAKE_ENV} ${MAKE_PROGRAM} ${MAKE_FLAGS})
#	@(cd ${WRKSRC}/sim && ${SETENV} ${MAKE_ENV} ${MAKE_PROGRAM} ${MAKE_FLAGS})

#do-regress:
#	@(cd ${WRKSRC}/sim && chmod 755 Test_mcsim && ./Test_mcsim)

TEST_TARGET =	check

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/mod/mod ${PREFIX}/bin/mod
#	${INSTALL_PROGRAM} ${WRKSRC}/sim/mcsim ${PREFIX}/bin/mcsim
# libmcsim.so
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/mcsim
	${INSTALL_DATA} ${WRKSRC}/doc/*.txt ${WRKSRC}/doc/MCSim* ${PREFIX}/share/doc/mcsim/
	${INSTALL_DATA} ${WRKSRC}/doc/mcsim.html ${WRKSRC}/doc/mcsim.pdf ${PREFIX}/share/doc/mcsim

.include <bsd.port.mk>
