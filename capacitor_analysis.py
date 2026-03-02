def series_capacitance(capacitors):
    reciprocal = sum(1/c for c in capacitors)
    return 1 / reciprocal

def parallel_capacitance(capacitors):
    return sum(capacitors)

def voltage_distribution(total_voltage, capacitors):
    total_cap = series_capacitance(capacitors)
    charges = total_cap * total_voltage
    voltages = [charges / c for c in capacitors]
    return voltages

def main():
    print("=== Capacitor Circuit Analyzer ===")

    mode = input("Series or Parallel? (s/p): ").lower()
    caps = input("Enter capacitance values (uF) separated by space: ")
    capacitors = [float(c) for c in caps.split()]

    if mode == 's':
        eq = series_capacitance(capacitors)
        print(f"\nEquivalent Capacitance: {eq:.2f} uF")

        voltage = float(input("Enter total voltage: "))
        voltages = voltage_distribution(voltage, capacitors)

        print("\nVoltage across each capacitor:")
        for i, v in enumerate(voltages):
            print(f"C{i+1}: {v:.2f} V")

    else:
        eq = parallel_capacitance(capacitors)
        print(f"\nEquivalent Capacitance: {eq:.2f} uF")

if __name__ == "__main__":
    main()