COMMENT=	gdb for ${CONFIG} cross-development

DISTNAME=	gdb-7.12.1
EXTRACT_SUFX=	.tar.xz
REVISION=	1

FLAVORS=	aarch64 arm
FLAVOR?=	arm

.if "${FLAVOR}" == "aarch64"
CONFIG=		aarch64-none-elf
.elif "${FLAVOR}" == "arm"
CONFIG=		arm-none-eabi
.else
ERRORS+=	"either aarch64 or arm FLAVOR should be set"
.endif

HOMEPAGE=	https://www.gnu.org/software/gdb/

WANTLIB=	${COMPILER_LIBCXX} c expat m curses pthread

SITES 	=	${SITE_GNU:=gdb/}
DIST_SUBDIR=	gdb

CFLAGS+=	-Dunix

CONFIGURE_ARGS+=--enable-multilib \
		--enable-thumb \
		--enable-interwork \
		--without-guile

MODULES=	lang/python
MODPY_VERSION =	${MODPY_DEFAULT_VERSION_2}

TEST_DEPENDS=devel/dejagnu

.include <bsd.port.mk>
