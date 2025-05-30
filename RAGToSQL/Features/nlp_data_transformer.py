
import pandas as pd

def apply_transformation(df: pd.DataFrame, instruction: str) -> pd.DataFrame:
    """
    Apply a limited set of transformations based on natural language instruction.
    (For demo purposes – extend with NLP parsing or fine-tuned models for production)
    """
    try:
        instruction = instruction.lower()

        if "remove nulls" in instruction or "drop nulls" in instruction:
            df = df.dropna()

        if "lowercase" in instruction:
            for col in df.select_dtypes(include='object').columns:
                df[col] = df[col].str.lower()

        if "uppercase" in instruction:
            for col in df.select_dtypes(include='object').columns:
                df[col] = df[col].str.upper()

        if "format date" in instruction:
            for col in df.columns:
                if "date" in col.lower():
                    try:
                        df[col] = pd.to_datetime(df[col]).dt.strftime("%d-%m-%Y")
                    except:
                        pass

        return df

    except Exception as e:
        raise RuntimeError(f"Error processing transformation: {e}")
