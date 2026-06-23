import pandas as pd
import matplotlib.pyplot as plt


def load_weather_data(filename):
    return pd.read_csv(filename)


def print_summary(df):
    print(df.describe())

    mean_temp = df["high_C"].mean()
    print(f"\nMean High Temperature: {mean_temp:.2f} C")


def add_celsius(df):
    df["high_C"] = (df["high"] - 32) * 5 / 9
    df["low_C"] = (df["low"] - 32) * 5 / 9
    return df


def clean_temperature_range(df, t_low_cut, t_high_cut):
    return df[(df["low_C"] >= t_low_cut) &
              (df["high_C"] <= t_high_cut)]


def plot_temperatures(df):
    plt.plot(df["day"], df["high_C"], label="High Temp")
    plt.plot(df["day"], df["low_C"], label="Low Temp")

    plt.xlabel("Day")
    plt.ylabel("Temperature (C)")
    plt.title("Daily Temperatures")
    plt.legend()
    plt.show()


def main():

    filename = "../data/weather_june.csv"

    dataframe = load_weather_data(filename)

    dataframe = add_celsius(dataframe)

    T_low_cut = 19.0
    T_high_cut = 31.0
    dataframe = clean_temperature_range(dataframe, T_low_cut, T_high_cut)

    print_summary(dataframe)

    plot_temperatures(dataframe)


main()