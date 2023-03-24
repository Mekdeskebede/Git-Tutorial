import pytest
from Arthemetic import ArthimeticClass

class TestArithmeticClass:

    def test_add(self ):
        # arrange
        x, y = 2.0, 1.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")

        expected_sub = 1.0
        actual_sub = ArthimeticClass.subtract(x,y)

        with pytest.raises(TypeError):
            ArthimeticClass.subtract("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.subtract("1", "2")

        expected_mul = 2.0
        actual_mul = ArthimeticClass.multiply(x,y)

        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.multiply("1", "2")

        expected_div = 2.0
        actual_div = ArthimeticClass.divide(x,y)
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.divide(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.divide("1", "2")
        with pytest.raises(ZeroDivisionError):
            ArthimeticClass.divide(1, 0)

        
        assert expected_output == actual_output
        assert expected_sub == actual_sub
        assert expected_mul == actual_mul
        assert expected_div == actual_div
