BROKEN-arm=	ICE: Bus error in unwind-dw2.c

COMMENT=	gcc for ${CONFIG} cross-development, Linaro version

VERSION=	7.5-2019.12
DISTNAME=	gcc-linaro-${VERSION}
EXTRACT_SUFX=	.tar.xz
PKGNAME=	${CONFIG}-gcc-linaro-${VERSION:S/-/./g}

FLAVORS=	aarch64 arm
FLAVOR?=	arm

.if "${FLAVOR}" == "aarch64"
CONFIG=		aarch64-none-elf
.elif "${FLAVOR}" == "arm"
CONFIG=		arm-none-eabi
.else
ERRORS+=	"either aarch64 or arm FLAVOR should be set"
.endif

GCC_VERSION=	7.5.0
SUBST_VARS+=	VERSION CONFIG GCC_VERSION

.if ${MACHINE_ARCH} == "powerpc64"
PATCH_LIST =	patch-* vecstep-*
.endif

WANTLIB=	c m ${COMPILER_LIBCXX} gmp mpfr mpc
DIST_SUBDIR=	gcc

MAKE_GXX=	No
MAKE_FORTRAN=	No
MAKE_OBJC=	No
MAKE_JAVA=	No
MAKE_ADA=	No

# The "base" prefix is somewhat arbitrary, and introduced mostly because
# portcheck complains about lines longer than 80 characters.
SITE_BASE =	https://releases.linaro.org/components
SITES = 	${SITE_BASE}/toolchain/gcc-linaro/${VERSION}/

MODULES=	lang/python

BUILD_DEPENDS+=	devel/autoconf/2.13 \
		devel/metaauto

.if ${FLAVOR:Maarch64}
BUILD_DEPENDS+=	devel/arm-none-eabi/binutils,aarch64 \
		devel/arm-none-eabi/newlib,aarch64
RUN_DEPENDS=	devel/arm-none-eabi/binutils,aarch64 \
		devel/arm-none-eabi/newlib,aarch64
.elif ${FLAVOR:Marm}
BUILD_DEPENDS+=	devel/arm-none-eabi/binutils,arm \
		devel/arm-none-eabi/newlib,arm
RUN_DEPENDS=	devel/arm-none-eabi/binutils,arm \
		devel/arm-none-eabi/newlib,arm
.else
ERRORS+=	"either aarch64 or arm FLAVOR should be set"
.endif

LIB_DEPENDS=	devel/mpfr \
		devel/libmpc

LANGS=		c,c++

CONFIGURE_ENV+=	AR_FOR_TARGET="${INSTALLDIR}/bin/${CONFIG}-ar" \
		RANLIB_FOR_TARGET="${INSTALLDIR}/bin/${CONFIG}-ranlib"
CONFIGURE_ARGS+=--enable-languages=${LANGS} \
		--with-as="${INSTALLDIR}/bin/${CONFIG}-as" \
		--with-ld="${INSTALLDIR}/bin/${CONFIG}-ld" \
		--with-sysroot="${INSTALLDIR}/${CONFIG}" \
		--enable-multilib \
		--enable-interwork \
		--with-gmp=${LOCALBASE} \
		--with-newlib \
		--disable-lto \
		--enable-cpp \
		--disable-plugin \
		--without-isl

TEST_DEPENDS=devel/dejagnu

post-install:
	chown -R ${SHAREOWN}:${SHAREGRP} \
		${PREFIX}/lib/gcc/${CONFIG}/${VERSION}/
	${MODPY_BIN} ${MODPY_LIBDIR}/compileall.py ${PREFIX}/${CONFIG}/

.include <bsd.port.mk>

# The preprocessed source exceeds the suggested implementation limit
# of 256 for nesting levels of parenthesized expressions within a
# full-expression as given in Annex B of the C++ standard.
.if ${PROPERTIES:Mclang}
CXXFLAGS+=	-fbracket-depth=512
.endif
