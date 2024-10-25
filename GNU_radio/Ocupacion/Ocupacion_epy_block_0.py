import numpy as np
from gnuradio import gr
import sqlite3
import mysql

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Bloque para almacenar la señal recibida en una base de datos SQLite"""

    def __init__(self, db_file='signals.db', table_name='signal_data'):  
        """Constructor: Define los parámetros de la base de datos"""
        gr.sync_block.__init__(
            self,
            name='SQLite Signal Storage Block',  # nombre del bloque en GRC
            in_sig=[np.complex64],  # tipo de señal de entrada
            out_sig=None  # no se necesita señal de salida
        )
        
        # Almacenar los parámetros de la base de datos
        self.db_file = db_file
        self.table_name = table_name

        # No se conecta aquí a la base de datos, se hará en cada work()

    def work(self, input_items, output_items):
        """Almacena las partes real e imaginaria de la señal recibida en la base de datos"""
        input_signal = input_items[0]

        # Conectar a la base de datos SQLite cada vez que se llame a work()
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Crear la tabla si no existe
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                real_part REAL,
                imag_part REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_query)

        # Preparar una lista de tuplas con los datos a insertar
        data_to_insert = [(float(sample.real), float(sample.imag)) for sample in input_signal]

        # Insertar los datos de la señal en la base de datos usando executemany para mayor eficiencia
        insert_query = f"INSERT INTO {self.table_name} (real_part, imag_part) VALUES (?, ?)"
        cursor.executemany(insert_query, data_to_insert)

        # Confirmar la transacción después de insertar todas las muestras
        conn.commit()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

        # Devolver el número de elementos de entrada procesados (todos)
        return len(input_items[0])


