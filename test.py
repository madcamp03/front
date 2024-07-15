# import os
# from openai import OpenAI
# import streamlit as st

# api_key = os.getenv("API_KEY")
# client = OpenAI(api_key=api_key)


# def show_test():
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-0125",
#         response_format={"type": "json_object"},
#         messages=[
#             {"role": "system",
#                 "content": "You are a helpful assistant designed to output JSON."},
#             {"role": "user", "content": "Who won the world series in 2020?"}
#         ]
#     )
#     st.write(response.choices[0].message.content)
