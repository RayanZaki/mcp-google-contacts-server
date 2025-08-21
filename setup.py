from setuptools import setup

setup(
    name="mcp-google-contacts-server",
    version="0.1.0",  # This will be replaced by the workflow based on the tag
    description="MCP server for Google Contacts integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rayan Zaki",
    author_email="rayan.hassici@ensia.edu.dz",
    url="https://github.com/rayanzaki/mcp-google-contacts-server",
    package_dir={"": "src"},
    py_modules=["config", "formatters", "google_contacts_service", "main", "tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "mcp-google-contacts=main:main",
        ],
    },
)
