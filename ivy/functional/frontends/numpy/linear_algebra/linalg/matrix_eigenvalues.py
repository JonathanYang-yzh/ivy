# for review
# global
import ivy


def eigh(a, UPLO='L'):
    return ivy.eigh(a, UPLO=UPLO)


eigh.unsupported_dtypes = ("float16",)
