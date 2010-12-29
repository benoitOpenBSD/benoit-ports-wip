# $OpenBSD: Makefile,v 1.12 2007/11/29 13:43:08 okan Exp $ 
# $FreeBSD: ports/math/netcdf/Makefile,v 1.7 2000/06/16 21:51:39 asami Exp $

COMMENT=	library for machine-independent, array-oriented data access

DISTNAME=	netcdf-4.0.1
CATEGORIES=	math

SHARED_LIBS=	netcdf		5.0	# .4.0
SHARED_LIBS+=	netcdff		5.0	# .4.0
SHARED_LIBS+=	netcdf_c++	5.0	# .4.0

HOMEPAGE=	http://www.unidata.ucar.edu/packages/netcdf/

MAINTAINER=	Benoit Lecocq <blq@arcane-labs.net>

# BSD-like
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=		c m

MASTER_SITES=		ftp://ftp.unidata.ucar.edu/pub/netcdf/

USE_GMAKE=		Yes
USE_LIBTOOL=		Yes

CONFIGURE_STYLE= 	gnu
CONFIGURE_ENV=		CPPFLAGS="${CPPFLAGS} -Df2cFortran"
CONFIGURE_ARGS+=	${CONFIGURE_SHARED} \
			--disable-f90 \
			--enable-examples \
			--enable-docs-install \
			--enable-extra-tests

post-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/doc/netcdf
			@cd ${WRKSRC}/man && ${INSTALL_DATA} *.txt *.pdf \
			${PREFIX}/share/doc/netcdf

# Some utf8 tests are failing
# NO_REGRESS=          Yes
REGRESS_TARGET=		check

.include <bsd.port.mk>
