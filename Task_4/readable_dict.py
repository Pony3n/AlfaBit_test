from traffic_info import tariff_info as tariff


def print_tariff_info(node, indent=0):
    if isinstance(node, dict):
        for key, value in node.items():
            print('    ' * indent + key)
            if isinstance(value, dict) and 'children' in value:
                print_tariff_info(value['children'], indent + 1)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        print_tariff_info(item, indent + 1)
                    elif isinstance(item, str):
                        print('    ' * (indent + 1) + item)
            elif isinstance(value, str):
                print('    ' * (indent + 1) + value)
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                print_tariff_info(item, indent + 1)
            elif isinstance(item, str):
                print('    ' * (indent + 1) + item)


print('root')
print_tariff_info(tariff['root']['children'], indent=0)
