import sys
import os

# Agregar la ruta al directorio raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Program import NavalBattle
import unittest

class GameTest(unittest.TestCase):

#Funcionalidad #1
#Inicializar campo de juego
    
    #Casos normales

    def testBoard(self):
        expected_board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
        
        game = NavalBattle.NavalBattle()
        board = game.generateBoard()
        self.assertEqual(expected_board, board)

    def testBoardSizes(self):
        expexted_board=[
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard()
        self.assertEqual(expexted_board, board)

    def testFourShips(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShips(4)
        self.assertEqual(4, game.ships_quantity)

    #Casos extraordinarios
    def testSmallBoard(self):
        expexted_board=[
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard(5,5)
        self.assertEqual(expexted_board, board)



    def testBigBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardIsTooBig, game.validateBoardDimensions, 21, 5)

    def testBigAndSmall(self):
        expexted_board=[
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard(9,9)
        self.assertEqual(expexted_board, board)


    #Casos de error
    def testZeroBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.validateBoardDimensions, 0, 6)
    
    def testnegativeBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.validateBoardDimensions, 6, -5)

    def testShipsInNoBoard(self):
        game = NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.addShips, 4)

    def testIDontKnow(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()


#Funcionalidad 2
#Disparar
    #Casos normales
    def testHitShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((1,2))
        coordinate = game.validateCoordinate("B3")
        resultado = game.shoot(coordinate[0], coordinate[1])

        self.assertEqual(resultado, True)

    def testMissedShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        coordinate = game.validateCoordinate("C2")
        resultado = game.shoot(coordinate[0], coordinate[1])

        self.assertEqual(resultado, False)

    def testDownedShip(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((0,0), False, 2)
        coordinate1 = game.validateCoordinate("A1")
        coordinate2 = game.validateCoordinate("B1")
        game.shoot(coordinate1[0], coordinate1[1])
        game.shoot(coordinate2[0], coordinate2[1])
        
        self.assertTrue(game.isShipDowned())


    def testNotDownedShip(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((0,0), False, 2)
        
        coordinate = game.validateCoordinate("A1")
        game.shoot(coordinate[0], coordinate[1])
        
        self.assertFalse(game.isShipDowned())

    #Casos extraordinarios
    def testShotSamePlace(self):
        game= NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((2,1), False, 2)
        coordinate = game.validateCoordinate("C2")
        game.shoot(coordinate[0], coordinate[1])
        self.assertFalse(game.shoot(coordinate[0], coordinate[1]))


    def testCornerShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((4,0))
        coordinate = game.validateCoordinate("e1")
        self.assertEqual(game.shoot(coordinate[0], coordinate[1]), True)


    def testLastOne(self):
        
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((4,0))
        coordinate = game.validateCoordinate("e3")
        self.assertEqual(game.shoot(coordinate[0], coordinate[1]), True)

    #Casos de error
    def testInvalidCoordinate(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.InvalidCoordinate, game.validateCoordinate, "A21")

    def testInvalidCoordinate2(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.ColumnOutOfRange, game.validateCoordinate, "44")

    def testColumnOutOfRange(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.ColumnOutOfRange, game.validateCoordinate, "K1")

    def testRowOutOfRange(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.RowOutOfRange, game.validateCoordinate, "A9")


if __name__ == '__main__':
    unittest.main()
