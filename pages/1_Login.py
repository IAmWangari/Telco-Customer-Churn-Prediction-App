import streamlit as st

# Function to handle login
def authenticate(username, password):
    return username == "admin" and password == "password"

# Function to display login page
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid username or password")

# Main function
def main():
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        login_page()
    else:
        st.title("Welcome to the App")
        st.write("You are logged in.")
        # Your app content here

if __name__ == "__main__":
    main()
