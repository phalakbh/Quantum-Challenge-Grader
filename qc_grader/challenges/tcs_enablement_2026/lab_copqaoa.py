# (C) Copyright IBM 2026
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from typeguard import typechecked

from qc_grader.grader.grade import grade_answer

_CHALLENGE = "tcs_enablement_2026"
_LAB = "lab_non_covalent_sqd"


def _grade(answer_dict, exercise: str) -> None:
    grade_answer(answer_dict, lab=_LAB, exercise=exercise, challenge=_CHALLENGE)


@typechecked
def grade_lab_non_covalent_sqd_ex1(answer_dict: float) -> None:
    """
    Grade Exercise 1: zero-variance extrapolated SQD energy for the
    (16e,24o) methane dimer at R(C-C) = 3.638 Å.

    Args:
        answer_dict: Final converged/extrapolated total energy in Hartree.
    """
    _grade(answer_dict, "ex1")