import json


def generate_list():
    with open("list.json", "r") as file:
        data = json.load(file)

    with open("README.md", "w") as file:
        file.write("# Open Source Python Packages in Hydrology\n")
        file.write(
            "My attempt to list interesting open source python projects that can be used in the field of Hydrology. Suggestions as issues or pull requests are welcome!\n\n"
        )
        file.write(
            'UPDATE: The Pypa package authority has now added ["Hydrology" as a classifier](https://github.com/pypa/warehouse/issues/5728) so we can start [collecting python packages](https://pypi.org/search/?q=&o=&c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Hydrology) used by the hydrological community! If you are maintaining a python package, please add `Topic :: Scientific/Engineering :: Hydrology` to your setup.py so people can find your package.\n\n'
        )
        file.write("Raoul A. Collenteur, Eawag.\n\n")

        categories = {}
        for package_name, package in data.items():
            category = package["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((package_name, package))

        for category, packages in categories.items():
            file.write(f"## {category}\n")
            file.write("| Project Name | Description | PyPI |\n")
            file.write("| ------------ | ----------- | ---- |\n")
            for package_name, package in packages:
                description = package["description"]
                url = package["url"]
                pypi_url = package.get("pypi", "")
                pypi_logo = (
                    f"[![PyPI](https://img.shields.io/badge/PyPI-3776AB?logo=python&logoColor=white)]({pypi_url})"
                    if pypi_url
                    else ""
                )
                file.write(
                    f"| [{package_name}]({url}) | {description} | {pypi_logo} |\n"
                )
            file.write("\n")


if __name__ == "__main__":
    generate_list()