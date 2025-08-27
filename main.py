# main.py

from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

def run_etl():
    # Paso 1: Extraer los datos
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()
    
    if df is not None:
        # Paso 2: Transformar los datos
        transformer = Transformer(df)
        cleaned_df = transformer.clean()
        
        # Paso 3: Cargar los datos limpios
        loader = Loader(cleaned_df)
        loader.to_csv(Config.OUTPUT_PATH)
    else:
        print("No se pudieron extraer los datos. El proceso ETL no se completó.")

if __name__ == "__main__":
    run_etl()

