# $OpenBSD: Makefile,v 1.13 2012/03/29 13:38:13 sthen Exp $

COMMENT=	gcc for arm-none-eabi cross-development

VERSION =	4.9.2
DISTNAME=	gcc-${VERSION}
PKGNAME=	${CONFIG}-gcc-${VERSION}

HOMEPAGE=	https://gcc.gnu.org

SUBST_VARS+=	VERSION

WANTLIB=	c gmp mpc mpfr
DIST_SUBDIR=	gcc

MAKE_GXX=	No
MAKE_FORTRAN=	No
MAKE_OBJC=	No
MAKE_JAVA=	No
MAKE_ADA=	No

SHARED_LIBS	+=	lto_plugin                0.0 # 0.0

MASTER_SITES= 	${MASTER_SITE_GCC:=releases/gcc-$(VERSION)/}

BUILD_DEPENDS+=	devel/autoconf/2.64	\
		devel/bison		\
		devel/metaauto		\
		devel/arm-none-eabi/binutils

LIB_DEPENDS=	devel/gmp>=4.3.2	\
		devel/mpfr>=2.4.2	\
		devel/libmpc>=0.8.1

LANGS=		c,c++
CC=		/usr/bin/gcc
CFLAGS=		-O2 -g

CONFIGURE_ARGS+=--enable-languages=${LANGS}	\
		--enable-multilib		\
		--enable-interwork		\
		--with-newlib			\
		--enable-cpp
CONFIGURE_ENV=	CPPFLAGS="-I${LOCALBASE}/include" \
		LDFLAGS="-L${LOCALBASE}/lib"

# cope with user settings in /etc/mk.conf
MAKE_FLAGS=	LANGUAGES="c c++" CFLAGS="-I/usr/local/include"
MAKE_ENV=	MACHINE_ARCH=arm-none-eabi

SEPARATE_BUILD=	Yes
USE_GMAKE=	Yes
YACC=		bison

TEST_DEPENDS=	devel/dejagnu

post-install:
	chown -R ${SHAREOWN}:${SHAREGRP} \
		${PREFIX}/lib/gcc/${CONFIG}/${VERSION}/

.include <bsd.port.mk>
