# -----------------------------
# DATUMFUNCTIES (OPGESCHOOND)
# -----------------------------

import os
from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"
DATE_PATH = os.path.join("data", "date_today.txt")


def get_date():
    """Lees de huidige SuperPy-datum uit het bestand."""
    if not os.path.exists(DATE_PATH):
        # Als het bestand ontbreekt → automatisch vandaag instellen
        today = datetime.today().strftime(DATE_FORMAT)
        set_date(today)
        return today

    with open(DATE_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()


def set_date(new_date):
    """Schrijf een nieuwe datum naar het datum-bestand."""
    with open(DATE_PATH, "w", encoding="utf-8") as f:
        f.write(new_date)


def advance_time(days):
    """Verzet de SuperPy-datum met X dagen."""
    current_date = parse_date(get_date())
    new_date = current_date + timedelta(days=days)
    formatted = new_date.strftime(DATE_FORMAT)

    set_date(formatted)
    print(f"Datum aangepast naar: {formatted}")


def reset_date():
    """Zet de SuperPy-datum terug naar vandaag."""
    today = datetime.today().strftime(DATE_FORMAT)
    set_date(today)
    print(f"Datum gereset naar vandaag: {today}")


def parse_date(date_str):
    """Zet een dd-mm-YYYY string om naar een datetime object."""
    return datetime.strptime(date_str, DATE_FORMAT)


def is_same_day(d1, d2):
    """Controleer of twee datums op dezelfde dag vallen."""
    return d1.date() == d2.date()


def is_same_week(d1, d2):
    """Controleer of twee datums in dezelfde ISO-week vallen."""
    return d1.isocalendar()[:2] == d2.isocalendar()[:2]


def is_same_month(d1, d2):
    """Controleer of twee datums in dezelfde maand vallen."""
    return d1.year == d2.year and d1.month == d2.month


# -----------------------------
# CSV FUNCTIES (OPGESCHOOND)
# -----------------------------

import os
import csv
from datetime import datetime
from rich.table import Table
from rich.console import Console


# -----------------------------
# HULPFUNCTIES
# -----------------------------

def read_csv(path):
    """Algemene CSV-reader voor alle bestanden."""
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def write_csv(path, rows):
    """Algemene CSV-writer voor volledige bestanden."""
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def append_csv_row(path, row, fieldnames):
    """Algemene functie om één rij toe te voegen aan een CSV-bestand."""
    file_exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        if not file_exists or os.path.getsize(path) == 0:
            writer.writeheader()
        writer.writerow(row)


# -----------------------------
# BOUGHT (INKOOP)
# -----------------------------

def read_bought_csv():
    return read_csv(BOUGHT_PATH)


def show_bought_table():
    rows = read_bought_csv()
    if not rows:
        print("Geen ingekochte producten gevonden.")
        return

    console = Console()
    table = Table(title="Ingekochte producten", show_lines=True)

    for h in rows[0].keys():
        table.add_column(h)

    for row in rows:
        table.add_row(*[row[h] for h in row.keys()])

    console.print(table)


def buy_product(product_name, buy_price, amount, expiration_date):
    rows = read_bought_csv()

    new_id = int(rows[-1]["id"]) + 1 if rows else 1
    buy_date = get_date()

    append_csv_row(
        BOUGHT_PATH,
        {
            "id": new_id,
            "product_name": product_name,
            "buy_date": buy_date,
            "buy_price": buy_price,
            "expiration_date": expiration_date
        },
        ["id", "product_name", "buy_date", "buy_price", "expiration_date"]
    )

    print(f"Gekocht: {product_name} voor €{buy_price}, exp: {expiration_date}")


# -----------------------------
# SOLD (VERKOOP)
# -----------------------------

def read_sold_csv():
    return read_csv(SOLD_PATH)


def show_sold_table():
    rows = read_sold_csv()
    if not rows:
        print("Geen verkochte producten gevonden.")
        return

    console = Console()
    table = Table(title="Verkochte producten", show_lines=True)

    for h in rows[0].keys():
        table.add_column(h)

    for row in rows:
        table.add_row(*[row[h] for h in row.keys()])

    console.print(table)


def append_sold_row(row):
    append_csv_row(SOLD_PATH, row, row.keys())


def sell_product(product_name, sell_price):
    bought_items = read_bought_csv()
    today = datetime.strptime(get_date(), "%d-%m-%Y")

    for item in bought_items:
        if item["product_name"] != product_name:
            continue

        exp = item.get("expiration_date")
        if exp:
            exp_date = datetime.strptime(exp, "%d-%m-%Y")
            if exp_date < today:
                continue

        sold_rows = read_sold_csv()
        new_id = int(sold_rows[-1]["id"]) + 1 if sold_rows else 1

        append_sold_row({
            "id": new_id,
            "bought_id": item["id"],
            "product_name": product_name,
            "sell_date": get_date(),
            "sell_price": str(sell_price)
        })

        print(f"Product verkocht: {product_name} voor €{sell_price}")
        return

    print(f"Geen verkoopbaar item gevonden voor: {product_name}")


# -----------------------------
# EXPIRED (VERLOPEN)
# -----------------------------

def read_expired_csv():
    return read_csv(EXP_PATH)


def append_expired_row(row):
    append_csv_row(
        EXP_PATH,
        row,
        ["id", "bought_id", "product_name", "buy_date", "buy_price",
         "expiration_date", "expired_on"]
    )


def remove_expired_products():
    bought_items = read_bought_csv()
    expired_rows = read_expired_csv()
    today = datetime.strptime(get_date(), "%d-%m-%Y")

    already_expired_ids = {row["bought_id"] for row in expired_rows}
    expired_items = []

    for item in bought_items:
        exp = item.get("expiration_date")
        if not exp:
            continue

        exp_date = datetime.strptime(exp, "%d-%m-%Y")
        if exp_date < today and item["id"] not in already_expired_ids:
            expired_items.append(item)

    next_id = int(expired_rows[-1]["id"]) + 1 if expired_rows else 1

    for item in expired_items:
        append_expired_row({
            "id": next_id,
            "bought_id": item["id"],
            "product_name": item["product_name"],
            "buy_date": item["buy_date"],
            "buy_price": item["buy_price"],
            "expiration_date": item["expiration_date"],
            "expired_on": get_date()
        })
        next_id += 1

    print(f"{len(expired_items)} producten geregistreerd als verlopen.")


def show_expired_table():
    rows = read_expired_csv()
    if not rows:
        print("Geen verlopen producten gevonden.")
        return

    console = Console()
    table = Table(title="Verlopen producten", show_lines=True)

    for h in rows[0].keys():
        table.add_column(h)

    total_cost = 0.0

    for row in rows:
        price = float(row["buy_price"].replace(",", "."))
        total_cost += price
        table.add_row(*[row[h] for h in row.keys()])

    console.print(table)
    console.print(f"[bold]Totaal verlopen producten:[/bold] {len(rows)}")
    console.print(f"[bold red]Totale verspilde inkoopkosten:[/bold red] €{total_cost:.2f}")

# -----------------------------
# BEREKENINGEN (OPGESCHOOND)
# -----------------------------

from datetime import datetime
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table


# -----------------------------
# VOORRAAD
# -----------------------------

def get_inventory():
    bought = read_bought_csv()
    sold_ids = {row["bought_id"] for row in read_sold_csv()}
    expired_ids = {row["bought_id"] for row in read_expired_csv()}

    return [
        item for item in bought
        if item["id"] not in sold_ids and item["id"] not in expired_ids
    ]


def show_inventory_table():
    rows = get_inventory()
    if not rows:
        print("Geen producten op voorraad.")
        return

    console = Console()
    table = Table(title="Voorraad", show_lines=True)

    table.add_column("ID", justify="right")
    table.add_column("Product")
    table.add_column("Gekocht op")
    table.add_column("Inkoopprijs", justify="right")
    table.add_column("Houdbaar tot")
    table.add_column("Status")

    today = parse_date(get_date())
    ALMOST_EXPIRED_DAYS = 2

    for row in rows:
        exp_date = parse_date(row["expiration_date"])
        days_left = (exp_date - today).days

        if days_left < 0:
            status = "[bold red]Verlopen[/bold red]"
        elif days_left <= ALMOST_EXPIRED_DAYS:
            status = f"[yellow]Bijna verlopen ({days_left} dagen)[/yellow]"
        else:
            status = f"[green]OK ({days_left} dagen)[/green]"

        table.add_row(
            row["id"],
            row["product_name"],
            row["buy_date"],
            row["buy_price"],
            row["expiration_date"],
            status
        )

    console.print(table)
    console.print(f"[bold]Totaal op voorraad:[/bold] {len(rows)} producten.")


# -----------------------------
# OMZET PER DAG (GRAFIEK)
# -----------------------------

def get_revenue_per_day():
    revenue = {}
    for row in read_sold_csv():
        date = row["sell_date"]
        price = float(row["sell_price"].replace(",", "."))
        revenue[date] = revenue.get(date, 0) + price
    return revenue


def plot_revenue_per_day():
    data = get_revenue_per_day()
    if not data:
        print("Geen verkoopdata beschikbaar om te plotten.")
        return

    dates = sorted(data.keys(), key=lambda d: parse_date(d))
    values = [data[d] for d in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker="o", color="blue")
    plt.title("Omzet per dag")
    plt.xlabel("Datum")
    plt.ylabel("Omzet (€)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -----------------------------
# FINANCIËLE BEREKENINGEN
# -----------------------------

def calculate_revenue():
    total = 0.0
    for item in read_sold_csv():
        total += float(item["sell_price"].replace(",", ".").replace("€", ""))
    return total


def calculate_cogs():
    sold = read_sold_csv()
    bought_lookup = {
        row["id"]: float(row["buy_price"].replace(",", "."))
        for row in read_bought_csv()
    }

    return sum(
        bought_lookup.get(item["bought_id"], 0.0)
        for item in sold
    )


def calculate_expired_cost():
    return sum(
        float(row["buy_price"].replace(",", "."))
        for row in read_expired_csv()
    )


def calculate_profit(include_expired=False):
    revenue = calculate_revenue()
    cogs = calculate_cogs()
    profit = revenue - cogs

    if include_expired:
        profit -= calculate_expired_cost()

    return profit


# -----------------------------
# FINANCIEEL OVERZICHT (PERIODE)
# -----------------------------

def calculate_financials(period="total"):
    today = parse_date(get_date())

    sold = read_sold_csv()
    expired = read_expired_csv()
    bought_lookup = {
        row["id"]: float(row["buy_price"].replace(",", "."))
        for row in read_bought_csv()
    }

    revenue = 0.0
    cogs = 0.0
    expired_cost = 0.0

    # Verkoopdata
    for item in sold:
        d = parse_date(item["sell_date"])
        if period == "day" and not is_same_day(d, today):
            continue
        if period == "week" and not is_same_week(d, today):
            continue
        if period == "month" and not is_same_month(d, today):
            continue

        revenue += float(item["sell_price"].replace(",", "."))
        cogs += bought_lookup[item["bought_id"]]

    # Verspilling
    for item in expired:
        d = parse_date(item["expired_on"])
        if period == "day" and not is_same_day(d, today):
            continue
        if period == "week" and not is_same_week(d, today):
            continue
        if period == "month" and not is_same_month(d, today):
            continue

        expired_cost += float(item["buy_price"].replace(",", "."))

    profit = revenue - cogs
    net_profit = profit - expired_cost

    return {
        "revenue": revenue,
        "cogs": cogs,
        "profit": profit,
        "expired_cost": expired_cost,
        "net_profit": net_profit
    }


# -----------------------------
# FINANCIËLE GRAFIEK
# -----------------------------

def plot_financials(period="total"):
    data = calculate_financials(period)

    labels = ["Omzet", "COGS", "Brutowinst", "Verspilling", "Netto winst"]
    values = [
        data["revenue"],
        data["cogs"],
        data["profit"],
        data["expired_cost"],
        data["net_profit"]
    ]

    colors = ["green", "orange", "blue", "red", "purple"]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=colors)
    plt.title(f"Financieel overzicht ({period})")
    plt.ylabel("Bedrag (€)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


# -----------------------------
# FINANCIËLE TABEL + GRAFIEK
# -----------------------------

def report_financials(period="total"):
    data = calculate_financials(period)

    console = Console()
    table = Table(title=f"Financieel rapport ({period})", show_lines=True)

    table.add_column("Categorie")
    table.add_column("Bedrag (€)", justify="right")

    table.add_row("Omzet", f"{data['revenue']:.2f}")
    table.add_row("COGS", f"{data['cogs']:.2f}")
    table.add_row("Brutowinst", f"{data['profit']:.2f}")
    table.add_row("Verspilling", f"[red]{data['expired_cost']:.2f}[/red]")

    net = data["net_profit"]
    color = "green" if net >= 0 else "red"
    table.add_row("Netto winst", f"[{color}]{net:.2f}[/{color}]")

    console.print(table)

    plot_financials(period)
