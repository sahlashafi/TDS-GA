import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest


st.title("Find the Largest Number")
st.write("Enter three numbers below:")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    largest = find_largest(num1, num2, num3)
    st.write("The largest number is:", largest)


