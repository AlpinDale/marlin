from setuptools import setup
from torch.utils import cpp_extension

setup(
    name='marlin-gptq',
    version='0.1.1',
    author='Elias Frantar',
    author_email='elias.frantar@ist.ac.at',
    description='Highly optimized FP16xINT4 CUDA matmul kernel.',
    install_requires=['numpy', 'torch==2.2.0', 'optimum'],
    url="https://github.com/AlpinDale/marlin",
    packages=['marlin'],
    ext_modules=[cpp_extension.CUDAExtension(
        'marlin_cuda', ['marlin/marlin_cuda.cpp', 'marlin/marlin_cuda_kernel.cu']
    )],
    cmdclass={'build_ext': cpp_extension.BuildExtension},
)
