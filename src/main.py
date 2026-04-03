
import argparse
from .solver import build_completed_demo, reconstruct_final_state
from .visualize import ascii_frame, edge_summary

def main():
    parser = argparse.ArgumentParser(description="Art installation demo toolkit")
    parser.add_argument("--input", default="sample_input.csv")
    parser.add_argument("--output", default="completed_output.csv")
    parser.add_argument("--show", action="store_true", help="Show final parsed frame from input")
    args = parser.parse_args()

    if args.show:
        state = reconstruct_final_state(args.input)
        print("Final frame from input:")
        print(ascii_frame(state))
        print("\nGlowing edges:")
        print(edge_summary(state) or "(none)")
    else:
        build_completed_demo(args.output)
        print(f"Wrote completed demo to {args.output}")

if __name__ == "__main__":
    main()
