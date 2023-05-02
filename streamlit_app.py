# streamlit_app.py

import streamlit as st

print(st.secrets)

# st.write("DB username:", st.secrets["username"])
# st.write("DB password:", st.secrets["password"])

# # Initialize connection.
# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
# df = conn.query('SELECT * from mytable;', ttl=600)

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")