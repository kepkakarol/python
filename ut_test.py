from unittest.mock import patch, MagicMock
import unittest
from module import Dumper, DumperFactory, Producent
import module




class KnownValues(unittest.TestCase):
    def side_effect(self):
        return
    # @patch('module.Dumper',create ="text")
    def test(unittes):#, dumperMock):

        text = "text"
        attrs = {'dump.return_value': text}
        dumperMock = MagicMock(**attrs)
        
        dumperMockNew = MagicMock()
        attrs = {'dump.return_value': 'new text'}
        dumperMockNew.configure_mock(**attrs)

        # attrs = {'create.return_value': dumperMock, 'createNew.return_value': dumperMockNew}
        mock = MagicMock(return_value=MagicMock(),**{'create.return_value': dumperMock, 'createNew.return_value': dumperMockNew} )
        # mock.configure_mock(**attrs)
        dump = mock.create()
        print(dump.dump())


        dump = mock.create()
        print(dump.dump())

        dump = mock.createNew()
        print(dump.dump())
        # f = DumperFactory()
        # p = Producent(f)
        #
        # product = p.produce()
        # print("lama", product)
        # assert product == "text"

if __name__ == "__main__":
    unittest.main()