import os
import unittest
import json
from dataProcessor import read_json_file, avg_age_country, max_age_country

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], 25)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avg_empty_json_file(self):
        with open('empty.json', 'w') as f:
            f.write('[]')
        
        result = max_age_country('empty.json')

        # Verifica se o resultado é um dicionário vazio
        self.assertDictEqual(result, {})

    def test_avg_missing_age_values(self):
        # Cria um arquivo JSON com valores de idade ausentes ou nulos
        data = [
            {"name": "Person 1", "country": "A", "age": 25},
            {"name": "Person 2", "country": "B", "age": None},
            {"name": "Person 3", "country": "A", "age": 30},
        ]

        with open('missing_age.json', 'w') as f:
            json.dump(data, f)

        result = avg_age_country('users.json')

        # Verifica se o resultado contém apenas as médias para as idades disponíveis
        expected_result = {"A": 27.5, "B": None}
        self.assertDictEqual(result, expected_result)

    def test_avg_missing_country_field(self):
        # Cria um arquivo JSON com campo 'country' ausente ou nulo
        data = [
            {"country": "A", "age": 25},
            {"age": 30},
            {"country": None, "age": 40},
        ]

        with open('missing_country.json', 'w') as f:
            json.dump(data, f)

        result = avg_age_country('users.json')

        # Verifica se a função lida corretamente com campos 'country' ausentes/nulos
        expected_result = {"A": 25.0}
        self.assertDictEqual(result, expected_result)

    def test_max_empty_json_file(self):
        with open('empty.json', 'w') as f:
            f.write('[]')

        result = max_age_country('empty.json')

        # Verifica se o resultado é um dicionário vazio
        self.assertDictEqual(result, {})

    def test_max_missing_age_values(self):
        # Cria um arquivo JSON com valores de idade ausentes ou nulos
        data = [
            {"country": "A", "age": 25},
            {"country": "B", "age": None},
            {"country": "A", "age": 30},
        ]

        with open('users.json', 'w') as f:
            json.dump(data, f)

        result = max_age_country('users.json')

        # Verifica se o resultado contém apenas as idades máximas disponíveis
        expected_result = {"A": 30, "B": None}
        self.assertDictEqual(result, expected_result)

    def test_max_missing_country_field(self):
        # Cria um arquivo JSON com campo 'country' ausente ou nulo
        data = [
            {"country": "A", "age": 25},
            {"age": 30},
            {"country": None, "age": 40},
        ]

        with open('users.json', 'w') as f:
            json.dump(data, f)

        result = max_age_country('users.json')

        # Verifica se a função lida corretamente com campos 'country' ausentes/nulos
        expected_result = {"A": 25, None: 40}
        self.assertDictEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()