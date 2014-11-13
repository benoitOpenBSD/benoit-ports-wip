# $OpenBSD: Makefile,v 1.4 2007/09/15 18:44:36 steven Exp $

COMMENT=	library for reading and writing Matlab MAT files

DISTNAME=	matio-1.3.3
SHARED_LIBS=	matio	2.0
CATEGORIES=	math

HOMEPAGE=	http://sourceforge.net/projects/matio/

# LGPLv2.1
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=matio/}

WANTLIB=	g2c m

BUILD_DEPENDS=	devel/doxygen

USE_LIBTOOL=	Yes
CONFIGURE_STYLE=gnu
CONFIGURE_ARGS=	${CONFIGURE_SHARED} \
		--enable-fortran=no \
		--enable-test=yes \
		--enable-docs=yes

TESTS=	copy write writecompressed writecell readslab \
	writeslab writesparse writenan writeinf readslab4 ind2sub sub2ind \
	write_compressed_cell write_compressed_sparse

do-regress:
.for t in ${TESTS}
	@echo "Testing ${t}"
	@cd ${WRKBUILD}/test && ./test_mat ${t}
.endfor

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/matio
	${INSTALL_DATA} ${WRKSRC}/doxygen/html/* ${PREFIX}/share/doc/matio
	@rm -rf ${PREFIX}/share/matio
	@rm -rf ${PREFIX}/bin/test_*

.include <bsd.port.mk>
