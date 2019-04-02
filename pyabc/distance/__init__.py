"""
Distance functions
==================

Distance functions measure closeness of observed and sampled data. This
module implements various commonly used distance functions for ABC, featuring
a few advanced concepts.

For custom distance functions, either pass a plain function to ABCSMC or
subclass the pyabc.Distance class.
"""

from .base import (
    Distance,
    NoDistance,
    IdentityFakeDistance,
    AcceptAllDistance,
    SimpleFunctionDistance,
    to_distance)
from .distance import (
    PNormDistance,
    AdaptivePNormDistance,
    ZScoreDistance,
    PCADistance,
    MinMaxDistance,
    PercentileDistance,
    RangeEstimatorDistance,
    DistanceWithMeasureList)
from .scales import (
    median_absolute_deviation,
    mean_absolute_deviation,
    standard_deviation,
    bias,
    root_mean_square_deviation,
    median_absolute_deviation_to_observation,
    mean_absolute_deviation_to_observation,
    combined_median_absolute_deviation,
    combined_mean_absolute_deviation,
    standard_deviation_to_observation)
from .kernel import (
    StochasticKernel,
    RET_SCALE_LIN,
    RET_SCALE_LOG,
    SimpleFunctionKernel,
    NormalKernel,
    IndependentNormalKernel,
    BinomialKernel)


__all__ = [
    # base
    "Distance",
    "NoDistance",
    "IdentityFakeDistance",
    "AcceptAllDistance",
    "SimpleFunctionDistance",
    "to_distance",
    # distance
    "PNormDistance",
    "AdaptivePNormDistance",
    "ZScoreDistance",
    "PCADistance",
    "MinMaxDistance",
    "PercentileDistance",
    "RangeEstimatorDistance",
    "DistanceWithMeasureList",
    # scales
    "median_absolute_deviation",
    "mean_absolute_deviation",
    "standard_deviation",
    "bias",
    "root_mean_square_deviation",
    "median_absolute_deviation_to_observation",
    "mean_absolute_deviation_to_observation",
    "combined_median_absolute_deviation",
    "combined_mean_absolute_deviation",
    "standard_deviation_to_observation",
    # kernels
    "StochasticKernel",
    "RET_SCALE_LIN",
    "RET_SCALE_LOG",
    "SimpleFunctionKernel",
    "NormalKernel",
    "IndependentNormalKernel",
    "BinomialKernel",
]