from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("ABCDABCD") == 215
        assert checkout_solution.checkout("AAAAAAAAAEEBBB") == 505


