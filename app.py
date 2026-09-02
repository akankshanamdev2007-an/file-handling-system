import streamlit as st
from pathlib import Path


# Page configuration
st.set_page_config(
    page_title="File Handler",
    page_icon="📁",
    layout="centered"
)


# Title
st.title("📁 File Handling System")
st.write("Create, Read, Update and Delete files easily")


# Sidebar
option = st.sidebar.selectbox(
    "Choose an operation",
    ["🏠 Home", "➕ Create File", "📖 Read File",
     "✏️ Update File", "🗑️ Delete File"]
)


# Home page
if option == "🏠 Home":

    st.header("Welcome to File Handling System 👋")

    st.info("""
    This application allows you to perform basic file operations using Python.

    ✅ Create Files  
    ✅ Read Files  
    ✅ Rename Files  
    ✅ Append Content  
    ✅ Overwrite Content  
    ✅ Delete Files
    """)


# CREATE FILE
elif option == "➕ Create File":

    st.header("➕ Create a File")

    name = st.text_input(
        "Enter file name",
        placeholder="example.txt"
    )

    data = st.text_area(
        "Write content",
        placeholder="Enter your file content here..."
    )

    if st.button("Create File"):

        try:
            if name:

                path = Path(name)

                if not path.exists():

                    with open(path, "w") as fs:
                        fs.write(data)

                    st.success("🎉 File created successfully!")

                else:
                    st.error("❌ File already exists!")

            else:
                st.warning("Please enter a file name.")

        except Exception as err:
            st.error(f"An error occurred: {err}")


# READ FILE
elif option == "📖 Read File":

    st.header("📖 Read a File")

    name = st.text_input(
        "Enter file name",
        placeholder="example.txt"
    )

    if st.button("Read File"):

        try:
            path = Path(name)

            if path.exists():

                with open(path, "r") as fs:
                    content = fs.read()

                st.success("File found successfully!")

                st.subheader("📄 File Content")
                st.code(content)

            else:
                st.error("❌ No such file exists!")

        except Exception as err:
            st.error(f"An error occurred: {err}")


# UPDATE FILE
elif option == "✏️ Update File":

    st.header("✏️ Update a File")

    name = st.text_input(
        "Enter existing file name",
        placeholder="example.txt"
    )

    operation = st.selectbox(
        "Choose update operation",
        [
            "Rename File",
            "Append Content",
            "Overwrite File"
        ]
    )


    # Rename
    if operation == "Rename File":

        newname = st.text_input(
            "Enter new file name",
            placeholder="newfile.txt"
        )

        if st.button("Rename File"):

            try:
                path = Path(name)
                new_path = Path(newname)

                if path.exists():

                    if not new_path.exists():

                        path.rename(new_path)
                        st.success("🎉 File renamed successfully!")

                    else:
                        st.error("❌ A file with this name already exists!")

                else:
                    st.error("❌ Original file does not exist!")

            except Exception as err:
                st.error(f"An error occurred: {err}")


    # Append
    elif operation == "Append Content":

        data = st.text_area(
            "Enter content to append"
        )

        if st.button("Append Content"):

            try:
                path = Path(name)

                if path.exists():

                    with open(path, "a") as fs:
                        fs.write("\n" + data)

                    st.success("🎉 Content appended successfully!")

                else:
                    st.error("❌ No such file exists!")

            except Exception as err:
                st.error(f"An error occurred: {err}")


    # Overwrite
    elif operation == "Overwrite File":

        data = st.text_area(
            "Enter new content"
        )

        if st.button("Overwrite File"):

            try:
                path = Path(name)

                if path.exists():

                    with open(path, "w") as fs:
                        fs.write(data)

                    st.success("🎉 File overwritten successfully!")

                else:
                    st.error("❌ No such file exists!")

            except Exception as err:
                st.error(f"An error occurred: {err}")


# DELETE FILE
elif option == "🗑️ Delete File":

    st.header("🗑️ Delete a File")

    name = st.text_input(
        "Enter file name to delete",
        placeholder="example.txt"
    )

    if st.button("Delete File"):

        try:
            path = Path(name)

            if path.exists():

                path.unlink()

                st.success("🎉 File deleted successfully!")

            else:
                st.error("❌ No such file exists!")

        except Exception as err:
            st.error(f"An error occurred: {err}")


# Footer
st.divider()
st.caption("Built with ❤️ using Python & Streamlit")
