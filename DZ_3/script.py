import re
import argparse
import toml

class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse_line(self, line):
        # Удаляем однострочные комментарии
        line = re.sub(r'NB\..*', '', line).strip()
        
        # Пропускаем пустые строки и строки с комментариями
        if not line or line.startswith('<#') or line.endswith('#>'):
            return None

        # Упрощенное регулярное выражение для обработки установки константы
        match = re.match(r'set\s+([a-z_]+)\s*=\s*(.*?);', line)
        if match:
            name, value = match.groups()
            evaluated_value = self.evaluate_value(value)
            self.constants[name] = evaluated_value
            return {name: evaluated_value}
        
        return None

    def evaluate_value(self, value):
        # Обработка числовых значений
        if value.isdigit():
            return int(value)
        
        # Обработка строковых значений
        if value.startswith('"') and value.endswith('"'):
            return value.strip('"')
        
        return value  # Если значение не опознано, возвращаем как есть

    def parse(self, text):
        result = {}
        
        # Удаляем многострочные комментарии
        text = re.sub(r'<#.*?#>', '', text, flags=re.DOTALL)
        lines = text.splitlines()
        
        for line in lines:
            line = line.strip()
            parsed_line = self.parse_line(line)
            if parsed_line:
                result.update(parsed_line)
                
        return result

def main():
    parser = argparse.ArgumentParser(description="Configuration language parser to TOML.")
    parser.add_argument('input', help="Input configuration file")
    parser.add_argument('output', help="Output TOML file path")
    args = parser.parse_args()
    
    # Чтение текста из входного файла с явным указанием кодировки
    with open(args.input, 'r', encoding='utf-8') as input_file:
        input_text = input_file.read()
    
    config_parser = ConfigParser()
    parsed_data = config_parser.parse(input_text)
    
    # Проверка, что данные корректно спарсены
    if not parsed_data:
        print("No data to write to TOML file. Parsed data is empty.")
    else:
        # Запись результата в выходной файл в формате TOML
        with open(args.output, 'w', encoding='utf-8') as output_file:
            toml.dump(parsed_data, output_file)
        print(f"Data successfully written to {args.output}")


if __name__ == "__main__":
    main()
