import pytest
import time
from calendar import isleap
from calculate import judge_leap_year

class Test_CalculateJudgeLeapYear70:

    @pytest.mark.valid
    @pytest.mark.positive
    def test_judge_leap_year_typical_leap(self):
        assert judge_leap_year(2000) == True

    @pytest.mark.valid
    @pytest.mark.negative
    def test_judge_leap_year_typical_non_leap(self):
        assert judge_leap_year(1999) == False

    @pytest.mark.valid
    @pytest.mark.positive
    def test_judge_leap_year_century_leap(self):
        assert judge_leap_year(1600) == True

    @pytest.mark.valid
    @pytest.mark.negative
    def test_judge_leap_year_century_non_leap(self):
        assert judge_leap_year(1700) == False

    @pytest.mark.valid
    @pytest.mark.negative
    def test_judge_leap_year_boundary_year(self):
        assert judge_leap_year(1582) == False

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_judge_leap_year_negative_year(self):
        assert judge_leap_year(-4) == False

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_judge_leap_year_year_zero(self):
        assert judge_leap_year(0) == False

    @pytest.mark.valid
    @pytest.mark.positive
    def test_judge_leap_year_large_year(self):
        assert judge_leap_year(1000000) == isleap(1000000)

    @pytest.mark.valid
    @pytest.mark.positive
    def test_judge_leap_year_leading_zeros(self):
        assert judge_leap_year(4) == True

    @pytest.mark.valid
    @pytest.mark.positive
    def test_judge_leap_year_trailing_zeros(self):
        assert judge_leap_year(4000) == isleap(4000)
