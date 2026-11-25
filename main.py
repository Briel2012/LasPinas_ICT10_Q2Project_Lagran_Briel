from pyscript import document

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "F": ("Fluorine", 9, 18.998),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90)
}

club_members = {
    "kenzo cutamora", "zach natividad", "keon cutamora",
    "arturo santos", "jack sabitsana", "kaizen sy", "briel lagran"
}


def search_element(e):
    document.getElementById("element_result").innerHTML = ""
    symbol = document.getElementById("element").value.strip().capitalize()
    element, atomic_number, atomic_mass = non_metals.get(
        symbol,
        ("Element not found", "-", "-")
    )
    document.getElementById("element_result").innerHTML = f"""
    <b>Symbol:</b> {symbol}<br>
    <b>Element:</b> {element}<br>
    <b>Atomic Number:</b> {atomic_number}<br>
    <b>Atomic Mass:</b> {atomic_mass}
    """


def candidate_checker(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate = f"{first_name} {last_name}".strip()
    result = document.getElementById("club_result")

    if not first_name or not last_name:
        result.textContent = "Please enter your first and last name."
        return

    if candidate.lower() in club_members:
        result.textContent = f"Congratulations, {candidate}! You are part of the basketball varsity."
    else:
        result.textContent = f"Sorry, {candidate}. Your name is not on the list."