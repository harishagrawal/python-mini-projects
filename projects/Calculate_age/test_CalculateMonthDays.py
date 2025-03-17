import pytest
import time
from calendar import isleap
from calculate import month_days

class Test_CalculateMonthDays:

    @pytest.mark.valid
    @pytest.mark.smoke
    def test_31_day_months(self):
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        for month in months_with_31_days:
            assert month_days(month, False) == 31

    @pytest.mark.valid
    @pytest.mark.smoke
    def test_30_day_months(self):
        months_with_30_days = [4, 6, 9, 11]
        for month in months_with_30_days:
            assert month_days(month, False) == 30

    @pytest.mark.valid
    @pytest.mark.regression
    def test_february_leap_year(self):
        assert month_days(2, True) == 29

    @pytest.mark.valid
    @pytest.mark.regression
    def test_february_non_leap_year(self):
        assert month_days(2, False) == 28

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_invalid_month_input(self):
        with pytest.raises(ValueError):
            month_days(13, False)

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_non_integer_month_input(self):
        with pytest.raises(TypeError):
            month_days("January", False)

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_non_boolean_leap_year_input(self):
        with pytest.raises(TypeError):
            month_days(2, "yes")

    @pytest.mark.valid
    @pytest.mark.edge
    def test_edge_case_month_inputs(self):
        assert month_days(1, False) == 31
        assert month_days(12, False) == 31

    @pytest.mark.valid
    @pytest.mark.regression
    def test_leap_year_non_february_months(self):
        months = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month in months:
            assert month_days(month, True) == month_days(month, False)

    @pytest.mark.valid
    @pytest.mark.regression
    def test_leap_year_february(self):
        assert month_days(2, True) == 29
