import unittest
import main

## Test 결과가 틀리면 통과하지 못하게 해보기

class MainTest(unittest.TestCase) :
    def test_helloworld(self) :
        ret = main.helloworld("Test")
        self.assertEqual(ret, "Hello World! Chris!")
    
if __name__ == "__main__" :
    unittest.main()