"""
Ejercicio de Programación 1: Compute Sales.
Programa CL para calcular las ventas totales de una compañía.
Recibe dos archivos JSON parametros:
- priceCatalogue.json: lista de productos con sus precios
- salesRecord.json: lista de ventas con los productos vendidos y sus cantidades
"""

import sys
import time
import json

DATE_FORMAT = "%b %d, %Y %H:%M:%S"


def load_json_file(file_path):
    """Cargar el contenido de un archivo JSON y manejar errores de lectura."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f'ERROR al procesar {file_path}: {error}')
        return None


def calculate_sales(catalogue_data, sales_data):
    """Calcular las ventas totales por producto."""
    price_list = {item['title']: item['price'] for item in catalogue_data
                  if 'title' in item and 'price' in item}

    sales_by_product = []
    total_sales = 0.0
    errors = []

    sales_summary = {}
    for record in sales_data:
        product = record.get('Product')
        quantity = record.get('Quantity', 0)

        if product in price_list:
            if product not in sales_summary:
                sales_summary[product] = {
                    'qty': 0,
                    'price': price_list[product]
                    }
            sales_summary[product]['qty'] += quantity
        else:
            errors.append(f'ERROR: [{product}] no está en el catálogo.')

    for prod, info in sales_summary.items():
        subtotal = info['qty'] * info['price']
        sales_by_product.append({
            'name': prod,
            'unit_price': info['price'],
            'total_qty': info['qty'],
            'subtotal': subtotal
        })
        total_sales += subtotal

    return sales_by_product, total_sales, errors


def save_results(sales_by_product, total_sales, times_data):
    """
    Guardar los datos procesados en un archivo:
    producto, precio unitario y ventas totales
    """
    results_file_name = "SalesResults.txt"

    start_str, end_str, exec_time_str = calculate_format_time(times_data)

    results = []
    results.append("=" * 60)
    results.append(f'{"Reporte de Ventas por Producto":^60}')
    results.append("=" * 60)
    results.append(
            f'{"Producto":<25} | {"P. Unit.":>10} | '
            f'{"Cant.":>6} | {"Total":>10}'
        )
    results.append("-" * 60)

    for sale in sales_by_product:
        line = (f'{sale["name"][:24]:<25} | ${sale["unit_price"]:>9.2f} | '
                f'{sale["total_qty"]:>6} | ${sale["subtotal"]:>9.2f}')
        results.append(line)

    results.append("-" * 60)
    results.append(f'{"Ventas Totales:":>47} ${total_sales:,.2f}')
    results.append("=" * 60)
    results.append(f'{"Inicio de procesamiento:":>15} {start_str}')
    results.append(f'{"Tiempo de ejecución:":>15} {exec_time_str}')
    results.append(f'{"Fin de procesamiento:":>15} {end_str}')
    results.append("=" * 60)

    final_result = "\n".join(results)
    print(final_result)

    try:
        with open(results_file_name, 'w', encoding='utf-8') as f_out:
            f_out.write(final_result)
    except IOError as file_error:
        print(f'ERROR al guardar resultados {results_file_name}: {file_error}')


def calculate_format_time(times_data):
    """Calcular el tiempo de ejecución.
    Convertir tiempo en un formato legible HH:MM:SS.mmmm."""
    start_time, end_time = times_data
    start_str = time.strftime(DATE_FORMAT, time.localtime(start_time))
    end_str = time.strftime(DATE_FORMAT, time.localtime(end_time))

    time_passed = end_time - start_time

    hours = int(time_passed // 3600)
    minutes = int((time_passed % 3600) // 60)
    seconds = time_passed % 60

    duration_str = f'{hours:02}:{minutes:02}:{seconds:07.4f}'
    return start_str, end_str, duration_str


def main():
    """Función principal para ejecutar el cálculo de ventas totales."""
    if len(sys.argv) != 3:
        print('ERROR: Debe proporcionar el nombre del archivo como parámetro.')
        return
    start_time = time.time()
    catalogue_data = load_json_file(sys.argv[1])
    sales_data = load_json_file(sys.argv[2])

    sales_by_product, total_sales, error_list = (
        calculate_sales(catalogue_data, sales_data)
    )
    for error in error_list:
        print(error)

    end_time = time.time()
    times_data = (start_time, end_time)
    save_results(sales_by_product, total_sales, times_data)


if __name__ == "__main__":
    main()
