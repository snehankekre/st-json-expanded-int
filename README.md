# Integer support for `st.json`'s `expanded` parameter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://st-json-expanded-int.streamlit.app)

Streamlit's [`st.json`](https://docs.streamlit.io/develop/api-reference/data/st.json) command now supports integer values for the `expanded` parameter, in addition to the existing `bool` support. This allows users to specify the depth to which the JSON should be expanded, collapsing deeper levels.


### `st.json`

Display object or string as a pretty-printed JSON string.

| Parameter | Description |
| --- | --- |
| `body` *(object or str)* | The object to print as JSON. All referenced objects should be serializable to JSON as well. If object is a string, we assume it contains serialized JSON. |
| `expanded` *(bool or int)* | Optionally controls the initial expansion state of the JSON. If boolean, `True` expands all levels, `False` collapses all levels. If int, specifies the depth to which the JSON should be expanded, collapsing deeper levels. Defaults to `True`. |


See the [PoC implementation](https://github.com/streamlit/streamlit/compare/develop...snehan/prototype/json-expanded-depth)