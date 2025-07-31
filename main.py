from core.controller import Controller
import json

def main():
    target = input("Enter domain or IP to scan: ").strip()
    controller = Controller(target)
    results = controller.run_all()
    print(json.dumps(results, indent=4))
    output_file = f"output/results_{target.replace('.', '_')}.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
