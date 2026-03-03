# Imports
import argparse
import csv
from datetime import date, datetime, timedelta
import os
from functions import advance_time, get_date, reset_date, show_bought_table, show_sold_table, show_inventory_table, sell_product, buy_product,  remove_expired_products, show_expired_table,calculate_revenue, calculate_profit, calculate_cogs, report_financials, calculate_expired_cost, plot_revenue_per_day
import matplotlib.pyplot as plt


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--advance-time", type=int, 
                    help="Verzet de datum met X dagen")
    parser.add_argument("--reset-date", action="store_true",
                    help="Reset de SuperPy-datum naar vandaag")
    parser.add_argument("--show-bought", action="store_true",
                    help="Toon alle ingekochte producten in tabelvorm")
    parser.add_argument("--buy", nargs=3, metavar=("PRODUCT", "PRICE", "EXPIRATION"),
                    help="Koop een product met prijs en houdbaarheidsdatum (DD-MM-YYYY)")
    parser.add_argument("--show-sold", action="store_true",
                    help="Toon alle verkochte producten in tabelvorm")
    parser.add_argument("--inventory", action="store_true",
                    help="Toon de huidige voorraad inclusief expiratie-status")
    parser.add_argument("--sell", nargs=2, metavar=("PRODUCT", "PRICE"),
                    help="Verkoop een product voor een bepaalde prijs")
    parser.add_argument("--clean-expired", action="store_true",
                    help="Verwijder verlopen producten uit de voorraad en schrijf ze weg naar expired.csv")
    parser.add_argument("--show-expired", action="store_true",
                    help="Toon alle verlopen producten in tabelvorm")
    parser.add_argument("--report-profit", action="store_true",
                    help="Toon totale winst en omzet")
    parser.add_argument("--report-profit-net", action="store_true",
                    help="Toon winst inclusief verspilling")
    parser.add_argument("--report", choices=["day", "week", "month", "total"],
                    help="Toon financieel rapport voor dag/week/maand/totaal")
    parser.add_argument("--plot-revenue", action="store_true",
                    help="Toon een grafiek van omzet per dag")




    args = parser.parse_args()

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

    # Standaard gedrag: toon huidige datum 
    print("De huidige SuperPy-datum:", get_date())

    if args.plot_revenue:
        plot_revenue_per_day()
        return


if __name__ == "__main__":
    main()
