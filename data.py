import os
import json

FILES_PATH = './DataBase/'


def save_data_to_file(data: dict, file_name: str):
	file_path = FILES_PATH + file_name + '.json'

	# Если файл не существует, создаем его
	if not os.path.exists(file_path):
		# Создаем директорию, если она не существует
		os.makedirs(FILES_PATH, exist_ok=True)
		with open(file_path, 'w') as file:
			json.dump([data], file, indent=4)
	else:
		# Если файл существует, пытаемся загрузить данные
		try:
			with open(file_path, 'r') as file:
				existing_data = json.load(file)
		except json.JSONDecodeError:
			# Если файл пустой или содержит некорректный JSON, начинаем с пустого списка
			existing_data = []

		# Добавляем новые данные
		existing_data.append(data)

		# Перезаписываем файл с обновленными данными
		with open(file_path, 'w') as file:
			json.dump(existing_data, file, indent=4)


def load_data_from_file(file_name: str, param_key: str, param_value=0, quantity=1):
	if not os.path.exists(FILES_PATH + file_name + '.json'):
		return None  # Если файла нет, пользователя нет

	with open(FILES_PATH + file_name + '.json', 'r') as file:
		data = json.load(file)

	if param_key == 'all':
		return data

	if param_key == 'id' and not param_value:
		return data[-1]['id']

	if quantity == 1:
		for i in data:
			if i.get(param_key) == param_value:
				return i

	list_of_data = []
	if quantity == 'all':
		for i in data:
			if i.get(param_key) == param_value:
				list_of_data.append(i)
		return list_of_data

	return None


def update_data(file_name: str, id, param_key: str, new_param_value):
	"""
	Обновляет параметр `status` объекта с заданным `id` в JSON-файле.

	:param file_name: Имя файла JSON, где хранятся данные.
	:param id: ID объекта, у которого нужно изменить статус.
	:param param_key: Параметр объекта которого нужно изменить.
	:param new_param_value: Новое значение для параметра `status`.
	"""
	file_path = FILES_PATH + file_name + '.json'
	try:
		# Открываем и загружаем данные из JSON-файла
		with open(file_path, 'r') as file:
			data = json.load(file)

		# Проходим по объектам и ищем нужный ID
		for obj in data:
			if obj.get(param_key):
				if obj['id'] == id:
					obj[param_key] = new_param_value
					break
			else:
				print(f"Key {param_key} not found.")
				return
		else:
			print(f"Объект с ID {id} не найден.")
			return

		# Сохраняем изменения обратно в файл
		with open(file_path, 'w') as file:
			json.dump(data, file, indent=4)

		print(f"Параметр {param_key} объекта с ID {id} успешно обновлён на {new_param_value}.")

	except FileNotFoundError:
		print(f"Файл {file_name} не найден.")
	except json.JSONDecodeError:
		print(f"Ошибка чтения JSON из файла {file_path}.")
	except Exception as e:
		print(f"Произошла ошибка: {e}")


def delete_data(file_name: str, param_key: str, param_value):
	"""
	Обновляет параметр `status` объекта с заданным `id` в JSON-файле.

	:param file_name: Имя файла JSON, где хранятся данные.
	:param id: ID объекта, у которого нужно изменить статус.
	:param param_key: Параметр объекта которого нужно изменить.
	:param new_param_value: Новое значение для параметра `status`.
	"""
	file_path = FILES_PATH + file_name + '.json'
	try:
		# Открываем и загружаем данные из JSON-файла
		with open(file_path, 'r') as file:
			data = json.load(file)


		for obj in data:
			if obj.get(param_key) == param_value:
				del obj

		# else:
		# 	print(f"Объект с Parametr key {id} не найден.")
		# 	return

		# Сохраняем изменения обратно в файл
		with open(file_path, 'w') as file:
			json.dump(data, file, indent=4)

		print(f"Удалены объекты с параметром {param_key} равных на {param_value}.")

	except FileNotFoundError:
		print(f"Файл {file_name} не найден.")
	except json.JSONDecodeError:
		print(f"Ошибка чтения JSON из файла {file_name}.")
	except Exception as e:
		print(f"Произошла ошибка: {e}")

# save_data_to_file(data={
#     'id': 2,
#     'username': "alex",
#     'first_name': "Alex",
#     'last_name': "Johnson",
#     'email': "alex@gmail.com",
#     'password': "securepassword123",
# }, path='users')

# print(load_data_from_file(file_name='users', param_key='id',))
