from auth import *
from rooms import *
# registration('Shavkat', "Kurbanov", "helloworld", 'alex12883@gmail.com', 'import123')
from data import load_data_from_file, update_data
# login_user('shavkat', 'fasfsdfasfdsf123')
# logout()
# print(is_logged_in())
# add_room("presidential_room", 5)

update_data(file_name='users', id=1, param_key='first_name', new_param_value="Shava")


# print(load_data_from_file('rooms', param_key='type', param_value='standard_double_room', ))

# You can choose from these: standard_single_room, standard_double_room, deluxe_single_room, deluxe_double_room, presidential_room