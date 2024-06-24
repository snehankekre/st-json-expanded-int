import streamlit as st

with st.sidebar:
    choice = st.radio("Type of `expanded` param", ["int", "bool", "float", "str"], horizontal=True, help="Choose the type of the `expanded` parameter. \n\nSupported types are `int`, `bool`. \n\nOther types will raise an error.")
    if choice == "int":
        expanded = st.slider("Choose the depth to expand to", 0, 10, 0, help="Choose the depth to expand to. \n\nThe default value is 0. \n\nIf the value is greater than the maximum depth of the JSON object, it will raise an error.")
    elif choice == "bool":
        expanded = st.toggle("Expand all levels", False)
    elif choice == "float":
        expanded = st.slider("Choose the depth to expand to", 0.0, 10.0, 0.0)
    else:
        expanded = st.text_input("Enter the depth to expand to", "0")

sample_data = {
    "level_1": {
        "level_2": {
            "level_3a": {
                "item1": "value1",
                "item2": "value2",
            },
            "level_3b": {
                "item3": "value3",
                "level_4": {
                    "item4": "value4",
                    "level_5": {
                        "item5": "value5"
                    }
                }
            }
        },
        "simple_item": "simple_value"
    },
    "top_level_item": "top_level_value"
}

col1, col2 = st.columns([0.9, 1])

col1.json(sample_data, expanded=expanded)

col2.code(
f"""
sample_data = {{
    "level_1": {{
        "level_2": {{
            "level_3a": {{
                "item1": "value1",
                "item2": "value2",
            }},
            "level_3b": {{
                "item3": "value3",
                "level_4": {{
                    "item4": "value4",
                    "level_5": {{
                        "item5": "value5"
                    }}
                }}
            }}
        }},
        "simple_item": "simple_value"
    }},
    "top_level_item": "top_level_value"
}}

st.json(sample_data, expanded={expanded})
"""
)