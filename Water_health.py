import pandas as pd


def evaluate_water_quality(pH, Iron, Nitrate, Chloride, Lead, Zinc, Turbidity, Fluoride, Copper, Sulfate, Chlorine, Manganese,
                           Total_Dissolved_Solids):
    healthy_checks = [
        6.5 <= pH <= 9.0,
        Iron < 0.3,
        Nitrate < 10,
        Chloride < 250,
        Lead < 0.015,
        Zinc < 5,
        Turbidity < 5,
        0.7 <= Fluoride <= 1.5,
        Copper < 1.3,
        Sulfate < 250,
        Chlorine < 4.0,
        Manganese < 0.05,
        Total_Dissolved_Solids < 500,
    ]

    score = sum(healthy_checks)
    percentage = (score / len(healthy_checks)) * 100
    is_good = 0 if score == len(healthy_checks) else 1

    return is_good, percentage


def manual_input():
    features = [
        'pH', 'Iron', 'Nitrate', 'Chloride', 'Lead', 'Zinc', 'Turbidity',
        'Fluoride', 'Copper', 'Sulfate', 'Chlorine', 'Manganese', 'Total Dissolved Solids'
    ]
    inputs = []
    print("\nEnter water quality values:")
    for f in features:
        val = float(input(f"{f}: "))
        inputs.append(val)

    result, percent = evaluate_water_quality(*inputs)
    print(f"\nWater Health Score: {percent:.1f}%")
    if result == 0:
        print(" Water quality is habitable for aquatic life.")
    else:
        print(" Water quality is NOT habitable for aquatic life.")


def random_predict_from_file():
    try:
        test_df = pd.read_csv('C:/Users/Acer/Documents/Neural_Ocean/Notebooks_PyFiles/test_data/test_df')
        data = test_df.drop(['Target', 'Color', 'Odor'], axis=1)
        sample = data.sample(n=1)
        print("\nRandom Sample Data:\n", sample)

        result, percent = evaluate_water_quality(*sample.values[0])
        print(f"\nWater Health Score: {percent:.1f}%")
        if result == 0:
            print(" Water quality is habitable for aquatic life.")
        else:
            print(" Water quality is NOT habitable for aquatic life.")
    except FileNotFoundError:
        print("\n Error: Dataset file not found. Please check the file path.")


def main():
    print("==== Water Quality Assessment ====")
    print("1. Manual input")
    print("2. Random input from dataset")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        manual_input()
    elif choice == '2':
        random_predict_from_file()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
