
def getPage(name: str) -> str:
    """
    Gets a webpage from the frontend folder, adds CSS. If not found, will return the 404 page.
    
        **name**: name of the file, excluding path and extensions

        Current pages available:
            index
            login
            register
            profile
    """
    page = open(f"app/frontend/{name}.html", "r").read()
    page += "<style>" + open(f"app/frontend/styles/main.css").read() + "</style>"
    return page