import os
from pyswip import Prolog

def run_tests():
    prolog = Prolog()
    kb_path = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base', 'specialization.pl')
    kb_path = kb_path.replace('\\', '/')
    prolog.consult(kb_path)

    test_profiles = [
        {
            "name": "Quantum Specialist Profile",
            "scores": {"math_strength": 5, "linear_algebra": 5, "quantum_physics": 5, "algorithms_interest": 4},
            "expected": "quantum_computing"
        },
        {
            "name": "Bioinformatics Profile",
            "scores": {"biology_interest": 5, "algorithms_interest": 5, "data_analysis": 4, "statistics": 4},
            "expected": "bioinformatics"
        },
        {
            "name": "Cybersecurity Expert Profile",
            "scores": {"security_interest": 5, "ethical_hacking": 5, "operating_systems": 4, "networking_skill": 4},
            "expected": "cyber_defense"
        },
        {
            "name": "Generalist Architect Profile",
            "scores": {k: 5 for k in ["math_strength", "programming_skill", "linear_algebra", "physics_robotics", "linguistics", "distributed_systems", "security_interest", "cryptography", "statistics", "embedded_systems", "graphics_interest", "algorithms_interest", "biology_interest", "quantum_physics", "ux_design"]},
            "expected": "generalist_architect"
        },
        {
            "name": "Negative Case (Undecided)",
            "scores": {k: 0 for k in ["math_strength", "programming_skill"]},
            "expected": None
        }
    ]

    print("\n[Tech People] Starting Logic Integrity Verification Suite...")
    print("-" * 60)

    for profile in test_profiles:
        list(prolog.query("clear_scores"))
        for trait, val in profile["scores"].items():
            prolog.assertz(f"student_score({trait}, {val})")
        
        results = list(prolog.query("recommendation(X)"))
        actual = results[0]['X'] if results else None
        
        status = "PASSED" if actual == profile["expected"] else "FAILED"
        print(f"Test: {profile['name']:<30} | Status: {status}")
        if status == "FAILED":
            print(f"  --> Expected: {profile['expected']}, Actual: {actual}")

    print("-" * 60)
    print("Verification Suite Complete.\n")

if __name__ == "__main__":
    run_tests()
