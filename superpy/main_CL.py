import argparse
from functions_CL import (
    advance_time, get_date, reset_date,
    show_bought_table, show_sold_table, show_inventory_table,
    sell_product, buy_product, remove_expired_products,
    show_expired_table, calculate_revenue, calculate_profit,
    calculate_cogs, calculate_expired_cost, report_financials,
    plot_revenue_per_day
)


def main():
    parser = argparse.ArgumentParser(description="SuperPy – voorraad & financieel systeem")

    # Tijdbeheer
    parser.add_argument("--advance-time", type=int, help="Verzet de datum met X dagen")
    parser.add_argument("--reset-date", action="store_true", help="Reset de datum naar vandaag")

    # Inkoop & verkoop
    parser.add_argument("--buy", nargs=3, metavar=("PRODUCT", "PRICE", "EXPIRATION"),
                        help="Koop een product (DD-MM-YYYY)")
    parser.add_argument("--sell", nargs=2, metavar=("PRODUCT", "PRICE"),
                        help="Verkoop een product")

    # Tabellen
    parser.add_argument("--show-bought", action="true", help="Toon ingekochte producten")
    parser.add_argument("--show-sold", action="true", help="Toon verkochte producten")
    parser.add_argument("--inventory", action="true", help="Toon voorraad")
    parser.add_argument("--show-expired", action="true", help="Toon verlopen producten")

    # Verlopen producten verwerken
    parser.add_argument("--clean-expired", action="true",
                        help="Verplaats verlopen producten naar expired.csv")

    # Financieel
    parser.add_argument("--report", choices=["day", "week", "month", "total"],
                        help="Financieel rapport voor periode")
    parser.add_argument("--report-profit", action="true", help="Toon omzet, COGS en winst")
    parser.add_argument("--report-profit-net", action="true",
                        help="Toon winst inclusief verspilling")

    # Grafieken
    parser.add_argument("--plot-revenue", action="true", help="Plot omzet per dag")

    args = parser.parse_args()

    # -----------------------------
    # COMMANDS
    # -----------------------------

    if args.advance_time is not None:
        advance_time(args.advance_time)
        return

    if args.reset_date:
        reset_date()
        return

    if args.show_bought:
        show_bought_table()
        return

    if args.buy:
        product, price, expiration = args.buy
        buy_product(product, float(price), 1, expiration)
        return

    if args.show_sold:
        show_sold_table()
        return

    if args.inventory:
        show_inventory_table()
        return

    if args.sell:
        product, price = args.sell
        sell_product(product, float(price))
        return

    if args.clean_expired:
        remove_expired_products()
        return

    if args.show_expired:
        show_expired_table()
        return

    if args.report:
        report_financials(args.report)
        return

    if args.report_profit:
        revenue = calculate_revenue()
        cogs = calculate_cogs()
        profit = calculate_profit()
        print(f"Revenue: €{revenue:.2f}")
        print(f"COGS: €{cogs:.2f}")
        print(f"Profit: €{profit:.2f}")
        return

    if args.report_profit_net:
        revenue = calculate_revenue()
        cogs = calculate_cogs()
        expired = calculate_expired_cost()
        profit = calculate_profit(include_expired=True)
        print(f"Revenue: €{revenue:.2f}")
        print(f"COGS: €{cogs:.2f}")
        print(f"Expired cost: €{expired:.2f}")
        print(f"Net Profit: €{profit:.2f}")
        return

    if args.plot_revenue:
        plot_revenue_per_day()
        return

    # Default gedrag
    print("De huidige SuperPy-datum:", get_date())


if __name__ == "__main__":
    main()
