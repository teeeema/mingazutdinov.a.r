import subprocess

def get_dependencies(package_name):
    try:
        result = subprocess.run(['apt-cache', 'depends', package_name],
                                capture_output=True, text=True, check=True)
        dependencies = result.stdout.splitlines()
        print(f"Dependencies for {package_name}: {dependencies}")
        return [line.split(': ')[-1].strip() for line in dependencies if line.startswith('  Зависит:')]
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving dependencies for {package_name}: {e}")
        return []

def visualize_dependencies(package_name, output_file, max_depth, visualization_tool_path, repo_url):
    dependencies_graph = 'digraph G {\n'
    dependencies_graph += f'  "{package_name}"\n'
    
    def add_dependencies(package, depth, graph):
        if depth < max_depth:
            dependencies = get_dependencies(package)
            for dep in dependencies:
                # Добавляем зависимость в граф
                graph += f'  "{package}" -> "{dep.strip()}"\n'  # Убираем лишние пробелы
                graph = add_dependencies(dep.strip(), depth + 1, graph)  # Рекурсивно добавляем зависимости
        return graph

    dependencies_graph = add_dependencies(package_name, 0, dependencies_graph)
    
    dependencies_graph += '}\n'

    with open(output_file, 'w') as f:
        f.write(dependencies_graph)

    print(dependencies_graph)