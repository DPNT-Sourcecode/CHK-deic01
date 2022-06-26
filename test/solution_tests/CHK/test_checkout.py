from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("ABCDABCD") == 215
        assert checkout_solution.checkout("AAAAAAAAAEEBBB") == 505
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("ZST") == 45
        assert checkout_solution.checkout("AAABBBEEZSS") == 300

